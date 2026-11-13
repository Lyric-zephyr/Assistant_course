# 模块五：留数相关及应用

来源：高瑜《复变函数与积分变换》2024 秋讲义，原 PDF 第 27–35 页。

本模块合并既有校订稿，公式采用标准 LaTeX，保留内容中的必要条件与歧义说明；不是逐字转录。

若 $f$ 在 $0<|z-a|<\delta$ 解析，则考察洛朗展开 $\sum c_n(z-a)^n$。

可去奇点：所有负幂系数为零，等价于有限极限存在，也等价于去心邻域内有界；补定义后解析。

$m$ 阶极点：$c_{-m}\ne0$ 且更低负幂系数为零，等价于 $f(z)=(z-a)^{-m}g(z)$、$g(a)\ne0$，也等价于 $|f(z)|\to\infty$（不含阶数判断）。

本性奇点：无穷多个负幂项非零，既无有限极限，也不趋于无穷。例：$\sin z/z$ 在 $0$ 可去；$1/(z-i)^3$ 在 $i$ 为三阶极点；$e^{1/z}$ 在 $0$ 为本性奇点。

**聚集着其他奇点的点不是孤立奇点。** $1/\sin(1/z)$ 的极点 $z=1/(k\pi)$ 趋于零，所以零不是它的孤立奇点。

解析函数 $f$ 在 $a$ 有 $m$ 阶零点，当且仅当

$$
f(z)=(z-a)^mg(z),\quad g(a)\ne0
\iff f(a)=\cdots=f^{(m-1)}(a)=0,\quad f^{(m)}(a)\ne0.
$$

非恒零解析函数的零点孤立。$f$ 的 $m$ 阶极点对应 $1/f$ 的 $m$ 阶零点。商函数的阶由分子、分母零点阶数之差决定，**必须先检查约去与抵消。**

例：$1/\sin z$ 在 $k\pi$ 为一阶极点；$(e^z-1)/z^3$ 在零为二阶极点。

令 $w=1/z$，以 $f(1/w)$ 在 $w=0$ 的奇点类型定义 $f$ 在无穷远点的类型，前提是 $f$ 在充分大的 $|z|$ 区域解析。

$1/z$ 在无穷远可去，$z/(1+z)$ 在无穷远可去且极限为 $1$；非零次数多项式在无穷远为相应阶极点；$1/\sin z$ 因有任意大的有限极点，无穷远不是孤立奇点。

$$
\boxed{\operatorname{Res}(f,a)=c_{-1}=\frac1{2\pi i}\oint_{|z-a|=r}f(z)\,dz}.
$$

若 $a$ 为一阶极点，$\operatorname{Res}(f,a)=\lim_{z\to a}(z-a)f(z)$。若 $f=P/Q$、$Q(a)=0$、$Q'(a)\ne0$，则

