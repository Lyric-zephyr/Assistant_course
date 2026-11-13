<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC14%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6%E7%B1%BB-%E5%88%9D%E8%B5%9B%E7%AC%AC%E4%BA%8C%E6%AC%A1%E8%A1%A5%E8%B5%9B-2023.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第十四届全国大学生数学竞赛初赛第二次补赛试题及参考答案（非数学类）

> **年份**：2023 年（第十四届初赛第二次补赛，考试日期 2023 年 3 月 5 日）｜**类别**：非数学专业（非数学类）
> **考试形式**：闭卷｜**时间**：150 分钟（竞赛通用设置，卷面未标注）｜**满分**：100 分
> **来源**：扫描版 PDF（标题为"第十四届全国大学生数学竞赛初赛第二次补赛试题 及参考答案（非数学类, 2023年3月5日）"，页面含「大学生数学竞赛网 www.cmathc.cn」水印）｜原始文件：`../第十四届全国大学生数学竞赛初赛（非数学类）第二次补赛试题及参考答案.pdf`
> **转录说明**：原卷为扫描版，本文件由视觉逐页转写，公式采用 KaTeX 语法；正文【解】【证】为原卷参考答案的逐字转写（行文中标注为"解答"/"证明"），原卷在行尾以虚横线加"N 分"标注评分点，本转录记作"……（N 分）"；填空题"答案"为据原卷【解】归纳的结果。

---

## 卷面结构

| 题号 | 一 | 二 | 三 | 四 | 五 | 六 | 总分 |
|---|---|---|---|---|---|---|---|
| 满分 | 30 | 14 | 14 | 14 | 14 | 14 | 100 |
| 形式 | 填空题 ×5 | 解答题 | 解答题 | 解答题 | 解答题 | 解答题 | |

---

## 一、填空题（本题满分 30 分，每小题 6 分）

**(1)** 极限 $\lim\limits_{n\to\infty}\dfrac{1}{n^3}\left[1^2+3^2+\cdots+(2n-1)^2\right] = \underline{\qquad}$。

> **答案**：$\dfrac{4}{3}$
>
> **解答**：利用定积分的定义，得
> $$\lim_{n\to\infty}\frac{1}{n^3}\left[1^2+3^2+\cdots+(2n-1)^2\right] = 4\lim_{n\to\infty}\frac{1}{n}\sum_{k=1}^{n}\left(\frac{k}{n}-\frac{1}{2n}\right)^2 = 4\int_0^1 x^2\,\mathrm{d}x = \frac{4}{3}.$$

**(2)** 设函数 $f(x)$ 在 $x=1$ 的某一邻域内可微，且满足
$$f(1+x)-3f(1-x)=4+2x+o(x),$$
其中 $o(x)$ 是当 $x\to 0$ 时 $x$ 的高阶无穷小，则曲线 $y=f(x)$ 在点 $(1,f(1))$ 处的切线方程为 $\underline{\qquad}$。

> **答案**：$x-2y-5=0$
>
> **解答**：由于 $f(x)$ 在 $x=1$ 处可微，因而连续，故对所给等式求极限 $x\to 0$，可得 $-2f(1)=4$，所以 $f(1)=-2$。仍由所给等式，得
> $$\frac{f(1+x)-f(1)}{x}+3\cdot\frac{f(1-x)-f(1)}{-x}=2+\frac{o(x)}{x},$$
> 两边取极限 $x\to 0$，并根据导数的定义，得 $4f'(1)=2$，所以 $f'(1)=\dfrac{1}{2}$。
>
> 因此，曲线 $y=f(x)$ 在点 $(1,f(1))$ 处的切线方程为
> $$y-f(1)=f'(1)(x-1),\qquad 即\quad x-2y-5=0.$$

**(3)** 设 $y=y(x)$ 是初值问题 $\begin{cases}y''-2y'-3y=1, \\ y(0)=0,\ y'(0)=1\end{cases}$ 的解，则 $y(x) = \underline{\qquad}$。

