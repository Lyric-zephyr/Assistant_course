<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC15%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6A%E7%B1%BB-%E5%88%9D%E8%B5%9B-2023.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第十五届全国大学生数学竞赛初赛试题及参考答案（非数学 A 类）

> **年份**：2023 年（第十五届）｜**类别**：非数学专业 A 类（理工类）
> **考试形式**：闭卷｜**时间**：150 分钟｜**满分**：100 分
> **来源**：原始文件 `../第十五届全国大学生数学竞赛初赛（非数学A类）试题及参考答案.pdf`（卷面标题：「第十五届全国大学生数学竞赛初赛试卷参考答案（非数学 A 类，2023 年）」；页面带「大学生数学竞赛网 www.cmathc.org.cn」水印）
> **转录说明**：原卷为扫描版，本文件由视觉逐页转写，公式采用 KaTeX 语法；「答案」与「解答」均来自原卷参考答案，评分标注（如"（5 分）"）为原卷过程分点。

---

## 卷面结构

| 题号 | 一 | 二 | 三 | 四 | 五 | 六 | 总分 |
|---|---|---|---|---|---|---|---|
| 满分 | 30 | 14 | 14 | 14 | 14 | 14 | 100 |
| 形式 | 填空题 ×5 | 解答题 | 解答题 | 解答题 | 解答题 | 解答题 | |

> **卷头注意事项（原卷）**：
> 1. 所有答题都须写在本试卷指定的答题区域内.
> 2. 密封线左边请勿答题, 密封线外不得有姓名及相关标记.
> 3. 如答题空白不够, 可写在当页背面, 并标明题号.

---

## 一、填空题（本题 30 分，每小题 6 分）

**(1)** $\lim\limits_{x\to 3}\dfrac{\sqrt{x^3+9}-6}{2-\sqrt{x^3-23}} = \underline{\qquad}$。

> **答案**：$-\dfrac{1}{3}$
>
> **解答**：使用洛必达法则, 得
> $$\lim_{x\to 3}\frac{\sqrt{x^3+9}-6}{2-\sqrt{x^3-23}} = \lim_{x\to 3}\frac{\dfrac{3x^2}{2\sqrt{x^3+9}}}{-\dfrac{3x^2}{2\sqrt{x^3-23}}} = -\lim_{x\to 3}\frac{\sqrt{x^3-23}}{\sqrt{x^3+9}} = -\frac{1}{3}.$$

**(2)** 设 $z = f(x^2-y^2,\,xy)$, 且 $f(u,v)$ 有连续的二阶偏导数, 则 $\dfrac{\partial^2 z}{\partial y} = \underline{\qquad}$。

> 注：此处原卷题面印为 $\dfrac{\partial^2 z}{\partial y}$，疑为排版时脱漏 $\partial x$；对照解答过程（先求 $z_x$，再对 $y$ 求偏导），题面正确应为 $\dfrac{\partial^2 z}{\partial x\partial y}$。
>
> **答案**：$f_2 - 4xy f_{11} + 2(x^2-y^2) f_{12} + xy f_{22}$
>
> **解答**：
> $$z_x = 2xf_1 + yf_2,$$
> $$z_{xy} = 2x\left(f_{11}(-2y) + xf_{12}\right) + f_2 + y\left(f_{21}(-2y) + xf_{22}\right)$$
> $$= f_2 - 4xy f_{11} + 2(x^2-y^2) f_{12} + xy f_{22}.$$

**(3)** 设 $f(x) = \dfrac{1}{x^2-3x+2}$, 则 $f^{(n)}(0) = \underline{\qquad}$。

> **答案**：$n!\left(1-\dfrac{1}{2^{n+1}}\right)$
>
> **解答**：
> $$f(x) = -\frac{1}{x-1} + \frac{1}{x-2}.$$
> $$f^{(n)}(x) = (-1)^{n+1}\cdot n!\left(\frac{1}{(x-1)^{n+1}} - \frac{1}{(x-2)^{n+1}}\right).$$
> $$f^{(n)}(0) = n!\left(1-\frac{1}{2^{n+1}}\right).$$

**(4)** 幂级数 $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}x^{2n}}{n(2n-1)}$ 的收敛域为 $\underline{\qquad}$。

