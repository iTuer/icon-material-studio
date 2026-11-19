# 3D 软陶图标生成器

**简体中文** · [English](README.en.md)

说一个物品，或给一张图片。生成软陶图标。

![Soft clay icon gallery](assets/gallery/page.png)

## 案例：牛角包

![Croissant reference and generated result](assets/croissant-case/page.png)

**牛角包 PNG 可作为付费 App 的普通界面图标。** 它由文字生成，原照片只用于识别主题。原照片本身的商业再利用授权仍待确认。 [下载透明 PNG](assets/croissant-clay.png) · [来源与依据](assets/CREDITS.md)

## 怎么用

把下面这句话发给 Codex。

> 从 https://github.com/iTuer/soft-clay-icons 安装 Skill。`SKILL.md` 在仓库根目录，请安装到 `~/.codex/skills/soft-clay-icons/`。

也可以下载仓库 ZIP，将含有 `SKILL.md` 的目录解压为上述目录。如果 Codex 设置了其他技能目录，请使用对应位置。安装后开启新会话，发送「用 `$soft-clay-icons` 做一个牛角包图标」，或上传参考图片。出图需要当前会话提供图片生成工具，运行质检脚本需要 Python 3。

默认输出透明背景的软陶 PNG。配色和商用条件按需补充。

简单物品默认直接生成，不强制检索外部图标。使用内置标定板时，会明确记录为 AI 材质参考；它可帮助保持一致，但不保证完全一致。

## 工作流程

简单物品可直接出图。想找参考时，先查来源和授权。按指定图改造时，先核对该图的使用条件。成图经过小尺寸检查后，以 PNG 或 ZIP 交付。

需要检索造型时，优先检索免费可商用资源；没有合适结果时，再提供付费商用候选，附原素材和许可链接，购买前确认。

## 来源与交付

检索渠道包括已安装图标库、项目素材、原作者网站与 GitHub、Iconify、OpenMoji、Wikimedia Commons 和商用素材平台。交付时逐项说明能用于哪些商业用途、需要满足什么条件，以及哪些素材的授权还待确认，并附来源、许可和下载链接。

## 示例参考

| 示例 | 造型参考 | 材质参考 |
|---|---|---|
| 书籍 | [Solar notebook-2](https://icon-sets.iconify.design/solar/notebook-2-bold-duotone/) | - |
| 完成、小白菜、胡萝卜、南瓜、番茄 | - | 已生成的书籍图 |
| 茄子 | - | - |

示例为 AI 生成 PNG，部分历史参考的商用授权尚未确认。[详细来源与授权](assets/CREDITS.md)。

[SKILL.md](SKILL.md) · [Test report](TEST-REPORT.md)

## 只读检查

`python3 scripts/inspect_icon.py icon.png --out-dir preview`

区分完全不透明与接近不透明像素，校验支持格式的 PNG 数据，生成 1:1 与小尺寸浅深底预览。不支持的编码会明确报告，不能当作通过；视觉效果仍需实际查看。