> **答案**：$y(x)=\dfrac{1}{3}\left(e^{3x}-1\right)$
>
> **解答**：对于齐次微分方程 $y''-2y'-3y=0$，其特征方程 $\lambda^2-2\lambda-3=0$ 的根为 $\lambda_1=3$，$\lambda_2=-1$，所以 $y''-2y'-3y=0$ 的通解为 $y=C_1e^{3x}+C_2e^{-x}$。
>
> 经观察，非齐次微分方程 $y''-2y'-3y=1$ 的一个特解为 $y_0=-\dfrac{1}{3}$。所以，方程的通解为 $y(x)=C_1e^{3x}+C_2e^{-x}-\dfrac{1}{3}$。
>
> 又由 $y(0)=0$，$y'(0)=1$ 解得，$C_1=\dfrac{1}{3}$，$C_2=0$，因此 $y(x)=\dfrac{1}{3}\left(e^{3x}-1\right)$。

**(4)** 设可微函数 $z=z(x,y)$ 满足 $x^2\dfrac{\partial z}{\partial x}+y^2\dfrac{\partial z}{\partial y}=2z^2$，又设 $u=x$，$v=\dfrac{1}{y}-\dfrac{1}{x}$，$w=\dfrac{1}{z}-\dfrac{1}{x}$，则对函数 $w=w(u,v)$，偏导数 $\left.\dfrac{\partial w}{\partial u}\right|_{\substack{u=2\\ v=1}} = \underline{\qquad}$。

> **答案**：$-\dfrac{1}{4}$
>
> **解答**：由 $u=x$，$v=\dfrac{1}{y}-\dfrac{1}{x}$ 解得 $x=u$，$y=\dfrac{u}{uv+1}$，且 $w=\dfrac{1}{z}-\dfrac{1}{u}$，所以
> $$\frac{\partial w}{\partial u}=\frac{\partial}{\partial u}\left(\frac{1}{z}-\frac{1}{u}\right)=-\frac{1}{z^2}\cdot\frac{\partial z}{\partial u}+\frac{1}{u^2}=-\frac{1}{z^2}\left(\frac{\partial z}{\partial x}\cdot\frac{\partial x}{\partial u}+\frac{\partial z}{\partial y}\cdot\frac{\partial y}{\partial u}\right)+\frac{1}{u^2}$$
> $$=-\frac{1}{z^2}\left(\frac{\partial z}{\partial x}+\frac{\partial z}{\partial y}\cdot\frac{uv+1-uv}{(uv+1)^2}\right)+\frac{1}{u^2}=-\frac{1}{z^2}\left(\frac{\partial z}{\partial x}+\frac{\partial z}{\partial y}\cdot\frac{1}{(uv+1)^2}\right)+\frac{1}{u^2}$$
> $$=-\frac{1}{z^2}\left(\frac{\partial z}{\partial x}+\frac{\partial z}{\partial y}\cdot\frac{y^2}{u^2}\right)+\frac{1}{u^2}=-\frac{1}{z^2u^2}\left(x^2\frac{\partial z}{\partial x}+y^2\frac{\partial z}{\partial y}\right)+\frac{1}{u^2}=-\frac{1}{u^2}.$$
> 因此 $\left.\dfrac{\partial w}{\partial u}\right|_{\substack{u=2\\ v=1}}=-\dfrac{1}{4}$。

**(5)** 设 $a>0$，则均匀曲面 $x^2+y^2+z^2=a^2$（$x\ge 0$，$y\ge 0$，$z\ge 0$）的重心坐标为 $\underline{\qquad}$。

> **答案**：$\left(\dfrac{a}{2},\ \dfrac{a}{2},\ \dfrac{a}{2}\right)$
>
> **解答**：记所给曲面为 $\Sigma$，并设 $\Sigma$ 的面密度为常数 $\mu$，$\Sigma$ 的重心坐标为 $(\bar{x},\bar{y},\bar{z})$。
>
> 由于 $\Sigma$ 的质量为 $M=\dfrac{1}{8}\cdot 4\pi a^2\mu=\dfrac{\pi a^2\mu}{2}$，所以
> $$\bar{z}=\frac{1}{M}\iint_\Sigma z\mu\,\mathrm{d}S=\frac{2}{\pi a^2}\iint_\Sigma z\,\mathrm{d}S.$$
> 设 $\Sigma$ 的外法向量与 $z$ 轴正向的夹角为 $\gamma$，则 $\cos\gamma=\dfrac{z}{a}$，所以
> $$\bar{z}=\frac{2}{\pi a^2}\iint_\Sigma z\,\mathrm{d}S=\frac{2}{\pi a}\iint_\Sigma \cos\gamma\,\mathrm{d}S=\frac{2}{\pi a}\iint_\Sigma \mathrm{d}x\mathrm{d}y=\frac{2}{\pi a}\cdot\frac{1}{4}\pi a^2=\frac{a}{2}.$$
> 根据对称性，$\bar{x}=\bar{y}=\dfrac{a}{2}$，因此曲面的重心坐标为 $\left(\dfrac{a}{2},\dfrac{a}{2},\dfrac{a}{2}\right)$。

