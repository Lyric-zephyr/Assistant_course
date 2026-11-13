<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC03%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6%E7%B1%BB-%E5%88%9D%E8%B5%9B-2011-%E5%8F%82%E8%80%83%E8%A7%A3%E7%AD%94.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第3届（2011）非数学类初赛 · 官方参考解答

> 来源：考研竞赛数学公众号版（原文件：第03届非数学类-初赛(试题及参考解答).pdf）｜本文件仅含解答，题面见同目录《第03届非数学类-初赛-2011.md》
> 转录说明：视觉逐页转写，公式 KaTeX 语法；"【参考解答】"为原文件表述。

## 一(1)（6分）

**【参考解答】**：因为
$$\frac{(1+x)^{\frac{2}{x}} - e^2\left(1-\ln(1+x)\right)}{x} = \frac{e^{\frac{2}{x}\ln(1+x)} - e^2\left(1-\ln(1+x)\right)}{x}$$
$$\lim_{x\to 0}\frac{e^2\ln(1+x)}{x} = e^2,$$
$$\lim_{x\to 0}\frac{e^{\frac{2}{x}\ln(1+x)} - e^2}{x} = e^2\lim_{x\to 0}\frac{e^{\frac{2}{x}\ln(1+x)-2} - 1}{x} = e^2\lim_{x\to 0}\frac{\frac{2}{x}\ln(1+x) - 2}{x}$$
$$= 2e^2\lim_{x\to 0}\frac{\ln(1+x) - x}{x^2} = 2e^2\lim_{x\to 0}\frac{\frac{1}{1+x} - 1}{2x} = -e^2.$$
所以
$$\lim_{x\to 0}\frac{(1+x)^{\frac{2}{x}} - e^2\left(1-\ln(1+x)\right)}{x} = 0.$$

**【注】** 可以考虑洛必达法则、带皮亚诺余项的麦克劳林公式，具体参见视频解析！

## 一(2)（6分）

**【参考解答】**：若 $\theta = 0$，则 $\lim\limits_{n\to\infty} a_n = 1$。

若 $\theta \neq 0$，则当 $n$ 充分大，使得 $0 < \left|\dfrac{\theta}{2^n}\right| < \dfrac{\pi}{2}$ 时，
$$a_n = \cos\frac{\theta}{2}\cdot\cos\frac{\theta}{2^2}\cdots\cdots\cos\frac{\theta}{2^n} = \cos\frac{\theta}{2}\cdot\cos\frac{\theta}{2^2}\cdots\cdots\cos\frac{\theta}{2^n}\cdot\sin\frac{\theta}{2^n}\cdot\frac{1}{\sin\frac{\theta}{2^n}}$$
$$= \cos\frac{\theta}{2}\cdot\cos\frac{\theta}{2^2}\cdots\cdots\cos\frac{\theta}{2^{n-2}}\cdot\frac{1}{2^2}\sin\frac{\theta}{2^{n-2}}\cdot\frac{1}{\sin\frac{\theta}{2^n}} = \frac{\sin\theta}{2^n\sin\frac{\theta}{2^n}}.$$
从而有，
$$\lim_{n\to\infty} a_n = \lim_{n\to\infty}\frac{\sin\theta}{2^n\sin\frac{\theta}{2^n}} = \frac{\sin\theta}{\theta}.$$

## 一(3)（6分）

