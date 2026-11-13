# 傅里叶变换、卷积与广义函数

来源：高瑜《复变函数与积分变换》2024 秋讲义，原文件第 36–42 页。

本篇为阅读手写内容后的整理稿，采用标准 LaTeX 补全公式和必要条件，合并重复说明、略写部分证明；不是逐字转录。


## 统一约定与逆变换

本讲义采用角频率约定：

$$
\boxed{F(\omega)=\mathcal F[f](\omega)=\int_{-\infty}^{\infty}f(t)e^{-i\omega t}\,dt},\qquad
\boxed{f(t)=\frac1{2\pi}\int_{-\infty}^{\infty}F(\omega)e^{i\omega t}\,d\omega}.
$$

$f\in L^1$ 时正变换存在。满足相应 Dirichlet/反演条件时，逆积分在跳跃点恢复 $[f(t-)+f(t+)]/2$。教材中还可能使用 $2\pi\xi$ 或对称归一化约定，**换约定必须同时更换逆变换与各公式系数。**

## 典型变换对

$$
\begin{aligned}
\mathbf1_{[-1,1]}(t)&\longleftrightarrow\frac{2\sin\omega}{\omega},\\
e^{-\beta t}u(t)&\longleftrightarrow\frac1{\beta+i\omega},\quad\beta>0,\\
Ee^{-\beta t^2}&\longleftrightarrow E\sqrt{\frac\pi\beta}e^{-\omega^2/(4\beta)},\quad\beta>0.
\end{aligned}
$$

首式在 $\omega=0$ 用连续延拓。$u$ 为单位阶跃函数。高斯变换可用矩形闭路把积分线平移后求出。

## 性质

变换和逆变换均线性。对 $a\ne0$，

$$
\begin{aligned}
\mathcal F[F](t)&=2\pi f(-t),\\
\mathcal F[f(at+b)](\omega)&=\frac1{|a|}e^{i\omega b/a}F(\omega/a),\\
\mathcal F[e^{i\omega_0t}f(t)](\omega)&=F(\omega-\omega_0),\\
\mathcal F[f^{(n)}](\omega)&=(i\omega)^nF(\omega),\\
F^{(n)}(\omega)&=\mathcal F[(-it)^nf(t)](\omega).
\end{aligned}
$$

普通函数的微分式需要可积性及分部积分边界项为零；广义函数框架下按分布导数解释。

$$
\mathcal F[f(t)\cos\omega_0t]=\tfrac12[F(\omega-\omega_0)+F(\omega+\omega_0)],
$$
$$
\mathcal F[f(t)\sin\omega_0t]=\tfrac1{2i}[F(\omega-\omega_0)-F(\omega+\omega_0)].
$$

Parseval 公式为

$$
\int f(t)\overline{g(t)}\,dt=\frac1{2\pi}\int F(\omega)\overline{G(\omega)}\,d\omega,
\qquad \int|f|^2=\frac1{2\pi}\int|F|^2.
$$

例如 $\int_{-\infty}^{\infty}\sin^2\omega/\omega^2\,d\omega=\pi$，$\int_{-\infty}^{\infty}\sin^4\omega/\omega^2\,d\omega=\pi/2$。

## 卷积

$$
(f*g)(t)=\int_{-\infty}^{\infty}f(\tau)g(t-\tau)\,d\tau,\qquad
\boxed{\mathcal F[f*g]=FG},\qquad \mathcal F[fg]=\frac1{2\pi}(F*G).
$$

卷积交换、结合、分配；在适当条件下 $(f*g)'=f'*g=f*g'$。$L^1$ 函数卷积仍属于 $L^1$，范数满足 $\|f*g\|_1\le\|f\|_1\|g\|_1$。

**例：** $a,b>0$ 时，$e^{-at^2}*e^{-bt^2}=\sqrt{\pi/(a+b)}e^{-ab t^2/(a+b)}$。

## Dirac 分布

**$\delta$ 不是通常意义下的函数。** 它由对测试函数的作用定义：$\langle\delta,\varphi\rangle=\varphi(0)$。Schwartz 空间由光滑、各阶导数均快速衰减的函数组成；缓增分布是其连续线性泛函。

$$
\begin{aligned}
\int\delta(t-a)\varphi(t)\,dt&=\varphi(a),\\
\langle\delta^{(n)},\varphi\rangle&=(-1)^n\varphi^{(n)}(0),\\
\delta(at)&=|a|^{-1}\delta(t),\quad u'=\delta,\quad\delta*f=f.
\end{aligned}
$$

本约定下 $\langle\mathcal F T,\varphi\rangle=\langle T,\mathcal F\varphi\rangle$。广义变换线性，并保留缩放、平移与分布微分性质。

$$
\begin{aligned}
\delta(t-a)&\longleftrightarrow e^{-i\omega a},&
1&\longleftrightarrow2\pi\delta(\omega),\\
e^{i\omega_0t}&\longleftrightarrow2\pi\delta(\omega-\omega_0),\\
\cos\omega_0t&\longleftrightarrow\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)],\\
\sin\omega_0t&\longleftrightarrow\frac\pi i[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)],\\
\operatorname{sgn}t&\longleftrightarrow2\operatorname{PV}\frac1{i\omega},&
u(t)&\longleftrightarrow\pi\delta(\omega)+\operatorname{PV}\frac1{i\omega}.
\end{aligned}
$$

**不能由 $\mathcal F[u']=i\omega\mathcal F[u]=1$ 直接得 $\mathcal F[u]=1/(i\omega)$：乘以 $\omega$ 会丢失 $\delta$ 项。** 讲义中写成 $1/\omega$ 的奇异表达在这里补为主值分布。

**例：** $\mathcal F^{-1}\{[(3+i\omega)(4+3i\omega)]^{-1}\}=(e^{-4t/3}-e^{-3t})u(t)/5$。积分微分方程可经变换化为频域代数关系，再作逆变换；含 $1/(i\omega)$ 时需明确边界条件与分布含义。
