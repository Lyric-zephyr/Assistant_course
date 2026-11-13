"""Create one file per complex-analysis textbook chapter, with section markers.

The existing page OCR stays untouched. Each new fragment identifies its source
file, PDF page, and OCR line range. Run with --check to verify without writing.
"""

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import re

from build_course_index import ROOT, CA_CHAPTER_MAP, CA_MODULES, dump, keywords

PREFIX = "Course/Complex_Analysis"
INDEX = PREFIX + "/index.json"
PAGE = re.compile(r"(?ms)^## 原文件第 (\d+) 页([^\n]*)\n\n```text\n(.*?)\n```")
SOURCE = re.compile(r"/Textbook/(\d{2}_[^/]+)/pages_\d+-\d+\.md$")
# Section starts are original PDF pages (printed page + 15); summaries are separate.
CONTENTS = {
    1: [(1, "复数运算及几何表示", 16), (2, "复平面上的点集", 29),
        (3, "复变函数", 32), (99, "本章小结", 38)],
    2: [(1, "解析函数的概念", 43), (2, "函数解析的充要条件", 47),
        (3, "解析函数与调和函数", 51), (4, "初等函数", 58),
        (5, "解析函数的物理意义", 69), (99, "本章小结", 75)],
    3: [(1, "复变函数积分的概念", 82), (2, "柯西积分定理", 88),
        (3, "柯西积分公式", 94), (99, "本章小结", 105)],
    4: [(1, "复变函数项级数", 111), (2, "幂级数", 120),
        (3, "泰勒级数", 131), (4, "洛朗级数", 137), (99, "本章小结", 145)],
    5: [(1, "孤立奇点", 151), (2, "留数", 159),
        (3, "留数在定积分计算中的应用", 168), (4, "辐角原理与儒歇定理", 177),
        (99, "本章小结", 184)],
    6: [(1, "保形映射的概念", 191), (2, "分式线性映射", 194),
        (3, "分式线性映射的性质", 200), (4, "两个重要的分式线性映射", 205),
        (5, "几个初等函数所构成的映射", 209), (99, "本章小结", 220)],
    7: [(1, "傅里叶积分与傅里叶积分定理", 225),
        (2, "傅里叶变换与傅里叶逆变换", 232), (3, "单位脉冲函数", 237),
        (4, "广义傅里叶变换", 244), (5, "傅里叶变换的性质", 247),
        (6, "卷积", 256), (7, "相关函数", 266), (8, "傅里叶变换的应用", 273),
        (9, "多维傅里叶变换", 277), (99, "本章小结", 282)],
    8: [(1, "拉普拉斯变换的概念", 290), (2, "拉普拉斯变换的性质（一）", 300),
        (3, "拉普拉斯变换的性质（二）", 309), (4, "拉普拉斯逆变换", 316),
        (5, "拉普拉斯变换在解方程中的应用", 322), (99, "本章小结", 327)],
}


def normalized(text):
    return re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]", "", text)


def heading_line(page, chapter, section, title):
    target = f"第{chapter}章小结" if section == 99 else f"{chapter}{section}{normalized(title)}"
    targets = {target}
    if chapter == 8 and section != 99:
        targets.add(f"{section}{normalized(title)}")  # OCR reads '8.' as '&'.
    matches = []
    for i in range(len(page["lines"])):
        for length in (1, 2, 3):
            if normalized("".join(page["lines"][i:i+length])) in targets:
                matches.append(i)
                break
    if not matches:
        # In section 2.5 OCR separated the number from its title with formula lines.
        matches = [i for i, line in enumerate(page["lines"]) if normalized(line) == normalized(title)]
        if len(matches) != 1:
            raise ValueError(f"Cannot locate heading {chapter}.{section} {title} on PDF page {page['page']}")
    # A running header can announce the next section while the preceding text continues.
    return max(matches)


def read_pages(records):
    chapters = defaultdict(dict)
    for item in records:
        match = SOURCE.search(item["path"])
        if not match:
            continue
        folder = match[1]
        chapter = int(folder[:2])
        text = (ROOT / item["path"]).read_text(encoding="utf-8-sig")
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        pages = list(PAGE.finditer(text))
        expected = list(range(item["source_pages"][0], item["source_pages"][1]+1))
        if [int(page[1]) for page in pages] != expected:
            raise ValueError(f"Missing or duplicate page blocks in {item['path']}")
        for page in pages:
            number = int(page[1])
            if number in chapters[chapter]:
                raise ValueError(f"Duplicate source page {number}")
            chapters[chapter][number] = {"page": number, "folder": folder, "source": item,
                "header": f"## 原文件第 {number} 页{page[2]}", "sha256": digest,
                "lines": (page[3]+"\n").splitlines(keepends=True)}
    return chapters


def render(lines, positions, start, stop):
    pieces, fragments = [], []
    cursor = start
    while cursor < stop:
        page, line = positions[cursor]
        end = cursor+1
        while end < stop and positions[end][0] is page:
            end += 1
        last_line = positions[end-1][1]+1
        raw = "".join(lines[cursor:end])
        pieces.append(f"#{page['header']}；本页 OCR 第 {line+1}–{last_line} 行\n\n```text\n{raw}```\n")
        fragments.append({"path": page["source"]["path"], "page": page["page"],
                          "lines": [line+1, last_line], "sha256": page["sha256"]})
        cursor = end
    return "\n".join(pieces), fragments