> **答案**：$[-1,\,1]$
>
> **解答**：因为 $\lim\limits_{n\to\infty}\sqrt[n]{\dfrac{1}{n(2n-1)}} = 1$, 所以收敛半径为 1. 当 $x = \pm 1$ 时, $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n(2n-1)}$ 绝对收敛, 故收敛域为 $[-1,1]$.

**(5)** 设曲面 $\Sigma$ 是平面 $y+z=5$ 被柱面 $x^2+y^2=25$ 所截得的部分, 则 $\displaystyle\iint_{\Sigma}(x+y+z)\,\mathrm{d}S = \underline{\qquad}$。

> **答案**：$125\sqrt{2}\,\pi$
>
> **解答**：$\Sigma$ 的方程为 $z = 5-y$, 故
> $$\mathrm{d}S = \sqrt{2}\,\mathrm{d}x\mathrm{d}y.$$
> $\Sigma$ 在 $xOy$ 平面的投影 $D_{xy}: x^2+y^2 \leqslant 25$, 故
> $$I = \sqrt{2}\iint_{D_{xy}}(x+5)\,\mathrm{d}x\mathrm{d}y = 5\sqrt{2}\iint_{D_{xy}}\,\mathrm{d}x\mathrm{d}y = 125\sqrt{2}\,\pi.$$

---

## 二、（本题 14 分）

解方程
$$(x^2+y^2+3)\frac{\mathrm{d}y}{\mathrm{d}x} = 2x\left(2y - \frac{x^2}{y}\right).$$

> **解答**：原方程变形为
> $$\frac{y\,\mathrm{d}y}{x\,\mathrm{d}x} = \frac{2(2y^2-x^2)}{x^2+y^2+3}.$$
> 令 $u = x^2$, $v = y^2$, 则原方程化为
> $$\frac{\mathrm{d}v}{\mathrm{d}u} = \frac{2(2v-u)}{u+v+3}. \qquad\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \quad（5 分）$$
> 解方程 $2v-u = 0$, $u+v+3 = 0$, 得到 $u = -2$, $v = -1$, 再令 $U = u+2$, $V = v+1$, 上述方程化为
> $$\frac{\mathrm{d}V}{\mathrm{d}U} = \frac{2(2V-U)}{U+V}. \qquad\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \quad（8 分）$$
> 作变量替换 $W = \dfrac{V}{U}$ 得到
> $$U\frac{\mathrm{d}W}{\mathrm{d}U} = -\frac{W^2-3W+2}{W+1}. \qquad\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \quad（11 分）$$
> 这是分离变量方程, 解之得 $U(W-2)^3 = C(W-1)^2$, 回代得
> $$(y^2-2x^2-3)^3 = C(y^2-x^2-1)^2. \qquad\cdots\cdots\cdots\cdots\cdots\cdots \quad（14 分）$$

---

## 三、（本题 14 分）

设 $\Sigma_1$ 是以 $(0,4,0)$ 为顶点且与曲面 $\Sigma_2: \dfrac{x^2}{3}+\dfrac{y^2}{4}+\dfrac{z^2}{3}=1\ (y>0)$ 相切的圆锥面, 求曲面 $\Sigma_1$ 与 $\Sigma_2$ 所围成的空间区域的体积.

