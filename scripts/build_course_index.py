"""Build small, lossless textbook excerpts and module/keyword indexes.

Run from any directory: python scripts/build_course_index.py [--check]
Original OCR files are retained. Source hashes use UTF-8 with LF line endings,
so Windows checkout settings do not change them. Changed OCR content requires
reviewing the section boundaries below.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LIMIT = 6000
BODY = "<!-- source-body -->\n"
MATH_MODULES = {
    1: ("01_limit",), 2: ("02_diff1",), 3: ("02_diff1",),
    4: ("03_int1",), 5: ("03_int1",), 6: ("03_int1",),
    7: ("06_series",), 8: ("04_diffn", "05_intn"), 9: ("04_diffn",),
    10: ("05_intn",), 11: ("05_intn",), 12: ("06_series",),
}
TERMS = """映射 函数 数列 极限 连续 间断点 无穷小 无穷大 等价 夹逼 单调 有界
导数 微分 中值定理 罗尔 拉格朗日 柯西 洛必达 泰勒 极值 最值 凹凸 曲率
不定积分 定积分 积分应用 原函数 换元 分部积分 有理函数 反常积分 审敛 Gamma
微分方程 齐次方程 线性方程 伯努利 降阶 常系数 特征方程 欧拉
向量 数量积 向量积 混合积 平面 直线 曲面 空间曲线
多元 极限连续 偏导 全微分 复合函数 隐函数 方向导数 梯度 多元极值 条件极值 最小二乘
重积分 二重积分 三重积分 极坐标 换元 雅可比 质心 转动惯量 含参变量
曲线积分 曲面积分 格林 Green 高斯 Gauss 斯托克斯 Stokes 通量 散度 旋度 路径无关
级数 正项 交错 绝对收敛 条件收敛 幂级数 收敛半径 收敛域 一致收敛 傅里叶 Fourier
复数 辐角 点集 区域 解析函数 C-R 调和 保形 复积分 柯西 原函数 泰勒 洛朗 留数 奇点 极点 主值
拉普拉斯 Laplace 卷积 Dirac 初值 变换""".split()

# 1-based source lines, checked against the printed contents and body (not running headers).
# The first section includes the chapter introduction. Exercises stay with their section.
CHAPTERS = [
    (1, 1, "Limits_and_Continuity", "函数与极限", 519, [
        (524, "映射与函数"), (1108, "数列的极限"), (1387, "函数的极限"),
        (1638, "无穷小与无穷大"), (1766, "极限运算法则"),
        (2066, "极限存在准则、两个重要极限"), (2336, "无穷小的比较"),
        (2496, "函数的连续性与间断点"), (2684, "连续函数的运算与初等函数的连续性"),
        (2877, "闭区间上连续函数的性质")]),
    (1, 2, "Derivatives", "导数与微分", 3111, [
        (3115, "导数概念"), (3516, "函数的求导法则"), (4072, "高阶导数"),
        (4254, "隐函数及由参数方程所确定的函数的导数、相关变化率"), (4584, "函数的微分")]),
    (1, 3, "Derivative_Applications", "微分中值定理与导数的应用", 5124, [
        (5129, "微分中值定理"), (5389, "洛必达法则"), (5660, "泰勒公式"),
        (5894, "函数的单调性与曲线的凹凸性"), (6192, "函数的极值与最大值最小值"),
        (6567, "函数图形的描绘"), (6776, "曲率"), (7088, "方程的近似解")]),
    (1, 4, "Indefinite_Integrals", "不定积分", 7315, [
        (7319, "不定积分的概念与性质"), (7646, "换元积分法"), (8306, "分部积分法"),
        (8508, "有理函数的积分"), (8751, "积分表的使用")]),
    (1, 5, "Definite_Integrals", "定积分", 8967, [
        (8971, "定积分的概念与性质"), (9377, "微积分基本公式"),
        (9647, "定积分的换元法和分部积分法"), (9994, "反常积分"),
        (10192, "反常积分的审敛法、Gamma 函数")]),
    (1, 6, "Integral_Applications", "定积分的应用", 10578, [
        (10582, "定积分的元素法"), (10643, "定积分在几何学上的应用"),
        (11081, "定积分在物理学上的应用")]),
    (1, 7, "Differential_Equations", "微分方程", 11295, [
        (11302, "微分方程的基本概念"), (11470, "可分离变量的微分方程"),
        (11700, "齐次方程"), (11898, "一阶线性微分方程"),
        (12143, "可降阶的高阶微分方程"), (12390, "高阶线性微分方程"),
        (12697, "常系数齐次线性微分方程"), (13023, "常系数非齐次线性微分方程"),
        (13322, "欧拉方程"), (13411, "常系数线性微分方程组解法举例")]),
    (2, 8, "Vectors_and_Geometry", "向量代数与空间解析几何", 329, [
        (337, "向量及其线性运算"), (746, "数量积、向量积、混合积"),
        (1116, "平面及其方程"), (1350, "空间直线及其方程"),
        (1628, "曲面及其方程"), (1920, "空间曲线及其方程")]),
    (2, 9, "Multivariable_Differentiation", "多元函数微分法及其应用", 2167, [
        (2174, "多元函数的基本概念"), (2601, "偏导数"), (2886, "全微分"),
        (3133, "多元复合函数的求导法则"), (3508, "隐函数的求导公式"),
        (3774, "多元函数微分学的几何应用"), (4191, "方向导数与梯度"),
        (4500, "多元函数的极值及其求法"), (4853, "二元函数的泰勒公式"),
        (5010, "最小二乘法")]),
    (2, 10, "Multiple_Integrals", "重积分", 5440, [
        (5446, "二重积分的概念与性质"), (5605, "二重积分的计算法"),
        (6220, "三重积分"), (6547, "重积分的应用"), (6925, "含参变量的积分")]),
    (2, 11, "Line_and_Surface_Integrals", "曲线积分与曲面积分", 7227, [
        (7232, "对弧长的曲线积分"), (7408, "对坐标的曲线积分"),
        (7745, "格林公式及其应用"), (8295, "对面积的曲面积分"),
        (8445, "对坐标的曲面积分"), (8757, "高斯公式、通量与散度"),
        (9066, "斯托克斯公式、环流量与旋度")]),
    (2, 12, "Infinite_Series", "无穷级数", 9483, [
        (9488, "常数项级数的概念和性质"), (9734, "常数项级数的审敛法"),
        (10195, "幂级数"), (10504, "函数展开成幂级数"),
        (10794, "函数的幂级数展开式的应用"),
        (11183, "函数项级数的一致收敛性及一致收敛级数的基本性质"),
        (11435, "傅里叶级数"), (11949, "一般周期函数的傅里叶级数")]),
]
HASHES = {
    1: "e38ee5951caf0b1b1280a7763d68666358eb085642e08710354143036c01ff9e",
    2: "fcc48573efd692367d4fa9964394a3fc40bf97dfb2b39a29697bbed38e0816b8",
}
BODY_END = {1: 13637, 2: 12281}  # exclusive; appendices/answers remain in originals
CA_MODULES = ["01_complex_numbers", "02_analytic_functions", "03_complex_integration",
              "04_series", "05_residues", "06_fourier", "07_laplace"]
CA_CHAPTER_MAP = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 2, 7: 6, 8: 7}
CA_NOTE_MAP = {1: 1, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 5, 8: 6, 9: 7}


def keywords(text, title):
    compact = re.sub(r"\s+", "", text)
    # Title terms first; body terms provide synonyms without making whole-book bags of words.
    return sorted(set(word for word in TERMS if word.casefold() in title.casefold())) + [
        word for word in dict.fromkeys(TERMS) if word not in title and compact.count(word) >= 2][:20]


def chunks(lines, start, stop):
    """Partition on source line boundaries, preferring sentence/paragraph endings."""
    while start < stop:
        end, size, preferred = start, 0, None
        while end < stop and size + len(lines[end]) <= LIMIT:
            size += len(lines[end])
            end += 1
            if size >= LIMIT * 0.65 and (not lines[end-1].strip() or re.search(r"[。．；？！]\s*$", lines[end-1])):
                preferred = end
        if end == start:
            raise ValueError(f"Source line {start+1} exceeds the chunk limit")
        if end < stop and preferred:
            end = preferred
        yield start, end, "".join(lines[start:end])
        start = end


def textbook_files(subject):
    prefix = f"Course/{subject}"
    items, originals, contents = [], [], ["# 同济高等数学（第七版）目录索引", "",
        "按教材正文划分章节；OCR 原文未校订。正文块保留源文件、行号和哈希，可回查原书。", ""]
    for volume in (1, 2):
        name = f"Tongji_Higher_Mathematics_7th_Edition_Volume_{volume}_OCR.md"
        source = ROOT / prefix / name
        text = source.read_text(encoding="utf-8-sig")
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        if digest != HASHES[volume]:
            raise ValueError(f"{source}: OCR changed; review source line boundaries first")
        lines = text.splitlines(keepends=True)
        original = {"path": f"{prefix}/{name}", "sha256": digest, "kind": "archive", "indexed": False,
                    "body_lines": [next(c[4] for c in CHAPTERS if c[0] == volume), BODY_END[volume]-1]}
        originals.append(original)
        chapters = [c for c in CHAPTERS if c[0] == volume]
        for j, (_, number, slug, title, chapter_start, sections) in enumerate(chapters):
            chapter_end = chapters[j+1][4] if j+1 < len(chapters) else BODY_END[volume]
            contents.extend([f"## 第{number}章 {title}", ""])
            for k, (heading_line, heading) in enumerate(sections):
                start = chapter_start if k == 0 else heading_line
                stop = sections[k+1][0] if k+1 < len(sections) else chapter_end
                assert chapter_start <= start < stop <= chapter_end
                paths, recovered = [], []
                for part, (a, b, raw) in enumerate(chunks(lines, start-1, stop-1), 1):
                    path = (f"{prefix}/Textbook/Tongji_Volume_{volume}/{number:02}_{slug}/"
                            f"section_{k+1:02}_part_{part:02}.md")
                    paths.append(path)
                    recovered.append(raw)
                    label = f"第{number}章 {title} / 第{k+1}节 {heading}"
                    payload = (f"# {label}（{part}）\n\n> OCR 原文未校订；公式请核对原书。\n"
                               f"> 来源：{name}，第 {a+1}–{b} 行。\n\n{BODY}{raw}")
                    yield path, payload
                    items.append({"path": path, "title": label, "kind": "textbook_section",
                        "quality": "ocr_unverified", "volume": volume, "chapter": number,
                        "section": k+1, "part": part, "modules": list(MATH_MODULES[number]),
                        "keywords": keywords(raw, label), "source_path": original["path"],
                        "source_sha256": digest, "source_lines": [a+1, b], "characters": len(raw)})
                assert "".join(recovered) == "".join(lines[start-1:stop-1])
                first = paths[0].removeprefix(prefix + "/")
                contents.append(f"- [{number}.{k+1} {heading}]({first})（{len(paths)} 块；源第 {start}–{stop-1} 行）")
            contents.append("")
    yield prefix + "/contents.md", "\n".join(contents).rstrip() + "\n"
    yield prefix + "/index.json", dump({"subject": subject, "encoding": "UTF-8", "version": 2,
        "contents": prefix + "/contents.md", "originals": originals, "items": items})


def complex_index():
    path = "Course/Complex_Analysis/index.json"
    data = json.loads((ROOT / path).read_text(encoding="utf-8-sig"))
    note_ranges = [(item.get("source_id"), item.get("source_pages"), CA_NOTE_MAP.get(
        int(Path(item["path"]).name.split("_", 1)[0])))
        for item in data["items"] if "/Notes/" in item["path"]]
    for item in data["items"]:
        parts = Path(item["path"]).parts
        module = None
        if "Textbook" in parts:
            name = parts[parts.index("Textbook")+1]
            if name[:2].isdigit():
                module = CA_CHAPTER_MAP[int(name.split("_", 1)[0])]
            elif name == "Transform_Tables":
                item["modules"] = CA_MODULES[-2:]
            elif name in ("Front_Matter", "References"):
                item["kind"] = "archive"
        elif "Notes" in parts:
            note = int(Path(item["path"]).name.split("_", 1)[0])
            module = CA_NOTE_MAP.get(note)
        elif "Lectures" in parts and item.get("source_pages"):
            start, stop = item["source_pages"]
            item["modules"] = sorted({CA_MODULES[number-1] for source_id, pages, number in note_ranges
                if number and pages and source_id == item.get("source_id")
                and max(start, pages[0]) <= min(stop, pages[1])})
        if module:
            item["modules"] = [CA_MODULES[module-1]]
        raw = (ROOT / item["path"]).read_text(encoding="utf-8-sig")
        item["keywords"] = keywords(raw, item["title"])
    data["version"] = 2
    yield path, dump(data)


def dump(data):
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify generated files without writing")
    args = parser.parse_args()
    generated = {}
    for subject in ("Mathematics_Competition", "Higher_Mathematics"):
        generated.update(textbook_files(subject))
    generated.update(complex_index())
    for name, text in generated.items():
        path = ROOT / name
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != text:
                raise SystemExit(f"Out of date: {name}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8", newline="\n")
    counts = Counter(name.split("/")[1] for name in generated if "/Textbook/" in name)
    print(("Verified" if args.check else "Generated"), dict(counts), "plus indexes/contents")


if __name__ == "__main__":
    main()
