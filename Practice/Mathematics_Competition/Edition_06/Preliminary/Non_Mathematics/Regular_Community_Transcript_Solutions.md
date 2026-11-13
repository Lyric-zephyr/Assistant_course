<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC06%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6%E7%B1%BB-%E5%88%9D%E8%B5%9B-2014-%E5%8F%82%E8%80%83%E8%A7%A3%E7%AD%94.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第六届（2014）非数学类初赛 · 官方参考解答

> **来源**：原文件《第06届非数学类-初赛(试题及参考解答).pdf》，卷面标题为「2014 年全国大学生数学竞赛预赛试题参考答案」，水印/页脚为微信公众号「竞赛资料网」｜本文件仅含解答，题面见同目录《第06届非数学类-初赛-2014.md》
> **转录说明**：视觉逐页转写（dpi=200 逐字符核对），公式采用 KaTeX 语法；「[参考解答]」「[参考解答与评分标准]」「[解]」「答案：」及右侧「……（N 分）」评分标注均为原文件表述；卷面水印与页脚推广信息已省略。

---

## 一(1)（6分）

**答案**：$y''(x)-2y'(x)+y(x)=0$

**[参考解答]** 由题设知该方程的特征方程有二重根 $r=1$，故所求微分方程是 $y''(x)-2y'(x)+y(x)=0$。

---

## 一(2)（6分）

**答案**：$2x+2y+z+\dfrac{3}{2}=0$

**[参考解答]** 设 $P_0(x_0,y_0,z_0)$ 为 $S$ 上一点，则 $S$ 在 $P_0$ 的切平面方程是

$$-2x_0(x-x_0)-4y_0(y-y_0)+(z-z_0)=0.$$

由于该切平面与已知平面 $L$ 平行，则 $(-2x_0,-4y_0,1)$ 平行于 $(2,2,1)$，故存在常数 $k\neq 0$ 使得

$$(-2x_0,-4y_0,1)=k(2,2,1),$$

从而 $k=1$。故得 $x_0=-1$，$y_0=-\dfrac{1}{2}$，这样就有 $z_0=\dfrac{3}{2}$。所求切面方程是

$$2x+2y+z+\dfrac{3}{2}=0.$$

---

## 一(3)（6分）

**答案**：$y'=3$

**[参考解答]** 易知在 $y(0)=1$（原文如此，「在」疑为「有」之误）。对方程的两边关于 $x$ 求导，得