$$
\operatorname{Res}(P/Q,a)=\frac{P(a)}{Q'(a)}.
$$

若 $a$ 为 $m$ 阶极点，则

$$
\boxed{\operatorname{Res}(f,a)=\frac1{(m-1)!}\lim_{z\to a}\frac{d^{m-1}}{dz^{m-1}}\big[(z-a)^mf(z)\big]}.
$$

也可直接用级数提取 $1/(z-a)$ 项，常比高阶求导简单。例：$(z-\sin z)/z^6=1/(6z^3)-1/(120z)+\cdots$，因此在零留数为 $-1/120$。

若正向简单闭曲线 $C$ 内只有有限个孤立奇点 $a_k$，且曲线上无奇点，则

$$
\boxed{\oint_Cf(z)\,dz=2\pi i\sum_{a_k\text{ 在内部}}\operatorname{Res}(f,a_k)}.
$$

$$
\operatorname{Res}(f,\infty)=-\operatorname{Res}\!\left(\frac1{w^2}f(1/w),0\right).
$$

若扩充复平面上只有有限个孤立奇点，则有限点留数之和加无穷远留数等于零。计算大圆积分时可用外部有限点与无穷远点来减少工作；**无穷远奇点类型用 $f(1/w)$，留数公式另有因子 $1/w^2$，二者不能混淆。**

**例：** $\oint_{|z|=2}ze^z/(z^2-1)\,dz=\pi i(e+e^{-1})$；$\oint_{|z|=2}z/(z^4-1)\,dz=0$；$\oint_{|z|=2}e^z/[z(z-1)^2]\,dz=2\pi i$。

对于 $\int_0^{2\pi}R(\cos\theta,\sin\theta)\,d\theta$，置

$$
z=e^{i\theta},\quad d\theta=\frac{dz}{iz},\quad
\cos\theta=\frac{z+z^{-1}}2,\quad
\sin\theta=\frac{z-z^{-1}}{2i}.
$$

转为单位圆内的留数和，需检查单位圆上是否有奇点。

**例：** $0<\rho<1$ 时，$\displaystyle\int_0^{2\pi}\frac{\cos2\theta}{1-2\rho\cos\theta+\rho^2}\,d\theta=\frac{2\pi\rho^2}{1-\rho^2}$；$\displaystyle\int_0^{2\pi}\frac{d\theta}{1+8\cos^2\theta}=\frac{2\pi}3$。

设 $R=P/Q$ 无实轴极点，$\deg Q-\deg P\ge2$，则上半大圆弧积分趋零，得到

$$
\boxed{\int_{-\infty}^{\infty}R(x)\,dx
=2\pi i\sum_{\operatorname{Im}a_k>0}\operatorname{Res}(R,a_k)}.
$$

偶函数的半轴积分可取整轴积分的一半。若存在实轴奇点，须先判断普通广义积分还是柯西主值，不能直接套用。

**例：** $a,b>0$ 时

$$
\int_{-\infty}^{\infty}\frac{x^2\,dx}{(x^2+a^2)(x^2+b^2)}=\frac\pi{a+b},\qquad
\int_{-\infty}^{\infty}\frac{x^2+1}{x^4+1}\,dx=\sqrt2\pi.
$$

当 $a=b$ 时上半平面的极点变为二阶，结果仍为 $\pi/(2a)$。

对 $a>0$，$e^{iaz}$ 在上半平面衰减。若有理函数 $R$ 在无穷远至少为 $O(1/z)$，用 Jordan 引理控制大弧；无实轴奇点时

$$
\int_{-\infty}^{\infty}R(x)e^{iax}\,dx
=2\pi i\sum_{\operatorname{Im}z_k>0}\operatorname{Res}(R(z)e^{iaz},z_k).
$$

若实轴上有一阶极点，用上半小圆弧凹进绕开，在相应主值存在的条件下

$$
\operatorname{PV}\!\int_{-\infty}^{\infty}R(x)e^{iax}\,dx
=2\pi i\sum_{\operatorname{Im}z_k>0}\operatorname{Res}(R(z)e^{iaz},z_k)
+\pi i\sum_{x_j\in\mathbb R}\operatorname{Res}(R(z)e^{iaz},x_j).
$$

$a<0$ 宜在下半平面闭合，方向与符号随之改变。**普通广义积分要求两侧分别收敛；主值只要求对称截断的极限存在，二者不同。**

$$
\operatorname{PV}\!\int_{-\infty}^{\infty}f(x)\,dx=\lim_{R\to\infty}\int_{-R}^Rf(x)\,dx.
$$

**例：** $a,b>0$ 时

$$
\int_0^\infty\frac{x\sin x}{x^2+a^2}\,dx=\frac\pi2e^{-a},\qquad
\int_{-\infty}^{\infty}\frac{\sin(ax)}{x(x^2+b^2)}\,dx
=\frac\pi{b^2}(1-e^{-ab}),\qquad
\int_0^\infty\frac{\sin x}{x}\,dx=\frac\pi2.
$$

第二个被积函数在零可补成连续，辅助函数 $e^{iaz}/[z(z^2+b^2)]$ 则有实轴极点，推导时须处理小半圆。

沿夹角 $\pi/4$ 的扇形积分 $e^{iz^2}$，利用斜射线上 $z=e^{i\pi/4}t$，并证明圆弧积分趋零，可得

$$
\int_0^\infty e^{ix^2}\,dx=\frac{\sqrt\pi}{2\sqrt2}(1+i),\qquad
\boxed{\int_0^\infty\sin x^2\,dx=\int_0^\infty\cos x^2\,dx=\sqrt{\frac\pi8}}.
$$
