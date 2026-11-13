<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC09%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6%E7%B1%BB-%E5%88%9D%E8%B5%9B-2017-%E5%8F%82%E8%80%83%E8%A7%A3%E7%AD%94.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第9届（2017）非数学类初赛 · 官方参考解答（含评分标准）

> **来源**：公众号「竞赛资料网」版《2017 年数学竞赛预赛（非数学类）试题评分标准及参考答案》（原文件：`第09届非数学类-初赛(试题及参考解答).pdf`，共 5 页；页脚标注"更多竞赛资料、考试资料，尽在微信公众号：竞赛资料网"）｜本文件仅含解答与评分标准，题面见同目录《第09届非数学类-初赛-2017.md》
> **转录说明**：视觉逐页转写，关键公式放大至 200/300 dpi 逐字符核对；公式采用 KaTeX 语法。原文件解答以「解：」领起（第四题作「证.」、第五题作「证明：」），本文件统一以「参考解答」标注并保留原解答全文；行末「----X分」为原文件评分标准（步骤分）标注。填空题每小题 7 分为卷面标注，本参考解答文件未逐题标注填空题分值。原扫描件中少数省略号（⋯）被水印遮挡，按数学惯例补全。

## 一(1)（7分）

**参考解答**：在方程两边求导得

$$f'(x)\cos x+f(x)\sin x=1,\quad f'(x)+f(x)\tan x=\sec x.$$

从而

$$f(x)=e^{-\int\tan x\,\mathrm{d}x}\left(\int \sec x\,e^{\int\tan x\,\mathrm{d}x}\,\mathrm{d}x+c\right)$$

$$=e^{-\ln\cos x}\left(\int\frac{1}{\cos x}e^{-\ln\cos x}\,\mathrm{d}x+c\right)=\cos x\left(\int\frac{1}{\cos^2 x}\,\mathrm{d}x+c\right)$$

$$=\cos x(\tan x+c)=\sin x+c\cos x.$$

由于 $f(0)=1$，故 $f(x)=\sin x+\cos x$。

## 一(2)（7分）

**参考解答**：由于

$$\sin^2\left(\pi\sqrt{n^2+n}\right)=\sin^2\left(\pi\sqrt{n^2+n}-n\pi\right)$$

$$=\sin^2\left(\frac{n\pi}{\sqrt{n^2+n}+n}\right)\to 1。$$

## 一(3)（7分）

**参考解答**：$w_x=f_1+f_2,\quad w_{xx}=f_{11}+2f_{12}+f_{22},$

$$w_y=c(f_2-f_1),$$

$$w_{yy}=c\frac{\partial}{\partial y}(f_2-f_1)=c(cf_{11}-cf_{12}-cf_{21}+cf_{22})=c^2(f_{11}-2f_{12}+f_{22})。$$

所以 $w_{xx}-\dfrac{1}{c^2}w_{yy}=4f_{12}$。

## 一(4)（7分）

**参考解答**：$f(x)=f(0)+f'(0)x+\dfrac{1}{2}f''(\xi)x^2$，所以 $f(\sin^2 x)=\dfrac{1}{2}f''(\xi)\sin^4 x$。

这样

$$\lim_{x\to 0}\frac{f(\sin^2 x)}{x^4}=\lim_{x\to 0}\frac{f''(\xi)\sin^4 x}{2x^4}=3。$$

## 一(5)（7分）

**参考解答**：由于

$$I=2\int\frac{e^{-\sin x}\sin x\cos x}{(1-\sin x)^2}\,\mathrm{d}x\ \stackrel{\sin x=v}{=}\ 2\int\frac{ve^{-v}}{(1-v)^2}\,\mathrm{d}v=2\int\frac{(v-1+1)e^{-v}}{(1-v)^2}\,\mathrm{d}v$$

$$=2\int\frac{e^{-v}}{v-1}\,\mathrm{d}v+2\int\frac{e^{-v}}{(v-1)^2}\,\mathrm{d}v=2\int\frac{e^{-v}}{v-1}\,\mathrm{d}v-2\int e^{-v}\,\mathrm{d}\frac{1}{v-1}$$

