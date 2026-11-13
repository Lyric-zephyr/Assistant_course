<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC01%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6%E7%B1%BB-%E5%88%9D%E8%B5%9B-2009-%E5%8F%82%E8%80%83%E8%A7%A3%E7%AD%94.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第 1 届（2009）非数学类初赛 · 官方参考解答

> 来源：考研竞赛数学公众号版（原文件：第01届非数学类-初赛(试题及参考解答).pdf）｜本文件仅含解答，题面见同目录《第01届非数学类-初赛-2009.md》
> 转录说明：视觉逐页转写（全 6 页，200 dpi 逐字符核对），公式采用 KaTeX 语法；「【参考答案】」「【参考证法一/二】」「【参考解法】」「【解法一/二】」为原文件解答标记，按原文保留；原文件笔误照抄并以"（转录注：…）"标出。

## 一(1)（5 分）

【参考答案】令 $\sqrt{1-x-y}=u$，$1+\dfrac{y}{x}=v$，解得 $x=\dfrac{1-u^{2}}{v}$，$y=\dfrac{(1-u^{2})(v-1)}{v}$

$$D_{uv}=\{(u,v)\mid 0<u\leqslant 1,\ 1\leqslant v<+\infty\}$$

$$\frac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}\dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v}\\[6pt] \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v}\end{vmatrix}=\begin{vmatrix}-\dfrac{2u}{v} & -\dfrac{1-u^{2}}{v^{2}}\\[6pt] -\dfrac{2u(v-1)}{v} & \dfrac{1-u^{2}}{v^{2}}\end{vmatrix}=\frac{2u(u^{2}-1)}{v^{2}}$$

$$\left|\frac{\partial(x,y)}{\partial(u,v)}\right|=\frac{2u(1-u^{2})}{v^{2}},\qquad \frac{(x+y)\ln\left(1+\dfrac{y}{x}\right)}{\sqrt{1-x-y}}=\frac{(1-u^{2})\ln v}{u},$$

所以由二重积分换元法的积分变换公式，原积分也就等于

$$\iint_{D}\frac{(x+y)\ln\left(1+\dfrac{y}{x}\right)}{\sqrt{1-x-y}}\,\mathrm{d}x\,\mathrm{d}y=2\iint_{D_{uv}}(1-u^{2})^{2}\cdot\frac{\ln v}{v^{2}}\,\mathrm{d}u\,\mathrm{d}v$$

$$=2\int_{0}^{1}(1-u^{2})^{2}\,\mathrm{d}u\int_{1}^{+\infty}\frac{\ln v}{v^{2}}\,\mathrm{d}v=2\cdot\frac{8}{15}\cdot 1=\frac{16}{15}.$$

## 一(2)（5 分）

【参考答案】令 $A=\displaystyle\int_{0}^{2}f(x)\,\mathrm{d}x$，$f(x)=3x^{2}-2-A$，

$$\int_{0}^{2}\left(3x^{2}-2-A\right)\mathrm{d}x=\left[x^{3}-2x-Ax\right]_{0}^{2}=8-4-2A=4-2A$$

所以 $A=4-2A\Rightarrow A=\dfrac{4}{3}$，代入所设函数表达式，得

$$f(x)=3x^{2}-2-A=3x^{2}-2-\frac{4}{3}=3x^{2}-\frac{10}{3}.$$

## 一(3)（5 分）

【参考答案】曲面在任意点 $(x,y,z)$ 处的法向量可以取为 $\vec{n}_{S}=\left(f'_{x},f'_{y},-1\right)=(x,2y,-1)$。平面 $\boldsymbol{\pi}:2x+2y-z=0$ 的法向量为 $\vec{n}_{\pi}=(2,2,-1)$。于切平面的法向量与平面 $\pi$ 的法向量平行（转录注：原文如此，疑脱"是"字，当作"于是切平面的法向量……"），也就有

$$\vec{n}_{S}\mathbin{/\!/}\vec{n}_{\pi}=(x,2y,-1)\mathbin{/\!/}(2,2,-1)$$

所以 $\dfrac{x}{2}=\dfrac{2y}{2}=\dfrac{-1}{-1}$，即 $\dfrac{x}{2}=y=1$，得 $x=2,\ y=1$，

$$z(2,1)=\left.\left(\frac{x^{2}}{2}+y^{2}-2\right)\right|_{(2,1)}=2+1-2=1$$

因此，所求的平面即为经过点 $(2,1,1)$，法向量为 $\vec{n}_{S}=(2,2,-1)$ 的平面，于是有平面的点法式方程，有 $2(x-2)+2(y-1)-(z-1)=0$，展开化简后有 $2x+2y-z-5=0$。

