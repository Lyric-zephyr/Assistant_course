<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC05%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6%E7%B1%BB-%E5%88%9D%E8%B5%9B-2013-%E5%8F%82%E8%80%83%E8%A7%A3%E7%AD%94.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第五届（2013）非数学类初赛 · 官方参考解答

> **来源**：原文件《第05届非数学类-初赛(试题及参考解答).pdf》（共 4 页），页眉/页脚为微信公众号「考研竞赛数学（ID: xwmath）」推广文字｜本文件仅含解答，题面见同目录《第05届非数学类-初赛-2013.md》
> **转录说明**：视觉逐页转写（dpi=200 逐字符核对），公式采用 KaTeX 语法；「【参考解答】」「【参考证明】」为原文件表述；原文件题面与解答交错排版，本文件省略题面；卷面页眉、页脚推广信息已省略；原解答中的笔误一律「照抄＋加注（原文如此……）」。

---

## 一(1)（6分）

**【参考解答】** 因为
$$\sin\left(\pi\sqrt{1+4n^2}\right)=\sin\left(\pi\sqrt{1+4n^2}-2n\pi\right)=\sin\frac{\pi}{\sqrt{1+4n^2}+2n}.$$

原式
$$=\lim_{n\to\infty}\left(1+\sin\frac{\pi}{\sqrt{1+4n^2}+2n}\right)^n$$
$$=\exp\left[\lim_{n\to\infty}n\ln\left(1+\sin\frac{\pi}{\sqrt{1+4n^2}+2n}\right)\right]=\exp\left[\lim_{n\to\infty}n\sin\frac{\pi}{\sqrt{1+4n^2}+2n}\right]$$
$$=\exp\left[\lim_{n\to\infty}\frac{n\pi}{\sqrt{1+4n^2}+2n}\right]=e^{\frac{\pi}{4}}.$$

---

## 一(2)（6分）

**【参考证明】** $a_n=\displaystyle\int_{n\pi}^{(n+1)\pi}\frac{|\sin x|}{x}\,\mathrm{d}x$。只要证明 $\displaystyle\sum_{n=0}^{\infty}a_n$ 发散。

因为 $a_n\geq\dfrac{1}{(n+1)\pi}\displaystyle\int_{n\pi}^{(n+1)\pi}|\sin x|\,\mathrm{d}x=\dfrac{1}{(n+1)\pi}\int_0^{\pi}\sin x\,\mathrm{d}x=\dfrac{2}{(n+1)\pi}$。

$\displaystyle\sum_{n=0}^{\infty}\frac{2}{(n+1)\pi}$ 发散。由正项级数的比较判别法可知，$\displaystyle\sum_{n=0}^{\infty}a_n$ 发散，即 $\displaystyle\int_0^{+\infty}\frac{\sin x}{x}\,\mathrm{d}x$ 不绝对收敛。

---

## 一(3)（6分）

**【参考解答】** 方程两边对 $x$ 求导，得 $3x^2+6xy+3x^2y'-6y^2y'=0\Rightarrow y'=\dfrac{x(x+2y)}{2y^2-x^2}$。

令 $y'(x)=0\Rightarrow x=0,\ x=-2y$。将 $x=0,\ x=-2y$ 代入所给方程，得
$$x=0,\ y=-1;\quad x=-2,\ y=1.$$

又有
$$y''=\frac{(2y^2-x^2)(2x+2xy'+2y)+(x^2+2xy)(4yy'-2x)}{(2y^2-x^2)^2},$$
（原文如此，按商的求导法则两项之间应为「$-$」，原解答印为「$+$」，疑为笔误；因下面代入的两点处 $y'=0$，不影响取值结果）从而有
$$y''\Big|_{\substack{x=0\\ y=-1\\ y'=0}}=-1<0,\quad y''\Big|_{\substack{x=-2\\ y=1\\ y'=0}}=1>0.$$

所以，$y(0)=-1$ 为极大值，$y(-2)=1$ 为极小值。

