<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC14%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6%E7%B1%BB-%E5%88%9D%E8%B5%9B-2022.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第十四届全国大学生数学竞赛初赛试题及参考答案（非数学类）

> **年份**：2022 年（第十四届）｜**类别**：非数学专业（非数学类）
> **考试日期**：2022 年 11 月 12 日（卷面副标题标注）｜**考试形式**：闭卷｜**时间**：150 分钟（按竞赛通用设置，卷面未标注）｜**满分**：100 分
> **来源**：扫描版 PDF（页面含 cmathc.org.cn 水印；页眉"2022 年 11 月初赛试题及解答(非数学类)"）｜原始文件：`../第十四届全国大学生数学竞赛初赛（非数学类）试题及参考答案.pdf`
> **转录说明**：原卷为扫描版，本文件由视觉逐页转写，公式采用 KaTeX 语法；正文【解】【证】为原卷参考答案的逐字转写，其中行尾"------ N 分"为原卷评分点标注；填空题"答案"为据原卷【解】归纳的结果。

---

## 卷面结构

| 题号 | 一 | 二 | 三 | 四 | 五 | 六 | 总分 |
|---|---|---|---|---|---|---|---|
| 满分 | 30 | 14 | 14 | 14 | 14 | 14 | 100 |
| 形式 | 填空题 ×5 | 解答题 | 解答题 | 解答题 | 解答题 | 解答题 | |

---

## 一、填空题（本题满分 30 分，每小题 6 分）

**(1)** 极限 $\lim\limits_{x\to 0}\dfrac{1-\sqrt{1-x^2}\cos x}{1+x^2-\cos^2 x} = \underline{\qquad}$。

> **答案**：$\dfrac{1}{2}$
>
> **【解】** 利用洛必达法则，得
> 原式 $= \lim\limits_{x\to 0}\dfrac{\sqrt{1-x^2}\sin x + \dfrac{x\cos x}{\sqrt{1-x^2}}}{2x+2\cos x\sin x} = \lim\limits_{x\to 0}\dfrac{\sqrt{1-x^2}\cdot\dfrac{\sin x}{x} + \dfrac{\cos x}{\sqrt{1-x^2}}}{2+2\dfrac{\sin x}{x}\cdot\cos x} = \dfrac{1}{2}$。

**(2)** 设 $f(x) = \begin{cases}1, & x>0, \\ 0, & x\le 0,\end{cases}$ $g(x) = \begin{cases}x-1, & x\ge 1, \\ 1-x, & x<1,\end{cases}$ 则复合函数 $f[g(x)]$ 的间断点为 $x = \underline{\qquad}$。

> **答案**：$x = 1$
>
> **【解】** 显然，复合函数 $f[g(x)] = \begin{cases}1, & g(x)>0, \\ 0, & g(x)\le 0,\end{cases} = \begin{cases}1, & x\ne 1, \\ 0, & x=1,\end{cases}$ 所以 $f[g(x)]$ 的惟一间断点为 $x = 1$。

**(3)** 极限 $\lim\limits_{x\to 1^-}(1-x)^3\sum\limits_{n=1}^{\infty}n^2x^n = \underline{\qquad}$。

> **答案**：$2$
>
> **【解】** 易知，$\sum\limits_{n=1}^{\infty}n^2x^n$ 的和函数为：$\sum\limits_{n=1}^{\infty}n^2x^n = \dfrac{x^2+x}{(1-x)^3}$，$|x|<1$，所以
> $$\lim_{x\to 1^-}(1-x)^3\sum_{n=1}^{\infty}n^2x^n = \lim_{x\to 1^-}(x^2+x) = 2.$$

**(4)** 微分方程 $\dfrac{\mathrm{d}y}{\mathrm{d}x}x\ln x\sin y + \cos y(1-x\cos y) = 0$ 的通解为 $\underline{\qquad}$。

