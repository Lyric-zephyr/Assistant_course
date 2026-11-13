<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC12%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6%E7%B1%BB-%E5%88%9D%E8%B5%9B-2020.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第十二届全国大学生数学竞赛初赛试题及参考答案（非数学类）

> **年份**：2020 年（第十二届，卷面标注"2020 年 11 月"）｜**类别**：非数学类
> **考试形式**：闭卷｜**时间**：150 分钟｜**满分**：100 分
> **来源**：大学生数学竞赛网（cmathc.org.cn）转载 PDF｜原始文件：`../第十二届全国大学生数学竞赛初赛（非数学类）试题及参考答案.pdf`
> **转录说明**：原卷为扫描版，本文件由视觉逐页转写，公式采用 KaTeX 语法；原卷为「试题＋参考答案」合一版，每题题面之后紧跟原卷【解】，过程分标注（如"……（4 分）"）为原卷所标。

---

## 卷面结构

| 题号 | 一 | 二 | 三 | 四 | 五 | 六 | 七 | 总分 |
|---|---|---|---|---|---|---|---|---|
| 满分 | 30 | 10 | 10 | 12 | 12 | 12 | 14 | 100 |
| 形式 | 填空题 ×5 | 解答题 | 解答题 | 解答题 | 解答题 | 解答题 | 解答题 | |

---

## 一、填空题（本题满分 30 分，每小题 6 分）

**【1】** 极限 $\lim\limits_{x\to 0}\dfrac{(x-\sin x)e^{-x^2}}{\sqrt{1-x^3}-1} = \underline{\qquad}$。

> **【解】** 利用等价无穷小：当 $x\to 0$ 时，有 $\sqrt{1-x^3}-1 \sim -\dfrac{1}{2}x^3$，所以
> $$\lim_{x\to 0}\frac{(x-\sin x)e^{-x^2}}{\sqrt{1-x^3}-1} = -2\lim_{x\to 0}\frac{x-\sin x}{x^3} = -2\lim_{x\to 0}\frac{1-\cos x}{3x^2} = -\frac{1}{3}.$$

**【2】** 设函数 $f(x) = (x+1)^ne^{-x^2}$，则 $f^{(n)}(-1) = \underline{\qquad}$。

> **【解】** 利用莱布尼兹求导法则，得
> $$f^{(n)}(x) = n!\,e^{-x^2} + \sum_{k=0}^{n-1}C_n^k\left[(x+1)^n\right]^{(k)}\left(e^{-x^2}\right)^{(n-k)},$$
> 所以 $f^{(n)}(-1) = \dfrac{n!}{e}$。

**【3】** 设 $y = f(x)$ 是由方程 $\arctan\dfrac{x}{y} = \ln\sqrt{x^2+y^2} - \dfrac{1}{2}\ln 2 + \dfrac{\pi}{4}$ 确定的隐函数，且满足 $f(1) = 1$，则曲线 $y = f(x)$ 在点 $(1,1)$ 处的切线方程为 $\underline{\qquad}$。

