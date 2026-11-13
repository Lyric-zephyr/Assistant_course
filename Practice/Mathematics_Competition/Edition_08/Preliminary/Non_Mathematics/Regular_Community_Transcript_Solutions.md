<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC08%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6%E7%B1%BB-%E5%88%9D%E8%B5%9B-2016-%E5%8F%82%E8%80%83%E8%A7%A3%E7%AD%94.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第八届（2016）非数学类初赛 · 官方参考解答

> 来源：考研竞赛数学公众号版（原文件：第08届非数学类-初赛(试题及参考解答).pdf）｜本文件仅含解答，题面见同目录《第08届非数学类-初赛-2016.md》
> 转录说明：视觉逐页转写（关键公式均以 dpi=200 放大逐字符核对），公式 KaTeX 语法。原文件解答以"解"（填空题）、"证明"（解答题）引出，本文件统一记为"**参考解答**"，并完整保留原有推导步骤与说明文字；原解答中的笔误按原样转抄并以 ⚠️ 加注。
> 原文件卷首信息：考试形式 **闭卷**，考试时间 **150 分钟**，满分 **100 分**；一（填空题）30 分共 5 小题、标注"每小题 6 分"（5×6=30，与满分自洽；对照题面转录文档，其扫描版标注"每小题 5 分"，两版标注不一致，本文件以参考解答版标注为准）；第二～六题各 14 分。

---

## 一(1)（6分）

**参考解答**：$\lim\limits_{n\to+\infty}\left(\dfrac{f\left(a+\frac{1}{n}\right)}{f(a)}\right)^n=\lim\limits_{n\to+\infty}\left(\dfrac{f(a)+f'(a)\frac{1}{n}+o\left(\frac{1}{n}\right)}{f(a)}\right)^n=e^{\frac{f'(a)}{f(a)}}$

---

## 一(2)（6分）

**参考解答**：

$$I=\lim_{x\to 0}\frac{f(\sin^2 x+\cos x)\tan 3x}{(e^{x^2}-1)\sin x}$$

$$=\lim_{x\to 0}\frac{f(\sin^2 x+\cos x)\times 3x}{x^2\times x}=3\lim_{x\to 0}\frac{f(\sin^2 x+\cos x)}{x^2}$$

$$=3\lim_{x\to 0}\left(\frac{f(\sin^2 x+\cos x)-f(1)}{\sin^2 x+\cos x-1}\cdot\frac{\sin^2 x+\cos x-1}{x^2}\right)$$

$$=3f'(1)\lim_{x\to 0}\frac{x^2-\frac{1}{2}x^2+o(x^2)}{x^2}$$

$$=\frac{3}{2}f'(1)$$

---

## 一(3)（6分）

**参考解答**：由题设得 $\dfrac{\partial z}{\partial x}=f'(e^x y^2)e^x y=f(e^x y^2)$（⚠️ 原文如此：中间因子印作 $e^x y$，按链式法则应为 $e^x y^2$，照抄原文并加注），令 $u=e^x y^2$，

得到当 $u>0$ 有 $f'(u)u=f(u)$，即 $\dfrac{f'(u)}{f(u)}=\dfrac{1}{u}$，从而 $(\ln f(u))'=(\ln u)'$

所以有 $\ln f(u)=\ln u+C_1$，$f(u)=Cu$．再而由初始条件得 $f(u)=2u$

故当 $x>0$ 有 $f(x)=2x$

---

## 一(4)（6分）

**参考解答**：由 Taylor 展开式得

$$f(x)=\left[1+x+\frac{1}{2!}x^2+\frac{1}{3!}x^3+o(x^3)\right]\left[2x-\frac{1}{3!}(2x)^3+o(x^4)\right]$$

所以 $f(x)$ 展开式的 4 次项 $\dfrac{-1}{3!}(2x)^3\times x+\dfrac{1}{3!}x^3\times(2x)=-x^4$，从而 $\dfrac{f^{(4)}(x)}{4!}=1$，