> **解答**：设 $L$ 是 $xOy$ 平面上过点 $(0,4)$ 且与 $\dfrac{x^2}{3}+\dfrac{y^2}{4}=1$ 相切于点 $(x_0,y_0)$ 的直线, 则
> $$\frac{x_0^2}{3}+\frac{y_0^2}{4} = 1 \ \text{且切线斜率}\ \frac{y_0-4}{x_0} = -\frac{4x_0}{3y_0}, \ \text{解得}\ x_0 = \pm\frac{3}{2},\, y_0 = 1.$$
> ……（5 分）
>
> 显然, $\Sigma_1$ 与 $\Sigma_2$ 分别是切线 $L$ 和曲线 $\dfrac{x^2}{3}+\dfrac{y^2}{4}=1$ 绕 $y$ 轴旋转而成的曲面, 它们的交线位于平面 $y_0 = 1$ 上. ……（8 分）
>
> 记该平面与 $\Sigma_1$, $\Sigma_2$ 围成的空间区域分别记为 $\Omega_1$ 和 $\Omega_2$.
>
> 由于 $\Sigma_1$ 是底面圆的半径为 $\dfrac{3}{2}$, 高为 3 的圆锥体, 所以其体积 $V_1 = \dfrac{1}{3}\cdot\pi\cdot\left(\dfrac{3}{2}\right)^2\cdot 3 = \dfrac{9\pi}{4}$. 又 $\Omega_2$ 的体积为
> $$V_2 = \iiint_{\Omega_2}\mathrm{d}V = \int_1^2 \mathrm{d}y\iint_{x^2+z^2 \leqslant 3\left(1-\frac{y^2}{4}\right)}\mathrm{d}x\mathrm{d}z = \pi\int_1^2 3\left(1-\frac{y^2}{4}\right)\mathrm{d}y = \frac{5\pi}{4}.$$
> 因此, 曲面 $\Sigma_1$ 与 $\Sigma_2$ 所围成的空间区域的体积为 $\dfrac{9\pi}{4}-\dfrac{5\pi}{4} = \pi$. ……（14 分）

---

## 四、（本题 14 分）

设 $I_n = n\displaystyle\int_1^a \frac{\mathrm{d}x}{1+x^n}$, 其中 $a > 1$. 求极限 $\lim\limits_{n\to\infty} I_n$.

> **解答**：记 $b = \dfrac{1}{a}$, 则 $0 < b < 1$. 作变量替换 $x = \dfrac{1}{t}$, 得到
> $$I_n = \int_b^1 \frac{nt^{n-1}}{t(1+t^n)}\mathrm{d}t = \int_b^1 \frac{\mathrm{d}\left(\ln(1+t^n)\right)}{t}.$$
> 分部积分得
> $$I_n = \ln 2 - \frac{\ln(1+b^n)}{b} + \int_b^1 \frac{\ln(1+t^n)}{t^2}\mathrm{d}t. \qquad\cdots\cdots\cdots\cdots \quad（8 分）$$
> 当 $t \in [b,1]$ 时, $\dfrac{\ln(1+t^n)}{t^2} \leqslant t^{n-2}$,
> $$0 \leqslant \int_b^1 \frac{\ln(1+t^n)}{t^2}\mathrm{d}t \leqslant \int_b^1 t^{n-2}\mathrm{d}t = \frac{1-b^{n-1}}{n-1}.$$
> 显然, $\lim\limits_{n\to\infty}\dfrac{1-b^{n-1}}{n-1} = 0$. 由夹逼准则, $\lim\limits_{n\to\infty}\displaystyle\int_b^1 \frac{\ln(1+t^n)}{t^2}\mathrm{d}t = 0$.
> 又 $\lim\limits_{n\to\infty}\dfrac{\ln(1+b^n)}{b} = 0$, $\lim\limits_{n\to\infty} I_n = \ln 2$. ……（14 分）

---

## 五、（本题 14 分）

设 $f(x)$ 在 $[0,1]$ 上有连续的导数且 $f(0) = 0$. 求证:
$$\int_0^1 f^2(x)\,\mathrm{d}x \leqslant 4\int_0^1 (1-x)^2|f'(x)|^2\,\mathrm{d}x,$$
并求使上式成为等式的 $f(x)$.

> **解答**：由分部积分法
> $$\int_0^1 f^2(x)\mathrm{d}x = (x-1)f^2(x)\Big|_0^1 - \int_0^1 (x-1)2f(x)f'(x)\mathrm{d}x = 2\int_0^1 (1-x)f'(x)\cdot f(x)\mathrm{d}x.$$
> ……（4 分）
>
> 由 Cauchy 积分不等式, 有
> $$\int_0^1 (1-x)f'(x)\cdot f(x)\mathrm{d}x \leqslant \left(\int_0^1 (1-x)^2\left(f'(x)\right)^2\mathrm{d}x\right)^{\frac{1}{2}}\left(\int_0^1 f^2(x)\mathrm{d}x\right)^{\frac{1}{2}}.$$
> 于是
> $$\int_0^1 f^2(x)\mathrm{d}x \leqslant 4\int_0^1 (1-x)^2|f'(x)|^2\mathrm{d}x. \qquad\cdots\cdots\cdots\cdots \quad（10 分）$$
> 等式成立时应有常数 $c$ 使得 $(1-x)f'(x) = cf(x)$. 因此当 $x \in (0,1)$ 时, 有
> $$\left((1-x)^c f(x)\right)' = (1-x)^{c-1}\left((1-x)f'(x) - cf(x)\right) = 0.$$
> 因而存在常数 $d$ 使得 $f(x) = d(1-x)^{-c}$ $(0 < x < 1)$.
> 当 $x \to 0$ 时, $f(x) \to 0$, 故 $d = 0$. 于是 $f = 0$. 所以使得题中不等式成为等式的函数是 $f(x) = 0$. ……（14 分）

