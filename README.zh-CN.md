# Agent Skills 🧰

[English](README.md) | 中文

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Built for Agents](https://img.shields.io/badge/Built%20for-AI%20Agents-blue)
![Maintained](https://img.shields.io/badge/Maintained-yes-success)
![GitHub stars](https://img.shields.io/github/stars/hicoldcat/skills?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/hicoldcat/skills)

一个面向 AI 编程代理的 skill 合集。

> 🚀 开源、实用、易扩展。

## 当前可用的 Skills ✨

### random-image-placeholder

基于 [Lorem Picsum](https://picsum.photos/) 生成随机/可复现的占位图 URL（可选下载到本地）。

**适用场景：**

- 做 UI mock / 文档 / demo，需要图片但不想托管静态资源
- 测试/快照需要可复现图片（使用 `seed`）
- 用户提到 picsum / 占位图 / grayscale / blur / seed / id

**示例：**

```bash
python skills/random-image-placeholder/scripts/picsum.py url --seed avatar-42 --width 400 --height 400 --grayscale --blur 2
```

```bash
python skills/random-image-placeholder/scripts/picsum.py download --seed avatar-42 --width 120 --height 80 --out ./tmp/picsum_test.jpg
```

相关文档：

- `skills/random-image-placeholder/README.md`
- `skills/random-image-placeholder/SKILL.md`

## 安装 📦

常见有三种方式：

1. **通过 ClawHub 安装（推荐给使用者）**
   - 打开：`https://clawhub.ai/hicoldcat/random-image-placeholder`
   - 在页面点击安装/导入按钮，将 skill 加入你的代理工作区
2. **通过 skills.sh CLI 安装**
   - 运行：

```bash
npx skills add https://github.com/hicoldcat/skills --skill random-image-placeholder
```

3. **源码方式（适合本地开发）**
   - clone 仓库后直接使用 `skills/` 下的 skill 文件与脚本

## 使用 🧪

安装/导入后，skill 会根据你的编辑器/代理规则自动可用。若 skill 自带脚本，建议在需要“确定性输出”时直接运行脚本获得稳定结果。

## Skill 结构 🗂️

每个 skill 通常包含：

- `SKILL.md`：给代理的使用说明
- `scripts/`：可选的辅助脚本（更稳定、可复用）
- `references/`：可选的参考资料
- `assets/`：可选的资源文件

## 许可 📄

MIT，见 [LICENSE](LICENSE)。
