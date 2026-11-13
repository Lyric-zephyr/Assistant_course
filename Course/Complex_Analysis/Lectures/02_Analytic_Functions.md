# 模块二：解析函数及应用

来源：高瑜《复变函数与积分变换》2024 秋讲义，原 PDF 第 9–15 页。

本模块合并既有校订稿，公式采用标准 LaTeX，保留内容中的必要条件与歧义说明；不是逐字转录。

$$
f'(z_0)=\lim_{\Delta z\to0}\frac{f(z_0+\Delta z)-f(z_0)}{\Delta z}.
$$

点上可导只要求该点的导数存在；在点上解析要求在它的某邻域处处可导；在全平面解析称整函数。可导必连续，连续未必可导。和、积、商及复合求导法则与实变量情形相似。

**例：** $z'=1$；$\bar z$ 处处不可导；$|z|^2$ 仅在 $z=0$ 可导且导数为零，但不在任何点解析。有理函数在分母不为零处解析。

设 $f=u+iv$。在一点复可导，当且仅当 $u,v$ 在该点实可微且

$$
\boxed{u_x=v_y,\qquad u_y=-v_x},\qquad
f'=u_x+iv_x=v_y-iu_y.
$$

在邻域内一阶偏导连续且满足 C-R 条件是解析的充分条件。**单独满足 C-R 条件不够。** 例如 $f(z)=\sqrt{|xy|}$ 在原点的偏导满足 C-R，但沿 $y=kx$ 考察差商即可看出不可导。

**例：** $f=x^2+axy+by^2+i(cx^2+dxy+y^2)$ 解析时，$a=2,b=-1,c=-1,d=2$。

在区域内，$f'\equiv0$ 推出 $f$ 为常数；$f$ 与 $\bar f$ 同时解析、或解析函数模恒定，也推出常数。在 $f'\ne0$ 处，$u,v$ 的等值曲线正交。

$$
e^z=e^x(\cos y+i\sin y),\quad (e^z)'=e^z,\quad |e^z|=e^x,\quad e^{z+2\pi i}=e^z\ne0.
$$

$$
\operatorname{Ln}z=\ln|z|+i(\arg z+2k\pi),\quad k\in\mathbb Z.
$$

沿一条射线割开复平面后可选择解析对数分支，导数为 $1/z$。主值对数在负实轴的割线两侧有跳跃。$\ln i=i\pi/2$，$\operatorname{Ln}(-1)=i\pi+2k\pi i$。

**主值对数的乘积公式一般需加 $2k\pi i$。** 不得无条件写成 $\ln(zw)=\ln z+\ln w$。

复幂由 $a^b=\exp(b\operatorname{Ln}a)$ 定义。整数幂为单值，既约有理数 $p/q$ 次幂有 $q$ 个值；一般复幂需逐项检查分支。

$$
i^i=e^{-\pi/2-2k\pi},\qquad
(-3)^{\sqrt5}=3^{\sqrt5}e^{i\sqrt5(\pi+2k\pi)}.
$$

$$
\sin z=\frac{e^{iz}-e^{-iz}}{2i},\quad
\cos z=\frac{e^{iz}+e^{-iz}}2,\quad
\sinh z=\frac{e^z-e^{-z}}2,\quad
\cosh z=\frac{e^z+e^{-z}}2.
$$

正弦、余弦为整函数，导数分别为 $\cos z,-\sin z$，具有周期 $2\pi$，在复平面上不再有界。

$$
\sin(x+iy)=\sin x\cosh y+i\cos x\sinh y,\quad
\cos(x+iy)=\cos x\cosh y-i\sin x\sinh y.
$$

例如 $\cos(\pi+5i)=-\cosh5$。反函数通过对数表达且通常为多值：$\arctan z=\dfrac1{2i}\operatorname{Ln}\dfrac{1+iz}{1-iz}$；$\arccos z=-i\operatorname{Ln}(z+\sqrt{z^2-1})$，取值时需协调根与对数分支。

调和函数满足 $\Delta u=u_{xx}+u_{yy}=0$。解析函数的实部、虚部都调和。已知 $u$ 求共轭调和函数 $v$ 可用

$$
dv=-u_y\,dx+u_x\,dy.
$$

**单连通区域内的调和函数存在全局共轭调和函数，且相差实常数。** 非单连通区域只保证局部存在；$u=\ln|z|$ 在 $\mathbb C\setminus\{0\}$ 没有全局单值共轭。

**例：** $v=\arctan(y/x)$，$x>0$，可取 $u=\tfrac12\ln(x^2+y^2)+C$，$f=\log z+C$。

**例：** $u=e^x\cos y+x+y$ 且 $f(0)=1$，得到 $v=e^x\sin y-x+y$，$f(z)=e^z+(1-i)z$。