---

## 一(4)（6分）

**【参考解答】** 设切点 $A$ 的坐标为 $\left(t,\sqrt[3]{t}\right)$，曲线过 $A$ 点的切线为
$$y-\sqrt[3]{t}=\frac{1}{3\sqrt[3]{t^2}}(x-t).$$

令 $y=0$，可得切线与 $x$ 轴交点的横坐标为 $x_0=-2t$。因此平面图形的面积

$S=\triangle Ax_0t$ 的面积－曲边梯形 $OtA$ 的面积
$$S=\frac{1}{2}\sqrt[3]{t}\cdot 3t-\int_0^t\sqrt[3]{x}\,\mathrm{d}x=\frac{3}{4}t\sqrt[3]{t}=\frac{3}{4}\Rightarrow t=1.$$

所以 $A$ 的坐标为 $(1,1)$。

---

## 第二题（12分）

**【参考解答】**
$$I=\int_{-\pi}^{0}\frac{x\sin x\cdot\arctan e^{x}}{1+\cos^2 x}\,\mathrm{d}x+\int_{0}^{\pi}\frac{x\sin x\cdot\arctan e^{x}}{1+\cos^2 x}\,\mathrm{d}x$$
$$=\int_{0}^{\pi}\frac{x\sin x\cdot\arctan e^{-x}}{1+\cos^2 x}\,\mathrm{d}x+\int_{0}^{\pi}\frac{x\sin x\cdot\arctan e^{x}}{1+\cos^2 x}\,\mathrm{d}x$$
$$=\int_{0}^{\pi}\left(\arctan e^{-x}+\arctan e^{x}\right)\frac{x\sin x}{1+\cos^2 x}\,\mathrm{d}x$$
$$=\frac{\pi}{2}\int_{0}^{\pi}\frac{x\sin x}{1+\cos^2 x}\,\mathrm{d}x=\left(\frac{\pi}{2}\right)^2\int_{0}^{\pi}\frac{\sin x}{1+\cos^2 x}\,\mathrm{d}x=-\left(\frac{\pi}{2}\right)^2\arctan(\cos x)\Big|_{0}^{\pi}=\frac{\pi^3}{8}.$$

（其中 $\arctan e^{-x}+\arctan e^{x}=\dfrac{\pi}{2}$，另外
$$\int_{0}^{\pi}\frac{x\sin x}{1+\cos^2 x}\,\mathrm{d}x=\int_{0}^{\pi}\frac{(\pi-u)\sin u}{1+\cos^2 u}\,\mathrm{d}u=-\int_{0}^{\pi}\frac{x\sin x}{1+\cos^2 x}\,\mathrm{d}x+\pi\int_{0}^{\pi}\frac{\sin x}{1+\cos^2 x}\,\mathrm{d}x.$$
这样可以得到第二个 $\dfrac{\pi}{2}$）

---

## 第三题（12分）

**【参考证明】** 由于 $f(x)$ 在 $x=0$ 处连续且 $\lim\limits_{x\to 0}\dfrac{f(x)}{x}=0$，则
$$f(0)=\lim_{x\to 0}f(x)=\lim_{x\to 0}\frac{f(x)}{x}\cdot x=0,\quad f'(0)=\lim_{x\to 0}\frac{f(x)-f(0)}{x-0}=0.$$

应用洛必达法则，则有
$$\lim_{x\to 0}\frac{f(x)}{x^2}=\lim_{x\to 0}\frac{f'(x)}{2x}=\lim_{x\to 0}\frac{f'(x)-f'(0)}{2(x-0)}=\frac{1}{2}f''(0).$$

所以
$$\lim_{x\to 0}\frac{\left|f\left(\frac{1}{n}\right)\right|}{\frac{1}{n^2}}=\frac{1}{2}f''(0).$$
（原文如此，此处下标「$x\to 0$」按上下文应为「$n\to\infty$」，疑为笔误，照录原文）由于 $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2}$ 收敛，所以 $\displaystyle\sum_{n=1}^{\infty}\left|f\left(\frac{1}{n}\right)\right|$ 收敛。