**【参考解答】**：设
$$D_1 = \left\{(x,y)\mid 0 \leqslant x \leqslant \frac{1}{2},\ 0 \leqslant y \leqslant 2\right\},$$
$$D_2 = \left\{(x,y)\mid \frac{1}{2} \leqslant x \leqslant 2,\ 0 \leqslant y \leqslant \frac{1}{x}\right\},\quad D_3 = \left\{(x,y)\mid \frac{1}{2} \leqslant x \leqslant 2,\ \frac{1}{x} \leqslant y \leqslant 2\right\},$$
$$\iint_{D_1\cup D_2}\mathrm{d}x\,\mathrm{d}y = 1 + \int_{\frac{1}{2}}^{2}\frac{\mathrm{d}x}{x} = 1 + 2\ln 2,\qquad \iint_{D_3}\mathrm{d}x\,\mathrm{d}y = 3 - 2\ln 2,$$
$$\iint_D \operatorname{sgn}(xy-1)\,\mathrm{d}x\,\mathrm{d}y = \iint_{D_3}\mathrm{d}x\,\mathrm{d}y - \iint_{D_1\cup D_2}\mathrm{d}x\,\mathrm{d}y = 2 - 4\ln 2.$$

**【注】** 由积分的几何意义，积分等于 2 倍 $D_3$ 矩形的面积减去矩形的面积．具体分析参见解析视频！

> *转录注：以上【注】句按原文照录；其中"2 倍 $D_3$ 矩形的面积"疑为原文笔误，按几何意义应为"2 倍 $D_3$ 的面积减去矩形 $D$ 的面积"，即 $\iint_D\operatorname{sgn}(xy-1)\,\mathrm{d}x\,\mathrm{d}y = 2\iint_{D_3}\mathrm{d}x\,\mathrm{d}y - \iint_D\mathrm{d}x\,\mathrm{d}y$。*

## 一(4)（6分）

**【参考解答】**：令 $S(x) = \sum\limits_{n=1}^{\infty}\frac{2n-1}{2^n}x^{2n-2}$，定义区间为 $\left(-\sqrt{2},\sqrt{2}\right)$．$\forall x \in \left(-\sqrt{2},\sqrt{2}\right)$，则
$$\int_0^x S(t)\,\mathrm{d}t = \sum_{n=1}^{\infty}\int_0^x \frac{2n-1}{2^n}t^{2n-2}\,\mathrm{d}t = \sum_{n=1}^{\infty}\frac{x^{2n-1}}{2^n} = \frac{x}{2}\sum_{n=1}^{\infty}\left(\frac{x^2}{2}\right)^{n-1} = \frac{x}{2-x^2}.$$
所以有
$$S(x) = \left(\frac{x}{2-x^2}\right)' = \frac{2+x^2}{\left(2-x^2\right)^2},\quad x \in \left(-\sqrt{2},\sqrt{2}\right).$$
$$\sum_{n=1}^{\infty}\frac{2n-1}{2^{2n-1}} = \sum_{n=1}^{\infty}\frac{2n-1}{2^n}\left(\frac{1}{\sqrt{2}}\right)^{2n-2} = S\left(\frac{1}{\sqrt{2}}\right) = \frac{10}{9}.$$

**【注】** 一般思路参见解析视频！

## 第二题（16分）

**【参考证明】**：

**1.** 由 $\lim\limits_{n\to\infty} a_n = a$，$\exists M > 0$ 使得 $|a_n| \leqslant M$，且 $\forall \varepsilon > 0, \exists N_1 \in N$，当 $n > N_1$ 时，$|a_n - a| < \dfrac{\varepsilon}{2}$．因为 $\exists N_2 > N_1$，当 $n > N_2$ 时，$\dfrac{N_1(M+|a|)}{n} < \dfrac{\varepsilon}{2}$．于是
$$\left|\frac{a_1 + a_2 + \cdots + a_n}{n} - a\right| \leqslant \frac{N_1(M+|a|)}{n}\cdot\frac{\varepsilon}{2} + \frac{n-N_1}{n}\cdot\frac{\varepsilon}{2} < \varepsilon,$$
所以 $\lim\limits_{n\to\infty}\dfrac{a_1 + a_2 + \cdots + a_n}{n} = a$．

> *转录注：上式右端第一项按原文照录为 $\frac{N_1(M+|a|)}{n}\cdot\frac{\varepsilon}{2}$；按证明思路该项即为 $\frac{N_1(M+|a|)}{n} < \frac{\varepsilon}{2}$，此处多出的 $\frac{\varepsilon}{2}$ 因子疑为原文笔误。*