> **【解】** 对所给方程两端关于 $x$ 求导，得
> $$\frac{\dfrac{y-xy'}{y^2}}{1+\left(\dfrac{x}{y}\right)^2} = \frac{x+yy'}{x^2+y^2},$$
> 即 $(x+y)y' = y-x$，所以 $f'(1) = 0$，曲线 $y = f(x)$ 在点 $(1,1)$ 处的切线方程为 $y = 1$。

**【4】** 已知 $\displaystyle\int_0^{+\infty}\frac{\sin x}{x}\,\mathrm{d}x = \frac{\pi}{2}$，则 $\displaystyle\int_0^{+\infty}\!\!\int_0^{+\infty}\frac{\sin x\sin(x+y)}{x(x+y)}\,\mathrm{d}x\mathrm{d}y = \underline{\qquad}$。

> **【解】** 令 $u = x+y$，得
> $$I = \int_0^{+\infty}\frac{\sin x}{x}\,\mathrm{d}x\int_0^{+\infty}\frac{\sin(x+y)}{x+y}\,\mathrm{d}y = \int_0^{+\infty}\frac{\sin x}{x}\,\mathrm{d}x\int_x^{+\infty}\frac{\sin u}{u}\,\mathrm{d}u$$
> $$= \int_0^{+\infty}\frac{\sin x}{x}\,\mathrm{d}x\left(\int_0^{+\infty}\frac{\sin u}{u}\,\mathrm{d}u - \int_0^x\frac{\sin u}{u}\,\mathrm{d}u\right) = \left(\int_0^{+\infty}\frac{\sin x}{x}\,\mathrm{d}x\right)^2 - \int_0^{+\infty}\frac{\sin x}{x}\,\mathrm{d}x\int_0^x\frac{\sin u}{u}\,\mathrm{d}u.$$
> 令 $F(x) = \displaystyle\int_0^x\frac{\sin u}{u}\,\mathrm{d}u$，则 $F'(x) = \dfrac{\sin x}{x}$，$\lim\limits_{x\to+\infty}F(x) = \dfrac{\pi}{2}$，所以
> $$I = \frac{\pi^2}{4} - \int_0^{+\infty}F(x)F'(x)\,\mathrm{d}x = \frac{\pi^2}{4} - \left.\frac{1}{2}[F(x)]^2\right|_0^{+\infty} = \frac{\pi^2}{4} - \frac{1}{2}\left(\frac{\pi}{2}\right)^2 = \frac{\pi^2}{8}.$$

**【5】** 设 $f(x)$，$g(x)$ 在 $x=0$ 的某一邻域 $U$ 内有定义，对任意 $x\in U$，$f(x)\neq g(x)$，且 $\lim\limits_{x\to 0}f(x) = \lim\limits_{x\to 0}g(x) = a > 0$，则 $\lim\limits_{x\to 0}\dfrac{[f(x)]^{g(x)}-[g(x)]^{g(x)}}{f(x)-g(x)} = \underline{\qquad}$。

> **【解】** 根据极限的保号性，存在 $x=0$ 的一个去心邻域 $U_1$，使得 $x\in U_1$ 时 $f(x)>0$，$g(x)>0$。当 $x\to 0$ 时，有 $e^x-1\sim x$，$\ln(1+x)\sim x$，利用等价无穷小替换，得
> $$\lim_{x\to 0}\frac{[f(x)]^{g(x)}-[g(x)]^{g(x)}}{f(x)-g(x)} = \lim_{x\to 0}[g(x)]^{g(x)}\frac{\left(\frac{f(x)}{g(x)}\right)^{g(x)}-1}{f(x)-g(x)} = a^a\lim_{x\to 0}\frac{\left(\frac{f(x)}{g(x)}\right)^{g(x)}-1}{f(x)-g(x)}$$
> $$= a^a\lim_{x\to 0}\frac{e^{g(x)\ln\frac{f(x)}{g(x)}}-1}{f(x)-g(x)} = a^a\lim_{x\to 0}\frac{g(x)\ln\frac{f(x)}{g(x)}}{f(x)-g(x)} = a^a\lim_{x\to 0}\frac{g(x)\ln\left(1+\left(\frac{f(x)}{g(x)}-1\right)\right)}{f(x)-g(x)}$$
> $$= a^a\lim_{x\to 0}\frac{g(x)\left(\frac{f(x)}{g(x)}-1\right)}{f(x)-g(x)} = a^a.$$

---

## 二、（本题满分 10 分）

设数列 $\{a_n\}$ 满足：$a_1 = 1$，且 $a_{n+1} = \dfrac{a_n}{(n+1)(a_n+1)}$，$n\geq 1$。求极限 $\lim\limits_{n\to\infty}n!\,a_n$。

> **【解】** 利用归纳法易知 $a_n > 0$（$n\geq 1$）。由于
> $$\frac{1}{a_{n+1}} = (n+1)\left(1+\frac{1}{a_n}\right) = (n+1) + (n+1)\frac{1}{a_n} = (n+1) + (n+1)\left(n + n\frac{1}{a_{n-1}}\right)$$
> $$= (n+1) + (n+1)n + (n+1)n\frac{1}{a_{n-1}},$$
> ……（4 分）
>
> 如此递推，得
> $$\frac{1}{a_{n+1}} = (n+1)!\left(\sum_{k=1}^n\frac{1}{k!} + \frac{1}{a_1}\right) = (n+1)!\sum_{k=0}^n\frac{1}{k!},$$
> ……（3 分）
>
> 因此
> $$\lim_{n\to\infty}n!\,a_n = \frac{1}{\lim\limits_{n\to\infty}\sum\limits_{k=0}^{n-1}\dfrac{1}{k!}} = \frac{1}{e}.$$
> ……（3 分）

---

## 三、（本题满分 10 分）

设 $f(x)$ 在 $[0,1]$ 上连续，$f(x)$ 在 $(0,1)$ 内可导，且 $f(0) = 0$，$f(1) = 1$。

证明：（1）存在 $x_0\in(0,1)$ 使得 $f(x_0) = 2-3x_0$；（2）存在 $\xi,\eta\in(0,1)$，且 $\xi\neq\eta$，使得 $[1+f'(\xi)][1+f'(\eta)] = 4$。

> **【解】**（1）令 $F(x) = f(x) - 2 + 3x$，则 $F(x)$ 在 $[0,1]$ 上连续，且 $F(0) = -2$，$F(1) = 2$。根据连续函数介值定理，存在 $x_0\in(0,1)$ 使得 $F(x_0) = 0$，即 $f(x_0) = 2-3x_0$。……（5 分）
>
> （2）在区间 $[0,x_0]$，$[x_0,1]$ 上利用拉格朗日中值定理，存在 $\xi,\eta\in(0,1)$，且 $\xi\neq\eta$，使得
> $$\frac{f(x_0)-f(0)}{x_0-0} = f'(\xi),\quad\text{且}\quad \frac{f(x_0)-f(1)}{x_0-1} = f'(\eta).$$
> 所以
> $$[1+f'(\xi)][1+f'(\eta)] = 4.$$
> ……（5 分）

---

## 四、（本题满分 12 分）

已知 $z = xf\left(\dfrac{y}{x}\right) + 2y\varphi\left(\dfrac{x}{y}\right)$，其中 $f$，$\varphi$ 均为二次可微函数。

（1）求 $\dfrac{\partial z}{\partial x}$，$\dfrac{\partial^2 z}{\partial x\partial y}$；

（2）当 $f = \varphi$，且 $\left.\dfrac{\partial^2 z}{\partial x\partial y}\right|_{x=a} = -by^2$ 时，求 $f(y)$。

> **【解】**（1）
> $$\frac{\partial z}{\partial x} = f\left(\frac{y}{x}\right) - \frac{y}{x}f'\left(\frac{y}{x}\right) + 2\varphi'\left(\frac{x}{y}\right),\qquad \frac{\partial^2 z}{\partial x\partial y} = -\frac{y}{x^2}f''\left(\frac{y}{x}\right) - \frac{2x}{y^2}\varphi''\left(\frac{x}{y}\right).$$
> ……（3 分）
>
> （2）
> $$\left.\frac{\partial^2 z}{\partial x\partial y}\right|_{x=a} = -\frac{y}{a^2}f''\left(\frac{y}{a}\right) - \frac{2a}{y^2}\varphi''\left(\frac{a}{y}\right) = -by^2.$$
> 因为 $f = \varphi$，所以
> $$\frac{y}{a^2}f''\left(\frac{y}{a}\right) + \frac{2a}{y^2}f''\left(\frac{a}{y}\right) = by^2.$$
> 令 $y = au$，则 $\dfrac{u}{a}f''(u) + \dfrac{2}{au^2}f''\left(\dfrac{1}{u}\right) = a^2bu^2$，即
> $$u^3f''(u) + 2f''\left(\frac{1}{u}\right) = a^3bu^4.$$
> 上式中以 $\dfrac{1}{u}$ 换 $u$ 得
> $$2f''\left(\frac{1}{u}\right) + 4u^3f''(u) = 2a^3b\,\frac{1}{u}.$$
> ……（5 分）
>
> 联立二式，解得 $-3u^3f''(u) = a^3b\left(u^4 - \dfrac{2}{u}\right)$，所以 $f''(u) = \dfrac{a^3b}{3}\left(\dfrac{2}{u^4}-u\right)$，从而有
> $$f(u) = \frac{a^3b}{3}\left(\frac{1}{3u^2} - \frac{u^3}{6}\right) + C_1u + C_2.$$
> 故
> $$f(y) = \frac{a^3b}{3}\left(\frac{1}{3y^2} - \frac{y^3}{6}\right) + C_1y + C_2.$$
> ……（4 分）

---

## 五、（本题满分 12 分）

计算 $I = \displaystyle\oint_\Gamma\left|\sqrt{3}y-x\right|\mathrm{d}x - 5z\,\mathrm{d}z$，曲线 $\Gamma:\begin{cases}x^2+y^2+z^2 = 8,\\ x^2+y^2 = 2z,\end{cases}$ 从 $z$ 轴正向往坐标原点看去取逆时针方向。

> **【解】** 曲线 $\Gamma$ 也可表示为 $\begin{cases}z = 2,\\ x^2+y^2 = 4,\end{cases}$ 所以 $\Gamma$ 的参数方程为
> $$\begin{cases}x = 2\cos\theta,\\ y = 2\sin\theta,\\ z = 2,\end{cases}$$
> 参数的范围：$0\leq\theta\leq 2\pi$。……（4 分）
>
> 注意到在曲线 $\Gamma$ 上 $\mathrm{d}z = 0$，所以
> $$I = -\int_0^{2\pi}\left|2\sqrt{3}\sin\theta - 2\cos\theta\right|2\sin\theta\,\mathrm{d}\theta = -8\int_0^{2\pi}\left|\frac{\sqrt{3}}{2}\sin\theta - \frac{1}{2}\cos\theta\right|\sin\theta\,\mathrm{d}\theta$$
> $$= -8\int_0^{2\pi}\left|\cos\left(\theta + \frac{\pi}{3}\right)\right|\sin\theta\,\mathrm{d}\theta = -8\int_{\frac{\pi}{3}}^{2\pi+\frac{\pi}{3}}|\cos t|\sin\left(t - \frac{\pi}{3}\right)\mathrm{d}t.\quad(\text{代换：}t = \theta + \frac{\pi}{3})$$
> 根据周期函数的积分性质，得
> $$I = -8\int_{-\pi}^{\pi}|\cos t|\sin\left(t - \frac{\pi}{3}\right)\mathrm{d}t = -4\int_{-\pi}^{\pi}|\cos t|\left(\sin t - \sqrt{3}\cos t\right)\mathrm{d}t = 8\sqrt{3}\int_0^{\pi}|\cos t|\cos t\,\mathrm{d}t.$$
> ……（4 分）
>
> 令 $u = t - \dfrac{\pi}{2}$，则
> $$I = -8\sqrt{3}\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}|\sin u|\sin u\,\mathrm{d}u = 0.$$
> ……（4 分）