def build():
    data = json.loads((ROOT / INDEX).read_text(encoding="utf-8-sig"))
    originals = [item for item in data["items"] if SOURCE.search(item["path"])]
    chapters = read_pages(originals)
    if set(chapters) != set(CONTENTS):
        raise ValueError("The textbook must contain all eight chapters")
    generated, added = {}, []
    contents = ["# 复变函数与积分变换（第三版）章节目录", "",
        "按教材的 8 个大章节各存一份，1.1、1.2 等小节作为章内标题标记，不单独拆文件。页码均指原 PDF。", ""]
    for chapter, pages in sorted(chapters.items()):
        ordered = [pages[number] for number in sorted(pages)]
        if sorted(pages) != list(range(ordered[0]["page"], ordered[-1]["page"]+1)):
            raise ValueError(f"Noncontiguous chapter pages: {chapter}")
        folder = ordered[0]["folder"]
        base = f"{PREFIX}/Textbook/{folder}"
        title = ordered[0]["source"]["title"].split("：", 1)[0]
        lines, positions, offsets = [], [], {}
        for page in ordered:
            offsets[page["page"]] = len(lines)
            for number, line in enumerate(page["lines"]):
                lines.append(line)
                positions.append((page, number))
        starts = [0]
        for section, name, number in CONTENTS[chapter][1:]:
            starts.append(offsets[number] + heading_line(pages[number], chapter, section, name))
        starts.append(len(lines))
        if starts != sorted(set(starts)):
            raise ValueError(f"Overlapping section boundaries: {chapter}")
        path = base + "/chapter.md"
        contents.extend([f"## [第{chapter}章 {title}]({path.removeprefix(PREFIX+'/')})", ""])
        chapter_readme = [f"# 第{chapter}章 {title}", "",
            f"原 PDF 第 {ordered[0]['page']}–{ordered[-1]['page']} 页，保留为一个大章节文件。", "",
            "[阅读本章正文](chapter.md)", ""]
        body = [f"# 第{chapter}章 {title}", "",
            "> 按教材目录整理的 OCR 原文，公式未逐式校订。保留章内小节标记、来源页码和 OCR 行号。", ""]
        recovered, source_fragments, sections = [], [], []
        for i, (section, name, _) in enumerate(CONTENTS[chapter]):
            start, stop = starts[i:i+2]
            raw, fragments = render(lines, positions, start, stop)
            recovered.extend(lines[start:stop])
            source_fragments.extend(fragments)
            page_start, page_end = positions[start][0]["page"], positions[stop-1][0]["page"]
            name = "本章小结" if section == 99 else f"{chapter}.{section} {name}"
            anchor = "chapter-summary" if section == 99 else f"section-{chapter}-{section}"
            body.extend([f'<a id="{anchor}"></a>', "", f"## {name}", "", raw])
            sections.append({"title": name, "anchor": anchor, "source_pages": [page_start, page_end]})
            contents.append(f"- [{name}]({path.removeprefix(PREFIX+'/')}#{anchor})（PDF 第 {page_start}–{page_end} 页）")
            chapter_readme.append(f"- [{name}](chapter.md#{anchor})（PDF 第 {page_start}–{page_end} 页）")
        if "".join(recovered) != "".join(lines):
            raise ValueError(f"Chapter {chapter} lost OCR content")
        generated[path] = "\n".join(body).rstrip() + "\n"
        label = f"第{chapter}章 {title}"
        added.append({"path": path, "title": label, "kind": "textbook_chapter",
            "quality": "ocr_unverified", "chapter": chapter,
            "modules": [CA_MODULES[CA_CHAPTER_MAP[chapter]-1]],
            "keywords": keywords(generated[path], label), "sections": sections,
            "source_id": ordered[0]["source"]["source_id"],
            "source_name": ordered[0]["source"]["source_name"],
            "source_pages": [ordered[0]["page"], ordered[-1]["page"]],
            "source_fragments": source_fragments, "characters": sum(map(len, lines))})
        contents.append("")
        source_links = " · ".join(f"[{item['source_pages'][0]}–{item['source_pages'][1]}]({Path(item['path']).name})"
                                  for item in originals if f"/{folder}/" in item["path"])
        generated[base+"/README.md"] = "\n".join(chapter_readme) + "\n\n原始页段（供回查）：" + source_links + "\n"
    for item in originals:
        item["kind"] = "archive"
    retained = [item for item in data["items"] if not ("/Textbook/" in item["path"]
                and item["path"].endswith("/chapter.md"))]
    data["items"] = retained + added
    data["contents"] = PREFIX + "/contents.md"
    generated[INDEX] = dump(data)
    generated[data["contents"]] = "\n".join(contents).rstrip() + "\n"
    readme_path = PREFIX + "/Textbook/README.md"
    readme = (ROOT / readme_path).read_text(encoding="utf-8-sig")
    readme = readme.replace("按理论、习题与答案分开缓存，页码可回溯到桌面原文件。",
        "按教材目录分为 8 个大章节文件，1.1、1.2 等小节保留为章内标题标记。\n\n[完整章节目录](../contents.md)")
    generated[readme_path] = readme
    return generated, len(added)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    generated, count = build()
    for name, text in generated.items():
        path = ROOT / name
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8-sig") != text:
                raise SystemExit(f"Out of date: {name}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8", newline="\n")
    print(f"{'Verified' if args.check else 'Generated'} {count} chapter files with 38 section markers and 8 summaries")


if __name__ == "__main__":
    main()
