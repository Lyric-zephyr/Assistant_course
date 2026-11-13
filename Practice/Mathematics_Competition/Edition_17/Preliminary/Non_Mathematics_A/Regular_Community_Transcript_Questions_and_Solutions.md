<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC17%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6A%E7%B1%BB-%E5%88%9D%E8%B5%9B-2025.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第十七届全国大学生数学竞赛初赛试题及参考答案（非数学 A 类）

> **年份**：2025 年（第十七届）｜**类别**：非数学专业 A 类（理工类）
> **考试形式**：闭卷｜**时间**：150 分钟｜**满分**：100 分
> **来源**：大学生数学竞赛网（cmathc.org.cn）官方转载 PDF｜原始文件：`../第十七届全国大学生数学竞赛初赛试题及参考答案（非数学A类）.pdf`
> **转录说明**：原卷为扫描版，本文件由视觉逐页转写，公式采用 KaTeX 语法；「答案」与「解答」均来自原卷参考答案，评分标注（如"（6分）"）为原卷过程分点。

---

## 卷面结构

| 题号 | 一 | 二 | 三 | 四 | 五 | 六 | 总分 |
|---|---|---|---|---|---|---|---|
| 满分 | 30 | 14 | 14 | 14 | 14 | 14 | 100 |
| 形式 | 填空题 ×5 | 解答题 | 解答题 | 解答题 | 解答题 | 解答题 | |

---

## 一、填空题（本题 30 分，每小题 6 分）

**(1)** 设函数 $f(x) = x - \ln(1+x) - \dfrac{1}{2}x\sin x$，$g(x) = ax^3$，且满足 $\lim\limits_{x\to 0}\dfrac{f(x)}{g(x)} = 1$，则 $a = \underline{\qquad}$。

> **答案**：$a = -\dfrac{1}{3}$
>
> **解答**：根据 Taylor 公式，$\ln(1+x) = x - \dfrac{x^2}{2} + \dfrac{x^3}{3} + o(x^3)$，$\sin x = x - \dfrac{x^3}{6} + o(x^3)$，所以
> $$f(x) = -\frac{1}{3}x^3 + o(x^3).$$
> 因为 $\lim\limits_{x\to 0}\dfrac{f(x)}{g(x)} = 1$，即 $\lim\limits_{x\to 0}\dfrac{-\frac{1}{3}x^3 + o(x^3)}{ax^3} = 1$，所以 $a = -\dfrac{1}{3}$。

**(2)** 设平面过原点与点 $(6,-3,2)$，且与平面 $4x - y + 2z - 8 = 0$ 垂直，则此平面方程为 $\underline{\qquad}$。

> **答案**：$2x + 2y - 3z = 0$
>
> **注**：答案不唯一，系数差个倍数都对，例如 $-2x - 2y + 3z = 0$ 或 $x + y - \dfrac{3}{2}z = 0$ 也对。

**(3)** 极限 $\lim\limits_{x\to 0}\dfrac{\displaystyle\int_0^{\sin^2 x}\ln(1+t)\,\mathrm{d}t}{\left(\sqrt[3]{1+x^3} - 1\right)\sin x} = \underline{\qquad}$。

> **答案**：$\dfrac{3}{2}$
>
> **解答**：
> $$\lim_{x\to 0}\frac{\int_0^{\sin^2 x}\ln(1+t)\,\mathrm{d}t}{\left(\sqrt[3]{1+x^3}-1\right)\sin x} = \lim_{x\to 0}\frac{\int_0^{\sin^2 x}\ln(1+t)\,\mathrm{d}t}{\frac{1}{3}x^4}$$
> （这里用了 $\sqrt[3]{1+x^3}-1 \sim \frac{1}{3}x^3$，$\sin x \sim x$）继续用洛必达法则：
> $$= \lim_{x\to 0}\frac{\ln(1+\sin^2 x)\cdot 2\sin x\cos x}{\frac{4}{3}x^3} = \frac{3}{2}.$$

**(4)** 设函数 $f(u,v)$ 具有一阶连续偏导数，$f(2,0) = 3$，$f'_u(2,0) = 5$，又设 $z = z(x,y)$ 是由方程 $xz = f(2x-y,\,xyz)$ 确定的隐函数，则 $\left.\dfrac{\partial z}{\partial x}\right|_{\substack{x=1\\ y=0}} = \underline{\qquad}$。