**2.** 对于 $i = 0, 1, \cdots, p-1$，令 $A_n^{(i)} = a_{(n+1)p+i} - a_{np+i}$，易知 $\left\{A_n^{(i)}\right\}$ 为 $\left\{a_{n+p} - a_n\right\}$ 的子列。由于 $\lim\limits_{n\to\infty}\left(a_{n+p} - a_n\right) = \lambda$，知 $\lim\limits_{n\to\infty} A_n^{(i)} = \lambda$，从而
$$\lim_{n\to\infty}\frac{A_1^{(i)} + A_2^{(i)} + \cdots + A_n^{(i)}}{n} = \lambda,$$
而 $A_1^{(i)} + A_2^{(i)} + \cdots + A_n^{(i)} = a_{(n+1)p+i} - a_{p+i}$，所以
$$\lim_{n\to\infty}\frac{a_{(n+1)p+i} - a_{p+i}}{n} = \lambda.$$
由 $\lim\limits_{n\to\infty}\dfrac{a_{p+i}}{n} = 0$，知 $\lim\limits_{n\to\infty}\dfrac{a_{(n+1)p+i}}{n} = \lambda$．从而
$$\lim_{n\to\infty}\frac{a_{(n+1)p+i}}{(n+1)p+i} = \lim_{n\to\infty}\frac{n}{(n+1)p+i}\cdot\frac{a_{(n+1)p+i}}{n} = \frac{\lambda}{p}.$$
$\forall m \in N$，$\exists n, p, i \in N$，$(0 \leqslant i \leqslant p-1)$，使得 $m = np + i$，且当 $m \to \infty$ 时，$n \to \infty$，所以有
$$\lim_{m\to\infty}\frac{a_m}{m} = \frac{\lambda}{p}.$$

**【注】** 探索思路过程参见解析视频

## 第三题（15分）

**【参考证明】**：由麦克劳林公式，得
$$f(x) = f(0) + \frac{1}{2!}f''(0)x^2 + \frac{1}{3!}f'''(\eta)x^3,$$
$\eta$ 介于 $0$ 和 $x$ 之间，$x \in [-1,1]$．分别取 $x = 1$，$x = -1$，得
$$1 = f(1) = f(0) + \frac{1}{2!}f''(0) + \frac{1}{3!}f'''(\eta_1),\quad 0 < \eta_1 < 1.$$
$$0 = f(-1) = f(0) + \frac{1}{2!}f''(0) - \frac{1}{3!}f'''(\eta_2),\quad -1 < \eta_2 < 0.$$
两式相减，得 $f'''(\eta_1) + f'''(\eta_2) = 6$．

由于 $f'''(x)$ 在闭区间 $[-1,1]$ 上连续，因此 $f'''(x)$ 在闭区间 $[\eta_2,\eta_1]$ 上有最大值 $M$ 和最小值 $m$，从而有
$$m \leqslant \frac{f'''(\eta_1) + f'''(\eta_2)}{2} \leqslant M.$$
再由闭区间上连续函数的介值定理，至少存在一点 $x_0 \in [\eta_2,\eta_1] \subset (-1,1)$，使得
$$f'''(x_0) = \frac{f'''(\eta_1) + f'''(\eta_2)}{2} = 3.$$

## 第四题（15分）

