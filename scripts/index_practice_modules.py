"""Index exercises by learning module while preserving complete exam papers.

Chapter catalogs link to the existing source text, without duplicating papers.
Topic tags are retrieval hints, not certification of OCR or mathematical scope.
Run --check to verify the generated catalogs and indexes without writing.
"""

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import re

from build_course_index import ROOT, CA_CHAPTER_MAP, CA_MODULES, dump

CA_NAMES = ["复数与复变函数", "解析函数及应用", "复变函数的积分", "级数概念及分类",
            "留数相关及应用", "傅里叶变换相关", "拉普拉斯之变换"]
MATH_MODULES = ["01_limit", "02_diff1", "03_int1", "04_diffn", "05_intn", "06_series"]
MATH_NAMES = ["极限与连续", "一元微分学", "一元积分学", "多元微分学", "多元积分学", "级数与方程"]
PAGE = re.compile(r"(?ms)^## 原文件第 (\d+) 页[^\n]*\n\n```text\n(.*?)\n```")
TERMS = {
    "Complex_Analysis": [
        r"复数|辐角|幅角|共轭复数|复平面|开方|点集|单连通|多连通|complex number|argument of",
        r"解析函数|可导|调和|cauchy.riemann|C-R|保形|分式线性|单值分支|analytic|harmonic|conformal",
        r"柯西.*(?:定理|公式)|复积分|复变函数.*积分|原函数|路径无关|积分.*dz|contour|cauchy.*integral",
        r"级数|收敛半径|收敛圆|收敛环|洛朗|泰勒|laurent|taylor|power series|convergence",
        r"留数|奇点|极点|零点阶|主值|辐角原理|儒歇|residue|pole|singular|fresnel|rouch",
        r"傅里叶|傅氏|fourier|广义函数|单位脉冲|dirac|频谱",
        r"拉普拉斯|拉氏|laplace|终值定理|初值问题|初值定理",
    ],
    "Mathematics_Competition": [
        r"极限|连续|间断|无穷小|无穷大|夹逼|单调有界|stolz|\\lim\b",
        r"导数|求导|微分中值|罗尔|拉格朗日中值|高阶导|单调性|凹凸|切线|一元微分|derivative",
        r"定积分|不定积分|反常积分|变限积分|积分不等式|积分证明|旋转体|面积|分部积分|换元积分|integral",
        r"多元微分|多元函数微分|偏导|全微分|隐函数|方向导数|梯度|多元极值|条件极值|切平面|平面方程|空间解析几何|\\partial",
        r"重积分|曲线积分|曲面积分|三重积分|二重积分|格林|高斯公式|斯托克斯|通量|散度|\\iint|\\iiint|\\oint",
        r"级数|微分方程|收敛域|收敛半径|傅里叶|特征方程|伯努利|\\sum\b|differential equation",
    ],
}


def body(text):
    pages = list(PAGE.finditer(text))
    if pages:
        return "\n".join(page[2] for page in pages)
    return re.sub(r"(?ms)<!--.*?-->", "", text)


def tag(text, subject):
    keys = CA_MODULES if subject == "Complex_Analysis" else MATH_MODULES
    return [key for key, pattern in zip(keys, TERMS[subject]) if re.search(pattern, text, re.I)]


def line_spans(text, subject):
    """Conservative question boundaries: printed major headings or explicit Markdown numbering."""
    lines = text.splitlines()
    boundaries, fill_section, section = [], False, ""
    topics = {}
    if subject == "Mathematics_Competition":
        for line in lines:
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if line.startswith("|") and len(cells) >= 4 and re.fullmatch(r"[一二三四五六七八九十]+(?:[（(]\d+[)）])?", cells[0]):
                hint = " ".join(cells[2:])
                modules = tag(hint, subject)
                if "积分" in hint and not any(m in modules for m in ("03_int1", "05_intn")):
                    modules.append("03_int1")
                if "微分" in hint and not any(m in modules for m in ("02_diff1", "04_diffn", "06_series")):
                    modules.append("02_diff1")
                topics[cells[0].replace("（", "(").replace("）", ")")] = modules
    for n, line in enumerate(lines):
        major = re.match(r"^##\s+(?:第([一二三四五六七八九十]+)题|([一二三四五六七八九十]+)、)", line)
        fill = re.match(r"^\*\*\(?[（]?(\d+)[)）]\*\*", line)
        if major:
            section = major[1] or major[2]
            fill_section = "填空" in line
            boundaries.append((n, section))
        elif fill and fill_section:
            # Large-question subparts stay together with their shared assumptions.
            boundaries.append((n, f"{section}({fill[1]})"))
    appendix = next((i for i, line in enumerate(lines) if line.startswith("## 附")), len(lines))
    boundaries = [(n, label) for n, label in boundaries if n < appendix]
    spans = []
    for i, (start, label) in enumerate(boundaries):
        stop = boundaries[i+1][0] if i+1 < len(boundaries) else appendix
        fragment = "\n".join(lines[start:stop])
        modules = topics.get(label) or tag(fragment, subject)
        if len(fragment.strip()) < 30:
            continue
        spans.append({"label": label, "lines": [start+1, stop], "modules": modules,
                      "classification": "source_topic_table" if topics.get(label) else "keyword_inferred"})
    return spans