> **答案**：$7$
>
> **解答**：对方程两边关于 $x$ 求偏导数，得
> $$z + x\frac{\partial z}{\partial x} = 2f'_u + yf'_v\left(z + x\frac{\partial z}{\partial x}\right).$$
> 由此解得
> $$\frac{\partial z}{\partial x} = \frac{1}{x}\left(\frac{2f'_u}{1 - yf'_v} - z\right).$$
> 注意到 $x = 1,\,y = 0$ 时，$z = f(2,0) = 3$，$f'_u(2,0) = 5$，所以
> $$\left.\frac{\partial z}{\partial x}\right|_{\substack{x=1\\ y=0}} = 2f'_u(2,0) - 3 = 7.$$

**(5)** 设曲线 $L$ 为球面 $x^2+y^2+z^2 = 4$ 与平面 $x+y+z = 3$ 的交线，则曲线积分 $\displaystyle\int_L (x^2 + 2xy)\,\mathrm{d}s = \underline{\qquad}$。

> **答案**：$6\pi$
>
> **解答**：根据对称性，得
> $$\int_L (x^2+2xy)\,\mathrm{d}s = \frac{1}{3}\int_L (x^2+y^2+z^2)\,\mathrm{d}s + \frac{2}{3}\int_L (xy+yz+zx)\,\mathrm{d}s$$
> $$= \frac{1}{3}\int_L (x^2+y^2+z^2)\,\mathrm{d}s + \frac{1}{3}\int_L \left[(x+y+z)^2 - (x^2+y^2+z^2)\right]\mathrm{d}s$$
> $$= \frac{1}{3}\int_L (x+y+z)^2\,\mathrm{d}s = 6\pi.$$
> （其中用到球面与平面交线 $L$ 是圆：球心 $(0,0,0)$ 到平面 $x+y+z=3$ 的距离为 $\sqrt{3}$，故 $L$ 是半径为 $\sqrt{4-3}=1$ 的圆，周长 $2\pi$；于是 $\int_L (x+y+z)^2\mathrm{d}s = 9\cdot 2\pi = 18\pi$。）

---

## 二、（本题 14 分）

设 $f(x)$ 在 $(-\infty, +\infty)$ 上连续，在 $x = 0$ 处可导，且满足
$$f(x) = x^3 + x^2\lim_{x\to 0}\frac{f(x)}{x} - x\int_0^1 f(x)\,\mathrm{d}x.$$
求函数 $f(x)$ 的表达式。

> **解答**：易知 $f(0) = 0$，所以 $\lim\limits_{x\to 0}\dfrac{f(x)}{x} = \lim\limits_{x\to 0}\dfrac{f(x) - f(0)}{x - 0} = f'(0)$。
>
> 记 $a = f'(0)$，$b = \displaystyle\int_0^1 f(x)\,\mathrm{d}x$，则
> $$f(x) = x^3 + ax^2 - bx. \tag{1}$$
> 由此得 $a = \lim\limits_{x\to 0}\dfrac{f(x)}{x} = -b$。……（6 分）
>
> 再对式子 (1) 的两边在 $[0,1]$ 上作定积分，得
> $$b = \int_0^1 x^3\,\mathrm{d}x + a\int_0^1 x^2\,\mathrm{d}x - b\int_0^1 x\,\mathrm{d}x = \frac{1}{4} + \frac{1}{3}a - \frac{1}{2}b.$$
> ……（10 分）
>
> 与 $a = -b$ 联立解得 $a = -\dfrac{3}{22}$，$b = \dfrac{3}{22}$。所以
> $$f(x) = x^3 - \frac{3}{22}x^2 - \frac{3}{22}x,\qquad -\infty < x < +\infty.$$
> ……（14 分）

---

## 三、（本题 14 分）

求微分方程 $y'\,x\ln x\sin y + (1 - x\cos y)\cos y = 0$ 的通解。

> **解答**：将原方程变形为
> $$y'\sin y + \frac{1}{x\ln x}\cos y = \frac{1}{\ln x}\cos^2 y. \tag{1}$$
> 令 $z = \cos y$，则上述方程可化为 $n = 2$ 的 **Bernoulli 方程**
> $$z' - \frac{1}{x\ln x}z = -\frac{1}{\ln x}z^2.$$
> ……（6 分）
>
> 令 $u = z^{-1}$，原方程可进一步化为非齐次线性方程
> $$u' + \frac{1}{x\ln x}u = \frac{1}{\ln x}.$$
> 利用公式，得上述方程的通解为
> $$u = e^{-\int\frac{\mathrm{d}x}{x\ln x}}\left(\int\frac{1}{\ln x}e^{\int\frac{\mathrm{d}x}{x\ln x}}\,\mathrm{d}x + C\right) = \frac{1}{\ln x}(x + C).$$
> ……（12 分）
>
> 将其中的变量换回原变量：$u = z^{-1} = \dfrac{1}{\cos y}$，得所求通解为
> $$\frac{1}{\cos y} = \frac{1}{\ln x}(x + C).$$
> ……（14 分）