**【参考解答】**：在 $x$ 轴的 $x$ 处取一小段 $\mathrm{d}x$，其质量为 $\rho\,\mathrm{d}x$，到质点的距离为 $\sqrt{h^2 + x^2}$，这一小段与质点的引力是 $\mathrm{d}F = \dfrac{Gm\rho\,\mathrm{d}x}{h^2 + x^2}$（其中 $G$ 为引力常数），则有
$$F_x = \int_a^{+\infty}\mathrm{d}F_x = \int_a^{+\infty}\frac{Gm\rho x\,\mathrm{d}x}{\left(h^2 + x^2\right)^{3/2}} = \frac{Gm\rho}{2}\int_a^{+\infty}\frac{\mathrm{d}\left(x^2\right)}{\left(h^2 + x^2\right)^{3/2}}$$
$$= -Gm\rho\left(h^2 + x^2\right)^{-1/2}\Big|_a^{+\infty} = \frac{Gm\rho}{\sqrt{h^2 + a^2}}.$$
类似有
$$F_y = \int_a^{+\infty}\mathrm{d}F_y = \int_a^{+\infty}\frac{Gm\rho h\,\mathrm{d}x}{\left(h^2 + x^2\right)^{3/2}} = \int_{\arctan\frac{a}{h}}^{\frac{\pi}{2}}\frac{Gm\rho h^2\sec^2 t\,\mathrm{d}t}{h^3\sec^3 t}$$
$$= \frac{Gm\rho}{h}\int_{\arctan\frac{a}{h}}^{\frac{\pi}{2}}\cos t\,\mathrm{d}t = \frac{Gm\rho}{h}\left(1 - \sin\arctan\frac{a}{h}\right).$$
所求引力向量为 $\vec{F} = \left(F_x, F_y\right)$．

## 第五题（15分）

**【参考解答】**：对方程两边分别关于 $x$，$y$ 求导，
$$\frac{\partial z}{\partial x}F_u' - \frac{1}{x^2}F_u' + \frac{\partial z}{\partial x}F_v' = 0,\qquad F_u'\frac{\partial z}{\partial y} + F_v'\frac{\partial z}{\partial y} + F_v'\frac{1}{y^2} = 0$$
由此可得
$$\frac{\partial z}{\partial x} = \frac{F_u'}{x^2\left(F_u' + F_v'\right)},\qquad \frac{\partial z}{\partial y} = \frac{-F_v'}{y^2\left(F_u' + F_v'\right)},$$
所以 $x^2\dfrac{\partial z}{\partial x} - y^2\dfrac{\partial z}{\partial y} = 1$．对该式再关于 $x$，$y$ 求导，有
$$2x\frac{\partial z}{\partial x} + x^2\frac{\partial^2 z}{\partial x^2} - y^2\frac{\partial^2 z}{\partial y\partial x} = 0,\qquad x^2\frac{\partial^2 z}{\partial x\partial y} - 2y\frac{\partial z}{\partial y} - y^2\frac{\partial^2 z}{\partial y^2} = 0$$
第一个等式乘以 $x$，第二个等式乘以 $y$，相加借助于第一个等式的结论可得
$$x^3\frac{\partial^2 z}{\partial x^2} + xy(x-y)\frac{\partial^2 z}{\partial x\partial y} - y^3\frac{\partial^2 z}{\partial y^2} + 2 = 0.$$

## 第六题（15分）

**【参考证明】**：由 $\Sigma$ 的面积为 $4\pi$。当 $a$，$b$，$c$ 都为零时，等式显然成立。当它们不全为 $0$ 时，可知原点到平面 $ax + by + cz + d = 0$ 的距离是
$$\frac{|d|}{\sqrt{a^2 + b^2 + c^2}}.$$
设平面 $P_u$：$u = \dfrac{ax + by + cz}{\sqrt{a^2 + b^2 + c^2}}$ 其中 $u$ 固定，则 $|u|$ 是原点到平面 $P_u$ 的距离，从而 $-1 \leqslant u \leqslant 1$。两平面 $P_u$ 和 $P_{u+\mathrm{d}u}$ 截单位球 $\Sigma$ 的截下的部分上，被积函数取值为 $f\left(\sqrt{a^2 + b^2 + c^2}\,u\right)$。这部分摊开可以看成是一个细长条，这个细长条的长是 $2\pi\sqrt{1-u^2}$，宽是 $\dfrac{\mathrm{d}u}{\sqrt{1-u^2}}$，它的面积为 $2\pi\,\mathrm{d}u$，故得证。