故 $f^{(4)}(0)=24$

（⚠️ 原解答笔误，照抄原文：由"4 次项 $=-x^4$"知 $x^4$ 的系数应为 $\frac{f^{(4)}(0)}{4!}=-1$、即 $f^{(4)}(0)=-24$；原文写作 $\frac{f^{(4)}(x)}{4!}=1$、$f^{(4)}(0)=24$。）

---

## 一(5)（6分）

**参考解答**：该曲面在点 $(x_0,y_0,z_0)$ 的切平面的法向量为 $(x_0,2y_0,-1)$。又该切平面于已知平面平行（⚠️ 原文用字"于"，按文意应为"与"），从而两平面法向量平行，故 $\dfrac{x_0}{2}=\dfrac{2y_0}{2}=\dfrac{-1}{-1}$

从而 $x_0=2$，$y_0=1$，得 $z_0=\dfrac{x_0^2}{2}+y_0^2=3$，从而所求切平面为

$$2(x-2)+2(y-1)-(z-3)=0$$

即

$$2x+2y-z=3$$

---

## 第二题（14分）

**参考解答**：设 $F(x)=\left(\int_0^x f(t)\,\mathrm{d}t\right)^2-\int_0^x f^3(t)\,\mathrm{d}t$，则 $F(0)=0$ 且要证明 $F'(x)>0$

设 $g(x)=2\int_0^x f(t)\,\mathrm{d}t-f^2(x)$，则 $F'(x)=f(x)g(x)$

由于 $f(0)=0$，$f'(x)>0$，故 $f(x)>0$，

从而只要证明 $g(x)>0$，$x>0$

而 $g(0)=0$，我们只要证明 $g'(x)>0$，$0<x<a$

而 $g'(x)=2f(x)\left[1-f'(x)\right]>0$，得证

---

## 第三题（14分）

**参考解答**：由于 $\Omega:\left(x-\dfrac{1}{2}\right)^2+\left(y-\dfrac{1}{2}\right)^2+2\left(z-\dfrac{1}{2}\right)^2\leqslant 1$，是一个椭球

其体积为 $V=\dfrac{4\pi}{3}\pi$（⚠️ 原文如此，照抄；按半轴 $1,1,\frac{1}{\sqrt2}$ 计算，椭球体积应为 $\frac{4\pi}{3}\cdot\frac{1}{\sqrt2}=\frac{2\sqrt2}{3}\pi$。后文 $A$ 的数值实际与单位球体积 $V=\frac{4\pi}{3}$ 一致），作变换 $u=x-\dfrac{1}{2}$，$v=y-\dfrac{1}{2}$，$w=\sqrt{2}\left(z-\dfrac{1}{2}\right)$

将 $\Omega$ 变为单位球 $\Sigma:u^2+v^2+w^2\leqslant 1$，而

$$J=\frac{\partial(u,v,w)}{\partial(x,y,z)}=\begin{vmatrix}1&0&0\\0&1&0\\0&0&\sqrt{2}\end{vmatrix}=\sqrt{2}$$

故 $\mathrm{d}u\,\mathrm{d}v\,\mathrm{d}w=\sqrt{2}\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$ 且

$$M=\frac{1}{\sqrt{2}}\iiint_{\Sigma}\left[\left(u+\frac{1}{2}\right)^2+\left(v+\frac{1}{2}\right)^2+\left(\frac{w}{\sqrt{2}}+\frac{1}{2}\right)^2\right]\mathrm{d}u\,\mathrm{d}v\,\mathrm{d}w$$

因一次项积分都是 0，故

$$M=\frac{1}{\sqrt{2}}\iiint_{\Sigma}\left(u^2+v^2+\frac{w^2}{2}\right)\mathrm{d}u\,\mathrm{d}v\,\mathrm{d}w+A$$

