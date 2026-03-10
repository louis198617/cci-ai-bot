#!/bin/bash
# ============================================================
#  AI 教练对话练习平台 · 本地服务器启动器
#  AI Coaching Practice Platform · Local Server Launcher
# ============================================================

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

PORT=8765
URL="http://localhost:${PORT}/coaching-platform.html"

echo ""
echo "============================================"
echo "  AI 教练对话练习平台 | CCI Coaching Platform"
echo "============================================"
echo ""

# Kill any existing process on our port (so restart always works)
lsof -ti:${PORT} 2>/dev/null | xargs kill -9 2>/dev/null
sleep 0.5

echo "🚀  正在启动服务器... Launching server..."
echo "📱  地址 URL: $URL"
echo ""
echo "⚠️   请勿关闭此窗口 — 关闭后平台将停止运行"
echo "⚠️   Keep this window open — closing it stops the platform"
echo ""

# Open Chrome after a delay so server can start
(sleep 2 && open -a "Google Chrome" "$URL" 2>/dev/null || open "$URL") &

# Run the proxy server
python3 server.py