---

## 六、（本题满分 12 分）

证明 $f(n) = \displaystyle\sum_{m=1}^n\int_0^m\cos\frac{2\pi n[x+1]}{m}\,\mathrm{d}x$ 等于 $n$ 的所有因子（包括 1 和 $n$ 本身）之和，其中 $[x+1]$ 表示不超过 $x+1$ 的最大整数，并计算 $f(2021)$。

> **【解】**
> $$\int_0^m\cos\frac{2\pi n[x+1]}{m}\,\mathrm{d}x = \sum_{k=1}^m\int_{k-1}^k\cos\frac{2\pi n[x+1]}{m}\,\mathrm{d}x = \sum_{k=1}^m\int_{k-1}^k\cos\frac{2\pi nk}{m}\,\mathrm{d}x = \sum_{k=1}^m\cos k\frac{2\pi n}{m}.$$
> ……（4 分）
>
> 如果 $m$ 是 $n$ 的因子，那么 $\displaystyle\int_0^m\cos\frac{2\pi n[x+1]}{m}\,\mathrm{d}x = m$；否则，根据三角恒等式
> $$\sum_{k=1}^m\cos kt = \cos\frac{m+1}{2}t\cdot\frac{\sin\frac{mt}{2}}{\sin\frac{t}{2}},$$
> 有
> $$\int_0^m\cos\frac{2\pi n[x+1]}{m}\,\mathrm{d}x = \cos\left(\frac{m+1}{2}\cdot\frac{2\pi n}{m}\right)\cdot\frac{\sin\left(\frac{m}{2}\cdot\frac{2\pi n}{m}\right)}{\sin\frac{2\pi n}{2m}} = 0,$$
> 因此得证。……（5 分）
>
> 由此可得
> $$f(2021) = 1 + 43 + 47 + 2021 = 2112.$$
> ……（3 分）

