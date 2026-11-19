# Icon Material Studio

[简体中文](README.md) · **English**

A word or an image. A soft-clay icon.

![Soft clay icon gallery](assets/gallery/page.png)

## Case: croissant

![Croissant reference and generated result](assets/croissant-case/page.png)

[Download transparent PNG](assets/croissant-clay.png). The supplied photo was used to identify the subject; the icon was generated from text without passing the photo to the image tool. AI-generated image; commercial use is subject to the applicable service terms. [Provenance](assets/CREDITS.md).

## Use it

Send this request to Codex.

> Install the skill from https://github.com/iTuer/icon-material-studio. `SKILL.md` is at the repository root. Install it in `~/.codex/skills/icon-material-studio/`.

You can also download the repository ZIP and extract the directory containing `SKILL.md` into that location or your configured skills directory. Start a new session and ask “Use `$icon-material-studio` to make a croissant icon,” or upload a reference image. Image generation requires an image tool in the current session. The inspection script requires Python 3.

The default output is a soft clay PNG with a transparent background. Add any color or commercial use requirements you need.

Simple objects are generated directly without a mandatory external search. When used, the built-in calibration image is disclosed as an AI material reference; it may help consistency but cannot guarantee it.

## Workflow

Generate simple subjects directly. For reference searches, check the source and its terms. For an exact transformation, check the supplied image first. Review generated images at small sizes before delivering PNG or ZIP files.

For asset-search tasks, free commercially usable resources are searched first. Paid commercial options are offered when needed, with source and license links. Purchases require authorization.

## Sources and delivery

Search channels include installed icon libraries, project assets, original creators and GitHub, Iconify, OpenMoji, Wikimedia Commons, and commercial catalogs. Each delivery lists the channels actually used, original asset links, license conditions, commercial status and file downloads.

## Example references

| Example | Shape reference | Material reference |
|---|---|---|
| Book | [Solar notebook-2](https://icon-sets.iconify.design/solar/notebook-2-bold-duotone/) | - |
| Completed / vegetables | - | Generated book |
| Eggplant | - | - |

These are AI-generated PNG illustrations. Some example input chains have unresolved commercial rights. [Full provenance and license notes](assets/CREDITS.md).

[SKILL.md](SKILL.md) · [Test report](TEST-REPORT.md)

## Read-only inspection

`python3 scripts/inspect_icon.py icon.png --out-dir preview`

Reports exact and near-opaque alpha separately, rejects damaged supported PNG files, and creates 1:1 plus small-size light/dark previews. Unsupported encodings are reported, not passed. Human visual review is still required.
