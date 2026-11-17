---
name: icon-material-studio
description: Create consistently 3D-looking soft-clay icons from sourced or original shapes, with commercial-use checks and image-file delivery. Use only when the user wants soft clay or a 3D icon with material unspecified; do not invoke for explicitly flat, vector, or other non-clay requests.
---

# Icon Material Studio

Complete a source-to-delivery **3D-look icon** workflow. Every icon produced under this skill must visibly use stable **soft clay** material. Do not output flat, paper, metallic, or arbitrary material variants under this skill. Treat “3D” as a visual material treatment unless an actual 3D model is produced. Keep provenance for every source and generated output. If the user explicitly rejects clay or requests another material, use ordinary image or vector capabilities without invoking this skill.

## 1. Define the brief without stalling

Extract: icon subjects and count; desired silhouette or reference; soft-clay material; palette; target pixel sizes and background; source-license constraints; image file format and delivery location; and whether the assets are for preview or a project. Inspect existing product visuals and design tokens when available. Guide the user through only the unresolved decisions, in their language: first show 2–4 recognizable shape candidates with source and commercial status, then ask for palette or output destination only if it changes the next step. Bundle choices into one short prompt when possible. Interpret short replies such as “02”, “purple”, or “try all” against the current candidate set; do not restart discovery. See [user interaction](references/user-interaction.md).

If the user requests a 3D icon without specifying material, use soft clay and explain it. If no output mode is specified, make downloadable transparent PNGs. Continue independent source research while waiting for an optional preference; never treat elapsed time as approval for paid resources.

Show a small, visually distinct candidate set before committing to a borrowed silhouette when the choice is subjective. When the user has selected an icon already, continue directly. Distinguish a source icon's shape from a style reference; note both if used as generation inputs.

## 2. Search and clear sources

Accept either user-provided images or a text description of the object. Inspect provided images and identify their role and known rights. Search free commercially usable resources first; if no suitable match exists, include clearly labeled paid commercial candidates with original asset and license links. Do not purchase without authorization. Always provide original source links for sourced candidates, including paid ones.

Search across installed icon skills/packages, the user's project assets, official maker catalogs and GitHub repositories, aggregators that link to original creators, and relevant public-domain or paid marketplaces when the brief warrants them. Broaden by subject synonyms and visual traits, not by downloading every result. Use aggregators for discovery, then verify the icon and license with the original publisher. See [search channels](references/search-channels.md). Browse current authoritative license pages before claiming commercial rights. Prefer sources with a clear official license and direct icon URL. Use the user's required license as a filter, not merely a label at the end. For commercial requests, avoid sources with unclear downstream image rights, “free for personal use,” missing attribution, or contradictory license terms unless a replacement or permission is obtained. Do not assume a repository's code license covers all images, examples, screenshots, or trademarks. “Free to download,” “open source,” “commercially usable,” and “public domain” are separate claims.

Record for each candidate: creator/library; exact source-icon URL; license URL and version; cost; commercial and attribution terms; whether the planned use is copying/modifying the source or using it only as inspiration; and confidence/unknowns. Recheck unstable license pages at use time. See [license and provenance](references/license-and-provenance.md). A source with unresolved rights may be shown as a clearly marked concept, but cannot be represented as commercially cleared.

## 3. Build a coherent material style

Define a small shared style contract before generating: silhouette simplicity; angle and depth; material response; light direction; palette; edge roundness; shadow; background transparency; safe-area; and detail budget at intended size. Keep all icons in one family. For soft clay use rounded mass, broad diffuse highlights, subtle surface texture and contact shadow. Reject outputs whose material reads as flat fill, simple gradient, paper, opaque plastic or metal; revise them as soft clay before delivery.

Use the `imagegen` skill and built-in image generation for bitmap materialized icons; one distinct call per icon/variant. State each input image's role (shape reference, style reference, or edit target). Use transparent backgrounds when requested and verify real alpha. Preserve semantic recognition and requested colors; avoid unrequested faces, words, and decorative parts. Generated bitmap is not an editable 3D model or open-source icon. If the existing source is editable SVG and the requested change is a simple vector treatment, use native vector editing instead of raster generation. For commercial-safe original work, prefer a fresh subject description and material contract over feeding an ambiguously licensed source image into generation.

Inspect each result at native and intended small size, on light and dark surfaces when relevant. Fix only observed problems. Build a contact sheet for selection if there are multiple options; do not present a mockup as the final asset. Preserve earlier versions unless replacement is explicitly requested.

## 4. Deliver image files

Copy selected final files to the requested location or project workspace, using stable descriptive names. Provide the actual downloadable files, a compact preview, intended-size notes, and a provenance manifest. Do not leave project-referenced assets only in a tool's generated-image cache. For a set, package the assets and manifest as ZIP. Verify file count, dimensions, alpha, and archive contents. If SVG is requested, only supply a true vector asset when one was actually created; do not relabel a raster or place a PNG inside an SVG shell without disclosure.

## 5. Report and handoff

Every user-facing handoff must include: the search channels **actually used** (and distinguish channels merely available), exact source-resource URL(s) or “text-only original, no source icon,” the direct file download link(s), and a clear commercial-use status with license/attribution conditions or uncertainty. Say what was produced and checked, including the soft-clay material treatment. Include the source/derivation chain for each asset. An AI output's terms and a source icon's license are distinct; recoloring or materializing a licensed silhouette does not automatically erase source obligations. If an input license or source is uncertain, say so and offer an independently generated replacement. State whether the work is a PNG 3D-look illustration or a true 3D model. For project changes, follow that project's own versioning and Git rules; do not imply deployment from a local file delivery.
