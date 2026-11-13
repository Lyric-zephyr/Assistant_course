<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC04%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6%E7%B1%BB-%E5%88%9D%E8%B5%9B-2012-%E5%8F%82%E8%80%83%E8%A7%A3%E7%AD%94.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第4届（2012）非数学类初赛 · 官方参考解答

> 来源：考研竞赛数学公众号版（原文件：`../初赛/第04届非数学类-初赛(试题及参考解答).pdf`，原文件首页标题为"2012 年第四届全国大学生数学竞赛初赛（非数学类）试卷及参考答案"）｜本文件仅含解答，题面见同目录《第04届非数学类-初赛-2012.md》
> 转录说明：视觉逐页转写（原 PDF 共 5 页，试题与解答混排，页首页脚的公众号推广信息已按规范省略），公式 KaTeX 语法；"【参考答案】/【参考解答】/【参考证明】/【解法一】/【解法二】"为原文件表述。

---

## 一(1)（6分）

**【参考答案】**：因为 $(n!)^{\frac{1}{n^2}} = e^{\frac{1}{n^2}\ln(n!)}$，而

$$\frac{1}{n^2}\ln(n!) \le \frac{1}{n}\left(\frac{\ln 1}{1} + \frac{\ln 2}{2} + \cdots + \frac{\ln n}{n}\right), \text{且} \lim_{n\to\infty}\frac{\ln n}{n} = 0.$$

所以 $\lim\limits_{n\to\infty}\dfrac{1}{n}\left(\dfrac{\ln 1}{1} + \dfrac{\ln 2}{2} + \cdots + \dfrac{\ln n}{n}\right) = 0$。即 $\lim\limits_{n\to\infty}\dfrac{1}{n^2}\ln(n!) = 0 \Rightarrow \lim\limits_{n\to\infty}(n!)^{\frac{1}{n^2}} = 1$。

---

## 一(2)（6分）

**【参考答案】**：过直线 $L$ 的平面束方程为 $\lambda(2x + y - 3z + 2) + \mu(5x + 5y - 4z + 3) = 0$，

即 $(2\lambda + 5\mu)x + (\lambda + 5\mu)y - (3\lambda + 4\mu)z + 2\lambda + 3\mu = 0$。

若平面 $\pi_1$ 过点 $(4, -3, 1)$，代入得 $\lambda + \mu = 0$，即 $\mu = -\lambda$，从而 $\pi_1$ 的方程为 $3x + 4y - z + 1 = 0$。

若平面束中的平面 $\pi_2$ 与 $\pi_1$ 垂直，则 $3(2\lambda + 5\mu) + 4(\lambda + 5\mu) + 1(3\lambda + 4\mu) = 0$。解得 $\lambda = -3\mu$，从而平面 $\pi_2$ 的方程为 $x - 2y - 5z + 3 = 0$。

---

## 一(3)（6分）

**【参考答案】**：

$$\frac{\partial z}{\partial x} = e^{ax+by}\left[\frac{\partial u}{\partial x} + au(x,y)\right], \qquad \frac{\partial z}{\partial y} = e^{ax+by}\left[\frac{\partial u}{\partial y} + bu(x,y)\right],$$

$$\frac{\partial^2 z}{\partial x\partial y} = e^{ax+by}\left[b\frac{\partial u}{\partial x} + a\frac{\partial u}{\partial y} + abu(x,y)\right],$$

$$\frac{\partial^2 z}{\partial x\partial y} - \frac{\partial z}{\partial x} - \frac{\partial z}{\partial y} + z = e^{ax+by}\left[(b-1)\frac{\partial u}{\partial x} + (a-1)\frac{\partial u}{\partial y} + (ab - a - b + 1)u(x,y)\right],$$

若是上式等于 $0$，只有 $(b-1)\dfrac{\partial u}{\partial x} + (a-1)\dfrac{\partial u}{\partial y} + (ab - a - b + 1)u(x,y) = 0$，由此可得 $a = b = 1$。

---

## 一(4)（6分）

**【参考答案】**：由 $\dfrac{\partial\left[(x + 2y)u\right]}{\partial y} = \dfrac{\partial\left[u\left(x + u^3\right)\right]}{\partial x}$，得

$$\left(x + 4u^3\right)u' = u, \text{即} \frac{dx}{du} - \frac{1}{u}x = 4u^2,$$

（原解答由上面的充要条件直接写出此一阶微分方程，展开过程从略。）

这是一个一阶线性微分方程，于是由公式有通解为