> **答案**：$(x+C)\cos y = \ln x$
>
> **【解】** 原方程等价于 $\dfrac{\mathrm{d}y}{\mathrm{d}x}\sin y + \dfrac{1}{x\ln x}\cos y = \dfrac{1}{\ln x}\cos^2 y$。令 $u = \cos y$，则方程可化为 $\dfrac{\mathrm{d}u}{\mathrm{d}x} - \dfrac{1}{x\ln x}u = -\dfrac{1}{\ln x}u^2$。再令 $w = \dfrac{1}{u}$，则方程可进一步化为 $\dfrac{\mathrm{d}w}{\mathrm{d}x} + \dfrac{1}{x\ln x}w = \dfrac{1}{\ln x}$。这是一阶线性微分方程，利用求解公式得
> $$w = e^{-\int\frac{\mathrm{d}x}{x\ln x}}\left(\int\frac{1}{\ln x}e^{\int\frac{\mathrm{d}x}{x\ln x}}\mathrm{d}x + C\right) = \frac{1}{\ln x}(x+C).$$
> 将变量 $w = \dfrac{1}{u} = \dfrac{1}{\cos y}$ 代回，得
> $$(x+C)\cos y = \ln x.$$

**(5)** 记 $D = \left\{(x,y)\,\middle|\,0\le x+y\le\dfrac{\pi}{2},\,0\le x-y\le\dfrac{\pi}{2}\right\}$，则
$$\iint_D y\sin(x+y)\,\mathrm{d}x\mathrm{d}y = \underline{\qquad}.$$

> **答案**：$\dfrac{\pi}{8} - \dfrac{\pi^2}{32}$
>
> **【解】**（方法 1）利用三角公式：$\sin(x+y) = \sin x\cos y + \cos x\sin y$，并根据重积分的对称性，得
> 原式 $= 2\displaystyle\int_0^{\frac{\pi}{4}}y\sin y\,\mathrm{d}y\int_y^{\frac{\pi}{2}-y}\cos x\,\mathrm{d}x = 2\int_0^{\frac{\pi}{4}}y\sin y(\cos y-\sin y)\,\mathrm{d}y$
> $$= \int_0^{\frac{\pi}{4}}y\sin 2y\,\mathrm{d}y + \int_0^{\frac{\pi}{4}}y\cos 2y\,\mathrm{d}y - \int_0^{\frac{\pi}{4}}y\,\mathrm{d}y$$
> $$= \frac{1}{4} + \left(\frac{\pi}{8}-\frac{1}{4}\right) - \frac{\pi^2}{32} = \frac{\pi}{8} - \frac{\pi^2}{32}.$$
>
> （方法 2）利用二元变量替换，令 $\begin{cases}u = x+y, \\ v = x-y,\end{cases}$ 则 $\begin{cases}x = \dfrac{1}{2}(u+v) \\ y = \dfrac{1}{2}(u-v)\end{cases}$。因为
> $$J = \begin{vmatrix}\dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\[6pt] \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v}\end{vmatrix} = \begin{vmatrix}\dfrac{1}{2} & \dfrac{1}{2} \\[6pt] \dfrac{1}{2} & -\dfrac{1}{2}\end{vmatrix} = -\frac{1}{2},$$
> 所以
> 原式 $= |J|\displaystyle\int_0^{\frac{\pi}{2}}\int_0^{\frac{\pi}{2}}\frac{1}{2}(u-v)\sin u\,\mathrm{d}u\mathrm{d}v = \frac{1}{4}\int_0^{\frac{\pi}{2}}\mathrm{d}v\int_0^{\frac{\pi}{2}}u\sin u\,\mathrm{d}u - \frac{1}{4}\int_0^{\frac{\pi}{2}}v\,\mathrm{d}v\int_0^{\frac{\pi}{2}}\sin u\,\mathrm{d}u$
> $$= \frac{1}{4}\times\frac{\pi}{2}\times 1 - \frac{1}{4}\times\frac{\pi^2}{8}\times 1 = \frac{\pi}{8} - \frac{\pi^2}{32}.$$

---

## 二、（本题满分 14 分）

记向量 $\overrightarrow{OA}$ 与 $\overrightarrow{OB}$ 的夹角为 $\alpha$，$|\overrightarrow{OA}| = 1$，$|\overrightarrow{OB}| = 2$，$\overrightarrow{OP} = (1-\lambda)\overrightarrow{OA}$，$\overrightarrow{OQ} = \lambda\overrightarrow{OB}$，$0\le\lambda\le 1$。

**(1)** 问当 $\lambda$ 为何值时，$|\overrightarrow{PQ}|$ 取得最小值；

**(2)** 设（1）中的 $\lambda$ 满足 $0 < \lambda < \dfrac{1}{5}$，求夹角 $\alpha$ 的取值范围。