$$=2\int\frac{e^{-v}}{v-1}\,\mathrm{d}v-2\left(e^{-v}\frac{1}{v-1}+\int\frac{e^{-v}}{v-1}\,\mathrm{d}v\right)=-\frac{2e^{-v}}{v-1}+C=\frac{2e^{-\sin x}}{1-\sin x}+C。$$

## 一(6)（7分）

**参考解答**：使用球面坐标

$$I=\iiint_V z\,\mathrm{d}x\mathrm{d}y\mathrm{d}z=\int_0^{2\pi}\mathrm{d}\theta\int_0^{\pi/4}\mathrm{d}\varphi\int_0^2\rho\cos\varphi\cdot\rho^2\sin\varphi\,\mathrm{d}\rho$$

$$=2\pi\cdot\frac{1}{2}\sin^2\varphi\Big|_0^{\pi/4}\cdot\frac{1}{4}\rho^4\Big|_0^2=2\pi。$$

## 二（本题满分 14 分）

**参考解答**：由于

$$\frac{\mathrm{d}g_\alpha(0)}{\mathrm{d}t}=(f_x,f_y)_{(0,0)}\binom{\cos\alpha}{\sin\alpha}=0$$

对一切 $\alpha$ 成立，故 $(f_x,f_y)_{(0,0)}=(0,0)$，即 $(0,0)$ 是 $f(x,y)$ 的驻点。----4分

记 $H_f(x,y)=\begin{pmatrix}f_{xx}&f_{xy}\\f_{yx}&f_{yy}\end{pmatrix}$，则

$$\frac{\mathrm{d}^2g_\alpha(0)}{\mathrm{d}t^2}=\frac{\mathrm{d}}{\mathrm{d}t}\left[(f_x,f_y)\binom{\cos\alpha}{\sin\alpha}\right]_{(0,0)}=(\cos\alpha,\sin\alpha)H_f(0,0)\binom{\cos\alpha}{\sin\alpha}>0.$$

----10分

上式对任何单位向量 $(\cos\alpha,\sin\alpha)$ 成立，故 $H_f(0,0)$ 是一个正定阵，而 $f(0,0)$ 是 $f$ 极小值。----14分

## 三（本题满分 14 分）

**参考解答**：记 $\Gamma_1$ 为从 $B$ 到 $A$ 的直线段，则 $x=t,\ y=0,\ z=1-t,\ 0\le t\le 1$，

$$\int_{\Gamma_1}y\,\mathrm{d}x+z\,\mathrm{d}y+x\,\mathrm{d}z=\int_0^1 t\,\mathrm{d}(1-t)=-\frac{1}{2}.$$

----4分

设 $\Gamma$ 和 $\Gamma_1$ 围成的平面区域 $\Sigma$，方向按右手法则。由 Stokes 公式得到

$$\left(\int_\Gamma+\int_{\Gamma_1}\right)y\,\mathrm{d}x+z\,\mathrm{d}y+x\,\mathrm{d}z=\iint_\Sigma\begin{vmatrix}\mathrm{d}y\mathrm{d}z&\mathrm{d}z\mathrm{d}x&\mathrm{d}x\mathrm{d}y\\[2pt]\dfrac{\partial}{\partial x}&\dfrac{\partial}{\partial y}&\dfrac{\partial}{\partial z}\\[4pt]y&z&x\end{vmatrix}=-\iint_\Sigma \mathrm{d}y\mathrm{d}z+\mathrm{d}z\mathrm{d}x+\mathrm{d}x\mathrm{d}y.$$

----8分

右边三个积分都是 $\Sigma$ 在各个坐标面上的投影面积，而 $\Sigma$ 在 $zx$ 面上投影面积为零。故

$$I+\int_{\Gamma_1}=-\iint_\Sigma \mathrm{d}y\mathrm{d}z+\mathrm{d}x\mathrm{d}y.$$