---

## 二、（本题满分 14 分）

设函数 $f(x)=e^{-x}\displaystyle\int_0^x\frac{t^{2023}}{1+t^2}\,\mathrm{d}t$，正整数 $n\le 2023$，求导数 $f^{(n)}(0)$。

> **解答**：令 $F(x)=\displaystyle\int_0^x\frac{t^{2023}}{1+t^2}\,\mathrm{d}t$，则 $F'(x)=\dfrac{x^{2023}}{1+x^2}$，$F''(x)=\dfrac{2023x^{2022}(1+x^2)-2x^{2024}}{(1+x^2)^2}$，所以 $F(0)=F'(0)=F''(0)=0$。……（5 分）
>
> 对 $f(x)=e^{-x}F(x)$ 利用 Leibniz 公式，再代入 $x=0$ 得
> $$f^{(n)}(0)=e^{-x}\sum_{k=0}^n(-1)^{n-k}C_n^kF^{(k)}(x)\Big|_{x=0}=\sum_{k=0}^n(-1)^{n-k}C_n^kF^{(k)}(0).$$
> ……（4 分）
>
> 欲求 $F^{(k)}(0)$，对 $(1+x^2)F'(x)=x^{2023}$ 两边求 $k-1$ 阶导数，并利用 Leibniz 公式，得
> $$(1+x^2)F^{(k)}(x)+2(k-1)xF^{(k-1)}(x)+(k-1)(k-2)F^{(k-2)}(x)=(x^{2023})^{(k-1)},$$
> 代入 $x=0$，并注意到 $k\le n\le 2023$，得 $F^{(k)}(0)=-(k-1)(k-2)F^{(k-2)}(0)$。由此递推，得
> $$F^{(2k)}(0)=\cdots=(-1)^{k-1}(2k-1)!F''(0)=0,$$
> $$F^{(2k+1)}(0)=\cdots=(-1)^k(2k)!F'(0)=0,$$
> 因此，$f^{(n)}(0)=\displaystyle\sum_{k=0}^n(-1)^{n-k}C_n^kF^{(k)}(0)=0$。……（5 分）

---

## 三、（本题满分 14 分）

设函数 $f(x)$ 在区间 $(0,1)$ 内有定义，$\lim\limits_{x\to 0^+}f(x)=0$，且
$$\lim_{x\to 0^+}\frac{f(x)-f\left(\dfrac{x}{3}\right)}{x}=0.$$
证明：$\lim\limits_{x\to 0^+}\dfrac{f(x)}{x}=0$。

> **证明**：根据题设条件得，对于任意非负整数 $k$，有
> $$\lim_{x\to 0^+}\frac{f\left(\dfrac{x}{3^k}\right)-f\left(\dfrac{x}{3^{k+1}}\right)}{\dfrac{x}{3^k}}=0.$$
> ……（4 分）
>
> 令 $k=0,1,2,\cdots,n-1$，并求和，可得
> $$\lim_{x\to 0^+}\frac{f(x)-f\left(\dfrac{x}{3^n}\right)}{x}=\lim_{x\to 0}\sum_{k=1}^{n}\frac{f\left(\dfrac{x}{3^k}\right)-f\left(\dfrac{x}{3^{k+1}}\right)}{\dfrac{x}{3^k}}\cdot\frac{1}{3^k}=0.$$
> ……（5 分）
>
> > **注**：此处原卷求和下标疑为笔误（原卷印为 $k=1$ 至 $n$）。按印刷下标，右端 telescoping 后为 $\dfrac{f(x/3)-f(x/3^{n+1})}{x}$，与左端 $\dfrac{f(x)-f(x/3^n)}{x}$ 不符；若求和下标取 $k=0$ 至 $n-1$，则两端吻合。
>
> 因此，有 $f(x)-f\left(\dfrac{x}{3^n}\right)=x\alpha(x)$，其中 $\alpha(x)$ 是当 $x\to 0^+$ 时的无穷小。
>
> 对上述式取极限 $n\to\infty$，并利用条件 $\lim\limits_{x\to 0^+}f(x)=0$，得 $f(x)=x\alpha(x)$。所以
> $$\lim_{x\to 0}\frac{f(x)}{x}=\lim_{x\to 0}\alpha(x)=0.$$
> ……（5 分）