> **【解】**（1）根据余弦定理，并注意到 $0\le\alpha\le\pi$，得
> $$f(\lambda) = |\overrightarrow{PQ}|^2 = (1-\lambda)^2 + 4\lambda^2 - 4\lambda(1-\lambda)\cos\alpha$$
> $$= (5+4\cos\alpha)\lambda^2 - 2(1+2\cos\alpha)\lambda + 1$$
> $$= (5+4\cos\alpha)\left(\lambda - \frac{1+2\cos\alpha}{5+4\cos\alpha}\right)^2 + 1 - \frac{(1+2\cos\alpha)^2}{5+4\cos\alpha},$$
> 因此，当 $\lambda = \dfrac{1+2\cos\alpha}{5+4\cos\alpha}$ 时，$0\le\lambda\le 1$，$|\overrightarrow{PQ}|$ 取得最小值。 ------ 6 分
>
> （2）令 $y = \cos\alpha$，则 $\lambda = \dfrac{1+2y}{5+4y}$ 的反函数为 $g(\lambda) = -\dfrac{1}{2}\times\dfrac{5\lambda-1}{2\lambda-1}$。易知 $g(\lambda)$ 在 $\left(0,\ \dfrac{1}{5}\right)$ 单调增加，其值域为 $\left(-\dfrac{1}{2},\ 0\right)$，所以 $-\dfrac{1}{2} < \cos\alpha < 0$，注意到 $\cos\alpha$ 在 $[0,\pi]$ 上单调减，解得 $\dfrac{\pi}{2} < \alpha < \dfrac{2\pi}{3}$，即夹角 $\alpha$ 的取值范围为 $\left(\dfrac{\pi}{2},\ \dfrac{2\pi}{3}\right)$。 ------ 8 分

---

## 三、（本题满分 14 分）

设函数 $f(x)$ 在 $(-1,1)$ 上二阶可导，$f(0) = 1$，且当 $x\ge 0$ 时，$f(x)\ge 0$，$f'(x)\le 0$，$f''(x)\le f(x)$，证明：$f'(0)\ge -\sqrt{2}$。

