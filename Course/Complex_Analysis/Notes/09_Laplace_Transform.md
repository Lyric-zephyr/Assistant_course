# 拉普拉斯变换与微分方程

来源：高瑜《复变函数与积分变换》2024 秋讲义，原文件第 43–46 页。

本篇为阅读手写内容后的整理稿，采用标准 LaTeX 补全公式和必要条件，合并重复说明、略写部分证明；不是逐字转录。


## 定义、收敛域与基本变换对

$$
\boxed{F(s)=\mathcal L[f](s)=\int_0^\infty f(t)e^{-st}\,dt},\quad s=\sigma+i\omega.
$$

使用单边变换；$t<0$ 部分视为零。若 $f$ 分段连续且 $|f(t)|\le Me^{ct}$，则在 $\operatorname{Re}s>c$ 绝对收敛。收敛域通常为右半平面；$F(\sigma+i\omega)=\mathcal F[e^{-\sigma t}f(t)u(t)](\omega)$。

$$
\begin{aligned}
1&\longleftrightarrow1/s,&e^{at}&\longleftrightarrow1/(s-a),\\
\cos at&\longleftrightarrow\frac{s}{s^2+a^2},&
\sin at&\longleftrightarrow\frac{a}{s^2+a^2},\\
t^\alpha&\longleftrightarrow\frac{\Gamma(\alpha+1)}{s^{\alpha+1}}\quad(\alpha>-1),&
\delta(t)&\longleftrightarrow1.
\end{aligned}
$$

单边分布变换对零点脉冲采用包含起点脉冲的约定。$\Gamma(x)=\int_0^\infty e^{-t}t^{x-1}\,dt$，$\Gamma(x+1)=x\Gamma(x)$，$\Gamma(n+1)=n!$。

## 性质

$$
\begin{aligned}
\mathcal L[\alpha f+\beta g]&=\alpha F+\beta G,\\
\mathcal L[f(t-\tau)u(t-\tau)]&=e^{-\tau s}F(s)\quad(\tau>0),\\
\mathcal L[e^{at}f(t)]&=F(s-a),\\
\mathcal L[f^{(n)}]&=s^nF(s)-\sum_{k=0}^{n-1}s^{n-1-k}f^{(k)}(0+),\\
F^{(n)}(s)&=\mathcal L[(-t)^nf(t)],\\
\mathcal L\!\left[\int_0^tf(\tau)\,d\tau\right]&=F(s)/s.
\end{aligned}
$$

**延迟后的整个函数都要把 $t$ 换成 $t-\tau$。** 时域微分会引入初值，频域微分对应乘 $-t$，两者不要混淆。

因果卷积为 $(f*g)(t)=\int_0^tf(\tau)g(t-\tau)\,d\tau$，其变换为 $FG$。例：$t*\sin t=t-\sin t$；$\mathcal L[\int_0^t\tau e^{a\tau}\sin(a\tau)\,d\tau]=2a(s-a)/[s((s-a)^2+a^2)^2]$。

## 反演

$$
f(t)=\frac1{2\pi i}\int_{\gamma-i\infty}^{\gamma+i\infty}F(s)e^{st}\,ds,\qquad t>0,
$$

$\gamma$ 位于收敛半平面。若闭路积分的条件满足、左侧闭合弧贡献消失，则反演化为 $\sum\operatorname{Res}(F(s)e^{st},s_k)$。对真有理函数，部分分式及常见变换对通常更直接；**不能对带延迟指数的任意式子不检查闭合弧就套留数和。**

**例：**

$$
\begin{aligned}
\mathcal L^{-1}\!\left[\frac1{s^4+5s^2+4}\right]
&=\frac13\sin t-\frac16\sin2t,\\
\mathcal L^{-1}\!\left[\frac{s+3}{s^3+3s^2+6s+4}\right]
&=\frac13e^{-t}\bigl(2-2\cos\sqrt3t+\sqrt3\sin\sqrt3t\bigr),\\
\mathcal L^{-1}\!\left[\frac1{(s^2+2s+2)^2}\right]
&=\frac12e^{-t}(\sin t-t\cos t),\\
\mathcal L^{-1}\!\left[\frac{1+e^{-2s}}{s^2}\right]
&=tu(t)+(t-2)u(t-2).
\end{aligned}
$$

对 $F(s)=\log[(s^2-1)/s^2]$，取右半平面相容分支并对 $s$ 求导，可得 $F'(s)=2/[s(s^2-1)]$，从而 $f(t)=(2-e^{-t}-e^t)/t$（$t>0$）。

## 初值问题

对 $f''+4f'+3f=e^{-t}$、$f(0)=f'(0)=1$，变换得到

$$
F(s)=\frac{s+5}{(s+1)(s+3)}+\frac1{(s+1)^2(s+3)},\qquad
f(t)=-\frac34e^{-3t}+\frac74e^{-t}+\frac12te^{-t}.
$$

对 $x'+x-y=e^t$、$3x+y'-2y=2e^t$、$x(0)=y(0)=1$，解得 $X=Y=1/(s-1)$，故 $x(t)=y(t)=e^t$。