曲线 $\Gamma$ 在 $xy$ 面上投影的方程为

$$\frac{(x-1/2)^2}{(1/2)^2}+\frac{y^2}{(1/\sqrt{2})^2}=1.$$

----12分

又该投影（半个椭圆）的面积得知 $\displaystyle\iint_\Sigma \mathrm{d}x\mathrm{d}y=\frac{\pi}{4\sqrt{2}}$。同理，$\displaystyle\iint_\Sigma \mathrm{d}y\mathrm{d}z=\frac{\pi}{4\sqrt{2}}$。

这样就有 $I=\dfrac{1}{2}-\dfrac{\pi}{2\sqrt{2}}$。----14分

## 四（本题满分 15 分）

**参考解答**：由于 $\forall a,b(a<b)$，有

$$\int_a^b e^{-|t-x|}f(x)\,\mathrm{d}x\le\int_{-\infty}^{+\infty}e^{-|t-x|}f(x)\,\mathrm{d}x\le 1。$$

因此

$$\int_a^b \mathrm{d}t\int_a^b e^{-|t-x|}f(x)\,\mathrm{d}x\le b-a。$$

----4分

然而

$$\int_a^b \mathrm{d}t\int_a^b e^{-|t-x|}f(x)\,\mathrm{d}x=\int_a^b f(x)\left(\int_a^b e^{-|t-x|}\,\mathrm{d}t\right)\mathrm{d}x,$$

其中

$$\int_a^b e^{-|t-x|}\,\mathrm{d}t=\int_a^x e^{t-x}\,\mathrm{d}t+\int_x^b e^{x-t}\,\mathrm{d}t=2-e^{a-x}-e^{x-b}.$$

这样就有

$$\int_a^b f(x)(2-e^{a-x}-e^{x-b})\,\mathrm{d}x\le b-a\quad\cdots\cdots(1)$$

----10分

即

$$\int_a^b f(x)\,\mathrm{d}x\le\frac{b-a}{2}+\frac{1}{2}\left[\int_a^b e^{a-x}f(x)\,\mathrm{d}x+\int_a^b e^{x-b}f(x)\,\mathrm{d}x\right].$$

注意到

$$\int_a^b e^{a-x}f(x)\,\mathrm{d}x=\int_a^b e^{-|a-x|}f(x)\,\mathrm{d}x\le 1，\quad\text{和}\quad\int_a^b f(x)e^{x-b}\,\mathrm{d}x\le 1。$$

----13分

把以上两个式子入(1)（原文如此，疑脱"代"字），即得结论。----15分

## 五（本题满分 15 分）

**参考解答**：对于 $i=0,1,\cdots,p-1$，记

$$A_n^{(i)}\triangleq a_{(n+1)p+i}-a_{np+i}。$$

由题设 $\lim\limits_{n\to\infty}A_n^{(i)}=\lambda$，从而

$$\lim_{n\to\infty}\frac{A_1^{(i)}+A_2^{(i)}+\cdots+A_n^{(i)}}{n}=\lambda。$$

----5分

而

$$A_1^{(i)}+A_2^{(i)}+\cdots+A_n^{(i)}=a_{(n+1)p+i}-a_{p+i}。$$

由题设知

$$\lim_{n\to\infty}\frac{a_{(n+1)p+i}}{(n+1)p+i}=\lim_{n\to\infty}\frac{a_{(n+1)p+i}}{n}\cdot\frac{n}{(n+1)p+i}=\frac{\lambda}{p}。$$

----10分

对正整 $m$（原文如此，疑脱"数"字），设 $m=np+i$，其中 $0,1,\cdots,p-1$（原文如此，疑脱"$i=$"），从而可以把正整数依照 $i$ 分为 $p$ 个子类。考虑任何这样的子列，下面极限

$$\lim_{n\to\infty}\frac{a_{(n+1)p+i}}{(n+1)p+i}=\frac{\lambda}{p},$$

故

$$\lim_{n\to\infty}\frac{a_m}{m}=\frac{\lambda}{p}。$$

----15分