---

## 四、（本题满分 14 分）

设函数 $f(x)$ 在区间 $[0,1]$ 上连续，在 $(0,1)$ 内可导，且 $f(0)=0$，$f(1)=2$。证明：存在两两互异的点 $\xi_1,\xi_2,\xi_3\in(0,1)$，使得
$$f'(\xi_1)f'(\xi_2)\sqrt{1-\xi_3}\ge 2.$$

> **证明**：令 $F(x)=f(x)-2+x$，则 $F(x)$ 在 $[0,1]$ 上连续，且 $F(0)=-2$，$F(1)=1$。根据连续函数介值定理，存在 $\xi_3\in(0,1)$ 使得 $F(\xi_3)=0$，即 $f(\xi_3)=2-\xi_3$。……（5 分）
>
> 在区间 $[0,\xi_3]$、$[\xi_3,1]$ 上分别利用 Lagrange 中值定理，存在 $\xi_1\in(0,\xi_3)$，$\xi_2\in(\xi_3,1)$，使得
> $$\frac{f(\xi_3)-f(0)}{\xi_3-0}=f'(\xi_1),\qquad 且\qquad \frac{f(\xi_3)-f(1)}{\xi_3-1}=f'(\xi_2),$$
> 即 $f'(\xi_1)=\dfrac{2-\xi_3}{\xi_3}$，$f'(\xi_2)=\dfrac{\xi_3}{1-\xi_3}$，……（5 分）
>
> 所以
> $$f'(\xi_1)f'(\xi_2)=\frac{2-\xi_3}{1-\xi_3}=1+\frac{1}{1-\xi_3}\ge\frac{2}{\sqrt{1-\xi_3}},$$
> 因此，存在两两互异的点 $\xi_1,\xi_2,\xi_3\in(0,1)$，使得 $f'(\xi_1)f'(\xi_2)\sqrt{1-\xi_3}\ge 2$。……（4 分）

---

## 五、（本题满分 14 分）

设 $f(x)$ 是 $[-1,1]$ 上的连续的偶函数，计算曲线积分：
$$I=\oint_L\frac{x^2+y^2}{2\sqrt{1-x^2}}\,\mathrm{d}x+f(x)\,\mathrm{d}y,$$
其中曲线 $L$ 为正向圆周 $x^2+y^2=-2y$。

> **解答**：取圆的圆心角 $\theta$ 作参数，则曲线 $L$：$x^2+(y+1)^2=1$ 的参数方程为：
> $$x=\cos\theta,\qquad y+1=\sin\theta\qquad (0\le\theta\le 2\pi).$$
> 因为 $\mathrm{d}x=-\sin\theta\,\mathrm{d}\theta$，$\mathrm{d}y=\cos\theta\,\mathrm{d}\theta$，所以
> $$I=\int_0^{2\pi}\frac{1-\sin\theta}{|\sin\theta|}(-\sin\theta)\,\mathrm{d}\theta+\int_0^{2\pi}f(\cos\theta)\cos\theta\,\mathrm{d}\theta.$$
> ……（4 分）
>
> 其中第一项为
> $$I_1=\int_0^{2\pi}\frac{-(1-\sin\theta)}{|\sin\theta|}\sin\theta\,\mathrm{d}\theta=-\int_0^{\pi}(1-\sin\theta)\,\mathrm{d}\theta+\int_{\pi}^{2\pi}(1-\sin\theta)\,\mathrm{d}\theta=4,$$
> ……（5 分）
>
> 第二项为
> $$I_2=\int_0^{2\pi}f(\cos\theta)\cos\theta\,\mathrm{d}\theta=\int_0^{\pi}f(\cos\theta)\cos\theta\,\mathrm{d}\theta+\int_{\pi}^{2\pi}f(\cos\theta)\cos\theta\,\mathrm{d}\theta$$
> $$=\int_0^{\pi}f(\cos\theta)\cos\theta\,\mathrm{d}\theta+\int_0^{\pi}f(\cos(t+\pi))\cos(t+\pi)\,\mathrm{d}t$$
> $$=\int_0^{\pi}f(\cos\theta)\cos\theta\,\mathrm{d}\theta-\int_0^{\pi}f(-\cos t)\cos t\,\mathrm{d}t=0,$$
>
> 因此，原积分 $I=I_1+I_2=4$。……（5 分）

