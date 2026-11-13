# 级数、泰勒展开与洛朗展开

来源：高瑜《复变函数与积分变换》2024 秋讲义，原文件第 21–26 页。

本篇为阅读手写内容后的整理稿，采用标准 LaTeX 补全公式和必要条件，合并重复说明、略写部分证明；不是逐字转录。


## 复数项与函数项级数

$\sum\alpha_n$ 收敛等价于实部级数与虚部级数同时收敛。绝对收敛推出收敛，并有 $|\sum\alpha_n|\le\sum|\alpha_n|$。

函数级数 $\sum f_n(z)$ 的部分和为 $S_N$。一致收敛指：对任意 $\varepsilon>0$，存在与 $z$ 无关的 $N_0$，当 $N>N_0$ 时所有 $z$ 都满足 $|S_N(z)-S(z)|<\varepsilon$。

Weierstrass 判别法：$|f_n(z)|\le M_n$ 且 $\sum M_n<\infty$，则一致绝对收敛。一致收敛允许在适当条件下交换连续性、沿曲线积分与求和。解析函数列在每个紧子集上一致收敛时，极限解析，导数也在紧子集上一致收敛。

## 幂级数与收敛半径

$$
\sum_{n=0}^\infty c_n(z-a)^n,\qquad
\boxed{R^{-1}=\limsup_{n\to\infty}|c_n|^{1/n}}.
$$

若 $\lim|c_{n+1}/c_n|=\lambda$ 存在，则 $R=1/\lambda$；$\lambda=0$ 对应 $R=\infty$，$\lambda=\infty$ 对应 $R=0$。**边界 $|z-a|=R$ 须单独判断。** 圆内绝对收敛，在任意更小闭圆盘上一致收敛；圆外发散。

例如 $\sum z^n$ 的 $R=1$，和为 $1/(1-z)$；$\sum z^n/n^3$ 在 $|z|=1$ 绝对收敛；$\sum(z-1)^n/n$ 在 $z=0$ 条件收敛，在 $z=2$ 发散。

收敛圆内可逐项求导、积分，收敛半径不变：

$$
f'(z)=\sum_{n\ge1}nc_n(z-a)^{n-1}.
$$

## 泰勒定理与常用展开

若 $f$ 在 $|z-a|<R$ 解析，则

$$
\boxed{f(z)=\sum_{n=0}^\infty\frac{f^{(n)}(a)}{n!}(z-a)^n},\qquad |z-a|<R.
$$

展开唯一。可用直接求导、已知级数代入、乘除、逐项求导积分等方法。常用展开为

$$
\begin{aligned}
\frac1{1-z}&=\sum_{n\ge0}z^n&&(|z|<1),\\
e^z&=\sum_{n\ge0}\frac{z^n}{n!}&&(z\in\mathbb C),\\
\sin z&=\sum_{n\ge0}\frac{(-1)^nz^{2n+1}}{(2n+1)!},\quad
\cos z=\sum_{n\ge0}\frac{(-1)^nz^{2n}}{(2n)!},\\
\log(1+z)&=\sum_{n\ge1}\frac{(-1)^{n-1}z^n}{n}&&(|z|<1),\\
(1+z)^\alpha&=\sum_{n\ge0}\binom\alpha n z^n&&(|z|<1).
\end{aligned}
$$

最后两式取在 $z=0$ 附近值为 $0$ 的对数分支及相应幂分支；$\binom\alpha n=\alpha(\alpha-1)\cdots(\alpha-n+1)/n!$。例如 $\log\frac{1+z}{1-z}=2\sum_{n\ge0}z^{2n+1}/(2n+1)$。

## 洛朗定理

若 $f$ 在圆环 $r<|z-a|<R$ 解析，则

$$
\boxed{f(z)=\sum_{n=-\infty}^{\infty}c_n(z-a)^n},\qquad
c_n=\frac1{2\pi i}\oint_C\frac{f(\zeta)}{(\zeta-a)^{n+1}}\,d\zeta.
$$

$C$ 是圆环内绕 $a$ 一周的正向圆周。正幂部分称解析部分，负幂部分称主要部分。展开在所指圆环内唯一；不同圆环的展开可以不同。**洛朗系数不能一律用 $f^{(n)}(a)/n!$ 计算。**

**例：** 对 $f(z)=1/[(z-1)(z-2)]$，同一中心的三种展开是

$$
\begin{aligned}
|z|<1:\quad&\sum_{n\ge0}(1-2^{-n-1})z^n,\\
1<|z|<2:\quad&-\sum_{n\ge0}z^{-n-1}-\sum_{n\ge0}2^{-n-1}z^n,\\
2<|z|:\quad&\sum_{n\ge0}(2^n-1)z^{-n-1}.
\end{aligned}
$$

**例：** $z^3e^{1/z}=z^3+z^2+z/2!+1/3!+1/(4!z)+\cdots$。

积分只提取 $c_{-1}$：$\oint_Cf(z)\,dz=2\pi ic_{-1}$。因此 $\oint_{|z|=3}dz/[z(z+1)(z+4)]=-\pi i/6$，$\oint_{|z|=2}ze^{1/z}/(1-z)\,dz=-4\pi i$。

讲义补充练习包括：$\log\frac{1+z}{1-z}$、$1/[(z-1)(z-2)]$、$\tan z$ 的 Maclaurin 展开，$e^{z/(1-z)}$ 展开，以及围绕 $i$、$1$ 的指定圆环洛朗展开。未给出完整解答的练习不当作已有答案。