其中 $A=\dfrac{1}{\sqrt{2}}\left(\dfrac{1}{4}+\dfrac{1}{4}+\dfrac{1}{4}\right)V=\dfrac{\pi}{\sqrt{2}}$

记

$$I=\iiint_{\Sigma}\left(u^2+v^2+w^2\right)\mathrm{d}u\,\mathrm{d}v\,\mathrm{d}w=\int_0^{2\pi}\mathrm{d}\varphi\int_0^{\pi}\mathrm{d}\theta\int_0^1 r^2\cdot r^2\sin\theta\,\mathrm{d}r=\frac{4\pi}{5}$$

由于 $u^2,v^2,w^2$ 在 $\Sigma$ 上积分都是 $\dfrac{I}{3}$，故

$$M=\frac{1}{\sqrt{2}}\left(\frac{1}{3}+\frac{1}{3}+\frac{1}{6}\right)I+A=\frac{5\sqrt{2}}{6}\pi$$

---

## 第四题（14分）

**参考解答**：$n$ 等分区间 $[0,1]$，分点为 $0=x_0<x_1<\cdots<x_{n-1}<x_n=1$．

记 $h=\dfrac{1-0}{n}=\dfrac{1}{n}$，则 $x_k=0+kh=kh$，$x_k-x_{k-1}=h$，$k=1,2,\cdots,n$．

$$\lim_{n\to\infty}n\left(\int_0^1 f(x)\,\mathrm{d}x-\frac{1}{n}\sum_{k=1}^{n}f\left(\frac{k}{n}\right)\right)$$

$$=\lim_{n\to\infty}n\left(\sum_{k=1}^{n}\int_{x_{k-1}}^{x_k}f(x)\,\mathrm{d}x-\sum_{k=1}^{n}hf(x_k)\right)$$

$$=\lim_{n\to\infty}n\sum_{k=1}^{n}\int_{x_{k-1}}^{x_k}\left(f(x)-f(x_k)\right)\mathrm{d}x$$

$$=\lim_{n\to\infty}n\sum_{k=1}^{n}\int_{x_{k-1}}^{x_k}\frac{f(x)-f(x_k)}{x-x_k}\cdot(x-x_k)\,\mathrm{d}x$$

$$=\lim_{n\to\infty}n\sum_{k=1}^{n}\frac{f(\xi_k)-f(x_k)}{\xi_k-x_k}\cdot\int_{x_{k-1}}^{x_k}(x-x_k)\,\mathrm{d}x\qquad \xi_k\in(x_{k-1},x_k)$$

$$=\lim_{n\to\infty}n\sum_{k=1}^{n}f'(\eta_k)\left(-\frac{1}{2}(x_k-x_{k-1})^2\right)\qquad \eta_k\in(\xi_k,x_k)$$

$$=-\frac{1}{2}\lim_{n\to\infty}(1-0)\sum_{k=1}^{n}f'(\eta_k)h$$

$$=-\frac{1}{2}\int_0^1 f'(x)\,\mathrm{d}x$$

$$=\frac{1}{2}(f(1)-f(0))=-\frac{1}{2}$$

（⚠️ 原解答末行漏写负号，照抄原文；由上一行 $-\frac{1}{2}\int_0^1 f'(x)\,\mathrm{d}x$ 应得 $=-\frac{1}{2}(f(1)-f(0))=-\frac{1}{2}$。）

---

## 第五题（14分）

**参考解答**：设 $F(x)=\dfrac{1}{I}\int_0^x f(t)\,\mathrm{d}t$ 则 $F(0)=0$，$F(1)=1$．

由介值定理，存在 $\xi\in(0,1)$ 使得 $F(\xi)=\dfrac{1}{2}$

在两个子区间 $(0,\xi)$，$(\xi,1)$ 分别应用拉格朗日中值定理：