---

## 七、（本题满分 14 分）

设 $u_n = \displaystyle\int_0^1\frac{\mathrm{d}t}{(1+t^4)^n}$（$n\geq 1$）。

（1）证明数列 $\{u_n\}$ 收敛，并求极限 $\lim\limits_{n\to\infty}u_n$；

（2）证明级数 $\displaystyle\sum_{n=1}^\infty(-1)^nu_n$ 条件收敛；

（3）证明当 $p\geq 1$ 时级数 $\displaystyle\sum_{n=1}^\infty\frac{u_n}{n^p}$ 收敛，并求级数 $\displaystyle\sum_{n=1}^\infty\frac{u_n}{n}$ 的和。

> **【解】**（1）对任意 $\varepsilon > 0$，取 $0 < a < \dfrac{\varepsilon}{2}$，将积分区间分成两段，得
> $$u_n = \int_0^1\frac{\mathrm{d}t}{(1+t^4)^n} = \int_0^a\frac{\mathrm{d}t}{(1+t^4)^n} + \int_a^1\frac{\mathrm{d}t}{(1+t^4)^n}.$$
> 因为
> $$\int_a^1\frac{\mathrm{d}t}{(1+t^4)^n} \leq \frac{1-a}{(1+a^4)^n} < \frac{1}{(1+a^4)^n}\to 0\quad(n\to\infty),$$
> 所以存在正整数 $N$，当 $n > N$ 时，$\displaystyle\int_a^1\frac{\mathrm{d}t}{(1+t^4)^n} < \frac{\varepsilon}{2}$，从而
> $$0 \leq u_n < a + \int_a^1\frac{\mathrm{d}t}{(1+t^4)^n} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon,$$
> 所以 $\lim\limits_{n\to\infty}u_n = 0$。……（4 分）
>
> （2）显然 $0 < u_{n+1} = \displaystyle\int_0^1\frac{\mathrm{d}t}{(1+t^4)^{n+1}} \leq \int_0^1\frac{\mathrm{d}t}{(1+t^4)^n} = u_n$，即 $u_n$ 单调递减，又 $\lim\limits_{n\to\infty}u_n = 0$，故由莱布尼兹判别法知，$\displaystyle\sum_{n=1}^\infty(-1)^nu_n$ 收敛。……（3 分）
>
> 另一方面，当 $n\geq 2$ 时，有
> $$u_n = \int_0^1\frac{\mathrm{d}t}{(1+t^4)^n} \geq \int_0^1\frac{\mathrm{d}t}{(1+t)^n} = \frac{1}{n-1}\left(1-2^{1-n}\right),$$
> 由于 $\displaystyle\sum_{n=2}^\infty\frac{1}{n-1}$ 发散，$\displaystyle\sum_{n=2}^\infty\frac{1}{n-1}\frac{1}{2^{n-1}}$ 收敛，所以 $\displaystyle\sum_{n=2}^\infty\frac{1}{n-1}\left(1-\frac{1}{2^{n-1}}\right)$ 发散，从而 $\displaystyle\sum_{n=1}^\infty u_n$ 发散。因此 $\displaystyle\sum_{n=1}^\infty(-1)^nu_n$ 条件收敛。……（3 分）
>
> （3）先求级数 $\displaystyle\sum_{n=1}^\infty\frac{u_n}{n}$ 的和。因为
> $$u_n = \int_0^1\frac{\mathrm{d}t}{(1+t^4)^n} = \left.\frac{t}{(1+t^4)^n}\right|_0^1 + n\int_0^1\frac{4t^4}{(1+t^4)^{n+1}}\,\mathrm{d}t = \frac{1}{2^n} + 4n\int_0^1\frac{t^4}{(1+t^4)^{n+1}}\,\mathrm{d}t$$
> $$= \frac{1}{2^n} + 4n\int_0^1\frac{1+t^4-1}{(1+t^4)^{n+1}}\,\mathrm{d}t = \frac{1}{2^n} + 4n\left(u_n - u_{n+1}\right),$$
> 所以
> $$\sum_{n=1}^\infty\frac{u_n}{n} = \sum_{n=1}^\infty\frac{1}{n2^n} + 4\sum_{n=1}^\infty\left(u_n - u_{n+1}\right) = \sum_{n=1}^\infty\frac{1}{n2^n} + 4u_1.$$
> 利用展开式 $\ln(1+x) = \displaystyle\sum_{n=1}^\infty(-1)^{n-1}\frac{x^n}{n}$，取 $x = -\dfrac{1}{2}$，得 $\displaystyle\sum_{n=1}^\infty\frac{1}{n2^n} = \ln 2$。而
> $$u_1 = \int_0^1\frac{\mathrm{d}t}{1+t^4} = \frac{\sqrt{2}}{8}\left[\pi + 2\ln\left(1+\sqrt{2}\right)\right].$$
> 因此
> $$\sum_{n=1}^\infty\frac{u_n}{n} = \ln 2 + \frac{\sqrt{2}}{2}\left[\pi + 2\ln\left(1+\sqrt{2}\right)\right].$$
> 最后，当 $p\geq 1$ 时，因为 $\dfrac{u_n}{n^p} \leq \dfrac{u_n}{n}$，且 $\displaystyle\sum_{n=1}^\infty\frac{u_n}{n}$ 收敛，所以 $\displaystyle\sum_{n=1}^\infty\frac{u_n}{n^p}$ 收敛。……（4 分）