def page_spans(text, mapping):
    spans = []
    for page in PAGE.finditer(text):
        modules = mapping.get(int(page[1]), [])
        if modules:
            spans.append({"label": f"PDF 第 {page[1]} 页", "lines": [text.count("\n", 0, page.start())+1,
                text.count("\n", 0, page.end())+1], "modules": modules, "classification": "chapter_pages"})
    return spans


def collection_key(item):
    path = item["path"]
    for role in ("/Questions/", "/Solutions/", "/Answers/", "/Partial_Answers/"):
        if role in path:
            return path.split(role, 1)[0]
    if "/Textbook_Exercises/" in path and "/Answers/" not in path:
        return str(Path(path).parent)
    return path


def role(item):
    return ("Solutions" if any(part in item["path"] for part in ("/Solutions/", "/Answers/", "/Partial_Answers/"))
            else "Questions")


def build_complex():
    prefix = "Practice/Complex_Analysis"
    data = json.loads((ROOT / prefix / "index.json").read_text(encoding="utf-8-sig"))
    items = data["items"]
    groups = defaultdict(list)
    for item in items:
        path = item["path"]
        text = (ROOT / path).read_text(encoding="utf-8-sig")
        contents = body(text)
        modules, method = [], "keyword_inferred"
        chapter = re.search(r"/(?:Textbook_Exercises|Workbook)/(\d{2}|Exercises_(\d{2}))", path)
        topical = re.search(r"/Comprehensive/Set_(0[1-7])/", path)
        if chapter:
            number = int(chapter[2] or chapter[1])
            modules = [CA_MODULES[CA_CHAPTER_MAP[number]-1]]
            method = "chapter_directory"
        elif topical:
            modules = [CA_MODULES[int(topical[1])-1]]
            method = "topic_collection"
        else:
            modules = tag(contents, "Complex_Analysis")
        item["kind"] = "past_paper" if "/Exams/" in path else "exercise"
        if "/Front_Matter/" in path:
            item["kind"] = "archive"
        item["role"] = role(item)
        item["modules"] = modules or ["unclassified"]
        item["classification"] = method if modules else "needs_review"
        # Match the UTF-8/LF text served by GitHub despite Windows checkout line endings.
        item["source_sha256"] = hashlib.sha256(text.encode("utf-8")).hexdigest()
        if item["kind"] == "past_paper":
            item["topic_spans"] = line_spans(text, "Complex_Analysis")
        if "/Textbook_Exercises/Answers/" in path:
            page_modules = {335: [1], 336: [1], 337: [1, 2], 338: [2, 3], 339: [3, 4],
                            340: [4, 5], 341: [5, 2], 342: [2, 6], 343: [6, 7], 344: [7], 345: [7], 346: [7]}
            mapping = {p: [CA_MODULES[n-1] for n in ns] for p, ns in page_modules.items()}
            item["topic_spans"] = page_spans(text, mapping)
            item["modules"] = sorted({m for span in item["topic_spans"] for m in span["modules"]})
            item["classification"] = "chapter_pages"
        groups[collection_key(item)].append(item)
    textbook_answers = [i for i in items if "/Textbook_Exercises/Answers/" in i["path"]]
    for item in items:
        related = groups[collection_key(item)]
        if "/Textbook_Exercises/" in item["path"] and item["role"] == "Questions":
            related = textbook_answers
        item["paired_paths"] = [i["path"] for i in related if i["role"] != item["role"]
                                and set(i["modules"]) & set(item["modules"])]
        if item["paired_paths"]:
            item["pairing_level"] = "collection_not_individual_question"
    data["version"] = 3
    data["chapter_catalog"] = prefix + "/Chapters/README.md"
    return data


