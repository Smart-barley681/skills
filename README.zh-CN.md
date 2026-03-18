# Agent Skills 🧰

[English](README.md) | 中文

一个面向 AI 编程代理的 skill 合集。Skill 本质是可打包的说明与脚本，用来扩展代理能力。

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

## 安装

本仓库支持两种常见使用方式：

1. **直接用源码**：clone 仓库后直接使用 `skills/` 下的 skill 文件与脚本
2. **使用打包产物 `.skill`**：导入 `dist/` 下生成的 `.skill` 文件（如果你发布了 GitHub Releases，也可以从 Release 下载）

本地打包：

```bash
python scripts/package_skill.py skills/random-image-placeholder
```

## 使用

安装/导入后，skill 会根据你的编辑器/代理规则自动可用。若 skill 自带脚本，建议在需要“确定性输出”时直接运行脚本获得稳定结果。

## Skill 结构

每个 skill 通常包含：

- `SKILL.md`：给代理的使用说明
- `scripts/`：可选的辅助脚本（更稳定、可复用）
- `references/`：可选的参考资料
- `assets/`：可选的资源文件

## 许可

MIT，见 [LICENSE](LICENSE)。