---

## 附：本卷考点分布速览

| 题号 | 分值 | 考点板块 | 具体考点 |
|---|---|---|---|
| 一【1】 | 6 | 极限 | 等价无穷小替换 + 洛必达法则 |
| 一【2】 | 6 | 高阶导数 | 莱布尼茨（Leibniz）求导公式 |
| 一【3】 | 6 | 隐函数求导 | 方程两端求导 + 切线方程 |
| 一【4】 | 6 | 广义（反常）积分 | 换元 + 化归为 $\int\frac{\sin x}{x}\mathrm{d}x$ 型积分求值 |
| 一【5】 | 6 | 极限 | 幂指函数极限 + 等价无穷小替换 |
| 二 | 10 | 数列极限 | 递推数列取倒数 + 递推求和 + 与 $e$ 的级数表示联系 |
| 三 | 10 | 中值定理 | 介值定理 + 拉格朗日中值定理（双中值） |
| 四 | 12 | 多元微分学 | 复合函数一阶/二阶偏导 + 抽象函数化为微分方程求解 |
| 五 | 12 | 曲线积分 | 第二类曲线积分（含绝对值）+ 参数化 + 周期函数积分性质 |
| 六 | 12 | 定积分与初等数论 | 取整函数积分 + 三角和恒等式 + 因数求和（2021 = 43×47） |
| 七 | 14 | 含参积分与级数 | 含参变量积分极限 + 交错级数条件收敛（Leibniz 判别法）+ 分部积分求和 |
