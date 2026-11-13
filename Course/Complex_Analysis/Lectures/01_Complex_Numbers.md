# 模块一：复数与复变函数

来源：高瑜《复变函数与积分变换》2024 秋讲义，原 PDF 第 2–8 页。

本模块合并既有校订稿，公式采用标准 LaTeX，保留内容中的必要条件与歧义说明；不是逐字转录。

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

复数 $z$ 对应平面点 $(x,y)$。对 $z\ne0$，取主辐角 $\arg z\in(-\pi,\pi]$，全体辐角为 $\operatorname{Arg}z=\arg z+2k\pi$。**零没有辐角。**

$$
e^{i\theta}=\cos\theta+i\sin\theta,\qquad
z=r(\cos\theta+i\sin\theta)=re^{i\theta}.
$$

乘法模相乘、辐角相加；除法模相除、辐角相减。主辐角的结果需要按 $2\pi$ 调整到约定区间。

例如 $\arg(\sqrt3+i)=\pi/6$，$\arg(-3)=\pi$，$\arg(1-2i)=-\arctan2$，$\arg(-1-2i)=\arctan2-\pi$。

$$
(re^{i\theta})^n=r^ne^{in\theta},\qquad
w_k=r^{1/n}\exp\!\left(i\frac{\theta+2k\pi}{n}\right),\quad k=0,\ldots,n-1.
$$

后式给出非零复数的 $n$ 个不同 $n$ 次方根，均匀分布在半径 $r^{1/n}$ 的圆周上。

**例：** $(1+i)^{10}=32i$；$1+\sqrt3i=2e^{i\pi/3}$ 的三次方根是 $2^{1/3}e^{i(\pi/9+2k\pi/3)}$，$k=0,1,2$。

通过球极投影把复平面加上一个无穷远点，得到 $\widehat{\mathbb C}=\mathbb C\cup\{\infty\}$。趋于无穷远表示 $|z|\to\infty$，不区分方向；附近问题常用 $w=1/z$ 转为零点附近问题。

$B(z_0,r)=\{z:|z-z_0|<r\}$；去心邻域为 $0<|z-z_0|<r$；无穷远的去心邻域可写成 $|z|>1/r$。

内点有一个邻域包含于集合；边界点的每个邻域同时接触集合及其补集；聚点的每个去心邻域都含集合中的点。开集的点全是内点，闭集包含其全部聚点。有界集包含在某个有限半径圆盘内。

**区域是连通开集。** 平面开集的连通性可用区域内的折线路径理解。圆环 $r<|z|<R$ 有孔，是多连通区域。单连通区域内每条 Jordan 闭曲线的内部均属于区域。

曲线可写为 $z(t)=x(t)+iy(t)$。简单闭曲线又称 Jordan 曲线；分段光滑曲线由有限段光滑曲线拼接。闭曲线的正向是内部位于行进方向左侧；复合边界外圈逆时针、内圈顺时针。

**例：** $\left|\dfrac{z-3}{z-2}\right|>2$ 化为 $(x-\tfrac53)^2+y^2<\tfrac49$，同时排除原分母为零的点 $z=2$。讲义该处圆盘表达有笔误，这里按原不等式重新配方更正；化简时不能丢失原定义域。

$w=f(z)=u(x,y)+iv(x,y)$ 可看作平面到平面的映射。$w=z^2$ 时 $u=x^2-y^2$、$v=2xy$。应区分单值函数与多值关系；对数、开方等需要明确分支。

$$
\lim_{z\to z_0}f(z)=a+ib
\iff
\lim_{(x,y)\to(x_0,y_0)}u(x,y)=a,\quad
\lim_{(x,y)\to(x_0,y_0)}v(x,y)=b.
$$

**复极限必须与趋近路径无关。** 例如 $\operatorname{Re}z/|z|$ 在 $z\to0$ 时沿正实轴为 $1$，沿虚轴为 $0$，因此不存在极限。

有限极限满足加减、乘积、非零分母下的商及适用条件下的复合运算。$f$ 在 $z_0$ 连续等价于极限为 $f(z_0)$。多项式处处连续，有理函数在分母不为零处连续。连续函数在紧集上有界，模达到最大值与最小值。

$$
f(z)\to\infty\iff\frac1{f(z)}\to0,
\qquad
\lim_{z\to\infty}f(z)=\lim_{w\to0}f(1/w).
$$