---

## 四、（本题 14 分）

设 $\Omega$ 是由平面 $\Pi_1: x = 0$，$\Pi_2: x = y$，$\Pi_3: y = z$，$\Pi_4: z = 1$，$\Pi_5: z = 2$ 围成的空间区域，求三重积分
$$\iiint_\Omega \frac{\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z}{\sqrt{y^2 + z^2}}.$$

> **解答**：采用**先二后一法**。设 $1 \leqslant z \leqslant 2$，用平面 $Z = z$ 截 $\Omega$ 得平面区域：$D_z = \{(x,y) \mid 0 \leqslant x \leqslant z,\ 0 \leqslant y \leqslant x\}$，则
> $$\iiint_\Omega \frac{\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z}{\sqrt{y^2+z^2}} = \int_1^2 \mathrm{d}z \iint_{D_z}\frac{\mathrm{d}x\,\mathrm{d}y}{\sqrt{y^2+z^2}}.$$
> ……（5 分）
> $$= \int_1^2 \mathrm{d}z \int_0^z \mathrm{d}y \int_0^y \frac{\mathrm{d}x}{\sqrt{y^2+z^2}} = \int_1^2 \mathrm{d}z \int_0^z \frac{y}{\sqrt{y^2+z^2}}\,\mathrm{d}y$$
> ……（10 分）
> $$= \int_1^2 \left.\sqrt{y^2+z^2}\right|_0^z \mathrm{d}z = (\sqrt{2}-1)\int_1^2 z\,\mathrm{d}z = \frac{3(\sqrt{2}-1)}{2}.$$
> ……（14 分）

---

## 五、（本题 14 分）

判断级数 $\displaystyle\sum_{n=1}^{\infty} a_n$ 的收敛性，其中
$$a_n = \sin^2 x\,\sin^2 2x\,\cdots\,\sin^2 2^n x,\qquad x \in (-\infty, +\infty).$$

> **解答**：
> **(1)** 令 $f(x) = \sin^2 x\sin 2x$，则
> $$f'(x) = 2\sin^2 x\,(3 - 4\sin^2 x) = -8\sin^2 x\left(\sin x - \frac{\sqrt{3}}{2}\right)\left(\sin x + \frac{\sqrt{3}}{2}\right).$$
> 令 $f'(x) = 0$，在 $(0,\pi)$ 中得到两个根 $x_1 = \dfrac{\pi}{3}$，$x_2 = \dfrac{2\pi}{3}$。
> 容易证明函数 $f(x)$ 在 $\left(0,\dfrac{\pi}{3}\right)\cup\left(\dfrac{2\pi}{3},\pi\right)$ 上单调增加，在 $\left(\dfrac{\pi}{3},\dfrac{2\pi}{3}\right)$ 上单调减少。……（4 分）
>
> **(2)** 由于 $f(x)$ 的周期为 $\pi$，$f(0) = f(\pi) = 0$，$f(x)$ 在 $[0,\pi]$ 上的最大值和最小值分别为 $f\!\left(\dfrac{\pi}{3}\right) = \dfrac{3\sqrt{3}}{8}$ 和 $f\!\left(\dfrac{2\pi}{3}\right) = -\dfrac{3\sqrt{3}}{8}$。故 $|f(x)| \leqslant \dfrac{3\sqrt{3}}{8}$。……（9 分）
>
> 最后，由
> $$a_n^{3/2} = |\sin x|\cdot|f(x)f(2x)\cdots f(2^{n-1}x)|\cdot|\sin^2 2^n x| \leqslant \left(\frac{3\sqrt{3}}{8}\right)^n,$$
> 知 $a_n \leqslant \left(\dfrac{3\sqrt{3}}{8}\right)^{\frac{2n}{3}} = \left(\dfrac{3}{4}\right)^n$。从而级数 $\displaystyle\sum_{n=1}^\infty a_n$ 收敛。……（14 分）

---

## 六、（本题 14 分）

设函数 $f(x)$，$g(x)$ 在 $[a,b]$ 上连续可导且满足以下三个条件：

1. $\displaystyle\int_a^b f(x)\,\mathrm{d}x = \int_a^b g(x)\,\mathrm{d}x = 0$；
2. $f'(x)g(x) - f(x)g'(x) > 0$，$x \in [a,b]$；
3. $g(x)$ 在 $(a,b)$ 上有唯一零点 $\xi$。