def build_math():
    prefix = "Practice/Mathematics_Competition"
    manifest = json.loads((ROOT / prefix / "manifest.json").read_text(encoding="utf-8-sig"))
    items, generated = [], {}
    groups = defaultdict(list)
    for source in manifest["sources"]:
        path = prefix + "/" + source["file"]
        text = (ROOT / path).read_text(encoding="utf-8-sig")
        spans = line_spans(text, "Mathematics_Competition") if "Community_Transcript" in path else []
        modules = sorted({m for span in spans for m in span["modules"]}) or tag(body(text), "Mathematics_Competition")
        title = source.get("title") or next((line.lstrip("# ") for line in text.splitlines()
                                             if line.startswith("# ")), Path(path).stem)
        item = {"path": path, "title": title, "kind": "past_paper", "role": source["role"],
            "edition": source["edition"], "stage": source["stage"], "category": source["category"],
            "session": source["session"], "modules": modules or ["unclassified"],
            "quality": "community_transcript_unverified" if "Community_Transcript" in path else "extracted_text_unverified",
            "classification": "keyword_inferred" if modules else "needs_review", "topic_spans": spans,
            "source_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()}
        items.append(item)
        groups[(source["edition"], source["stage"], source["category"], source["session"],
                "Community_Transcript" in path)].append(item)
    for group in groups.values():
        for item in group:
            item["paired_paths"] = [i["path"] for i in group if i["role"] != item["role"]]
            if item["paired_paths"]:
                item["pairing_level"] = "collection_not_individual_question"
    for name in ("mathnet_calculus", "ocw_calculus"):
        bank = prefix + "/Open_Problems/" + name + ".json"
        problems = json.loads((ROOT / bank).read_text(encoding="utf-8"))["problems"]
        for problem in problems:
            slug = re.sub(r"[^A-Za-z0-9_.-]", "_", problem["id"])
            path = prefix + "/Open_Problems/Markdown/" + slug + ".md"
            modules = [MATH_MODULES[MATH_NAMES.index(m.split("：", 1)[1])] for m in problem["modules"]]
            text = (f"# {problem['id']}\n\n{problem['problem']}\n\n答案与解析：\n\n{problem['solution']}\n\n"
                    f"来源：{problem['source']}\n\n许可：{problem['license']}\n\n"
                    f"署名：{problem.get('attribution', '')}\n\n改动：{problem.get('changes', '')}\n")
            generated[path] = text
            items.append({"path": path, "title": problem["id"], "kind": "exercise", "modules": modules,
                "role": "Questions_and_Solutions", "classification": "existing_question_tags",
                "source_bank": bank, "question_id": problem["id"], "quality": "existing_open_reference",
                "license": problem["license"]})
    return {"subject": "Mathematics_Competition", "encoding": "UTF-8", "version": 3,
            "chapter_catalog": prefix + "/Chapters/README.md", "items": items}, generated


def catalogs(data, subject, modules, names):
    prefix = "Practice/" + subject
    generated, links = {}, []
    for module, name in zip(modules, names):
        selected = [i for i in data["items"] if module in i.get("modules", []) and i["kind"] != "archive"]
        filename = module + ".md"
        lines = [f"# {name}：习题与真题参考", "", "本目录只引用原文件，不重复保存题目。"
            "标签用于检索，OCR 和关键词归类尚未逐题校订；答案按资料组关联，仍须核对原题号。", ""]
        for kind, title in (("exercise", "章节习题"), ("past_paper", "完整真题参考")):
            rows = [i for i in selected if i["kind"] == kind]
            lines.extend([f"## {title}", ""])
            if not rows:
                lines.extend(["暂无已归类资料。", ""])
            for item in rows:
                relative = Path(item["path"]).relative_to(prefix).as_posix()
                label = item["title"].replace("[", "（").replace("]", "）")
                lines.append(f"- [{label}](../{relative})（{item['role']}）")
            lines.append("")
        generated[prefix + "/Chapters/" + filename] = "\n".join(lines).rstrip() + "\n"
        links.append(f"- [{name}]({filename})（{len(selected)} 份相关源文本）")
    unclassified = [i for i in data["items"] if i.get("classification") == "needs_review" and i["kind"] != "archive"]
    generated[prefix + "/Chapters/README.md"] = ("# 按模块查找习题\n\n普通习题按模块检索；真题仍以原年份、原卷和原答案保存，"
        "可作为章节题改编参考。综合题可关联多个模块，不复制成多份原题。\n\n" + "\n".join(links)
        + (f"\n\n另有 {len(unclassified)} 份源文本尚不能可靠归类，保留在原目录供核对，不强塞入单一章节。" if unclassified else "") + "\n")
    return generated


def build():
    complex_data = build_complex()
    math_data, generated = build_math()
    for subject, data, modules, names in (("Complex_Analysis", complex_data, CA_MODULES, CA_NAMES),
                                          ("Mathematics_Competition", math_data, MATH_MODULES, MATH_NAMES)):
        prefix = "Practice/" + subject
        generated[prefix + "/index.json"] = dump(data)
        generated.update(catalogs(data, subject, modules, names))
        readme_path = prefix + "/README.md"
        text = (ROOT / readme_path).read_text(encoding="utf-8-sig")
        intro = "[按学习模块查找章节习题与真题参考](Chapters/README.md)。完整真题、题号和答案保留原结构；AI 可选取相关题目改编章节训练。\n\n"
        if intro not in text:
            pos = text.index("\n") + 1
            text = text[:pos] + "\n" + intro + text[pos:].lstrip("\n")
        generated[readme_path] = text
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
    print(("Verified" if args.check else "Generated") + " chapter exercise catalogs; complete papers unchanged")


if __name__ == "__main__":
    main()
