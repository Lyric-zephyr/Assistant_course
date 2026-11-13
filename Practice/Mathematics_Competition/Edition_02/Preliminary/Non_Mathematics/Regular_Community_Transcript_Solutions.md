<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC02%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6%E7%B1%BB-%E5%88%9D%E8%B5%9B-2010-%E5%8F%82%E8%80%83%E8%A7%A3%E7%AD%94.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第2届（2010）非数学类初赛 · 官方参考解答

> 来源：考研竞赛数学公众号版（原文件：第02届非数学类-初赛(试题及参考解答).pdf）｜本文件仅含解答，题面见同目录《第02届非数学类-初赛-2010.md》
> 转录说明：视觉逐页转写（全页 dpi=140，公式逐字符处局部放大 300–1200 dpi 复核），公式 KaTeX 语法；原文件对解答的标注为「【参考答案】」（第二题作「【参考证法】」），本文件照原文保留；原解答中的笔误照抄并就地以 ⚠️ 加注。题号与分值（第一题 5 小题每题 5 分；第二至六题各 15 分）与原 PDF 标注及题面转录文件核对一致。

---

## 一(1)（5分）

**参考答案**：$x_n = \dfrac{1}{(1-a)}(1-a)(1+a)\cdot(1+a^2)\cdots(1+a^{2^n})$

$$= \dfrac{1}{(1-a)}(1-a^2)\cdot(1+a^2)\cdots(1+a^{2^n})$$

$$= \dfrac{1}{(1-a)}(1-a^4)\cdot(1+a^4)\cdots(1+a^{2^n}) = \dfrac{1-a^{2^{n+1}}}{1-a}$$

由于 $|a| < 1$，所以 $\lim\limits_{n\to\infty} a^{2^{n+1}} = 0 \Rightarrow \lim\limits_{n\to\infty} x_n = \dfrac{1}{1-a}$。

---

## 一(2)（5分）

**参考答案**：$\lim\limits_{x\to\infty} e^{-x}\left(1+\dfrac{1}{x}\right)^{x^2} = \lim\limits_{x\to\infty}\left[e^{-1}\left(1+\dfrac{1}{x}\right)^x\right]^x$

$$= \exp\left\{\lim\limits_{x\to\infty}\left[\ln\left(1+\frac{1}{x}\right)^x - 1\right]x\right\} = \exp\left\{\lim\limits_{x\to\infty} x\left[x\ln\left(1+\frac{1}{x}\right) - 1\right]\right\}$$

$$= \exp\left\{\lim\limits_{x\to\infty} x\left[x\left(\frac{1}{x} - \frac{1}{2x^2} + o\left(\frac{1}{x^2}\right)\right) - 1\right]\right\} = e^{-\frac{1}{2}}$$

【注】$\exp(x) = e^x$。

---

## 一(3)（5分）

**参考答案**：因为 $s > 0$ 时， $\lim\limits_{x\to+\infty} e^{-sx}x^n = 0$，所以

$$I_n = -\frac{1}{s}\int_0^{+\infty} x^n\,\mathrm{d}\left(e^{-sx}\right) = -\frac{1}{s}\left[x^n e^{-sx}\Big|_0^{+\infty} - \int_0^{+\infty} e^{-sx}\,\mathrm{d}\left(x^n\right)\right] = \frac{n}{s}I_{n-1}$$

由此得 $I_n = \dfrac{n}{s}I_{n-1} = \dfrac{n}{s}\cdot\dfrac{n-1}{s}I_{n-2} = \cdots = \dfrac{n!}{s^{n-1}}I_1$。

$$I_1 = \int_0^{+\infty} e^{-sx}x\,\mathrm{d}x = -\frac{1}{s}\left[x^n e^{-sx}\Big|_0^{+\infty} - \int_0^{+\infty} e^{-sx}\,\mathrm{d}x\right] = \frac{1}{s^2}$$

