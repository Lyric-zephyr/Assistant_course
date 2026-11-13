# 复数与几何表示

来源：高瑜《复变函数与积分变换》2024 秋讲义，原文件第 2–5 页。

本篇为阅读手写内容后的整理稿，采用标准 LaTeX 补全公式和必要条件，合并重复说明、略写部分证明；不是逐字转录。


## 复数运算

设 $z=x+iy$，其中 $x,y\in\mathbb R$，$i^2=-1$。$\operatorname{Re}z=x$，$\operatorname{Im}z=y$。

$$
\begin{aligned}
z_1z_2&=x_1x_2-y_1y_2+i(x_1y_2+x_2y_1),\\
\frac{z_1}{z_2}&=\frac{x_1x_2+y_1y_2+i(y_1x_2-x_1y_2)}{x_2^2+y_2^2}\quad(z_2\ne0).
\end{aligned}
$$

共轭复数 $\bar z=x-iy$，$|z|=\sqrt{x^2+y^2}$。共轭保持加法、乘法和非零分母下的除法。

$$
z\bar z=|z|^2,\quad
\operatorname{Re}z=\frac{z+\bar z}{2},\quad
\operatorname{Im}z=\frac{z-\bar z}{2i},\quad
|zw|=|z||w|,\quad
\bigl||z|-|w|\bigr|\le |z+w|\le |z|+|w|.
$$

**例：** $\dfrac{\sqrt3-i}{\sqrt3+2i}=\dfrac17-\dfrac{3\sqrt3}{7}i$；$z^2+2z+2=0$ 的根为 $-1\pm i$。

当 $|z|=1$、$k\in\mathbb R$ 且 $z\ne k$，有 $\left|\dfrac{kz-1}{z-k}\right|=1$。当 $|z|=1$ 且 $z\ne-1$ 时，$\dfrac{z-1}{z+1}$ 的实部为零；$z=1$ 时商为零。

## 辐角、极形式与乘除

复数 $z$ 对应平面点 $(x,y)$。对 $z\ne0$，取主辐角 $\arg z\in(-\pi,\pi]$，全体辐角为 $\operatorname{Arg}z=\arg z+2k\pi$。**零没有辐角。**

$$
e^{i\theta}=\cos\theta+i\sin\theta,\qquad
z=r(\cos\theta+i\sin\theta)=re^{i\theta}.
$$

乘法模相乘、辐角相加；除法模相除、辐角相减。主辐角的结果需要按 $2\pi$ 调整到约定区间。

例如 $\arg(\sqrt3+i)=\pi/6$，$\arg(-3)=\pi$，$\arg(1-2i)=-\arctan2$，$\arg(-1-2i)=\arctan2-\pi$。

## 乘方与开方

$$
(re^{i\theta})^n=r^ne^{in\theta},\qquad
w_k=r^{1/n}\exp\!\left(i\frac{\theta+2k\pi}{n}\right),\quad k=0,\ldots,n-1.
$$

后式给出非零复数的 $n$ 个不同 $n$ 次方根，均匀分布在半径 $r^{1/n}$ 的圆周上。

**例：** $(1+i)^{10}=32i$；$1+\sqrt3i=2e^{i\pi/3}$ 的三次方根是 $2^{1/3}e^{i(\pi/9+2k\pi/3)}$，$k=0,1,2$。

## 扩充复平面

通过球极投影把复平面加上一个无穷远点，得到 $\widehat{\mathbb C}=\mathbb C\cup\{\infty\}$。趋于无穷远表示 $|z|\to\infty$，不区分方向；附近问题常用 $w=1/z$ 转为零点附近问题。