$$x = e^{\ln u}\left(\int 4u^2 e^{-\ln u}\,du + C\right) = u\left(\int 4u\,du + C\right) = u\left(2u^2 + C\right)$$

由 $u(2) = 1$ 得 $C = 0$，所以 $u = \left(\dfrac{x}{2}\right)^{1/3}$。

---

## 一(5)（6分）

**【参考答案】**：因为当 $x > 1$ 时，

$$\left|\sqrt[3]{x}\int_x^{x+1}\frac{\sin t}{\sqrt{t + \cos t}}dt\right| \le \sqrt[3]{x}\int_x^{x+1}\frac{1}{\sqrt{t-1}}dt$$

$$\le 2\sqrt[3]{x}\left(\sqrt{x} - \sqrt{x-1}\right) = \frac{2\sqrt[3]{x}}{\sqrt{x} + \sqrt{x-1}} \to 0\quad (x \to +\infty)$$

所以 $\lim\limits_{x\to+\infty}\sqrt[3]{x}\displaystyle\int_x^{x+1}\frac{\sin t}{\sqrt{t + \cos t}}dt = 0$。

---

## 第二题（10分）

**【参考答案】**：由于

$$\int_0^{n\pi} e^{-2x}|\sin x|\,dx = \sum_{k=1}^{n}\int_{(k-1)\pi}^{k\pi} e^{-2x}|\sin x|\,dx = \sum_{k=1}^{n}\int_{(k-1)\pi}^{k\pi}(-1)^{k-1}e^{-2x}\sin x\,dx$$

应用分部积分法，有

$$\int_{(k-1)\pi}^{k\pi}(-1)^{k-1}e^{-2x}\sin x\,dx = \frac{1}{5}e^{-2k\pi}\left(1 + e^{2\pi}\right)$$

所以有 $\displaystyle\int_0^{n\pi} e^{-2x}|\sin x|\,dx = \frac{1}{5}\left(1 + e^{2\pi}\right)\sum_{k=1}^{n}e^{-2k\pi} = \frac{1}{5}\left(1 + e^{2\pi}\right)\frac{e^{-2\pi} - e^{-2(n+1)\pi}}{1 - e^{-2\pi}}$

当 $n\pi \le x \le (n+1)\pi$ 时，$\displaystyle\int_0^{n\pi} e^{-2x}|\sin x|\,dx \le \int_0^{x} e^{-2x}|\sin x|\,dx \le \int_0^{(n+1)\pi} e^{-2x}|\sin x|\,dx$

当 $n \to \infty$，由两边夹法则，得 $\displaystyle\int_0^{\infty} e^{-2x}|\sin x|\,dx = \lim_{x\to\infty}\int_0^{x} e^{-2x}|\sin x|\,dx = \frac{1}{5}\frac{e^{2\pi} + 1}{e^{2\pi} - 1}$。

**【注】** 如果最后不用夹逼准则，而用

$$\int_0^{\infty} e^{-2x}|\sin x|\,dx = \lim_{n\to\infty}\int_0^{n\pi} e^{-2x}|\sin x|\,dx = \frac{1}{5}\frac{e^{2\pi} + 1}{e^{2\pi} - 1}$$

需要先说明 $\displaystyle\int_0^{\infty} e^{-2x}|\sin x|\,dx$ 收敛。

---

## 第三题（10分）

**【参考解答】**：由泰勒公式 $\sin t = t - \dfrac{\sin(\theta t)}{2}t^2\ (0 < \theta < 1)$。令 $t = \dfrac{1}{x}$ 得

$$\sin\frac{1}{x} = \frac{1}{x} - \frac{\sin\left(\dfrac{\theta}{x}\right)}{2}\left(\frac{1}{x}\right)^2,$$

代入原方程，得

$$x - \frac{1}{2}\sin\left(\frac{\theta}{x}\right) = 2x - 501 \text{ 即 } x = 501 - \frac{1}{2}\sin\left(\frac{\theta}{x}\right)。$$

由此知 $x > 500, 0 < \dfrac{\theta}{x} < \dfrac{1}{500}$，所以有 $|x - 501| = \left|\dfrac{1}{2}\sin\left(\dfrac{\theta}{x}\right)\right| \le \dfrac{1}{2}\cdot\dfrac{\theta}{x} < \dfrac{1}{1000} = 0.001$，即当 $x = 501$ 即为满足题设条件的解。

---

## 第四题（12分）