> ⚠️ 上式中 $I_1$ 的方括号内首项原文件印为 $x^n e^{-sx}$，按题应为 $x\,e^{-sx}$（系原稿沿用前一式记号的笔误）；照抄如上。

$$I_n = \frac{n!}{s^{n-1}}I_1 = \frac{n!}{s^{n+1}}$$

---

## 一(4)（5分）

**参考答案**：因为 $\dfrac{\partial r}{\partial x} = \dfrac{x}{r}, \dfrac{\partial r}{\partial y} = \dfrac{y}{r}$，所以

$$\frac{\partial g}{\partial x} = -\frac{x}{r^3}f'\left(\frac{1}{r}\right), \quad \frac{\partial^2 g}{\partial x^2} = \frac{x^2}{r^6}f''\left(\frac{1}{r}\right) + \frac{2x^2 - y^2}{r^5}f'\left(\frac{1}{r}\right),$$

利用对称性，可得

$$\frac{\partial g}{\partial y} = -\frac{y}{r^3}f'\left(\frac{1}{r}\right), \quad \frac{\partial^2 g}{\partial y^2} = \frac{y^2}{r^6}f''\left(\frac{1}{r}\right) + \frac{2y^2 - x^2}{r^5}f'\left(\frac{1}{r}\right),$$

所以

$$\frac{\partial^2 g}{\partial x^2} + \frac{\partial^2 g}{\partial y^2} = \frac{1}{r^4}f''\left(\frac{1}{r}\right) + \frac{1}{r^3}f'\left(\frac{1}{r}\right).$$

---

## 一(5)（5分）

**参考答案**：直线 $l_1$ 的对称式方程为 $l_1: \dfrac{x}{1} = \dfrac{y}{1} = \dfrac{z}{0}$，记两直线的方向向量分别为 $\vec{l}_1 = (1,1,0), \vec{l}_2 = (4,-2,-1)$，两直线上两定点分别为 $P_1(0,0,0), P_2(2,1,3)$，并记

$$\vec{a} = \overrightarrow{P_1P_2} = (2,1,3), \quad \vec{l}_1\times\vec{l}_2 = (-1,1,-6);$$

于是两点间的距离为 $d = \dfrac{|\vec{a}\cdot(\vec{l}_1\times\vec{l}_2)|}{|\vec{l}_1\times\vec{l}_2|} = \dfrac{|-2+1-18|}{\sqrt{38}} = \sqrt{\dfrac{19}{2}}$。

---

## 第二题（15分）

**参考证法**：由于 $\lim\limits_{x\to+\infty} f'(x) = \alpha > 0$，必有一个充分大的 $a > x_0$，使得 $f'(a) > 0$。$f''(x) > 0$ 可知 $y = f(x)$ 对应的图形为凹函数，从而 $f(x) > f(a) + f'(a)(x-a)$（$x > a$）。当 $x \to +\infty$ 时，

$$f(+\infty) + f'(a)(x-a) \to +\infty.$$

故存在 $b > a$，使得 $f(b) > f(a) + f'(a)(b-a) > 0$。

由 $\lim\limits_{x\to-\infty} f'(x) = \beta < 0$，必有一个充分大的 $c < x_0$，使得 $f'(c) > 0$。$f''(x) > 0$ 可知 $y = f(x)$ 为凹函数，从而 $f(x) > f(c) + f'(c)(x-c)$（$x < c$）。当 $x \to -\infty$ 时，

$$f(-\infty) + f'(c)(x-c) \to +\infty.$$

故存在 $d < c$，使得 $f(d) > f(c) + f'(c)(d-c) > 0$。

在 $[x_0, b]$ 和 $[d, x_0]$ 利用零点定理，$\exists x_1\in(x_0,b), x_2\in(d,x_0)$ 使得 $f(x_1) = f(x_2) = 0$。

下面证明方程 $y = f(x)$ 只有两个实根。

