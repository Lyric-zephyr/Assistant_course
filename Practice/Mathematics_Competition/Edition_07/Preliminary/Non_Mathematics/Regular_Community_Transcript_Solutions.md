<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC07%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6%E7%B1%BB-%E5%88%9D%E8%B5%9B-2015-%E5%8F%82%E8%80%83%E8%A7%A3%E7%AD%94.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第07届（2015）非数学类初赛 · 参考答案

> **来源**：原文件页首/页脚水印为「公众号：竞赛资料网」（页脚原文：更多竞赛资料、考试资料，尽在微信公众号：竞赛资料网）；原文件：`第07届非数学类-初赛(试题及参考解答).pdf`｜本文件仅含解答，题面见同目录《第07届非数学类-初赛-2015.md》
> ⚠️ 任务描述称此件为「考研竞赛数学」公众号出品的参考解答版，但 PDF 内全部水印与页脚均作「竞赛资料网」，未出现「考研竞赛数学」字样，此处照实记录为「竞赛资料网」版；原件题注为「2015 年第七届预赛（非数学类）参考答案」，非官方发布，本标题据此转写。
> **转录说明**：全 5 页按 140 dpi 通读、关键公式以 288～560 dpi 局部放大逐字符核对后转写；公式为 KaTeX 语法。原件以「解：」「证明：」「【解】」标出解答，本文照录；原件各步骤后所附长虚线记分符（如「----------------------------4 分」）统一转写为「---------- 4 分」并保留；原文笔误照录并随文以〔〕加注。原件含若干无文字的黄色高亮批注（仅为视觉标记），转写不保留。

---

## 一(1)（6分）

**解**：由于
$$\frac{1}{n+1}\sum_{i=1}^{n}\sin\frac{i}{n}\pi\le\sum_{i=1}^{n}\frac{\sin\frac{i}{n}\pi}{n+\frac{i}{n}}\le\frac{1}{n}\sum_{i=1}^{n}\sin\frac{i}{n}\pi,$$
而
$$\lim_{n\to\infty}\frac{1}{n+1}\sum_{i=1}^{n}\sin\frac{i}{n}\pi=\lim_{n\to\infty}\frac{n}{(n+1)\pi}\cdot\frac{\pi}{n}\sum_{i=1}^{n}\sin\frac{i}{n}\pi=\frac{1}{\pi}\int_0^{\pi}\sin x\,dx=\frac{2}{\pi},$$
$$\lim_{n\to\infty}\frac{1}{n}\sum_{i=1}^{n}\sin\frac{i}{n}\pi=\lim_{n\to\infty}\frac{1}{\pi}\cdot\frac{\pi}{n}\sum_{i=1}^{n}\sin\frac{i}{n}\pi=\frac{1}{\pi}\int_0^{\pi}\sin x\,dx=\frac{2}{\pi}。$$
所以所求极限是 $\dfrac{2}{\pi}$。

---

## 一(2)（6分）

**解**：方程对 $x$ 求导，得到
$$\left(1+\frac{1}{y}\frac{\partial z}{\partial x}\right)F_u+\left(\frac{1}{x}\frac{\partial z}{\partial x}-\frac{z}{x^2}\right)F_v=0$$
即
$$x\frac{\partial z}{\partial x}=\frac{y(zF_v-x^2F_u)}{xF_u+yF_v}。$$
同样，方程对 $y$ 求导，得到
$$y\frac{\partial z}{\partial y}=\frac{x(zF_u-y^2F_v)}{xF_u+yF_v}。$$
于是
$$x\frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}=\frac{z(xF_u+yF_v)-xy(xF_u+yF_v)}{xF_u+yF_v}=z-xy$$

---

## 一(3)（6分）

**解**：曲面 $z=x^2+y^2+1$ 在点 $M(1,-1,3)$ 的切平面：$2(x-1)-2(y+1)-(z-3)=0$，
即 $z=2x-2y-1$。联立
$$\begin{cases}z=x^2+y^2\\ z=2x-2y-1\end{cases},$$
得到所围区域的投影 $D$ 为：$(x-1)^2+(y+1)^2\le 1$。

所求体积
$$V=\iint_D[(2x-2y-1)-(x^2+y^2)]dxdy=\iint_D[1-(x-1)^2-(y+1)^2]dxdy$$
令
$$\begin{cases}x-1=r\cos t\\ y+1=r\sin t\end{cases},\qquad V=\int_0^{2\pi}dt\int_0^1(1-r^2)rdr=\frac{\pi}{2}。$$

---

## 一(4)（6分）

**解**：由傅里叶收敛定理，易知 $f(0)=3/2$.

〔注：原文如此，表述从简；严格地说，应为其傅里叶级数在间断点 $x=0$ 处收敛于 $\dfrac{f(0^-)+f(0^+)}{2}=\dfrac{3+0}{2}=\dfrac{3}{2}$。〕