---

## 六、（本题 14 分）

设数列 $\{x_n\}$ 满足 $x_0 = \dfrac{1}{3}$,
$$x_{n+1} = \frac{x_n^2}{1-x_n+x_n^2},\quad n \geqslant 0.$$
证明: 无穷级数 $\displaystyle\sum_{n=0}^{\infty} x_n$ 收敛并求和.

> **解答**（方法 1）：根据数学归纳法可知 $x_n > 0$.
>
> 此外, $x_{n+1} - x_n = -\dfrac{x_n(1-x_n)^2}{1-x_n+x_n^2} < 0$.
>
> 故 $x_n$ 单调递减, $x_n \leqslant \dfrac{1}{3}$.
>
> 于是, $x_{n+1} = x_n\cdot\dfrac{x_n}{1-x_n+x_n^2} \leqslant \dfrac{4}{9}x_n$, $x_n$ 收敛于 0. ……（6 分）
>
> 令 $f(x) = \dfrac{x}{1+x}$, $x > 0$, 不难验证 $f(x)$ 严格单调递增且其反函数为 $f^{-1}(x) = \dfrac{x}{1-x}$.
>
> 注意到 $x_{n+1} = f\left(f^{-1}(x_n) - x_n\right)$, 故
> $$f^{-1}(x_{n+1}) = f^{-1}(x_n) - x_n, \qquad x_n = f^{-1}(x_n) - f^{-1}(x_{n+1}).$$
> $$\sum_{i=0}^n x_i = f^{-1}(x_0) - f^{-1}(x_{n+1}).$$
> $$\sum_{i=0}^{\infty} x_i = f^{-1}(x_0) - f^{-1}(0) = \frac{1}{2}. \qquad\cdots\cdots\cdots\cdots \quad（14 分）$$

> **解答**（方法 2）：证明 $x_n$ 收敛于 0 同方法 1.
>
> 注意到
> $$x_n = \frac{x_n}{1-x_n} - \frac{x_{n+1}}{1-x_{n+1}}.$$
> $$\sum_{i=0}^n x_i = \frac{x_0}{1-x_0} - \frac{x_{n+1}}{1-x_{n+1}}.$$
> $$\sum_{i=0}^{\infty} x_i = \frac{x_0}{1-x_0} = \frac{1}{2}. \qquad\cdots\cdots\cdots\cdots \quad（14 分）$$

---

## 附：本卷考点分布速览

| 题号 | 分值 | 考点板块 | 具体考点 |
|---|---|---|---|
| 一(1) | 6 | 极限 | 洛必达法则求 $\frac{0}{0}$ 型极限 |
| 一(2) | 6 | 多元微分 | 二阶混合偏导数（复合函数链式法则） |
| 一(3) | 6 | 高阶导数 | 有理函数裂项 + $n$ 阶导数公式 |
| 一(4) | 6 | 幂级数 | 收敛半径（根值法）+ 端点收敛性判定 |
| 一(5) | 6 | 曲面积分 | 第一类曲面积分（投影法 + 对称性） |
| 二 | 14 | 常微分方程 | 变量替换（两次）+ 齐次方程（分离变量求解） |
| 三 | 14 | 空间解析几何 / 重积分 | 旋转曲面切线与交线 + 体积（圆锥体积 − 三重积分截面法） |
| 四 | 14 | 极限 | 换元 + 分部积分 + 夹逼准则 |
| 五 | 14 | 积分不等式 | Cauchy 积分不等式 + 等号条件（化为微分方程） |
| 六 | 14 | 级数 | 递推数列单调有界 + 裂项相消求级数和 |