证明：

**(1)** $\displaystyle\int_a^b f(x)\left(\int_a^x g(s)\,\mathrm{d}s\right)\mathrm{d}x = -\int_a^b g(x)\left(\int_a^x f(s)\,\mathrm{d}s\right)\mathrm{d}x$。

**(2)** $\displaystyle\int_a^b f(x)\left(\int_a^x g(s)\,\mathrm{d}s\right)\mathrm{d}x > 0$。

> **证明**：
> **(1)** 记 $F(x) = \displaystyle\int_a^x f(s)\,\mathrm{d}s$，$G(x) = \displaystyle\int_a^x g(s)\,\mathrm{d}s$，则由分部积分
> $$\int_a^b f(x)G(x)\,\mathrm{d}x = \int_a^b G(x)\,\mathrm{d}F(x) = -\int_a^b F(x)g(x)\,\mathrm{d}x,$$
> 这里用到了条件 $F(b) = G(b) = 0$。……（4 分）
>
> **(2)** 显然，$g'(\xi) \neq 0$，不妨设 $g'(\xi) > 0$，则在 $[a,\xi)$ 上 $g(x) < 0$，在 $(\xi, b]$ 上 $g(x) > 0$。
> $$\int_a^b f(x)\left(\int_a^x g(s)\,\mathrm{d}s\right)\mathrm{d}x = \frac{1}{2}\iint_D \left(f(x)g(s) - f(s)g(x)\right)\mathrm{d}x\,\mathrm{d}s,$$
> 其中 $D = \{(x,s) \mid a \leqslant s \leqslant x \leqslant b\}$。……（8 分）
>
> 把 $D$ 分成三部分：$D = D_1 \cup D_2 \cup D_3$，其中
> $$D_1 = \{(x,s) \mid a \leqslant s \leqslant x \leqslant \xi\},\quad D_2 = \{(x,s) \mid a \leqslant s \leqslant \xi \leqslant x \leqslant b\},\quad D_3 = \{(x,s) \mid \xi \leqslant s \leqslant x \leqslant b\}.$$
> 由条件 $f'(x)g(x) - f(x)g'(x) > 0$ 知 $\dfrac{f(x)}{g(x)}$ 在 $[a,\xi)$ 和 $(\xi, b]$ 上严格单调递增，从而在 $D_1$ 和 $D_3$ 上，$f(x)g(s) - f(s)g(x) \geqslant 0$ 且不恒等于 0，故
> $$\iint_{D_1\cup D_3}\left(f(x)g(s) - f(s)g(x)\right)\mathrm{d}x\,\mathrm{d}s > 0.$$
> ……（12 分）
>
> 又
> $$\iint_{D_2}\left(f(x)g(s) - f(s)g(x)\right)\mathrm{d}x\,\mathrm{d}s = \int_\xi^b f(x)\,\mathrm{d}x\int_a^\xi g(s)\,\mathrm{d}s - \int_\xi^b g(x)\,\mathrm{d}x\int_a^\xi f(s)\,\mathrm{d}s = 0,$$
> 最后一个等式用到了 $\displaystyle\int_\xi^b f(x)\,\mathrm{d}x = -\int_a^\xi f(s)\,\mathrm{d}s$，$\displaystyle\int_\xi^b g(x)\,\mathrm{d}x = -\int_a^\xi g(s)\,\mathrm{d}s$。
>
> 综上，$\displaystyle\int_a^b f(x)\left(\int_a^x g(s)\,\mathrm{d}s\right)\mathrm{d}x > 0$。……（14 分）

---

## 附：本卷考点分布速览

| 题号 | 分值 | 考点板块 | 具体考点 |
|---|---|---|---|
| 一(1) | 6 | 极限 | Taylor 展开求参数 |
| 一(2) | 6 | 空间解析几何 | 平面方程（过点+垂直） |
| 一(3) | 6 | 极限 | 变限积分 + 等价无穷小 + 洛必达 |
| 一(4) | 6 | 多元微分 | 隐函数求偏导 |
| 一(5) | 6 | 曲线积分 | 第一类曲线积分 + 对称性 |
| 二 | 14 | 极限/微分 | 可导定义 + 定积分方程（自洽方程） |
| 三 | 14 | 常微分方程 | 伯努利方程 + 变量替换（换元两次） |
| 四 | 14 | 三重积分 | 先二后一法 |
| 五 | 14 | 级数 | 正项级数判敛（最值估计 + 放缩） |
| 六 | 14 | 积分证明 | 分部积分 + 二重积分化算子证明 |
