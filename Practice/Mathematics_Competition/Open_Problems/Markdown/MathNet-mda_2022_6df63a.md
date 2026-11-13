# MathNet-mda_2022_6df63a

求所有可导函数 $f:(0,+\infty)\to(0,+\infty)$，使 $f(1/2)=1$ 且 $f\prime(x)=-f^3(x)$。

答案与解析：

["Avem $\\left(f^{-2}(x)\\right)' = -2 f^{-3}(x) f'(x) = 2 f^{-3}(x) f^{3}(x) = 2$, adică derivata funcției $f^{-2}(x)$ este o constantă. Rezultă că funcția $f^{-2}(x)$ reprezintă o funcție liniară, ce poate fi scrisă în forma $f^{-2}(x) = a x + b$.\n\nDerivând, obținem $2 = \\left(f^{-2}(x)\\right)' = a$.\n\nÎn plus, din condiția $f\\left(\\frac{1}{2}\\right) = 1$ avem $1 = f^{-2}\\left(\\frac{1}{2}\\right) = 2 \\cdot \\frac{1}{2} + b = 1 + b$, ceea ce implică $b = 0$.\n\nObținem $f^{-2}(x) = 2x$, adică $f(x) = \\frac{1}{\\sqrt{2x}}$.\n\nObservăm că această funcție este definită pe întreg intervalul $(0, +\\infty)$ și este derivabilă pe același interval. Avem $f\\left(\\frac{1}{2}\\right) = \\frac{1}{\\sqrt{2 \\cdot \\frac{1}{2}}} = 1$ și\n$$\nf'(x) = \\left(\\frac{1}{\\sqrt{2x}}\\right)' = \\left(\\frac{1}{\\sqrt{2}} x^{-1/2}\\right)' = \\frac{1}{\\sqrt{2}} \\cdot \\left(-\\frac{1}{2}\\right) x^{-3/2} = -\\left(\\frac{1}{\\sqrt{2}} x^{-1/2}\\right)^3 = -f^3(x)\n$$\nDeci, funcția $f:(0,+\\infty) \\rightarrow (0,+\\infty)$, $f(x) = \\frac{1}{\\sqrt{2x}}$, este unica ce verifică condiția problemei."]

来源：https://mathnet.mit.edu/explorer.html#problem=mda_2022_6df63a

许可：CC BY 4.0

署名：Shaden Alshammari et al., MathNet: A Global Multimodal Benchmark for Mathematical Reasoning and Retrieval, ICLR 2026; Moldova Mathematical Olympiad, 2022, Moldova

改动：由 MathNet 罗马尼亚语题干翻译为中文；保留原题数据与原始题干，不宣称为全国大学生数学竞赛真题。
