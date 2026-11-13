# MathNet-mda_2023_dfee3a

计算 $\int_0^\pi\sqrt{1+\cos(4046x)}\,dx$。

答案与解析：

['Utilizând periodicitatea funcției $f(t)=\\cos t$, obținem\n$$\n\\begin{gathered}\n\\int_{0}^{\\pi} \\sqrt{1+\\cos (4046 x)}\\, d x = \\sqrt{2} \\int_{0}^{\\pi} |\\cos (2023 x)|\\, d x =\n\\left|\\begin{array}{c}\nt = 2023 x \\\\\nd x = \\frac{1}{2023} d t \\\\\nx = 0 \\Rightarrow t = 0 \\\\\nx = \\pi \\Rightarrow t = 2023 \\pi\n\\end{array}\\right| =\n\\frac{\\sqrt{2}}{2023} \\int_{0}^{2023 \\pi} |\\cos t|\\, d t\n$$\nObservăm că $2023$ este impar, deci $2023 \\pi = 1011 \\cdot 2\\pi + \\pi$. Astfel,\n$$\n\\int_{0}^{2023 \\pi} |\\cos t|\\, d t = 1011 \\int_{0}^{2\\pi} |\\cos t|\\, d t + \\int_{0}^{\\pi} |\\cos t|\\, d t\n$$\nDar $\\int_{0}^{2\\pi} |\\cos t|\\, d t = 4$ și $\\int_{0}^{\\pi} |\\cos t|\\, d t = 2$.\nAșadar,\n$$\n\\int_{0}^{2023 \\pi} |\\cos t|\\, d t = 1011 \\cdot 4 + 2 = 4046\n$$\nPrin urmare,\n$$\n\\int_{0}^{\\pi} \\sqrt{1+\\cos (4046 x)}\\, d x = \\frac{\\sqrt{2}}{2023} \\cdot 4046 = 2\\sqrt{2}\n$$']

来源：https://mathnet.mit.edu/explorer.html#problem=mda_2023_dfee3a

许可：CC BY 4.0

署名：Shaden Alshammari et al., MathNet: A Global Multimodal Benchmark for Mathematical Reasoning and Retrieval, ICLR 2026; Moldova Mathematical Olympiad, 2023, Moldova

改动：由 MathNet 罗马尼亚语题干翻译为中文；保留原题数据与原始题干，不宣称为全国大学生数学竞赛真题。