用反证法。假设 $f(x) = 0$ 在 $(-\infty, +\infty)$ 内有三个实根，不妨设为 $x_1, x_2, x_3$ 且 $x_1 < x_2 < x_3$。对 $f(x)$ 在区间 $[x_1,x_2]$、$[x_2,x_3]$ 上分别用罗尔定理，则各至少存在一点 $\xi_1\in(x_1,x_2), \xi_2\in(x_2,x_3)$，使得 $f'(\xi_1) = f'(\xi_2) = 0$。再将 $f'(x)$ 在 $[\xi_1,\xi_2]$ 上应用罗尔定理，则至少存在一点 $\eta\in(\xi_1,\xi_2)$，使得 $f''(\eta) = 0$，与已知条件 $f''(x) > 0$ 矛盾，所以方程不能多于两个实根。

> ⚠️ 本段原文件两处笔误照抄并加注：(i) 「使得 $f'(c) > 0$」应为 $f'(c) < 0$（由 $\beta < 0$ 及 $f'$ 单调递增，$x$ 充分小处 $f' < 0$；且后文 $f(-\infty) + f'(c)(x-c) \to +\infty$ 亦要求 $f'(c) < 0$）；(ii) 两处极限式起首的 $f(+\infty)$、$f(-\infty)$ 为原文件排印（按上下文应理解为对应的下界 $f(a)+f'(a)(x-a)$、$f(c)+f'(c)(x-c)$）。

---

## 第三题（15分）