---

## 第四题（10分）

**【参考证明】** 因为 $f'(x)\geq m>0\ (a\leq x\leq b)$，所以 $f(x)$ 在 $[a,b]$ 上严格单调增加，从而有反函数。设 $A=f(a)$，$B=f(b)$，$\varphi$ 是 $f$ 的反函数，则
$$0<\varphi'(y)=\frac{1}{f'(x)}\leq\frac{1}{m},$$
又 $|f(x)|\leq\pi$，则 $-\pi\leq A<B\leq\pi$，所以
$$\left|\int_a^b\sin f(x)\,\mathrm{d}x\right|\ \underline{\,x=\varphi(y)\,}\ \left|\int_A^B\varphi'(y)\sin y\,\mathrm{d}y\right|\leq\int_0^{\pi}\frac{\sin y}{m}\,\mathrm{d}y=\frac{2}{m}.$$
（原文如此，原解答在前后两个积分之间以带下划线的「$x=\varphi(y)$」标注代换，本文件照录）

---

## 第五题（14分）

**【参考解答】** 设 $\Sigma$ 围成的立体的体积为 $V$，则由高斯公式，有
$$I=\iiint_V\left(3x^2+6y^2+9z^2-3\right)\mathrm{d}V=3\iiint_V\left(x^2+2y^2+3z^2-1\right)\mathrm{d}V$$

为了使得 $I$ 达到最小，就是要求 $V$ 使得 $x^2+2y^2+3z^2-1\leq 0$ 的最大空间区域，即
$$V=\left\{(x,y,z)\,\middle|\,x^2+2y^2+3z^2\leq 1\right\}$$
所以 $V$ 是一个椭球，$\Sigma$ 是椭球 $V$ 的表面时，积分 $I$ 最小。

为了求该最小值，做变换 $x=u$，$y=v/\sqrt{2}$，$z=w/\sqrt{3}$，$\dfrac{\partial(x,y,z)}{\partial(u,v,w)}=\dfrac{1}{\sqrt{6}}$，
$$I=\frac{3}{\sqrt{6}}\iiint_{u^2+v^2+w^2\leq 1}\left(u^2+v^2+w^2-1\right)\mathrm{d}V$$
$$=\frac{3}{\sqrt{6}}\int_0^{2\pi}\mathrm{d}\varphi\int_0^{\pi}\mathrm{d}\theta\int_0^1\left(r^2-1\right)r^2\sin\theta\,\mathrm{d}r=-\frac{4\sqrt{6}}{15}\pi.$$

---

## 第六题（14分）

**【参考解答】** 作变换 $x=\dfrac{u-v}{\sqrt{2}}$，$y=\dfrac{u+v}{\sqrt{2}}$。曲线 $C$ 变为 $uOv$ 平面上的
$$\Gamma:\frac{3}{2}u^2+\frac{1}{2}v^2=r^2,$$
也是取正向且有 $x^2+y^2=u^2+v^2$，$y\,\mathrm{d}x-x\,\mathrm{d}y=v\,\mathrm{d}u-u\,\mathrm{d}v$，
$$I_a(r)=\int_{\Gamma}\frac{v\,\mathrm{d}u-u\,\mathrm{d}v}{(u^2+v^2)^a}.$$

作变换 $u=\sqrt{\dfrac{2}{3}}\,r\cos\theta$，$v=\sqrt{2}\,r\sin\theta$，则有 $v\,\mathrm{d}u-u\,\mathrm{d}v=-\dfrac{2}{\sqrt{3}}r^2\,\mathrm{d}\theta$
$$I_a(r)=-\frac{2r^{2(1-a)}}{\sqrt{3}}\int_0^{2\pi}\frac{\mathrm{d}\theta}{\left(2\cos^2\theta/3+2\sin^2\theta\right)^a}=-\frac{2r^2}{\sqrt{3}}J_a$$
（原文如此，第二个等号后指数印为「$2$」，按上一步及下文对 $a$ 的讨论，应为「$2(1-a)$」，疑漏印，照录原文）
其中 $J_a=\displaystyle\int_0^{2\pi}\frac{\mathrm{d}\theta}{\left(2\cos^2\theta/3+2\sin^2\theta\right)^a}$，$0<J_a<+\infty$。

