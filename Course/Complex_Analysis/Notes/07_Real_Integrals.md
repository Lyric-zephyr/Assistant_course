# 留数计算实积分与主值

来源：高瑜《复变函数与积分变换》2024 秋讲义，原文件第 32–35 页。

本篇为阅读手写内容后的整理稿，采用标准 LaTeX 补全公式和必要条件，合并重复说明、略写部分证明；不是逐字转录。


## 三角有理式积分

对于 $\int_0^{2\pi}R(\cos\theta,\sin\theta)\,d\theta$，置

$$
z=e^{i\theta},\quad d\theta=\frac{dz}{iz},\quad
\cos\theta=\frac{z+z^{-1}}2,\quad
\sin\theta=\frac{z-z^{-1}}{2i}.
$$

转为单位圆内的留数和，需检查单位圆上是否有奇点。

**例：** $0<\rho<1$ 时，$\displaystyle\int_0^{2\pi}\frac{\cos2\theta}{1-2\rho\cos\theta+\rho^2}\,d\theta=\frac{2\pi\rho^2}{1-\rho^2}$；$\displaystyle\int_0^{2\pi}\frac{d\theta}{1+8\cos^2\theta}=\frac{2\pi}3$。

## 有理函数的整轴积分

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

## 指数因子与实轴极点

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

## Fresnel 积分

沿夹角 $\pi/4$ 的扇形积分 $e^{iz^2}$，利用斜射线上 $z=e^{i\pi/4}t$，并证明圆弧积分趋零，可得

$$
\int_0^\infty e^{ix^2}\,dx=\frac{\sqrt\pi}{2\sqrt2}(1+i),\qquad
\boxed{\int_0^\infty\sin x^2\,dx=\int_0^\infty\cos x^2\,dx=\sqrt{\frac\pi8}}.
$$
