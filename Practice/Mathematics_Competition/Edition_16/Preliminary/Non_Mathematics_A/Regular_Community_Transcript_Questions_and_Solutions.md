<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC16%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6A%E7%B1%BB-%E5%88%9D%E8%B5%9B-2024.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第十六届全国大学生数学竞赛初赛试题及参考答案（非数学 A 类）

> **年份**：2024 年（第十六届）｜**类别**：非数学专业 A 类（理工类）
> **考试形式**：闭卷｜**时间**：150 分钟｜**满分**：100 分
> **来源**：大学生数学竞赛网（cmathc.org.cn）官方转载 PDF｜原始文件：`../第十六届全国大学生数学竞赛初赛（非数学A类）试题及答案解析.pdf`
> **转录说明**：原卷为扫描版（共 10 页），本文件由视觉逐页转写，公式采用 KaTeX 语法；「解答」过程均来自原卷参考答案，「答案」为原卷解答的最终结果；评分标注（如"（6分）"）为原卷过程分点，照原卷保留。

---

## 卷面结构

| 题号 | 一 | 二 | 三 | 四 | 五 | 六 | 总分 |
|---|---|---|---|---|---|---|---|
| 满分 | 30 | 14 | 14 | 14 | 14 | 14 | 100 |
| 形式 | 填空题 ×5 | 解答题 | 解答题 | 解答题 | 解答题 | 解答题 | |

> **原卷卷首「注意」事项**：
> 1. 所有答题都须写在本试卷指定的答题区域内.
> 2. 密封线左边请勿答题，密封线外不得有姓名及相关标记.
> 3. 如答题空白不够，可写在当页背面，并标明题号.

---

## 一、填空题（本题 30 分，每小题 6 分）

**(1)** $\displaystyle\int_0^1 \ln(1+x^2)\,\mathrm{d}x = \underline{\qquad}$。

> **答案**：$\ln 2 - 2 + \dfrac{\pi}{2}$
>
> **解答**：
> $$\int \ln(1+x^2)\,\mathrm{d}x = x\ln(1+x^2) - \int \frac{2x^2}{1+x^2}\,\mathrm{d}x = x\ln(1+x^2) - 2x + 2\arctan x + C.$$
> 故原式等于 $\ln 2 - 2 + \dfrac{\pi}{2}$。

**(2)** 设 $D: x^2+y^2 \leqslant r^2$，其中 $r > 0$。则
$$\lim_{r\to 0^+}\frac{\displaystyle\iint_D \left(\mathrm{e}^{x^2+y^2}-1\right)\mathrm{d}x\,\mathrm{d}y}{r^4} = \underline{\qquad}.$$

> **答案**：$\dfrac{\pi}{2}$
>
> **解答**：利用极坐标变换 $x = \rho\cos\theta$，$y = \rho\sin\theta$，则
> $$\iint_D \left(\mathrm{e}^{x^2+y^2}-1\right)\mathrm{d}x\,\mathrm{d}y = 2\pi\int_0^r \left(\mathrm{e}^{\rho^2}-1\right)\rho\,\mathrm{d}\rho = \pi\left(\mathrm{e}^{r^2}-1-r^2\right).$$
> 注意，$r \to 0^+$ 时，$\mathrm{e}^{r^2}-1-r^2 = \dfrac{r^4}{2} + o(r^4)$，故原式 $= \dfrac{\pi}{2}$。

**(3)** 已知函数 $z = f(xy,\, \mathrm{e}^{x+y})$，且 $f(x,y)$ 具有二阶连续偏导数。则
$$\frac{\partial^2 z}{\partial x\partial y} = \underline{\qquad}.$$

> **答案**：$xyf_{11} + (x+y)\mathrm{e}^{x+y}f_{12} + \mathrm{e}^{2(x+y)}f_{22} + f_1 + \mathrm{e}^{x+y}f_2$
>
> **解答**：
> $$z_x = yf_1 + \mathrm{e}^{x+y}f_2.$$
> $$z_{xy} = \left(xf_{11} + \mathrm{e}^{x+y}f_{12}\right)y + f_1 + \left(xf_{21} + \mathrm{e}^{x+y}f_{22}\right)\mathrm{e}^{x+y} + \mathrm{e}^{x+y}f_2$$
> $$= xyf_{11} + (x+y)\mathrm{e}^{x+y}f_{12} + \mathrm{e}^{2(x+y)}f_{22} + f_1 + \mathrm{e}^{x+y}f_2.$$