---

## 六、（本题满分 14 分）

设函数 $f(x)=\displaystyle\int_0^x\frac{\ln(1+t)}{1+e^{-t}\sin^3 t}\,\mathrm{d}t$（$x>0$），证明级数 $\displaystyle\sum_{n=1}^{\infty}f\left(\frac{1}{n}\right)$ 收敛，且
$$\frac{1}{3}<\sum_{n=1}^{\infty}f\left(\frac{1}{n}\right)<\frac{5}{6}.$$

> **解答**：利用不等式：当 $x\in(0,1]$ 时，$x-\dfrac{x^2}{2}\le\ln(1+x)\le x$，$\sin x\le x$，可得
> $$f(x)=\int_0^x\frac{\ln(1+t)}{1+e^{-t}\sin^3 t}\,\mathrm{d}t\ge\frac{1}{1+x}\int_0^x\left(t-\frac{t^2}{2}\right)\mathrm{d}t=\frac{1}{1+x}\left(\frac{x^2}{2}-\frac{x^3}{6}\right)>\frac{1}{3}\cdot\frac{x^2}{1+x},$$
> ……（3 分）
>
> 且 $f(x)=\displaystyle\int_0^x\frac{\ln(1+t)}{1+e^{-t}\sin^3 t}\,\mathrm{d}t\le\int_0^x t\,\mathrm{d}t=\frac{1}{2}x^2$，……（3 分）
>
> 所以
> $$\sum_{n=1}^{\infty}f\left(\frac{1}{n}\right)>\frac{1}{3}\sum_{n=1}^{\infty}\frac{\dfrac{1}{n^2}}{1+\dfrac{1}{n}}=\frac{1}{3}\sum_{n=1}^{\infty}\frac{1}{n(n+1)}=\frac{1}{3}\sum_{n=1}^{\infty}\left(\frac{1}{n}-\frac{1}{n+1}\right)=\frac{1}{3}.$$
> ……（4 分）
>
> $$\sum_{n=1}^{\infty}f\left(\frac{1}{n}\right)\le\frac{1}{2}\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{1}{2}\cdot\frac{\pi^2}{6}<\frac{5}{6}.$$
> ……（4 分）
>
> 综合上述，级数 $\displaystyle\sum_{n=1}^{\infty}f\left(\frac{1}{n}\right)$ 收敛，且 $\dfrac{1}{3}<\displaystyle\sum_{n=1}^{\infty}f\left(\frac{1}{n}\right)<\dfrac{5}{6}$。……（4 分）
>
> > **注**：原卷本题共标出 5 个评分点（3、3、4、4、4 分），合计 18 分，超出本题满分 14 分，疑为原卷标注问题，本转录照原卷保留。

---

## 附：本卷考点分布速览

| 题号 | 分值 | 考点板块 | 具体考点 |
|---|---|---|---|
| 一(1) | 6 | 极限 | 数列极限化为定积分（黎曼和定义） |
| 一(2) | 6 | 一元微分学 | 可微蕴含连续 + 导数定义（由函数方程求切线） |
| 一(3) | 6 | 常微分方程 | 二阶常系数非齐次线性方程 + 初值问题 |
| 一(4) | 6 | 多元微分学 | 变量替换下复合函数求偏导（一阶偏微分方程作约束） |
| 一(5) | 6 | 曲面积分与几何应用 | 均匀曲面重心（球面第一卦限部分 + 对称性 + 方向余弦） |
| 二 | 14 | 高阶导数 | 变限积分 + Leibniz 公式 + 系数递推求 $f^{(n)}(0)$ |
| 三 | 14 | 极限证明 | 迭代 $x/3$ 构造 telescoping 求和，证明 $f(x)/x\to 0$ |
| 四 | 14 | 微分中值定理 | 介值定理 + Lagrange 中值定理 + 基本不等式放缩 |
| 五 | 14 | 曲线积分 | 第二类曲线积分参数化计算 + 偶函数对称性化简 |
| 六 | 14 | 级数 | 积分放缩 + 级数收敛性与和的范围估计（$p$ 级数、裂项） |
