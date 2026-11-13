# MathNet-mda_2023_f9cc8a

设 $I(a)=\int_{-a}^{a}\frac{dx}{(e^x+1)(|x|+a)}$（$a>0$）。证明 $I(a)$ 为常数。

答案与解析：

['$$\n\\begin{gathered}\nI(a)=\\int_{-a}^{a} \\frac{d x}{\\left(e^{x}+1\\right)(|x|+a)}=\\left|\\begin{array}{c}\nx=-t \\\\\nd x=-d t \\\\\nx=-a \\Rightarrow t=a \\\\\nx=a \\Rightarrow t=-a\n\\end{array}\\right|=\\int_{-a}^{a} \\frac{d t}{\\left(e^{-t}+1\\right)(|t|+a)}= \\\\\n\\int_{-a}^{a} \\frac{e^{t} d t}{\\left(e^{t}+1\\right)(|t|+a)}=\\int_{-a}^{a} \\frac{d t}{|t|+a}-I(a) .\n\\end{gathered}\n$$\nAtunci $I(a)=\\frac{1}{2} \\int_{-a}^{a} \\frac{d t}{|t|+a}=\\int_{0}^{a} \\frac{d t}{t+a}=\\left.\\ln (t+a)\\right|_{0} ^{a}=\\ln 2$.']

来源：https://mathnet.mit.edu/explorer.html#problem=mda_2023_f9cc8a

许可：CC BY 4.0

署名：Shaden Alshammari et al., MathNet: A Global Multimodal Benchmark for Mathematical Reasoning and Retrieval, ICLR 2026; Moldova Mathematical Olympiad, 2023, Moldova

改动：由 MathNet 罗马尼亚语题干翻译为中文；保留原题数据与原始题干，不宣称为全国大学生数学竞赛真题。