**(4)** 直线 $L: \dfrac{x-1}{1} = \dfrac{y}{1} = \dfrac{z-1}{-1}$ 在平面 $\pi: x - y + 2z - 1 = 0$ 上的投影直线 $L_0$ 的单位方向向量为 $\underline{\qquad}$。

> **答案**：$\pm\left(-\dfrac{4}{\sqrt{21}},\ -\dfrac{2}{\sqrt{21}},\ \dfrac{1}{\sqrt{21}}\right)$
>
> **解答**：直线 $L$ 的一般式方程为 $\begin{cases} x - y - 1 = 0, \\ y + z - 1 = 0. \end{cases}$ 这样，过 $L$ 的平面束方程为
> $$x - y - 1 + \lambda(y + z - 1) = 0, \qquad 即 \qquad x + (\lambda-1)y + \lambda z - 1 - \lambda = 0,$$
> 其中 $\lambda$ 为参数。平面的法向量为 $(1,\, \lambda-1,\, \lambda)$。
> 此法向量与平面 $\pi$ 的法向量垂直当且仅当 $(1,\, \lambda-1,\, \lambda)\cdot(1,\, -1,\, 2) = 0$，即 $\lambda = -2$。
> 从而，过 $L$ 且与平面 $\pi$ 垂直的平面为 $x - 3y - 2z + 1 = 0$。于是，投影直线 $L_0$ 的方程为
> $$\begin{cases} x - 3y - 2z + 1 = 0, \\ x - y + 2z - 1 = 0. \end{cases}$$
> 由此，$L_0$ 的方向向量为 $(-4,\, -2,\, 1)$。故单位方向向量为 $\pm\left(-\dfrac{4}{\sqrt{21}},\ -\dfrac{2}{\sqrt{21}},\ \dfrac{1}{\sqrt{21}}\right)$。
> 注：单位方向向量有两个，得到一个即可。

**(5)** 设 $L$ 为圆周 $x^2+y^2 = 9$，取逆时针方向，则第二型曲线积分
$$\int_L \frac{-y}{4x^2+y^2}\,\mathrm{d}x + \frac{x}{4x^2+y^2}\,\mathrm{d}y = \underline{\qquad}.$$

> **答案**：$\pi$
>
> **解答**：记 $P = \dfrac{-y}{4x^2+y^2}$，$Q = \dfrac{x}{4x^2+y^2}$，$L_1: 4x^2+y^2 = 4$，取顺时针方向。
> 在 $L$ 与 $L_1$ 所围成的环状区域内，$P$，$Q$ 都是连续可微的且 $Q_x - P_y \equiv 0$。根据 Green 公式，
> $$\int_{L+L_1} P\,\mathrm{d}x + Q\,\mathrm{d}y = 0.$$
> 故
> $$\int_L P\,\mathrm{d}x + Q\,\mathrm{d}y = \int_{-L_1} P\,\mathrm{d}x + Q\,\mathrm{d}y = \frac{1}{4}\int_{-L_1} -y\,\mathrm{d}x + x\,\mathrm{d}y.$$
> 再由 Green 公式，
> $$\frac{1}{4}\int_{-L_1} -y\,\mathrm{d}x + x\,\mathrm{d}y = \frac{1}{4}\iint_D 2\,\mathrm{d}x\,\mathrm{d}y = \frac{1}{2}\sigma(D) = \pi,$$
> 其中 $D: 4x^2+y^2 \leqslant 4$，$\sigma(D) = 2\pi$ 为 $D$ 的面积。

---

## 二、（本题 14 分）

求微分方程 $(x^3 - y^2)\,\mathrm{d}x + (x^2y + xy)\,\mathrm{d}y = 0$ 的通解。