## 一(4)（5 分）

【参考答案】对等式两端分别关于 $x$ 求导数，$e^{f(y)}+xe^{f(y)}f'(y)y'(x)=e^{y}\cdot y'(x)\ln 29$。因为 $xe^{f(y)}=e^{y}\ln 29$，所以

$$y'(x)=\frac{e^{f(y)}}{\left[1-f'(y)\right]e^{y}\ln 29}$$

$$\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}=\left[y'(x)\right]'=\left[\frac{e^{f(y)}}{e^{y}\left[1-f'(y)\right]\ln 29}\right]'_{x}$$

$$=\frac{\left(e^{f(y)}\right)'\cdot e^{y}\left[1-f'(y)\right]-e^{f(y)}\cdot\left\{e^{y}\left[1-f'(y)\right]\right\}'_{x}}{e^{2y}\left[1-f'(y)\right]^{2}\ln 29}$$

$$=\Big\{e^{f(y)}\cdot f'(y)\cdot y'(x)\cdot e^{y}\left[1-f'(y)\right]-e^{f(y)}\cdot e^{y}y'(x)\left[1-f'(y)-f''(y)\right]\Big\}\Big/\Big\{e^{2y}\left[1-f'(y)\right]^{2}\ln 29\Big\}$$

$$=\frac{e^{f(y)}y'(x)\cdot\left\{2f'(y)-f'^{2}(y)-1+f''(y)\right\}}{e^{y}\left[1-f'(y)\right]^{2}\ln 29}$$

代入一阶导数表达式 $y'(x)=\dfrac{e^{f(y)}}{\left[1-f'(y)\right]e^{y}\ln 29}$，有

$$y''=\frac{e^{2f(y)}\left\{2f'(y)-f'^{2}(y)-1+f''(y)\right\}}{e^{2y}\left[1-f'(y)\right]^{3}\ln^{2}29}$$

由原等式 $xe^{f(y)}=e^{y}\ln 29$ 可以推得 $\dfrac{e^{2f(y)}}{e^{2y}\ln^{2}29}=\left(\dfrac{e^{f(y)}}{e^{y}\ln 29}\right)^{2}=\dfrac{1}{x^{2}}$，所以

$$y''=\frac{2f'(y)-f'^{2}(y)-1+f''(y)}{x^{2}\left[1-f'(y)\right]^{3}}=\frac{-\left[1-f'(y)\right]^{2}+f''(y)}{x^{2}\left[1-f'(y)\right]^{3}}$$

## 第二题（5 分）

【参考答案】原式 $=\lim\limits_{x\to 0}e^{\frac{e}{x}\ln\left(\frac{e^{x}+e^{2x}+\cdots+e^{nx}}{n}\right)}=e^{\lim\limits_{x\to 0}\frac{e}{x}\ln\left(\frac{e^{x}+e^{2x}+\cdots+e^{nx}}{n}\right)}$

由洛必达法则，有

$$\lim_{x\to 0}\frac{e\left[\ln\left(e^{x}+e^{2x}+\cdots+e^{nx}\right)-\ln n\right]}{x}=\lim_{x\to 0}\frac{e\left(e^{x}+2e^{x}+\cdots+ne^{nx}\right)}{e^{x}+e^{2x}+\cdots+e^{nx}}$$

（转录注：上式分子中第二项原文印作 $2e^{x}$，按逐项求导应为 $2e^{2x}$，此处照抄原文。）

$$=\frac{e(1+2+\cdots+n)}{n}=\frac{n+1}{2}e$$

于是 $\lim\limits_{x\to 0}\left(\dfrac{e^{x}+e^{2x}+\cdots+e^{nx}}{n}\right)^{\frac{e}{x}}=e^{\frac{n+1}{2}e}$.

## 第三题（15 分）

【参考答案】由题设，知 $f(0)=0$，$g(0)=0$. 令 $u=xt$，得 $g(x)=\dfrac{\int_{0}^{x}f(u)\,\mathrm{d}u}{x}\ (x\neq 0)$，

$$g'(x)=\frac{xf(x)-\int_{0}^{x}f(u)\,\mathrm{d}u}{x^{2}}\quad (x\neq 0)$$

由导数定义有 $g'(0)=\lim\limits_{x\to 0}\dfrac{\int_{0}^{x}f(u)\mathrm{d}u}{x^{2}}=\lim\limits_{x\to 0}\dfrac{f(x)}{2x}=\dfrac{A}{2}$. 由于

$$\lim_{x\to 0}g'(x)=\lim_{x\to 0}\frac{xf(x)-\int_{0}^{x}f(u)\mathrm{d}u}{x^{2}}$$

$$=\lim_{x\to 0}\frac{f(x)}{x}-\lim_{x\to 0}\frac{\int_{0}^{x}f(u)\mathrm{d}u}{x^{2}}=A-\frac{A}{2}=\frac{A}{2}=g'(0)$$

从而知 $g'(x)$ 在 $x=0$ 处连续.

## 第四题（15 分）

【参考证法一】由于区域 $D$ 为一正方形，可以直接用对坐标曲线积分的计算法计算.

$$\text{左边}=\int_{0}^{\pi}\pi e^{\sin y}\,\mathrm{d}y-\int_{\pi}^{0}\pi e^{-\sin x}\,\mathrm{d}x=\pi\int_{0}^{\pi}\left(e^{\sin x}+e^{-\sin x}\right)\mathrm{d}x,$$

$$\text{右边}=\int_{0}^{\pi}\pi e^{-\sin y}\,\mathrm{d}y-\int_{\pi}^{0}\pi e^{\sin x}\,\mathrm{d}x=\pi\int_{0}^{\pi}\left(e^{\sin x}+e^{-\sin x}\right)\mathrm{d}x,$$

所以 $\displaystyle\oint_{L}xe^{\sin y}\,\mathrm{d}y-ye^{-\sin x}\,\mathrm{d}x=\oint_{L}xe^{-\sin y}\,\mathrm{d}y-ye^{\sin x}\,\mathrm{d}x$.

由于 $e^{\sin x}+e^{-\sin x}\geqslant 2+\sin^{2}x$，

$$\oint_{L}xe^{\sin y}\,\mathrm{d}y-ye^{-\sin x}\,\mathrm{d}x=\pi\int_{0}^{\pi}\left(e^{\sin x}+e^{-\sin x}\right)\mathrm{d}x\geqslant\frac{5}{2}\pi^{2}$$

【参考证法二】(1) 根据格林公式，有

$$\oint_{L}xe^{\sin y}\,\mathrm{d}y-ye^{-\sin x}\,\mathrm{d}x=\iint_{D}\left(e^{\sin y}+e^{-\sin x}\right)\mathrm{d}\sigma$$

$$\oint_{L}xe^{-\sin y}\,\mathrm{d}y-ye^{\sin x}\,\mathrm{d}x=\iint_{D}\left(e^{-\sin y}+e^{\sin x}\right)\mathrm{d}\sigma$$

因为 关于 $y=x$ 对称，所以

$$\iint_{D}\left(e^{\sin y}+e^{-\sin x}\right)\mathrm{d}\sigma=\iint_{D}\left(e^{-\sin y}+e^{\sin x}\right)\mathrm{d}\sigma,$$

故 $\displaystyle\oint_{L}xe^{\sin y}\,\mathrm{d}y-ye^{-\sin x}\,\mathrm{d}x=\oint_{L}xe^{-\sin y}\,\mathrm{d}y-ye^{\sin x}\,\mathrm{d}x$.

(2) 由 $e^{t}+e^{-t}=2\displaystyle\sum_{n=0}^{\infty}\frac{t^{2n}}{(2n)!}\geqslant 2+t^{2}$，

$$\oint_{L}xe^{\sin y}\,\mathrm{d}y-ye^{-\sin x}\,\mathrm{d}x=\iint_{D}\left(e^{\sin y}+e^{-\sin x}\right)\mathrm{d}\sigma=\iint_{D}\left(e^{\sin x}+e^{-\sin x}\right)\mathrm{d}\delta\geqslant\frac{5}{2}\pi^{2}.$$

（转录注：上式第三个二重积分的微分符号原文印作 $\mathrm{d}\delta$，此处照抄；疑为 $\mathrm{d}\sigma$ 之误。）

## 第五题（10 分）

【参考解法】根据二阶线性非齐次微分方程解的结构有关知识，由题设可知: $e^{2x}$ 与 $e^{-x}$ 是相应齐次方程两个线性无关的解，且 $xe^{x}$ 是非齐次的一个特解. 因此可以用下述两种解法.

【解法一】：故此方程式 $y''-y'-2y=f(x)$。将 $y=xe^{x}$ 代入上式，得

$$f(x)=\left(xe^{x}\right)''-\left(xe^{x}\right)'-2xe^{x}=2e^{x}+xe^{x}-e^{x}-xe^{x}-2xe^{x}=e^{x}-2xe^{x}$$

因此所求方程为 $y''-y'-2y=e^{x}-2xe^{x}$.

【解法二】故 $y=xe^{x}+c_{1}e^{2x}+c_{2}e^{-x}$，是所求方程的通解，由

$$y'=e^{x}+xe^{x}+2c_{1}e^{2x}-c_{2}e^{-x},\qquad y''=4c_{1}e^{2x}+c_{2}e^{-x}+2e^{x}+xe^{x}$$

消去 $c_{1},c_{2}$ 得所求方程为 $y''-y'-2y=e^{x}-2xe^{x}$.

## 第六题（10 分）

【参考答案】因抛物线过原点，故 $c=1$，由题设有

$$\int_{0}^{1}\left(ax^{2}+bx\right)\mathrm{d}x=\frac{a}{3}+\frac{b}{2}=\frac{1}{3}.\ \text{即}\ b=\frac{2}{3}(1-a),$$

而 $V=\pi\displaystyle\int_{0}^{1}\left(ax^{2}+bx\right)^{2}\mathrm{d}x=\pi\left[\frac{1}{5}a^{2}+\frac{1}{2}ab+\frac{1}{3}b^{2}\right]$

$$=\pi\left[\frac{1}{5}a^{2}+\frac{1}{3}a(1-a)+\frac{1}{3}\cdot\frac{4}{9}(1-a)^{2}\right].$$

令 $\dfrac{\mathrm{d}v}{\mathrm{d}a}=\pi\left[\dfrac{2}{5}a+\dfrac{1}{3}-\dfrac{2}{3}a-\dfrac{8}{27}(1-a)\right]=0$，得 $a=-\dfrac{5}{4}$，代入 $b$ 的表达式 得 $b=\dfrac{3}{2}$. 所以 $y\geqslant 0$。

又因 $\left.\dfrac{\mathrm{d}^{2}v}{\mathrm{d}a^{2}}\right|_{a=-\frac{5}{4}}=\pi\left[\dfrac{2}{5}-\dfrac{2}{3}+\dfrac{8}{27}\right]=\dfrac{4}{135}\pi>0$ 及实际情况，当 $a=-\dfrac{5}{4}$，$b=\dfrac{3}{2}$，$c=1$ 时，体积最小.

## 第七题（15 分）

【参考答案】先解一阶常系数微分方程 $u_{n}'(x)-u_{n}(x)=x^{n-1}e^{x}$ 通解为

$$u_{n}(x)=e^{\int\mathrm{d}x}\left(\int x^{n-1}e^{x}e^{-\int\mathrm{d}x}\mathrm{d}x+c\right)=e^{x}\left(\frac{x^{n}}{n}+c\right)$$

由条件 $u_{n}(1)=\dfrac{e}{n}$，得 $c=0$，故 $u_{n}(x)=\dfrac{x^{n}e^{x}}{n}$，从而

$$\sum_{n=1}^{\infty}u_{n}(x)=\sum_{n=1}^{\infty}\frac{x^{n}e^{x}}{n}=e^{x}\sum_{n=1}^{\infty}\frac{x^{n}}{n}.\quad s(x)=\sum_{n=1}^{\infty}\frac{x^{n}}{n},$$

其收敛域为 $[-1,1)$，当 $x\in(-1,1)$ 时，有 $s'(x)=\displaystyle\sum_{n=1}^{\infty}x^{n-1}=\frac{1}{1-x}$，故

$$s(x)=\int_{0}^{x}\frac{1}{1-t}\mathrm{d}t=-\ln(1-x)。$$

当 $x=-1$ 时，$\displaystyle\sum_{n=1}^{\infty}u_{n}(x)=-e^{-1}\ln 2$. 于是，当 $-1\leqslant x<1$ 时，有

$$\sum_{n=1}^{\infty}u_{n}(x)=-e^{x}\ln(1-x).$$

## 第八题（10 分）

【参考答案】$\displaystyle\int_{0}^{+\infty}x^{t^{2}}\,\mathrm{d}t\leqslant\sum_{n=0}^{\infty}x^{n^{2}}\leqslant 1+\int_{0}^{+\infty}x^{t^{2}}\,\mathrm{d}t,$

$$\int_{0}^{+\infty}x^{t^{2}}\,\mathrm{d}t=\int_{0}^{+\infty}e^{-t^{2}\ln\frac{1}{x}}\,\mathrm{d}t=\frac{1}{\sqrt{\ln\frac{1}{x}}}\int_{0}^{+\infty}e^{-\left(t\sqrt{\ln\frac{1}{x}}\right)^{2}}\,\mathrm{d}\left(t\sqrt{\ln\frac{1}{x}}\right)$$

$$=\frac{1}{\sqrt{\ln\frac{1}{x}}}\int_{0}^{+\infty}e^{-t^{2}}\,\mathrm{d}t=\frac{1}{2}\sqrt{\frac{\pi}{\ln\frac{1}{x}}}\sim\frac{1}{2}\sqrt{\frac{\pi}{1-x}}.$$
