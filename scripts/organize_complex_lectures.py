"""Combine the reviewed complex-analysis lecture notes into seven flat modules.

One Markdown file per learning module, with only its top-level title. Existing
reviewed notes and page OCR remain available as indexed archives for checking.
Run with --check to verify the generated files without writing.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re

from build_course_index import ROOT, CA_MODULES, dump, keywords

PREFIX = "Course/Complex_Analysis"
INDEX = PREFIX + "/index.json"
MODULES = [
    ("01_Complex_Numbers", "模块一：复数与复变函数", ("01_Complex_Numbers", "02_Domains_and_Continuity")),
    ("02_Analytic_Functions", "模块二：解析函数及应用", ("03_Analytic_Functions",)),
    ("03_Complex_Integration", "模块三：复变函数的积分", ("04_Complex_Integration",)),
    ("04_Series", "模块四：级数概念及分类", ("05_Series",)),
    ("05_Residues", "模块五：留数相关及应用", ("06_Singularities_and_Residues", "07_Real_Integrals")),
    ("06_Fourier_Transform", "模块六：傅里叶变换相关", ("08_Fourier_Transform",)),
    ("07_Laplace_Transform", "模块七：拉普拉斯之变换", ("09_Laplace_Transform",)),
]


def note_body(text):
    """Keep every content paragraph and formula, removing headings and repeated prefaces."""
    return re.sub(r"\n{3,}", "\n\n", "\n".join(
        line for line in text.splitlines() if not re.match(r"^#{1,6}\s", line)
        and not line.startswith(("来源：", "本篇为阅读手写内容后的整理稿")))).strip()


def build():
    data = json.loads((ROOT / INDEX).read_text(encoding="utf-8-sig"))
    records = {item["path"]: item for item in data["items"]}
    ocr = [item for item in records.values() if "/Lectures/Page_Text/" in item["path"]]
    generated, added, archived = {}, [], set()
    links = []
    for number, (slug, title, names) in enumerate(MODULES):
        parts, source_parts, topics, sources = [], [], [], []
        for name in names:
            path = f"{PREFIX}/Notes/{name}.md"
            item = records[path]
            text = (ROOT / path).read_text(encoding="utf-8-sig")
            parts.append(note_body(text))
            topics.extend(re.findall(r"^##\s+(.+)$", text, re.M))
            source_parts.append({"path": path, "source_pages": item["source_pages"],
                                 "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()})
            sources.append(item)
            archived.add(path)
        ids = {item["source_id"] for item in sources}
        if len(ids) != 1:
            raise ValueError(f"Lecture sources differ in {title}")
        start, stop = sources[0]["source_pages"][0], sources[-1]["source_pages"][1]
        fragments = [{"path": item["path"], "source_pages": [max(start, item["source_pages"][0]),
                     min(stop, item["source_pages"][1])]} for item in ocr
                     if item.get("source_id") in ids
                     and max(start, item["source_pages"][0]) <= min(stop, item["source_pages"][1])]
        pages = [page for fragment in fragments for page in range(fragment["source_pages"][0], fragment["source_pages"][1]+1)]
        if sorted(pages) != list(range(start, stop+1)):
            raise ValueError(f"Missing or repeated original lecture pages for {title}")
        path = f"{PREFIX}/Lectures/{slug}.md"
        content = (f"# {title}\n\n来源：高瑜《复变函数与积分变换》2024 秋讲义，原 PDF 第 {start}–{stop} 页。\n\n"
                   "本模块合并既有校订稿，公式采用标准 LaTeX，保留内容中的必要条件与歧义说明；不是逐字转录。\n\n"
                   + "\n\n".join(parts) + "\n")
        if re.findall(r"^#{1,6}\s+.*", content, re.M) != [f"# {title}"]:
            raise ValueError(f"Unexpected subsection headings in {path}")
        generated[path] = content
        added.append({"path": path, "title": title, "kind": "cleaned_notes",
            "quality": "visually_reconstructed", "modules": [CA_MODULES[number]],
            "source_id": sources[0]["source_id"], "source_name": sources[0]["source_name"],
            "source_pages": [start, stop], "source_parts": source_parts, "ocr_fragments": fragments,
            "topics": topics, "keywords": keywords(content, title), "priority": 1})
        links.append(f"- [{title}]({slug}.md)（原 PDF 第 {start}–{stop} 页）")
    # Original notes and page batches remain accessible, but are not duplicate AI inputs.
    archived.update(item["path"] for item in ocr)
    for item in data["items"]:
        if item["path"] in archived:
            item["kind"] = "archive"
    module_paths = {item["path"] for item in added}
    retained = [item for item in data["items"] if item["path"] not in module_paths]
    chapters = [item for item in retained if item.get("kind") == "textbook_chapter"]
    data["items"] = [item for item in retained if item.get("kind") != "textbook_chapter"] + added + chapters
    data["lecture_modules"] = [item["path"] for item in added]
    generated[INDEX] = dump(data)
    generated[PREFIX+"/Lectures/README.md"] = (
        "# 复变讲义：七个学习模块\n\n每个模块一份正文文件，只保留模块标题，不再分小标题或小文件。"
        "原有校订稿的文字、公式和必要条件按模块合并，来源与页码保存在索引中。\n\n"
        + "\n".join(links) + "\n\n原始 [校订稿](../Notes/) 与 [逐页 OCR](Page_Text/) 留作回查，"
        "已标为存档，程序优先读取上面的七份模块正文。\n")
    generated[PREFIX+"/Notes/README.md"] = (
        "# 原始校订稿\n\n现已合并到 [讲义七模块目录](../Lectures/README.md)。"
        "此处保留原有校订稿供核对；程序不再将这些文件作为重复的讲义输入。\n\n"
        "[教材拓展提要](10_Textbook_Supplements.md) 仍供对应主题补充使用。\n")
    main = ROOT / PREFIX / "README.md"
    readme = main.read_text(encoding="utf-8-sig")
    readme = readme.replace("先读 [校订讲义目录](Notes/README.md)，按主题选一篇；",
                            "先读 [讲义七模块目录](Lectures/README.md)，每个模块一份正文，不设小标题；")
    readme = readme.replace("当前缓存没有修改应用的资料读取配置。", "程序通过模块索引读取对应正文，原始页段仅供回查。")
    generated[PREFIX+"/README.md"] = readme
    return generated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for name, text in build().items():
        path = ROOT / name
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8-sig") != text:
                raise SystemExit(f"Out of date: {name}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8", newline="\n")
    print(("Verified" if args.check else "Generated") + " seven lecture modules; no subsection headings")


if __name__ == "__main__":
    main()