> **解法 1**：设 $u = y^2$，则原方程化为
> $$\frac{\mathrm{d}u}{\mathrm{d}x} = \frac{2u}{x(1+x)} - \frac{2x^2}{x+1}. \qquad \cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \text{（6 分）}$$
> 这个线性方程的通解为
> $$\left(\frac{1+x}{x}\right)^2 u + (1+x)^2 = C.$$
> 即
> $$\left(\frac{1+x}{x}\right)^2 y^2 + (1+x)^2 = C.$$
> $$\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \text{（14 分）}$$
>
> **解法 2**：原方程可化为
> $$x\,\mathrm{d}x + y\,\mathrm{d}y + y\frac{x\,\mathrm{d}y - y\,\mathrm{d}x}{x^2} = 0,$$
> 即
> $$\frac{1}{2}\mathrm{d}\left(x^2+y^2\right) + y\,\mathrm{d}\left(\frac{y}{x}\right) = 0.$$
> $$\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \text{（6 分）}$$
> 两边同时除以 $\sqrt{x^2+y^2}$，得
> $$\frac{1}{2}\cdot\frac{\mathrm{d}\left(x^2+y^2\right)}{\sqrt{x^2+y^2}} + \frac{1}{\sqrt{1+\left(\frac{y}{x}\right)^2}}\cdot\frac{y}{x}\cdot\mathrm{d}\left(\frac{y}{x}\right) = 0,$$
> 即
> $$\mathrm{d}\left(\sqrt{x^2+y^2}\right) + \mathrm{d}\left(\sqrt{1+\left(\frac{y}{x}\right)^2}\right) = 0.$$
> 故
> $$\sqrt{x^2+y^2} + \frac{\sqrt{x^2+y^2}}{x} = C,$$
> 即
> $$(1+x)\sqrt{x^2+y^2} = Cx.$$
> $$\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \text{（14 分）}$$
>
> **解法 3**：将原方程化为 $x\,\mathrm{d}x + y\,\mathrm{d}y + y\dfrac{x\,\mathrm{d}y - y\,\mathrm{d}x}{x^2} = 0$，即
> $$\frac{1}{2}\mathrm{d}\left(x^2+y^2\right) + y\,\mathrm{d}\left(\frac{y}{x}\right) = 0.$$
> $$\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \text{（6 分）}$$
> 令 $x = r\cos\theta$，$y = r\sin\theta$，则 $r = \sqrt{x^2+y^2}$，$\tan\theta = \dfrac{y}{x}$，方程化为
> $$\frac{1}{2}\mathrm{d}r^2 + r\sin\theta\,\mathrm{d}\tan\theta = 0,$$
> $$\mathrm{d}r + \sec\theta\tan\theta\,\mathrm{d}\theta = 0.$$
> 积分得，$r + \sec\theta = C$。
> 换回原变量，得原方程的通解为
> $$\sqrt{x^2+y^2} + \frac{\sqrt{x^2+y^2}}{x} = C.$$
> $$\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \text{（14 分）}$$

---

## 三、（本题 14 分）

设函数
$$f(x) = \begin{cases} \dfrac{1}{\ln(1+x)} - \dfrac{1}{x}, & 0 < x \leqslant 1, \\[10pt] k, & x = 0. \end{cases}$$

**(1)** 求常数 $k$ 的值，使得 $f(x)$ 在区间 $[0,1]$ 上连续；

**(2)** 对 (1) 中 $k$ 的值，求函数 $f(x)$ 的最小值 $\lambda$ 与最大值 $\mu$。

> **解答**：
>
> **(1)**
> $$\lim_{x\to 0^+} f(x) = \lim_{x\to 0^+}\frac{x - \ln(1+x)}{x\ln(1+x)} = \lim_{x\to 0^+}\frac{x - \ln(1+x)}{x^2}$$
> $$= \lim_{x\to 0^+}\frac{1 - \frac{1}{1+x}}{2x} = \lim_{x\to 0^+}\frac{1}{2(1+x)} = \frac{1}{2}.$$
> 令 $k = \dfrac{1}{2}$，则 $\lim\limits_{x\to 0^+} f(x) = f(0) = \dfrac{1}{2}$。所以 $f(x)$ 在 $[0,1]$ 上连续。$\cdots\cdots$（4 分）
>
> **(2)** 易知，$f(x)$ 在 $(0,1)$ 内可导，且
> $$f'(x) = -\frac{1}{(1+x)\ln^2(1+x)} + \frac{1}{x^2} = \frac{g(x)}{x^2(1+x)\ln^2(1+x)},$$
> 其中 $g(x) = (1+x)\ln^2(1+x) - x^2$。$\cdots\cdots\cdots\cdots\cdots\cdots\cdots$（8 分）
> 因为 $g'(x) = \ln^2(1+x) + 2\ln(1+x) - 2x$，且
> $$g''(x) = \frac{2\ln(1+x)}{1+x} + \frac{2}{1+x} - 2 = \frac{2\ln(1+x) - 2x}{1+x} < 0 \qquad (0 < x \leqslant 1),$$
> 所以 $g'(x)$ 在 $[0,1]$ 上单调递减，故当 $0 < x \leqslant 1$ 时，$g'(x) < g'(0) = 0$。这又推出 $g(x)$ 在 $[0,1]$ 上单调递减，故当 $0 < x \leqslant 1$ 时，$g(x) < g(0) = 0$。从而 $f'(x) < 0$（$0 < x \leqslant 1$），又可推出 $f(x)$ 在 $[0,1]$ 上单调递减。因此，
> $$\min_{0\leqslant x\leqslant 1} f(x) = f(1) = \frac{1}{\ln 2} - 1, \qquad \max_{0\leqslant x\leqslant 1} f(x) = f(0) = \frac{1}{2}.$$
> 于是，函数 $f(x)$ 的最小值 $\lambda = \dfrac{1}{\ln 2} - 1$，最大值 $\mu = \dfrac{1}{2}$。$\cdots\cdots\cdots$（14 分）