---

## 一(5)（6分）

**【解】** 由于
$$u^2(x)=\int_0^{+\infty}e^{-xt^2}dt\int_0^{+\infty}e^{-xs^2}ds=\iint_{s\ge 0,\,t\ge 0}e^{-x(s^2+t^2)}dsdt,$$
故有
$$u^2(x)=\int_0^{\pi/2}d\varphi\int_0^{+\infty}e^{-x\rho^2}\rho d\rho=\frac{\pi}{4x}\int_0^{+\infty}e^{-x\rho^2}d_\rho(x\rho^2)=-\frac{\pi}{4x}e^{-x\rho^2}\Big|_{\rho=0}^{\rho=+\infty}=\frac{\pi}{4x}。$$
所以 $u(x)=\dfrac{\sqrt{\pi}}{2\sqrt{x}}$。

---

## 第二题（12分）

**解**：显然，$O(0,0,0)$ 为 $M$ 的顶点，$A(1,0,0),B(0,1,0),C(0,0,1)$ 在 $M$ 上。由 $A,B,C$ 三点决定的平面 $x+y+z=1$ 与球面 $x^2+y^2+z^2=1$ 的交线 $L$ 是 $M$ 的准线。---------- 4 分

设 $P(x,y,z)$ 是 $M$ 上的点，$(u,v,w)$ 是 $M$ 的母线 $OP$ 与 $L$ 的交点，则 $OP$ 的方程为 $\dfrac{x}{u}=\dfrac{y}{v}=\dfrac{z}{w}=\dfrac{1}{t}$，即 $u=xt,v=yt,w=zt$。---------- 8 分

代入准线方程，得
$$\begin{cases}(x+y+z)t=1\\ (x^2+y^2+z^2)t^2=1\end{cases}。$$
消除 $t$，得到圆锥面 $M$ 的方程 $xy+yz+zx=0$。---------- 12 分

---

## 第三题（12分）

**证明**　**1.** 若 $\beta=0$。
对于 $\forall x\in(a,b)$，有
$$f'(x)=\alpha f(x),\quad f''(x)=\alpha f'(x)=\alpha^2f(x),\cdots,f^{(n)}(x)=\alpha^nf(x)。$$
从而 $f(x)$ 在 $(a,b)$ 内无穷次可导。---------- 4 分