因此当 $a>1$ 和 $a<1$，所求极限分别为 $0$ 和 $-\infty$。当 $a=1$，
$$J_1=\int_0^{2\pi}\frac{\mathrm{d}\theta}{2\cos^2\theta/3+2\sin^2\theta}=\sqrt{3}\pi.$$

所求极限为
$$\lim_{r\to+\infty}I_a(r)=\begin{cases}0, & a>1,\\ -\infty, & a<1,\\ -2\pi, & a=1.\end{cases}$$

---

## 第七题（14分）

**【参考解答】** **(1)** 记 $a_n=1+\dfrac{1}{2}+\cdots+\dfrac{1}{n}$，$u_n=\dfrac{a_n}{(n+1)(n+2)}$，$n=1,2,\cdots$。

因为 $n$ 充分大时
$$0<a_n=1+\frac{1}{2}+\cdots+\frac{1}{n}<1+\int_1^n\frac{1}{x}\,\mathrm{d}x=1+\ln n<\sqrt{n}$$
所以 $u_n\leq\dfrac{\sqrt{n}}{(n+1)(n+2)}<\dfrac{1}{n^{3/2}}$，而 $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^{3/2}}$ 收敛，所以 $\displaystyle\sum_{n=1}^{\infty}u_n$ 收敛。

**(2)** $a_k=1+\dfrac{1}{2}+\cdots+\dfrac{1}{k}\ (k=1,2,\cdots)$，则
$$S_n=\sum_{k=1}^{n}\frac{1+\frac{1}{2}+\cdots+\frac{1}{k}}{(k+1)(k+2)}=\sum_{k=1}^{n}\frac{a_k}{(k+1)(k+2)}$$
$$=\sum_{k=1}^{n}\left(\frac{a_k}{k+1}-\frac{a_k}{k+2}\right)=\left(\frac{a_1}{2}-\frac{a_1}{3}\right)+\left(\frac{a_2}{3}-\frac{a_2}{4}\right)+\cdots+\left(\frac{a_{n-1}}{n}-\frac{a_{n-1}}{n+1}\right)+\left(\frac{a_n}{n+1}-\frac{a_n}{n+2}\right)$$
$$=\frac{1}{2}a_1+\frac{1}{3}(a_2-a_1)+\frac{1}{4}(a_3-a_2)+\cdots+\frac{1}{n+1}(a_n-a_{n-1})-\frac{1}{n+1}a_n$$
（原文如此，末项分母印为「$n+1$」，按上式并对照前一行应为「$n+2$」，疑为笔误）
$$=\left(\frac{1}{1\cdot 2}+\frac{1}{2\cdot 3}+\cdots+\frac{1}{n\cdot(n-1)}\right)-\frac{1}{n+2}a_n=1-\frac{1}{n}-\frac{1}{n+2}a_n.$$
（原文如此，括号内末项印为 $\dfrac{1}{n\cdot(n-1)}$、和为 $1-\dfrac{1}{n}$；按上式推导应分别为 $\dfrac{1}{n\cdot(n+1)}$ 与 $1-\dfrac{1}{n+1}$，疑为笔误，不影响最终极限值）

因为 $0<a_n<1+\ln n$，所以 $0<\dfrac{a_n}{n+2}<\dfrac{1+\ln n}{n+2}$ 且 $\lim\limits_{n\to\infty}\dfrac{1+\ln n}{n+2}=0$，所以
$$\lim_{n\to\infty}\frac{a_n}{n+2}=0.$$
于是 $S=\lim\limits_{n\to\infty}S_n=1-0-0=1$。