---

## 四、（本题 14 分）

求曲面积分
$$I = \iint_S (x^2-x)\,\mathrm{d}y\mathrm{d}z + (y^2-y)\,\mathrm{d}z\mathrm{d}x + (z^2-z)\,\mathrm{d}x\mathrm{d}y,$$
其中 $S$ 是上半球面 $x^2+y^2+z^2 = R^2$（$z \geqslant 0$）的上侧。

> **解法 1**：记 $\Sigma = \{(x,y,z) \mid z = 0,\ x^2+y^2 \leqslant R^2\}$，取下侧。由 Gauss 公式知
> $$\iint_{S+\Sigma} (x^2-x)\,\mathrm{d}y\mathrm{d}z + (y^2-y)\,\mathrm{d}z\mathrm{d}x + (z^2-z)\,\mathrm{d}x\mathrm{d}y = \iiint_\Omega (2(x+y+z)-3)\,\mathrm{d}x\mathrm{d}y\mathrm{d}z,$$
> 其中，$\Omega = \{(x,y,z) \mid z \geqslant 0,\ x^2+y^2+z^2 \leqslant R^2\}$。$\cdots\cdots\cdots\cdots\cdots$（4 分）
>
> 由于，
> $$\iint_\Sigma (x^2-x)\,\mathrm{d}y\mathrm{d}z + (y^2-y)\,\mathrm{d}z\mathrm{d}x + (z^2-z)\,\mathrm{d}x\mathrm{d}y = 0.$$
> 所以，
> $$I = \iiint_\Omega (2(x+y+z)-3)\,\mathrm{d}x\mathrm{d}y\mathrm{d}z.$$
> $$\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \text{（8 分）}$$
>
> 由对称性，
> $$I = \iiint_\Omega (2z-3)\,\mathrm{d}x\mathrm{d}y\mathrm{d}z.$$
> 用球坐标变换 $x = r\cos\theta\sin\varphi$，$y = r\sin\theta\sin\varphi$，$z = r\cos\varphi$，得
> $$I = \int_0^{2\pi}\mathrm{d}\theta\int_0^{\frac{\pi}{2}}\mathrm{d}\varphi\int_0^R (2r\cos\varphi - 3)r^2\sin\varphi\,\mathrm{d}r = 2\pi\left(\frac{R^4}{4} - R^3\right).$$
> $$\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \text{（14 分）}$$
>
> 注：最后一步直接利用直角坐标计算也可以。
>
> **解法 2**：$S$ 的参数方程为
> $$x = R\cos\theta\sin\varphi, \quad y = R\sin\theta\sin\varphi, \quad z = R\cos\varphi, \qquad \left(0 \leqslant \varphi \leqslant \frac{\pi}{2},\ 0 \leqslant \theta \leqslant 2\pi\right).$$
> 曲面 $S$ 上的点 $(x,y,z)$ 处的单位法向为 $\dfrac{(x,y,z)}{R}$。故，
> $$I = \iint_S (x^2-x,\ y^2-y,\ z^2-z)\cdot\frac{(x,y,z)}{R}\,\mathrm{d}S$$
> $$= \frac{1}{R}\iint_S \left[x^3+y^3+z^3 - (x^2+y^2+z^2)\right]\mathrm{d}S$$
> $$= \frac{1}{R}\iint_S \left[x^3+y^3+z^3 - R^2\right]\mathrm{d}S.$$
> $$\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \text{（6 分）}$$
>
> 由对称性可知
> $$\iint_S x^3\,\mathrm{d}S = \iint_S y^3\,\mathrm{d}S = 0.$$
> $$\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \text{（8 分）}$$
>
> 故，
> $$I = \frac{1}{R}\iint_S z^3\,\mathrm{d}S - R\iint_S \mathrm{d}S = \frac{1}{R}\iint_S z^3\,\mathrm{d}S - 2\pi R^3$$
> $$= \frac{1}{R}\iint\limits_{\substack{0 \leqslant \varphi \leqslant \frac{\pi}{2} \\ 0 \leqslant \theta \leqslant 2\pi}} (R\cos\varphi)^3 R^2\sin\varphi\,\mathrm{d}\varphi\mathrm{d}\theta - 2\pi R^3$$
> $$= 2\pi R^4\int_0^{\frac{\pi}{2}} \cos^3\varphi\sin\varphi\,\mathrm{d}\varphi - 2\pi R^3$$
> $$= 2\pi R^4\cdot\frac{1}{4} - 2\pi R^3 = \frac{\pi R^4}{2} - 2\pi R^3.$$
> $$\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \text{（14 分）}$$

