# AI教练对话练习平台 | AI Coaching Practice Platform

> 基于《建立可持续的教练文化》（作者：Eng Hooi）框架
> Based on "Building a Sustainable Coaching Culture" by Eng Hooi

---

## 项目背景 | About

本平台专为企业经理和领导力学习者设计，帮助他们通过 AI 模拟对话来练习**教练式领导**技能，或针对真实职场管理难题获取基于教练框架的解决方案。

This platform is designed for managers and leadership learners to practice **coaching conversations** via AI simulation, or to get coaching-based solutions for real workplace management challenges.

**核心理念 | Core Philosophy:**
- 提问而非指令 / Ask, don't tell
- 授权而非控制 / Empower, don't control
- 每一刻都是可教练的时机 / Every moment is a coachable moment

---

## 功能介绍 | Features

### 模式一：角色扮演练习 | Mode 1: Role-Play Practice

- 用户扮演**教练/经理**，AI 扮演**员工**进行真实对话练习
- 选择**难度级别**：初级 / 中级 / 高级
- 选择**教练模型**：GROW、CLEAR、OSKAR、ACHIEVE、PRACTICE、FUEL
- 选择**练习场景**（6种预设场景 + 自定义）
- 对话结束后获得**详细反馈报告**：
  - 逐句点评（✅良好 / ⚠️可改进 / ❌非教练式）
  - 整体评分（基于ICF能力框架，满分100分）
  - 亮点、改进建议、下次练习方向

### 模式二：实际案例分析 | Mode 2: Real Case Analysis

- 描述真实职场管理难题（情况、已尝试方法、期望结果）
- AI 给出：问题诊断、推荐教练模型、开场问题建议、注意事项

### 其他功能 | Other Features

- 🌐 中文 / English 双语切换（右上角）
- 📋 实时教练模型步骤参考卡（聊天界面右侧）
- 🔒 API Key 本地安全存储（仅 sessionStorage，不上传服务器）

---

## 支持的教练模型 | Supported Coaching Models

| 模型 | 全称 | 步骤 |
|------|------|------|
| **GROW** | Goal-Reality-Options-Will | 目标→现实→选择→行动意愿 |
| **CLEAR** | Contract-Listen-Explore-Action-Review | 签约→倾听→探索→行动→回顾 |
| **OSKAR** | Outcome-Scaling-Knowhow-Affirm-Review | 结果→量化→资源→行动→回顾 |
| **ACHIEVE** | Assess-Creative-Hone-Initiate-Evaluate-Valid-Encourage | 7步综合模型 |
| **PRACTICE** | Problem-Realistic-Alternative-Consequences-Target-Implementation-Celebration-Evaluation | 8步问题解决 |
| **FUEL** | Frame-Understand-Explore-Lay out | 框架→理解→探索→规划 |

---

## 如何本地运行 | How to Run Locally

本项目为**单文件 HTML 应用**，无需安装任何依赖、无需服务器。

This is a **single HTML file** application — no installation or server required.

### 步骤 | Steps:

1. **下载文件** | Download the file:
   ```
   coaching-platform.html
   ```

2. **用浏览器打开** | Open in browser:
   - 双击文件，或将文件拖入 Chrome / Safari / Edge / Firefox
   - Simply double-click, or drag into your browser

3. **输入 API Key** | Enter your API Key:
   - 在页面顶部输入您的 Anthropic API Key
   - Enter your Anthropic API Key in the input field on the home page

4. **开始使用** | Start using:
   - 选择模式，开始练习！
   - Choose a mode and start practicing!

---

## API Key 说明 | About the API Key

**您需要自备 Anthropic API Key 才能使用本平台。**
**You need your own Anthropic API Key to use this platform.**

- 申请地址 / Get one at: [https://console.anthropic.com](https://console.anthropic.com)
- 选择模型 / Model used: `claude-sonnet-4-20250514`
- **安全说明** / **Security**: Your API Key is stored only in your browser's `sessionStorage`. It is **never transmitted to any third-party server**. All API calls go directly from your browser to Anthropic's servers.
- API Key 在关闭标签页后自动清除 / Key is cleared when you close the browser tab

---

## 技术说明 | Technical Notes

- **架构**: 纯 HTML/CSS/JavaScript 单页应用，无框架依赖
- **Architecture**: Pure HTML/CSS/JS SPA, no framework dependencies
- **API**: Anthropic Claude API (direct browser access with `anthropic-dangerous-direct-browser-access: true` header)
- **存储**: 仅 `sessionStorage`，关闭标签页自动清除
- **Storage**: `sessionStorage` only — clears on tab close
- **兼容性**: 现代浏览器（Chrome, Safari, Edge, Firefox）
- **Compatibility**: Modern browsers (Chrome, Safari, Edge, Firefox)

---

## 知识框架来源 | Knowledge Framework

本平台的AI系统提示和评估框架基于：

- 📗 《建立可持续的教练文化》—— Eng Hooi 著
- 🏅 ICF（国际教练联合会）核心教练能力框架
- 🔬 教练技能评估维度：倾听与观察、提问质量、模型遵循、避免给答案、建立安全空间

The AI system prompts and evaluation framework are based on:

- 📗 "Building a Sustainable Coaching Culture" by Eng Hooi
- 🏅 ICF (International Coaching Federation) Core Coaching Competencies
- 🔬 Evaluation dimensions: Listening & Observation, Question Quality, Model Adherence, Avoiding Advice, Creating Safe Space

---

## 许可 | License

本项目仅供学习和内部培训使用。
For learning and internal training use only.

---

*Built with ❤️ for coaching culture development*