$$F'(x_1)=\frac{f(x_1)}{I}=\frac{F(\xi)-F(0)}{\xi-0}=\frac{1/2}{\xi}\ ,\qquad x_1\in(0,\xi)$$

$$F'(x_2)=\frac{f(x_2)}{I}=\frac{F(1)-F(\xi)}{1-\xi}=\frac{1/2}{1-\xi}\ ,\qquad x_2\in(0,\xi)$$

（⚠️ 原文此处写作 $x_2\in(0,\xi)$，按所在子区间应为 $x_2\in(\xi,1)$，照抄原文并加注。）

$$\frac{I}{f(x_1)}+\frac{I}{f(x_2)}=\frac{1}{F'(x_1)}+\frac{1}{F'(x_2)}=\frac{\xi}{1/2}+\frac{1-\xi}{1/2}=2$$

---

## 第六题（14分）

**参考解答**：由 $f(x)=f(x+2)$ 知 $f(x)$ 为以 2 为周期的周期函数，

其 Fourier 系数分别为：

$$a_n=\int_{-1}^{1}f(x)\cos n\pi x\,\mathrm{d}x\qquad b_n=\int_{-1}^{1}f(x)\sin n\pi x\,\mathrm{d}x$$

由 $f(x)=f(x+\sqrt{3})$ 知

$$a_n=\int_{-1}^{1}f(x+\sqrt{3})\cos n\pi x\,\mathrm{d}x$$

$$=\int_{-1+\sqrt{3}}^{1+\sqrt{3}}f(t)\cos n\pi(t-\sqrt{3})\,\mathrm{d}t$$

$$=\int_{-1+\sqrt{3}}^{1+\sqrt{3}}f(t)\left(\cos n\pi t\cos\sqrt{3}n\pi+\sin n\pi t\sin\sqrt{3}n\pi\right)\mathrm{d}t$$

$$=\cos\sqrt{3}n\pi\int_{-1+\sqrt{3}}^{1+\sqrt{3}}f(t)\cos n\pi t\,\mathrm{d}t+\sin\sqrt{3}n\pi\int_{-1+\sqrt{3}}^{1+\sqrt{3}}f(t)\sin n\pi t\,\mathrm{d}t$$

$$=\cos\sqrt{3}n\pi\int_{-1}^{1}f(t)\cos n\pi t\,\mathrm{d}t+\sin\sqrt{3}n\pi\int_{-1}^{1}f(t)\sin n\pi t\,\mathrm{d}t$$

所以 $a_n=a_n\cos\sqrt{3}n\pi+b_n\sin\sqrt{3}n\pi$

同理可得 $b_n=b_n\cos\sqrt{3}n\pi+a_n\sin\sqrt{3}n\pi$

（⚠️ 原文如此，照抄：由 $\sin n\pi(t-\sqrt{3})=\sin n\pi t\cos\sqrt{3}n\pi-\cos n\pi t\sin\sqrt{3}n\pi$，此处第二项应为 $-a_n\sin\sqrt{3}n\pi$；该符号不影响下文联立消元得 $a_n=b_n=0$ 的结论。）

联立

$$\begin{cases}a_n=a_n\cos\sqrt{3}n\pi+b_n\sin\sqrt{3}n\pi\\[4pt]b_n=b_n\cos\sqrt{3}n\pi+a_n\sin\sqrt{3}n\pi\end{cases}$$

得 $a_n=b_n=0$（$n=1,2,\cdots$）

而 $f(x)$ 可导，其 Fourier 级数处处收敛于 $f(x)$，所以

$$f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos nx+b_n\sin nx\right)=\frac{a_0}{2}$$

（⚠️ 原文级数项写作 $\cos nx$、$\sin nx$，照抄；因系数按 $\cos n\pi x$、$\sin n\pi x$ 定义，此处应为 $\cos n\pi x$、$\sin n\pi x$，属原解答笔误。）

其中 $a_0=\int_{-1}^{1}f(x)\,\mathrm{d}x$ 为常数
