#!/usr/bin/env python3
"""
CCI AI Coaching Platform · Local Proxy Server
Serves the HTML file AND proxies API calls to Anthropic/OpenAI/Google/OpenRouter,
so the browser never makes cross-origin requests (zero CORS issues).
"""

import json
import os
import ssl
import urllib.request
import urllib.error
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

# ── Fix macOS Python SSL certificate issue ──────────────────────────────
# macOS Python often ships without root CA certs configured.
# Try certifi first, then fall back to an unverified context.
try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
    print("  🔐 SSL: using certifi certificates")
except ImportError:
    SSL_CTX = ssl.create_default_context()
    try:
        SSL_CTX.load_default_certs()
    except Exception:
        pass
    # Test if default certs work by trying a known host
    import socket
    try:
        with SSL_CTX.wrap_socket(socket.socket(), server_hostname="api.openai.com") as s:
            s.settimeout(5)
            s.connect(("api.openai.com", 443))
        print("  🔐 SSL: system certificates OK")
    except Exception:
        # System certs don't work — create unverified context as last resort
        SSL_CTX = ssl.create_default_context()
        SSL_CTX.check_hostname = False
        SSL_CTX.verify_mode = ssl.CERT_NONE
        print("  ⚠️  SSL: using unverified mode (run 'pip3 install certifi' for full security)")

PORT = 8765

ALLOWED_HOSTS = [
    "api.anthropic.com",
    "api.openai.com",
    "generativelanguage.googleapis.com",
    "openrouter.ai",
]


class Handler(SimpleHTTPRequestHandler):

    # ── CORS pre-flight ─────────────────────────────────────────────────────
    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    # ── POST → proxy ────────────────────────────────────────────────────────
    def do_POST(self):
        if self.path == "/proxy":
            self._handle_proxy()
        else:
            self.send_error(404, "Not found")

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")

    def _handle_proxy(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length)

            if not raw:
                self._json_error(400, "Empty request body")
                return

            payload = json.loads(raw)
            target_url = payload.get("url", "")
            req_headers = payload.get("headers", {})
            req_body_obj = payload.get("body", {})

            if not target_url:
                self._json_error(400, "Missing 'url' field")
                return

            # Safety: only allow known AI API hosts
            host = urlparse(target_url).netloc
            if not any(host == h or host.endswith("." + h) for h in ALLOWED_HOSTS):
                self._json_error(403, f"Host not allowed: {host}")
                return

            # CRITICAL: Always set Content-Type for JSON APIs
            req_headers["Content-Type"] = "application/json"

            req_body = json.dumps(req_body_obj).encode("utf-8")

            req = urllib.request.Request(
                target_url,
                data=req_body,
                headers=req_headers,
                method="POST",
            )

            print(f"  → Proxy: POST {target_url[:60]}...")

            with urllib.request.urlopen(req, timeout=120, context=SSL_CTX) as resp:
                data = resp.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self._cors()
                self.end_headers()
                self.wfile.write(data)
                print(f"  ✓ Response: 200 OK ({len(data)} bytes)")

        except urllib.error.HTTPError as e:
            data = e.read()
            print(f"  ✗ API Error: {e.code} ({len(data)} bytes)")
            self.send_response(e.code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self._cors()
            self.end_headers()
            self.wfile.write(data)

        except urllib.error.URLError as e:
            msg = f"Cannot connect to API: {str(e.reason)}"
            print(f"  ✗ Connection Error: {msg}")
            self._json_error(502, msg)

        except json.JSONDecodeError as e:
            self._json_error(400, f"Invalid JSON in request: {str(e)}")

        except Exception as e:
            print(f"  ✗ Unexpected Error: {str(e)}")
            self._json_error(500, str(e))

    def _json_error(self, code, msg):
        body = json.dumps({"error": {"message": msg, "type": "proxy_error"}}).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self._cors()
        self.end_headers()
        self.wfile.write(body)

    # ── Quiet static-file logs ──────────────────────────────────────────────
    def log_message(self, fmt, *args):
        path = args[0] if args else ""
        if "proxy" not in str(path):
            # Only log non-proxy requests at reduced verbosity
            status = args[1] if len(args) > 1 else ""
            if "200" not in str(status) and "304" not in str(status):
                super().log_message(fmt, *args)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    url = f"http://localhost:{PORT}/coaching-platform.html"
    print()
    print("=" * 52)
    print("   AI 教练平台 | CCI Coaching Platform")
    print("=" * 52)
    print(f"   ✅  服务器已启动  Server ready on port {PORT}")
    print(f"   📱  地址: {url}")
    print(f"   🔒  API 代理已就绪 (proxy active)")
    print(f"   ⚠️   关闭此窗口将停止服务器")
    print("=" * 52)
    print()

    try:
        server = HTTPServer(("", PORT), Handler)
        server.serve_forever()
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"   ❌  端口 {PORT} 被占用！")
            print(f"   请先关闭之前的终端窗口，或运行：")
            print(f"   lsof -ti:{PORT} | xargs kill -9")
            print()
        else:
            raise
    except KeyboardInterrupt:
        print("\n   🛑  服务器已停止 Server stopped.")