**【参考答案】**：$y = f(x)$ 上点 $P(x, f(x))$ 处切线方程为 $Y - f(x) = f'(x)(X - x)$。令 $Y = 0$，$X = x - \dfrac{f(x)}{f'(x)}$，由此得 $u = x - \dfrac{f(x)}{f'(x)}$ 且有

$$\lim_{x\to 0}u = \lim_{x\to 0}\left[x - \frac{f(x)}{f'(x)}\right] = -\lim_{x\to 0}\left[\frac{\dfrac{f(x) - f(0)}{x}}{\dfrac{f'(x) - f'(0)}{x}}\right] = -\frac{f'(0)}{f''(0)} = 0.$$

由 $f(x)$ 在 $x = 0$ 处的二阶泰勒公式，

$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2}x^2 + o(x^2) = \frac{f''(0)}{2}x^2 + o(x^2)$$

可得

$$\lim_{x\to 0}\frac{u}{x} = 1 - \lim_{x\to 0}\frac{f(x)}{xf'(x)} = 1 - \lim_{x\to 0}\frac{\dfrac{f''(0)}{2}x^2 + o(x^2)}{xf'(x)}$$

$$= 1 - \frac{1}{2}\lim_{x\to 0}\frac{f''(0) + o(1)}{\dfrac{f'(x) - f'(0)}{x}} = 1 - \frac{1}{2}\cdot\frac{f''(0)}{f''(0)} = \frac{1}{2}.$$

$$\lim_{x\to 0}\frac{x^3 f(u)}{f(x)\sin^3 u} = \lim_{x\to 0}\frac{x^3\left(\dfrac{f''(0)}{2}u^2 + o(u^2)\right)}{u^3\left(\dfrac{f''(0)}{2}x^2 + o(x^2)\right)} = \lim_{x\to 0}\frac{x}{u} = 2.$$

---

## 第五题（12分）

**【参考答案】**：由于 $\displaystyle\int_0^1\left|f\left(\sqrt{x}\right)\right|dx = \int_0^1|f(t)|2t\,dt \le 2\int_0^1|f(t)|dt = 2$，取 $f_n(x) = (n+1)x^n$，则有

$$\int_0^1|f_n(x)|dx = \int_0^1 f_n(x)dx = 1$$

而 $\displaystyle\int_0^1 f_n\left(\sqrt{x}\right)dx = 2\int_0^1 t f_n(t)\,dt = 2\frac{n+1}{n+2} = 2\left(1 - \frac{1}{n+2}\right) \to 2\ (n \to \infty)$。因此最小的实数为 $C = 2$。

---

## 第六题（12分）

**【解法一】**：即 $g = g(t) = \dfrac{\sqrt{1 + 4t^2} - 1}{2}$，则 $\Omega$ 在 $xOy$ 面上的投影为 $x^2 + y^2 \le g$。在曲线

$$S:\begin{cases}z = x^2 + y^2,\\ x^2 + y^2 + z^2 = t^2\end{cases}$$

上任取一点 $(x, y, z)$，则圆雕到点的射线和 $z$ 轴的夹角为

$$\theta_t = \arccos\frac{z}{t} = \arccos\frac{g}{t}。$$

（"圆雕"原文如此，疑为"圆锥"之误。）

取 $\Delta t > 0$，则 $\theta_t > \theta_{t+\Delta t}$。对于固定的 $t > 0$，考虑积分差 $F(t + \Delta t) - F(t)$，这是一个在厚度为 $\Delta t$ 的球壳上的积分。原点到球壳边缘上的点的射线和 $z$ 轴的夹角在 $\theta_t, \theta_{t+\Delta t}$ 之间。用球坐标计算积分，由积分的连续性可知，存在 $\alpha = \alpha(\Delta t)$，$\theta_{t+\Delta t} \le \alpha \le \theta_t$ 使得

$$F(t + \Delta t) - F(t) = \int_0^{2\pi}d\varphi\int_0^{\alpha}d\theta\int_t^{t+\Delta t}f(r^2)r^2\sin\theta\,dr$$

即 $F(t + \Delta t) - F(t) = 2\pi(1 - \cos\alpha)\displaystyle\int_t^{t+\Delta t}f(r^2)r^2\,dr$。当 $\Delta t \to 0^+$，

$$\cos\alpha \to \cos\theta_t = \frac{g(t)}{t}, \qquad \frac{1}{\Delta t}\int_t^{t+\Delta t}f(r^2)r^2\,dr \to t^2 f(t^2).$$

故 $F(t)$ 的右导数为

$$2\pi\left(1 - \frac{g(t)}{t}\right)t^2 f(t^2) = \pi\left(2t + 1 - \sqrt{1 + 4t^2}\right)tf(t^2).$$

当 $\Delta t < 0$，考虑 $F(t + \Delta t) - F(t)$ 可得到同样的左导数，因此

$$F'(t) = \pi\left(2t + 1 - \sqrt{1 + 4t^2}\right)tf(t^2).$$

**【解法二】**：令 $x = r\cos\theta, y = r\sin\theta, z = z$，则区域 $\Omega$ 表示为

$$\Omega: 0 \le \theta \le 2\pi, 0 \le r \le a, r^2 \le z \le \sqrt{t^2 - r^2},$$

其中 $a$ 满足 $a^2 + a^4 = t^2$，$a = \dfrac{\sqrt{1 + 4t^2} - 1}{2}$（原文如此；由 $a^2 + a^4 = t^2$ 解出的应为 $a^2 = \dfrac{\sqrt{1 + 4t^2} - 1}{2}$），有

$$F(t) = \int_0^{2\pi}d\theta\int_0^{a}rdr\int_{r^2}^{\sqrt{t^2 - r^2}}f(r^2 + z^2)\,dz = 2\pi\int_0^{a}\left[\int_{r^2}^{\sqrt{t^2 - r^2}}f(r^2 + z^2)\,dz\right]rdr$$

从而有

$$F'(t) = 2\pi\left[a\int_{a^2}^{\sqrt{t^2 - a^2}}f(a^2 + z^2)\,dz\dfrac{da}{dt} + \int_0^{a}rf(r^2 + t^2 - r^2)\dfrac{t}{\sqrt{t^2 - r^2}}dr\right]$$

注意到 $\sqrt{t^2 - a^2} = a^2$，第一个积分为 $0$，所以有

$$F'(t) = 2\pi t f(t^2)\int_0^{a}\frac{r}{\sqrt{t^2 - r^2}}dr = -\pi t f(t^2)\int_0^{a}\frac{d\left(t^2 - r^2\right)}{\sqrt{t^2 - r^2}}$$

所以 $F'(t) = \pi t f(t^2)\left(2t + 1 - \sqrt{1 + 4t^2}\right)$。

---

## 第七题（14分）

> 题面原文对照：本解答版原文件中，小题 (1) 的条件用圆括号、小题 (2) 的条件用方括号（`[...]`），与题面转录文件的圆括号写法略有出入，此处按原样保留。

**【参考证明】**：**(1)** 设 $\lim\limits_{n\to\infty}\left(\dfrac{a_n}{a_{n+1}b_n} - \dfrac{1}{b_{n+1}}\right) = 2\delta > \delta > 0$，则存在 $N \in \mathbf{N}$，对于任意的 $n \ge N$ 时，

$$\frac{a_n}{a_{n+1}b_n} - \frac{1}{b_{n+1}} > \delta,\quad \frac{a_n}{b_n} - \frac{a_{n+1}}{b_{n+1}} > \delta a_{n+1},\quad a_{n+1} < \frac{1}{\delta}\left(\frac{a_n}{b_n} - \frac{a_{n+1}}{b_{n+1}}\right)$$

$$\sum_{n=N}^{m}a_{n+1} < \frac{1}{\delta}\sum_{n=N}^{m}\left(\frac{a_n}{b_n} - \frac{a_{n+1}}{b_{n+1}}\right) \le \frac{1}{\delta}\left(\frac{a_N}{b_N} - \frac{a_{m+1}}{b_{m+1}}\right) \le \frac{1}{\delta}\frac{a_N}{b_N},$$

因而 $\displaystyle\sum_{n=1}^{\infty}a_n$ 的部分和有上界，从而 $\displaystyle\sum_{n=1}^{\infty}a_n$ 收敛。

**(2)** 若 $\lim\limits_{n\to\infty}\left(\dfrac{a_n}{a_{n+1}b_n} - \dfrac{1}{b_{n+1}}\right) < \delta < 0$，则存在 $N \in \mathbf{N}$，对于任意的 $n \ge N$ 时，$\dfrac{a_n}{a_{n+1}} < \dfrac{b_n}{b_{n+1}}$，有

$$a_{n+1} > \frac{b_{n+1}}{b_n}a_n > \cdots > \frac{b_{n+1}}{b_n}\frac{b_n}{b_{n-1}}\cdots\frac{b_{N+1}}{b_N}a_N = \frac{a_N}{b_N}b_{n+1},$$

于是由 $\displaystyle\sum_{n=1}^{\infty}b_n$ 发散，得到 $\displaystyle\sum_{n=1}^{\infty}a_n$ 发散。