**参考答案**：因为 $\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{\psi'(t)}{2+2t}$，

$$\frac{\mathrm{d}^2 y}{\mathrm{d}x^2} = \frac{1}{2+2t}\cdot\frac{(2+2t)\psi''(t) - 2\psi'(t)}{(2+2t)^3} = \frac{(1+t)\psi''(t) - \psi'(t)}{4(1+t)^3}$$

> ⚠️ 上式中项分式的分母原文件印为 $(2+2t)^3$。按参数方程二阶导数公式，与前置因子 $\dfrac{1}{2+2t}$ 合并后的正确形式应为 $\dfrac{1}{2+2t}\cdot\dfrac{(2+2t)\psi''(t) - 2\psi'(t)}{(2+2t)^2}$（即分子分母合并后为 $(2+2t)^3$）；原文排印如此，照抄并加注。

由题设 $\dfrac{\mathrm{d}^2 y}{\mathrm{d}x^2} = \dfrac{3}{4(1+t)}$，故

$$\frac{(1+t)\psi''(t) - \psi'(t)}{4(1+t)^3} = \frac{3}{4(1+t)},$$

从而有 $(1+t)\psi''(t) - \psi'(t) = 3(1+t)^2$，即

$$\psi''(t) - \frac{1}{(1+t)}\psi'(t) = 3(1+t)$$

设 $u = \psi'(t)$，故有 $u' - \dfrac{1}{(1+t)}u = 3(1+t)$，由一阶非齐次线性微分方程通解计算公式，有

$$u = e^{-\int\left(-\frac{1}{1+t}\right)\mathrm{d}t}\left[\int 3(1+t)e^{\int\left(-\frac{1}{1+t}\right)\mathrm{d}t}\,\mathrm{d}t + C_1\right]$$

$$= (1+t)\left[\int 3(1+t)(1+t)^{-1}\,\mathrm{d}t + C_1\right] = (1+t)(3t + C_1)$$

由曲线 $y = \psi(t)$ 与 $y = \displaystyle\int_1^{t^2} e^{-u^2}\,\mathrm{d}u + \dfrac{3}{2e}$ 在 $t = 1$ 处相切知 $\psi(1) = \dfrac{3}{2e}, \psi'(1) = \dfrac{2}{e}$。所以有

$$u\big|_{t=1} = \psi'(1) = \frac{2}{e} \Rightarrow C_1 = \frac{1}{e} - 3.$$

于是有

$$\psi(t) = \int (1+t)(3t+C_1)\,\mathrm{d}t = t^3 + \frac{3+C_1}{2}t^2 + C_1 t + C_2$$

由 $\psi(1) = \dfrac{3}{2e} \Rightarrow C_2 = 2$，于是有 $\psi(t) = t^3 + \dfrac{1}{2e}t^2 + \left(\dfrac{1}{e} - 3\right)t + 2\ (t > -1)$。

---

## 第四题（15分）

**参考答案**：令 $f(x) = x^{1-\alpha}, x\in[S_{n-1}, S_n]$，将 $f(x)$ 在 $[S_{n-1}, S_n]$ 上用拉格朗日中值定理，存在 $\xi\in(S_{n-1}, S_n)$，使得 $f(S_n) - f(S_{n-1}) = f'(\xi)(S_n - S_{n-1})$，即

$$S_n^{1-\alpha} - S_{n-1}^{1-\alpha} = (1-\alpha)\xi^{-\alpha}a_n.$$

**(1)** 当 $\alpha > 1$ 时，$\dfrac{1}{S_{n-1}^{\alpha-1}} - \dfrac{1}{S_n^{\alpha-1}} = (\alpha-1)\dfrac{a_n}{\xi^\alpha} \ge (\alpha-1)\dfrac{a_n}{S_n^\alpha}$，显然 $\left\{\dfrac{1}{S_{n-1}^{\alpha-1}} - \dfrac{1}{S_n^{\alpha-1}}\right\}$ 的前 $n$ 项和有界，从而收敛，所以级数 $\sum\limits_{n=1}^{+\infty}\dfrac{a_n}{S_n^\alpha}$ 收敛。

**(2)** 当 $\alpha = 1$ 时，因为 $a_n > 0$，$S_n$ 单调递增，所以

$$\sum_{k=n+1}^{n+p}\frac{a_k}{S_k} \ge \frac{1}{S_{n+p}}\sum_{k=n+1}^{n+p}a_k = \frac{S_{n+p} - S_n}{S_{n+p}} = 1 - \frac{S_n}{S_{n+p}}$$

因为 $S_n \to +\infty$ 对任意的 $n$，当 $p \in N$，$\dfrac{S_n}{S_{n+p}} < \dfrac{1}{2}$，从而 $\sum\limits_{k=n+1}^{n+p}\dfrac{a_k}{S_k} \ge \dfrac{1}{2}$。所以级数 $\sum\limits_{n=1}^{+\infty}\dfrac{a_n}{S_n^\alpha}$ 发散。

**(3)** 当 $\alpha < 1$ 时，$\dfrac{a_n}{S_n^\alpha} \ge \dfrac{a_n}{S_n}$，由 $\sum\limits_{n=1}^{+\infty}\dfrac{a_n}{S_n}$ 发散及比较判别法，$\sum\limits_{n=1}^{+\infty}\dfrac{a_n}{S_n^\alpha}$ 发散。

---

## 第五题（15分）

**参考答案**：

**(1)** 设旋转轴 $l$ 的方向向量为 $\vec{s} = (\alpha,\beta,\gamma)$，椭球内任意点 $P(x,y,z)$ 的径向量为 $\vec{r}$，则点 $P$ 到旋转轴 $l$ 的距离的平方为

$$d^2 = \vec{r}^2 - (\vec{r}\cdot\vec{s}) = (1-\alpha^2)x^2 + (1-\beta^2)y^2 + (1-\gamma^2)z^2 - 2\alpha\beta xy - 2\beta\gamma yz - 2\alpha\gamma xz$$

由积分区域的对称性可知

$$\iiint_\Omega \left(2\alpha\beta xy + 2\beta\gamma yz + 2\alpha\gamma xz\right)\mathrm{d}V = 0,$$

其中 $\Omega = \left\{(x,y,z)\,\middle|\,\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} + \dfrac{z^2}{c^2} \le 1\right\}$ 而

$$\iiint_\Omega x^2\,\mathrm{d}V = \int_{-a}^{a}x^2\,\mathrm{d}x\iint_{\frac{y^2}{b^2}+\frac{z^2}{c^2}\le 1-\frac{x^2}{a^2}}\mathrm{d}y\,\mathrm{d}z = \int_{-a}^{a}x^2\cdot\pi ab\left(1-\frac{x^2}{a^2}\right)\mathrm{d}x = \frac{4a^3bc\pi}{15}.$$

或者使用换元法，有

$$\iiint_\Omega x^2\,\mathrm{d}V = \int_0^{2\pi}\mathrm{d}\theta\int_0^{\pi}\mathrm{d}\varphi\int_0^1 a^2r^2\sin^2\varphi\cos^2\theta\cdot abcr^2\sin\varphi\,\mathrm{d}r = \frac{4a^3bc\pi}{15}.$$

所以可得

$$\iiint_\Omega y^2\,\mathrm{d}V = \frac{4ab^3c\pi}{15}, \quad \iiint_\Omega y^2\,\mathrm{d}V = \frac{4abc^3\pi}{15}.$$

> ⚠️ 上式中第二式的被积函数原文件亦印为 $y^2$（按结果 $\dfrac{4abc^3\pi}{15}$ 应为 $z^2$）；另首式 $d^2$ 的中间项原文件印为 $(\vec{r}\cdot\vec{s})$（缺平方，应为 $(\vec{r}\cdot\vec{s})^2$）。两处均照抄并加注。

由转动惯量的定义，有

$$I_l = \iiint_\Omega d^2\,\mathrm{d}V = \frac{4abc\pi}{15}\left[(1-\alpha^2)a^2 + (1-\beta^2)b^2 + (1-\gamma^2)c^2\right].$$

**(2)** 考虑函数 $V(\alpha,\beta,\gamma) = (1-\alpha^2)a^2 + (1-\beta^2)b^2 + (1-\gamma^2)c^2$ 在约束条件 $\alpha^2 + \beta^2 + \gamma^2 = 1$ 的约束条件下的条件极值。

$$L(\alpha,\beta,\gamma,\lambda) = (1-\alpha^2)a^2 + (1-\beta^2)b^2 + (1-\gamma^2)c^2 + \lambda(\alpha^2 + \beta^2 + \gamma^2 - 1)$$

令 $L'_\alpha(\alpha,\beta,\gamma,\lambda) = 0, L'_\beta(\alpha,\beta,\gamma,\lambda) = 0, L'_\gamma(\alpha,\beta,\gamma,\lambda) = 0, L'_\lambda(\alpha,\beta,\gamma,\lambda) = 0$，解得极值点为

$$Q_1(\pm 1, 0, 0, a^2), \quad Q_2(0, \pm 1, 0, b^2), \quad Q_1(0, 0, \pm 1, c^2),$$

比较可知，绕 $z$ 轴（短轴）的转动惯量最大，并且有 $I_{\max} = \dfrac{4abc\pi}{15}(a^2+b^2)$。绕 $x$ 轴（长轴）的转动惯量最小，并且有 $I_{\max} = \dfrac{4abc\pi}{15}(b^2+c^2)$。

> ⚠️ 原文件两处笔误照抄：(i) 第三个极值点误记为 $Q_1$（应与前二者并列记为 $Q_3$）；(ii) 末句求最小值处仍印作 $I_{\max}$（应为 $I_{\min}$）。此外，各极值点括号内第四分量（$a^2,b^2,c^2$）对应 Lagrange 乘子 $\lambda$ 的取值。

---

## 第六题（15分）

**参考答案**：设 $\displaystyle\oint_L \frac{2xy\,\mathrm{d}x + \varphi(x)\,\mathrm{d}y}{x^4 + y^2} = I$，将曲线 $L$ 分割成两段 $L = L_1 + L_2$。设 $L_0$ 不经过原点的光滑曲线，使得 $L_0\cup\overline{L_1}$ 和 $L_0\cup L_2$ 分别组成围绕原点的分段光滑闭曲线。由已知条件可知 $L_0\cup\overline{L_1}$ 和 $L_0\cup L_2$ 上曲线积分相等，有

$$\oint_{L_0\cup\overline{L_1}} \frac{2xy\,\mathrm{d}x + \varphi(x)\,\mathrm{d}y}{x^4 + y^2} = \oint_{L_0\cup L_2} \frac{2xy\,\mathrm{d}x + \varphi(x)\,\mathrm{d}y}{x^4 + y^2}$$

$$\Rightarrow \int_{L_2} + \int_{L_0} = \int_{L_0} + \int_{\overline{L_1}} \Rightarrow \int_{L_2} - \int_{\overline{L_1}} = 0 \Rightarrow \int_{L_2+\overline{L_1}} = 0 \Rightarrow \oint_L \frac{2xy\,\mathrm{d}x + \varphi(x)\,\mathrm{d}y}{x^4 + y^2} = 0.$$

**(2)** 设 $P(x,y) = \dfrac{2xy}{x^4 + y^2}, Q(x,y) = \dfrac{\varphi(x)}{x^4 + y^2}$。令 $\dfrac{\partial P}{\partial y} = \dfrac{\partial Q}{\partial x}$，即

$$\frac{2x^5 - 2xy^2}{\left(x^4 + y^2\right)^2} = \frac{\varphi'(x)\left(x^4 + y^2\right) - 4x^3\varphi(x)}{\left(x^4 + y^2\right)^2}.$$

解得 $\varphi(x) = -x^2$。

**(3)** 设 $D$ 为正向闭曲线 $C_a: x^4 + y^2 = 1$ 所围的闭区域，则

$$\oint_C \frac{2xy\,\mathrm{d}x + \varphi(x)\,\mathrm{d}y}{x^4 + y^2} = \oint_{C_a} \frac{2xy\,\mathrm{d}x - x^2\,\mathrm{d}y}{x^4 + y^2}$$

利用格林公式，有

$$\oint_{C_a} \frac{2xy\,\mathrm{d}x - x^2\,\mathrm{d}y}{x^4 + y^2} = \oint_{C_a} 2xy\,\mathrm{d}x - x^2\,\mathrm{d}y = \iint_D (-4x)\,\mathrm{d}x\,\mathrm{d}y = 0.$$

---

## 附：本文件加注的原文笔误一览

| 位置 | 原文排印 | 按推导应为 |
|---|---|---|
| 一(3) $I_1$ 计算式括号内首项 | $x^n e^{-sx}$ | $x\,e^{-sx}$（仅记号沿用之笔误，结果 $\frac{1}{s^2}$ 无误） |
| 第二题 | 「使得 $f'(c) > 0$」 | $f'(c) < 0$ |
| 第二题 | 极限式起首 $f(+\infty)$、$f(-\infty)$ | 按上下文理解为 $f(a)+f'(a)(x-a)$、$f(c)+f'(c)(x-c)$ |
| 第三题 | $\frac{1}{2+2t}\cdot\frac{(2+2t)\psi''(t)-2\psi'(t)}{(2+2t)^3}$ | 中项分母应为 $(2+2t)^2$（与前置因子合并后为 $(2+2t)^3$） |
| 第五题(1) | $d^2 = \vec{r}^2 - (\vec{r}\cdot\vec{s})$ | $d^2 = \vec{r}^2 - (\vec{r}\cdot\vec{s})^2$ |
| 第五题(1) | 第二式 $\iiint_\Omega y^2\,\mathrm{d}V = \frac{4abc^3\pi}{15}$ | 应为 $\iiint_\Omega z^2\,\mathrm{d}V = \frac{4abc^3\pi}{15}$ |
| 第五题(2) | 第三极值点 $Q_1(0,0,\pm 1,c^2)$ | $Q_3(0,0,\pm 1,c^2)$ |
| 第五题(2) | 末句「转动惯量最小，并且有 $I_{\max} = \cdots$」 | $I_{\min} = \cdots$ |