> **【证】** 任取 $x\in(0,1)$，对 $f(x)$ 在 $[0,x]$ 上利用 Lagrange 中值定理，存在 $\xi\in(0,1)$，使得 $f(x)-f(0) = xf'(\xi)$。因为 $f(0) = 1$，$f(x)\ge 0\ (x>0)$，所以
> $$-\frac{1}{x}\le f'(\xi)\le 0.$$
> ------ 5 分
>
> 令 $F(x) = [f'(x)]^2 - [f(x)]^2$，则 $F(x)$ 在 $(0,1)$ 内可导，且
> $$F'(x) = 2f'(x)\left[f''(x)-f(x)\right].$$
> 根据题设条件，当 $x\ge 0$ 时，$f'(x)\le 0$，$f''(x)\le f(x)$，所以 $F'(x)\ge 0$。这表明 $F(x)$ 在 $[0,1]$ 上单调增加，从而有 $F(\xi)\ge F(0)$，可得
> $$[f'(\xi)]^2 - [f'(0)]^2 \ge [f(\xi)]^2 - [f(0)]^2 \ge -1,$$
> 因此 $[f'(0)]^2 \le [f'(\xi)]^2 + 1 \le 1 + \dfrac{1}{x^2}$。 ------ 7 分
>
> 由于 $\lim\limits_{x\to 1^-}\left(1+\dfrac{1}{x^2}\right) = 2$，所以 $[f'(0)]^2\le 2$，从而有 $f'(0)\ge -\sqrt{2}$。 ------ 2 分

---

## 四、（本题满分 14 分）

证明：对任意正整数 $n$，恒有：
$$\int_0^{\frac{\pi}{2}}x\left(\frac{\sin nx}{\sin x}\right)^4\mathrm{d}x \le \left(\frac{n^2}{4}-\frac{1}{8}\right)\pi^2.$$

> **【证】** 首先，利用归纳法易证：对 $n\ge 1$，$|\sin nx|\le n\sin x$（$0\le x\le \dfrac{\pi}{2}$）。 ------ 2 分
>
> 又由于 $|\sin nx|\le 1$，及 $\sin x\ge \dfrac{2}{\pi}x$（$0\le x\le \dfrac{\pi}{2}$）， ------ 2 分
>
> 所以当 $n>1$ 时，得
> $$\int_0^{\frac{\pi}{2}}x\left(\frac{\sin nx}{\sin x}\right)^4\mathrm{d}x = \int_0^{\frac{\pi}{2n}}x\left(\frac{\sin nx}{\sin x}\right)^4\mathrm{d}x + \int_{\frac{\pi}{2n}}^{\frac{\pi}{2}}x\left(\frac{\sin nx}{\sin x}\right)^4\mathrm{d}x$$
> $$\le n^4\int_0^{\frac{\pi}{2n}}x\,\mathrm{d}x + \int_{\frac{\pi}{2n}}^{\frac{\pi}{2}}x\left(\frac{1}{2x/\pi}\right)^4\mathrm{d}x = \frac{n^4}{2}\left(\frac{\pi}{2n}\right)^2 + \frac{\pi^4}{16}\int_{\frac{\pi}{2n}}^{\frac{\pi}{2}}\frac{\mathrm{d}x}{x^3}$$
> $$= \frac{n^2\pi^2}{8} + \frac{\pi^4}{16}\cdot\left.\frac{1}{(-2x^2)}\right|_{\frac{\pi}{2n}}^{\frac{\pi}{2}} = \frac{n^2\pi^2}{8} - \frac{\pi^4}{16}\left(\frac{2}{\pi^2}-\frac{2n^2}{\pi^2}\right) = \left(\frac{n^2}{4}-\frac{1}{8}\right)\pi^2.$$
> ------ 8 分
>
> 当 $n = 1$ 时，$\displaystyle\int_0^{\frac{\pi}{2}}x\,\mathrm{d}x = \frac{\pi^2}{8}$，等号成立。 ------ 2 分

---

## 五、（本题满分 14 分）

设 $z = f(x,y)$ 是区域 $D = \{(x,y)\mid 0\le x\le 1,\,0\le y\le 1\}$ 上的可微函数，$f(0,0) = 0$，且 $\mathrm{d}z\big|_{(0,0)} = 3\mathrm{d}x + 2\mathrm{d}y$，求极限
$$\lim_{x\to 0^+}\frac{\displaystyle\int_0^{x^2}\mathrm{d}t\int_x^{\sqrt{t}}f(t,u)\,\mathrm{d}u}{1-\sqrt[4]{1-x^4}}.$$

> **【解】** 交换二次积分的次序，得
> $$\int_0^{x^2}\mathrm{d}t\int_x^{\sqrt{t}}f(t,u)\,\mathrm{d}u = -\int_0^x\mathrm{d}u\int_0^{u^2}f(t,u)\,\mathrm{d}t.$$
> ------ 3 分
>
> 由于 $f(x,y)$ 在 $D$ 上可微，所以 $f(x,y)$ 在点 $(0,0)$ 的半径为 1 的扇形域内连续，从而 $\varphi(u) = \displaystyle\int_0^{u^2}f(t,u)\,\mathrm{d}t$ 在 $u = 0$ 的某邻域内连续，因此
> $$I = \lim_{x\to 0^+}\frac{\displaystyle\int_0^{x^2}\mathrm{d}t\int_x^{\sqrt{t}}f(t,u)\,\mathrm{d}u}{1-\sqrt[4]{1-x^4}} = \lim_{x\to 0^+}\frac{-\displaystyle\int_0^x\varphi(u)\,\mathrm{d}u}{\dfrac{x^4}{4}} = -\lim_{x\to 0^+}\frac{\varphi(x)}{x^3} = -\lim_{x\to 0^+}\frac{\displaystyle\int_0^{x^2}f(t,x)\,\mathrm{d}t}{x^3}$$
> $$= -\lim_{x\to 0^+}\frac{f(\xi,x)x^2}{x^3} = -\lim_{x\to 0^+}\frac{f(\xi,x)}{x},\qquad 0<\xi<x^2.$$
> ------ 6 分
>
> 因为 $\mathrm{d}z\big|_{(0,0)} = 3\mathrm{d}x + 2\mathrm{d}y$，所以 $f_x(0,0) = 3$，$f_y(0,0) = 2$。又 $f(0,0) = 0$，于是
> $$f(\xi,x) = f(0,0) + f_x(0,0)\xi + f_y(0,0)x + o\left(\sqrt{\xi^2+x^2}\right) = 3\xi + 2x + o\left(\sqrt{\xi^2+x^2}\right).$$
> 注意到 $0 < \dfrac{\xi}{x} < x$，故由夹逼准则知 $\lim\limits_{x\to 0^+}\dfrac{\xi}{x} = 0$，从而
> $$\lim_{x\to 0^+}\frac{o\left(\sqrt{\xi^2+x^2}\right)}{x} = \lim_{x\to 0^+}\frac{o\left(\sqrt{\xi^2+x^2}\right)}{\sqrt{\xi^2+x^2}}\cdot\sqrt{1+\left(\frac{\xi}{x}\right)^2} = 0.$$
> 所以
> $$I = -\lim_{x\to 0^+}\frac{f(\xi,x)}{x} = -\lim_{x\to 0^+}\frac{3\xi + 2x + o\left(\sqrt{\xi^2+x^2}\right)}{x} = -2.$$
> ------ 5 分

---

## 六、（本题满分 14 分）

设正项级数 $\sum\limits_{n=1}^{\infty}a_n$ 收敛，证明：存在收敛的正项级数 $\sum\limits_{n=1}^{\infty}b_n$，使得 $\lim\limits_{n\to\infty}\dfrac{a_n}{b_n} = 0$。

> **【证】** 因为 $\sum\limits_{n=1}^{\infty}a_n$ 收敛，所以 $\forall\varepsilon>0$，存在 $N\in\mathbf{N}$，使得当 $n>N$ 时 $\sum\limits_{k=n}^{\infty}a_k<\varepsilon$。
>
> 特别，对 $k = 1,2,\cdots$，取 $\varepsilon = \dfrac{1}{3^k}$，则存在 $1 < n_1 < n_2 < \cdots < n_{k-1} < n_k$，使得 $\sum\limits_{l=n_k}^{\infty}a_l < \dfrac{1}{3^k}$。 ------ 4 分
>
> 构造 $\{b_n\}$ 如下：当 $1\le n < n_1$ 时，$b_n = a_n$；当 $n_k\le n < n_{k+1}$ 时，$b_n = 2^ka_n$，$k = 1,2,\cdots$。 ------ 5 分
>
> 显然，当 $n\to\infty$ 时，$k\to\infty$，且
> $$\lim_{n\to\infty}\frac{a_n}{b_n} = \lim_{k\to\infty}\frac{a_n}{2^ka_n} = \lim_{k\to\infty}\frac{1}{2^k} = 0.$$
> 此时，有
> $$\sum_{n=1}^{\infty}b_n = \sum_{n=1}^{n_1-1}a_n + \sum_{l=n_1}^{n_2-1}2a_l + \sum_{l=n_2}^{n_3-1}2^2a_l + \cdots$$
> $$\le \sum_{n=1}^{n_1-1}a_n + 2\cdot\frac{1}{3} + 2^2\cdot\left(\frac{1}{3}\right)^2 + \cdots$$
> $$= \sum_{n=1}^{n_1-1}a_n + \sum_{k=1}^{\infty}\frac{2^k}{3^k} = \sum_{n=1}^{n_1-1}a_n + 2 < +\infty$$
> 因此，正项级数 $\sum\limits_{n=1}^{\infty}b_n$ 收敛。 ------ 5 分

---

## 附：本卷考点分布速览

| 题号 | 分值 | 考点板块 | 具体考点 |
|---|---|---|---|
| 一(1) | 6 | 极限 | 洛必达法则（含根式求导、凑 $\frac{\sin x}{x}$） |
| 一(2) | 6 | 函数 | 分段函数复合的间断点判定 |
| 一(3) | 6 | 级数 | 幂级数求和函数后求单侧极限 |
| 一(4) | 6 | 常微分方程 | 伯努利方程（两次换元化为一阶线性方程）求通解 |
| 一(5) | 6 | 二重积分 | 三角公式 + 对称性 / 变量替换（雅可比行列式） |
| 二 | 14 | 向量代数与最值 | 余弦定理建模 + 二次函数配方求最值 + 反函数 + 三角函数范围 |
| 三 | 14 | 微分中值定理 | Lagrange 中值定理 + 构造辅助函数 $F=[f']^2-[f]^2$ 证不等式 |
| 四 | 14 | 定积分不等式 | 归纳法 + 积分估计放缩（$\sin x\ge\frac{2}{\pi}x$） |
| 五 | 14 | 多元微分与极限 | 交换积分次序 + 全微分定义（可微展开）+ 积分中值定理 |
| 六 | 14 | 级数 | 正项级数收敛的构造性证明（尾部收敛构造 $b_n=2^ka_n$） |