---

## 五、（本题 14 分）

设 $f(x)$ 是 $(-\infty, +\infty)$ 上具有连续导数的非负函数，且存在 $M > 0$ 使得对任意的 $x, y \in (-\infty, +\infty)$，有 $|f'(x) - f'(y)| \leqslant M|x - y|$。证明：对于任意实数 $x$，恒有 $(f'(x))^2 \leqslant 2Mf(x)$。

> **证明**：任取 $x \in (-\infty, +\infty)$，对任意 $h \in (-\infty, +\infty)$，且 $h \neq 0$，恒有
> $$0 \leqslant f(x+h) = f(x) + \int_0^h f'(x+t)\,\mathrm{d}t$$
> $$= f(x) + \int_0^h \left(f'(x+t) - f'(x)\right)\mathrm{d}t + f'(x)h.$$
> $$\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \text{（6 分）}$$
>
> 取 $h$ 使得 $hf'(x) \leqslant 0$，则
> $$-f'(x)h \leqslant f(x) + \int_0^h \left(f'(x+t) - f'(x)\right)\mathrm{d}t \leqslant f(x) + M\frac{h^2}{2}.$$
> $$|f'(x)| \leqslant \frac{f(x)}{|h|} + M\frac{|h|}{2}.$$
> $$\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \text{（12 分）}$$
>
> 取 $|h| = \sqrt{\dfrac{2f(x)}{M}}$，即得所证不等式 $(f'(x))^2 \leqslant 2Mf(x)$。$\cdots\cdots\cdots$（14 分）

---

## 六、（本题 14 分）

证明：级数 $\displaystyle\sum_{n=1}^\infty\sum_{k=1}^\infty \frac{(-1)^{[\sqrt{n}]}}{n^2+k^2}$ 收敛，其中 $[x]$ 表示不超过 $x$ 的最大整数。

> **证明**：对于任意固定的 $n$ 和 $N$，有
> $$\sum_{k=1}^N \frac{1}{k^2+n^2} \leqslant \sum_{k=1}^N \int_{k-1}^k \frac{1}{y^2+n^2}\,\mathrm{d}y = \int_0^N \frac{1}{y^2+n^2}\,\mathrm{d}y = \frac{1}{n}\arctan\frac{N}{n}.$$
>
> $$\sum_{k=1}^N \frac{1}{k^2+n^2} \geqslant \sum_{k=1}^N \int_k^{k+1} \frac{1}{y^2+n^2}\,\mathrm{d}y = \int_1^{N+1} \frac{1}{y^2+n^2}\,\mathrm{d}y = \frac{1}{n}\left(\arctan\frac{N+1}{n} - \arctan\frac{1}{n}\right).$$
>
> $$\left|\sum_{k=1}^N \frac{1}{k^2+n^2} - \frac{\pi}{2n}\right| \leqslant \frac{\pi}{2n} - \frac{1}{n}\left(\arctan\frac{N+1}{n} - \arctan\frac{1}{n}\right).$$
>
> 令 $N \to \infty$，即有
> $$\left|\sum_{k=1}^\infty \frac{1}{k^2+n^2} - \frac{\pi}{2n}\right| \leqslant \frac{1}{n}\arctan\frac{1}{n}.$$
> $$\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \text{（4 分）}$$
>
> 注意到
> $$\sum_{n=1}^\infty\left|\sum_{k=1}^\infty \frac{(-1)^{[\sqrt{n}]}}{n^2+k^2} - \frac{\pi}{2}\frac{(-1)^{[\sqrt{n}]}}{n}\right| = \sum_{n=1}^\infty\left|\sum_{k=1}^\infty \frac{1}{k^2+n^2} - \frac{\pi}{2n}\right| \leqslant \sum_{n=1}^\infty \frac{1}{n}\arctan\frac{1}{n} < +\infty.$$
> 即 $\displaystyle\sum_{n=1}^\infty \left(\sum_{k=1}^\infty \frac{(-1)^{[\sqrt{n}]}}{n^2+k^2} - \frac{\pi}{2}\frac{(-1)^{[\sqrt{n}]}}{n}\right)$ 绝对收敛，从而收敛。由此，级数 $\displaystyle\sum_{n=1}^\infty\sum_{k=1}^\infty \frac{(-1)^{[\sqrt{n}]}}{n^2+k^2}$ 与级数 $\displaystyle\sum_{n=1}^\infty \frac{\pi}{2}\frac{(-1)^{[\sqrt{n}]}}{n}$ 同敛散。以下只需证级数 $\displaystyle\sum_{n=1}^\infty \frac{(-1)^{[\sqrt{n}]}}{n}$ 收敛。$\cdots\cdots$（8 分）
>
> 记 $S_n$ 为级数 $\displaystyle\sum_{n=1}^\infty \frac{(-1)^{[\sqrt{n}]}}{n}$ 的前 $n$ 项部分和，则有
> $$S_{n^2} = \sum_{m=1}^{n-1}\sum_{k=m^2}^{(m+1)^2-1} \frac{(-1)^{[\sqrt{k}]}}{k} + \frac{(-1)^n}{n^2} = \sum_{m=1}^{n-1} (-1)^m C_m + \frac{(-1)^n}{n^2},$$
> 其中
> $$C_m = \sum_{k=m^2}^{(m+1)^2-1} \frac{1}{k}.$$
> 由 $C_m < m\cdot\dfrac{1}{m^2} + \dfrac{1}{m^2+m}\cdot(m+1) = \dfrac{2}{m}$ 知，$C_m \to 0$，$m \to \infty$。
> 此外，$C_m > (m+1)\cdot\dfrac{1}{m^2+m} + \dfrac{1}{m^2+2m}\cdot m > \dfrac{2}{m+1} > C_{m+1}$，从而 $C_m$ 单调递减，级数 $\displaystyle\sum_{m=1}^\infty (-1)^m C_m$ 收敛，$S_{n^2}$ 收敛。$\cdots\cdots\cdots$（12 分）
>
> 对于其它的 $N$，存在 $n$ 使得
> $$n^2 \leqslant N < (n+1)^2, \qquad |S_N - S_{n^2}| \leqslant C_n < \frac{2}{n} \to 0, \quad N \to \infty.$$
> 故级数 $\displaystyle\sum_{n=1}^\infty \frac{(-1)^{[\sqrt{n}]}}{n}$ 收敛，证毕。$\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots$（14 分）

---

## 附：本卷考点分布速览

| 题号 | 分值 | 考点板块 | 具体考点 |
|---|---|---|---|
| 一(1) | 6 | 定积分 | 分部积分计算定积分 |
| 一(2) | 6 | 重积分与极限 | 极坐标变换 + 二重积分 + Taylor 展开求极限 |
| 一(3) | 6 | 多元微分 | 抽象复合函数二阶混合偏导（链式法则 $f_1, f_2, f_{11}, f_{12}, f_{22}$） |
| 一(4) | 6 | 空间解析几何 | 平面束 + 两平面交线（投影直线）+ 单位方向向量 |
| 一(5) | 6 | 曲线积分 | 第二型曲线积分 + Green 公式（挖洞法处理奇点） |
| 二 | 14 | 常微分方程 | 一阶方程通解（换元化线性 / 凑全微分 / 极坐标换元三种解法） |
| 三 | 14 | 极限与导数应用 | 分段函数连续性求参数 + 二阶导判定单调性求最值 |
| 四 | 14 | 曲面积分 | 第二型曲面积分（Gauss 公式 + 球坐标 + 对称性；另有参数化解法） |
| 五 | 14 | 微分不等式证明 | 由 Lipschitz 条件出发的积分估计（配方法取 $|h|$） |
| 六 | 14 | 级数 | 二重级数收敛性（积分估计 $\arctan$ + 部分和 $S_{n^2}$ 分组估计） |