**2.** 若 $\beta\ne 0$。对于 $\forall x\in(a,b)$，有
$$f''(x)=\frac{f'(x)-\alpha f(x)}{\beta}=A_1f'(x)+B_1f(x),\tag{1}$$
其中 $A_1=1/\beta,\ B_1=\alpha/\beta$。---------- 6 分

〔注：原文如此。由上式右端 $\dfrac{f'(x)-\alpha f(x)}{\beta}$ 展开应得 $B_1=-\alpha/\beta$，原文此处脱漏负号，本转录照录。〕

因为（1）右端可导，从而
$$f'''(x)=A_1f''(x)+B_1f'(x)。$$---------- 8 分

设 $f^{(n)}(x)=A_1f^{(n-1)}(x)+B_1f^{(n-2)}(x),n>1$，则 $f^{(n+1)}(x)=A_1f^{(n)}(x)+B_1f^{(n-1)}(x)$。
故 $f(x)$ 任意阶可导。---------- 12 分

---

## 第四题（14分）

**解**：因
$$\lim_{n\to\infty}\frac{a_{n+1}}{a_n}=\lim_{n\to\infty}\frac{(n+1)^3+2}{(n+2)(n^3+2)}=0。$$
固收敛半径 $R=+\infty$，收敛域为 $(-\infty,+\infty)$。---------- 4 分

〔注：「固」原文如此，应为「故」。〕

由
$$\frac{n^3+2}{(n+1)!}=\frac{(n+1)n(n-1)}{(n+1)!}+\frac{n+1}{(n+1)!}+\frac{1}{(n+1)!}=\frac{1}{(n-2)!}+\frac{1}{n!}+\frac{1}{(n+1)!}\quad(n\ge 2)$$
及幂级数 $\displaystyle\sum_{n=2}^{\infty}\frac{1}{(n-2)!}(x-1)^n$，$\displaystyle\sum_{n=0}^{\infty}\frac{1}{n!}(x-1)^n$ 和 $\displaystyle\sum_{n=0}^{\infty}\frac{1}{(n+1)!}(x-1)^n$ 的收敛域皆为 $(-\infty,+\infty)$ 得
$$\sum_{n=0}^{\infty}\frac{n^3+2}{(n+1)!}(x-1)^n=\sum_{n=2}^{\infty}\frac{1}{(n-2)!}(x-1)^n+\sum_{n=0}^{\infty}\frac{1}{n!}(x-1)^n+\sum_{n=0}^{\infty}\frac{1}{(n+1)!}(x-1)^n。$$---------- 7 分

用 $S_1(x)$，$S_2(x)$ 和 $S_3(x)$ 分别表示上式右端三个幂级数的和函数。依据 $e^x$ 的展开式得到
$$S_1(x)=(x-1)^2\sum_{n=0}^{\infty}\frac{1}{n!}(x-1)^n=(x-1)^2e^{x-1},\qquad S_2(x)=e^{x-1}$$
再由
$$(x-1)S_3(x)=\sum_{n=0}^{\infty}\frac{1}{(n+1)!}(x-1)^{n+1}=\sum_{n=1}^{\infty}\frac{1}{n!}(x-1)^n=e^{x-1}-1$$
得到，当 $x\ne 1$ 时 $S_3(x)=\dfrac{1}{x-1}(e^{x-1}-1)$。---------- 10 分

又 $S_3(1)=1$。---------- 12 分

综合以上讨论，最终得到所给幂级数的和函数
$$S(x)=\begin{cases}(x^2-2x+2)e^{x-1}+\dfrac{1}{x-1}(e^{x-1}-1),& x\ne 1\\[2pt] 2,& x=1\end{cases}$$---------- 14 分

〔注：原件此处分段函数排版略挤压（「$2$」与「$x=1$」两处原带黄色高亮标记），内容如上照录。〕

---

## 第五题（16分）

**证明**：（1）若 $\forall x\in[0,1]$，$|f(x)|\le 4$，则
$$1=\int_0^1\left(x-\frac{1}{2}\right)f(x)dx\le\int_0^1\left|x-\frac{1}{2}\right||f(x)|dx\le 4\int_0^1\left|x-\frac{1}{2}\right|dx=1$$---------- 4 分

因此 $\displaystyle\int_0^1\left|x-\frac{1}{2}\right||f(x)|dx=1$。而 $4\displaystyle\int_0^1\left|x-\frac{1}{2}\right|dx=1$，
故
$$\int_0^1\left|x-\frac{1}{2}\right|(4-|f(x)|)dx=0，$$---------- 8 分

所以对于任意的 $x\in[0,1]$，$|f(x)|=4$，由连续性知 $f(x)\equiv 4$ 或 $f(x)\equiv -4$。
这就与条件 $\displaystyle\int_0^1 f(x)dx=0$ 矛盾。
故 $\exists x_0\in[0,1],$ 使 $|f(x_0)|>4$---------- 10 分

（2）先证 $\exists x_2\in[0,1]$，使 $|f(x_2)|<4$。若不然，对任何 $x\in[0,1]$，$|f(x)|\ge 4$ 成立。则，
$f(x)\ge 4$ 恒成立，或者 $f(x)\le -4$ 恒成立，与 $\displaystyle\int_0^1 f(x)dx=0$ 矛盾。再由 $f(x)$ 的连续性及（1）的结果，利用介值定理 $\exists x_1\in[0,1]$ 使 $|f(x_1)|=4$。---------- 16 分

---

## 第六题（16分）

**证明**：在点 $(0,0)$ 展开 $f(x,y)$ 得
$$f(x,y)=\frac{1}{2}\left(x\frac{\partial}{\partial x}+y\frac{\partial}{\partial y}\right)^2f(\theta x,\theta y)=\frac{1}{2}\left(x^2\frac{\partial^2}{\partial x^2}+2xy\frac{\partial^2}{\partial x\partial y}+y^2\frac{\partial^2}{\partial y^2}\right)f(\theta x,\theta y),$$
其中 $\theta\in(0,1)$。---------- 6 分

记 $(u,v,w)=\left(\dfrac{\partial^2}{\partial x^2},\dfrac{\partial^2}{\partial x\partial y},\dfrac{\partial^2}{\partial y^2}\right)f(\theta x,\theta y)$，则
$$f(x,y)=\frac{1}{2}\left(ux^2+2vxy+wy^2\right)。$$
由于 $\|(u,\sqrt{2}v,w)\|=\sqrt{u^2+2v^2+w^2}\le\sqrt{M}$ 以及 $\|(x^2,\sqrt{2}xy,y^2)\|=x^2+y^2$，我们有
$$\left|(u,\sqrt{2}v,w)\cdot(x^2,\sqrt{2}xy,y^2)\right|\le\sqrt{M}\left(x^2+y^2\right),$$
即
$$|f(x,y)|\le\frac{1}{2}\sqrt{M}\left(x^2+y^2\right)。$$---------- 13 分

从而
$$\left|\iint_{x^2+y^2\le 1}f(x,y)dxdy\right|\le\frac{\sqrt{M}}{2}\iint_{x^2+y^2\le 1}(x^2+y^2)dxdy=\frac{\pi\sqrt{M}}{4}。$$---------- 16 分