$$1=\sin^2\left(\frac{\pi}{4}(y-x)\right)(y'-1),$$

于是

$$y'=\csc^2\left(\frac{\pi}{4}(y-x)\right)+1,$$

把 $x=0$ 代入上式，得 $y'=3$。

---

## 一(4)（6分）

**答案**：$1$

**[参考解答]**

$$x_n=\sum_{k=1}^{n}\frac{k}{(k+1)!}=\sum_{k=1}^{n}\left(\frac{1}{k!}-\frac{1}{(k+1)!}\right)$$

$$=\left(1-\frac{1}{2!}\right)+\left(\frac{1}{2!}-\frac{1}{3!}\right)+\left(\frac{1}{3!}-\frac{1}{4!}\right)+\cdots+\left(\frac{1}{n!}-\frac{1}{(n+1)!}\right)=1-\frac{1}{(n+1)!}\to 1.$$

---

## 一(5)（6分）

**答案**：$2$

**[参考解答]** 由 $\lim\limits_{x\to 0}\left(1+x+\dfrac{f(x)}{x}\right)^{\frac{1}{x}}=e^3$ 知 $\lim\limits_{x\to 0}\dfrac{1}{x}\ln\left(1+x+\dfrac{f(x)}{x}\right)=3$，于是有

$$\frac{1}{x}\ln\left(1+x+\frac{f(x)}{x}\right)=3+\alpha,$$

其中 $\alpha\to 0\,(x\to 0)$，即有

$$\frac{f(x)}{x^2}=\frac{e^{3x+\alpha x}-1}{x}-1,$$

从而

$$\lim_{x\to 0}\frac{f(x)}{x^2}=\lim_{x\to 0}\frac{e^{3x+\alpha x}-1}{x}-1=\lim_{x\to 0}\frac{3x+\alpha x}{x}-1=2.$$

---

## 第二题（12分）

**[参考解答与评分标准]**

$$I=\int_{e^{-2n\pi}}^{1}\left|\frac{\mathrm{d}}{\mathrm{d}x}\cos\left(\ln\frac{1}{x}\right)\right|\mathrm{d}x=\int_{e^{-2n\pi}}^{1}\left|\frac{\mathrm{d}}{\mathrm{d}x}\cos(\ln x)\right|\mathrm{d}x=\int_{e^{-2n\pi}}^{1}|\sin\ln x|\,\frac{1}{x}\,\mathrm{d}x.$$

……（6 分）

令 $\ln x=u$，则有

$$I=\int_{-2n\pi}^{0}|\sin u|\,\mathrm{d}u=\int_{0}^{2n\pi}|\sin t|\,\mathrm{d}t=4n\int_{0}^{\pi/2}|\sin t|\,\mathrm{d}t=4n.$$

……（12 分）

---

## 第三题（14分）

**[参考解答与评分标准]** 由泰勒公式，有

$$f(0)=f(x)+f'(x)(0-x)+\frac{1}{2}f''(\xi)(0-x)^2,\quad \xi\in(0,x),$$

$$f(1)=f(x)+f'(x)(1-x)+\frac{1}{2}f''(\eta)(1-x)^2,\quad \eta\in(x,1),$$

……（5 分）

上述两式相减，得到 $f(0)-f(1)=-f'(x)-\dfrac{1}{2}f''(\eta)(1-x)^2+\dfrac{1}{2}f''(\xi)x^2$，于是

$$f'(x)=f(1)-f(0)-\frac{1}{2}f''(\eta)(1-x)^2+\frac{1}{2}f''(\xi)x^2.$$

……（8 分）

由条件 $|f(x)|\leq A$，$|f''(x)|\leq B$，得到

$$|f'(x)|\leq 2A+\frac{B}{2}\left((1-x)^2+x^2\right).$$

……（11 分）

因 $x^2+(1-x)^2=2x^2-2x+1$ 在 $[0,1]$ 的最大值为 $1$，故

$$|f'(x)|\leq 2A+\frac{B}{2}.$$

……（14 分）

---

## 第四题（14分）

**[参考解答与评分标准]**

**(1)** 设球缺所在的球体表面的方程为 $x^2+y^2+z^2=R^2$，球缺的中心线为 $z$ 轴，且设球缺所在圆锥顶角为 $2\alpha$。记球缺的区域为 $\Omega$，则其体积为

$$\iiint_{\Omega}\mathrm{d}v=\int_{R-h}^{R}\mathrm{d}z\iint_{D_z}\mathrm{d}x\mathrm{d}y=\int_{R-h}^{R}\pi(R^2-z^2)\,\mathrm{d}z=\frac{\pi}{3}(3R-h)h^2.$$

……（3 分）

由于球面的面积微元是 $\mathrm{d}S=R^2\sin\theta\,\mathrm{d}\theta$（原文如此，球面面积微元应为 $\mathrm{d}S=R^2\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi$），故球冠的面积为

$$\int_{0}^{2\pi}\mathrm{d}\varphi\int_{0}^{\alpha}R^2\sin\theta\,\mathrm{d}\theta=2\pi R^2(1-\cos\alpha)=2\pi Rh.$$

……（6 分）

**(2)** 记球缺 $\Omega$ 的底面圆为 $P_1$，方向指向球缺外，且记 $J=\displaystyle\iint_{P_1}x\,\mathrm{d}y\mathrm{d}z+y\,\mathrm{d}z\mathrm{d}x+z\,\mathrm{d}x\mathrm{d}y$。由 Gauss 公式，有

$$I+J=\iiint_{\Omega}3\,\mathrm{d}v=3v(\Omega),$$

……（9 分）

其中 $v(\Omega)$ 为 $\Omega$ 的体积。由于平面 $P$ 的正向单位法向量为 $\dfrac{-1}{\sqrt{3}}(1,1,1)$，故

$$J=\frac{-1}{\sqrt{3}}\iint_{P_1}(x+y+z)\,\mathrm{d}S=\frac{-6}{\sqrt{3}}\sigma(P_1)=-2\sqrt{3}\,\sigma(P_1),$$

其中 $\sigma(P_1)$ 是 $P_1$ 的面积。故 $I=3v(\Omega)-J=3v(\Omega)+2\sqrt{3}\,\sigma(P_1)$。

……（12 分）

因为球缺底面圆心为 $Q=(2,2,2)$，而球缺的顶点为 $D=(3,3,3)$，故球缺的高度 $h=|QD|=\sqrt{3}$。再由 (1) 所证并代入 $h=\sqrt{3}$ 和 $R=2\sqrt{3}$ 得

$$I=3\cdot\frac{\pi}{3}(3R-h)h^2+2\sqrt{3}\pi(2Rh-h^2)=33\sqrt{3}\pi.$$

……（14 分）

---

## 第五题（15分）

**证明**：先考虑特殊情形：$a=0,b=1$。下证 $\lim\limits_{n\to\infty}x_n=1$。

首先 $x_n\in[0,1]$，即 $x_n\leq 1$，只要证明 $\forall\varepsilon>0\ (\varepsilon<1)$，$\exists N$，$\forall n>N$ 时，$1-\varepsilon<x_n$。由 $f$ 在 $[0,1]$ 严格单增，就是要证明

$$f^n(1-\varepsilon)<f^n(x_n)=\int_{0}^{1}f^n(x)\,\mathrm{d}x.$$

……（3 分）

由于 $\forall c\in(0,1)$，有 $\displaystyle\int_{c}^{1}f^n(x)\,\mathrm{d}x>f^n(c)(1-c)$，现取 $c=1-\dfrac{\varepsilon}{2}$，则 $f(1-\varepsilon)<f(c)$，即 $\dfrac{f(1-\varepsilon)}{f(c)}<1$，于是 $\lim\limits_{n\to\infty}\left(\dfrac{f(1-\varepsilon)}{f(c)}\right)^n=0$，所以 $\exists N$，$\forall n>N$ 时有

$$\left(\frac{f(1-\varepsilon)}{f(c)}\right)^n<\frac{\varepsilon}{2}=1-c.$$

……（8 分）

即 $f^n(1-\varepsilon)<f^n(c)(1-c)\leq\displaystyle\int_{c}^{1}f^n(x)\,\mathrm{d}x\leq\int_{0}^{1}f^n(x)\,\mathrm{d}x=f^n(x_n)$，从而 $1-\varepsilon<x_n$。由 $\varepsilon$ 的任意性得

$$\lim_{n\to\infty}x_n=1.$$

……（10 分）

再考虑一般情形。令 $F(t)=f(a+t(b-a))$，由 $f$ 在 $[a,b]$ 上非负连续，严格单增知 $F$ 在 $[0,1]$ 上非负连续，严格单增。从而 $\exists t_n\in[0,1]$，使得 $F^n(t_n)=\displaystyle\int_{0}^{1}F^n(t)\,\mathrm{d}t$，且 $\lim\limits_{n\to\infty}t_n=1$，即

$$f^n(a+t_n(b-a))=\int_{0}^{1}f^n(a+t(b-a))\,\mathrm{d}t.$$

记 $x_n=a+t_n(b-a)$，则有

$$[f(x_n)]^{n}=\frac{1}{b-a}\int_{a}^{b}[f(x)]^{n}\,\mathrm{d}x,$$

且 $\lim\limits_{n\to\infty}x_n=a+(b-a)=b$。

……（15 分）

---

## 第六题（15分）

**[解]** 令 $f(x)=\dfrac{1}{1+x^2}$，因 $A_n=\dfrac{1}{n}\displaystyle\sum_{i=1}^{n}\frac{1}{1+i^2/n^2}$，故 $\lim\limits_{n\to\infty}A_n=\displaystyle\int_{0}^{1}f(x)\,\mathrm{d}x=\frac{\pi}{4}$。

……（5 分）

记 $x_i=\dfrac{i}{n}$，则 $A_n=\displaystyle\sum_{i=1}^{n}\int_{x_{i-1}}^{x_i}f(x_i)\,\mathrm{d}x$，故 $J_n=n\displaystyle\sum_{i=1}^{n}\int_{x_{i-1}}^{x_i}(f(x)-f(x_i))\,\mathrm{d}x$（原文未显式定义 $J_n$，按上下文 $J_n=n\left(\dfrac{\pi}{4}-A_n\right)$）。

……（8 分）

由拉格朗日中值定理，存在 $\zeta_i\in(x_{i-1},x_i)$ 使得 $J_n=n\displaystyle\sum_{i=1}^{n}\int_{x_{i-1}}^{x_i}f'(\zeta_i)(x-x_i)\,\mathrm{d}x$。

……（10 分）

记 $m_i$ 和 $M_i$ 分别是 $f'(x)$ 在 $[x_{i-1},x_i]$ 上的最小值和最大值，则 $m_i\leq f'(\zeta_i)\leq M_i$，故积分 $\displaystyle\int_{x_{i-1}}^{x_i}f'(\zeta_i)(x-x_i)\,\mathrm{d}x$ 介于 $m_i\displaystyle\int_{x_{i-1}}^{x_i}(x-x_i)\,\mathrm{d}x$ 和 $M_i\displaystyle\int_{x_{i-1}}^{x_i}(x-x_i)\,\mathrm{d}x$ 之间，所以存在 $\eta_i\in(x_{i-1},x_i)$ 使得

$$\int_{x_{i-1}}^{x_i}f'(\zeta_i)(x-x_i)\,\mathrm{d}x=-f'(\eta_i)\frac{(x_i-x_{i-1})^2}{2},$$

……（12 分）

于是，有 $J_n=\dfrac{-n}{2}\displaystyle\sum_{i=1}^{n}f'(\eta_i)(x_i-x_{i-1})^2=\frac{-1}{2n}\displaystyle\sum_{i=1}^{n}f'(\eta_i)$。从而

$$\lim_{n\to\infty}n\left(\frac{\pi}{4}-A_n\right)=\lim_{n\to\infty}J_n=-\frac{1}{2}\int_{0}^{1}f'(x)\,\mathrm{d}x=-\frac{1}{2}[f(1)-f(0)]=\frac{1}{4}.$$

……（15 分）
