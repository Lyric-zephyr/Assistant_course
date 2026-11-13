<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC13%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6%E7%B1%BB-%E5%88%9D%E8%B5%9B%E8%A1%A5%E8%B5%9B-2021.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第十三届全国大学生数学竞赛初赛补赛试题及参考答案（非数学类，2021 年）

> **年份**：2021 年（第十三届，初赛补赛卷）｜**类别**：非数学类
> **考试形式**：闭卷｜**时间**：150 分钟（按历届初赛通则；本卷面未标注）｜**满分**：100 分
> **来源**：大学生数学竞赛网（www.cmathc.org.cn）扫描版转载｜原始文件：`../第十三届全国大学生数学竞赛初赛（非数学类）补赛试题及参考答案.pdf`
> **转录说明**：原卷为扫描版，本文件由视觉逐页转写，公式采用 KaTeX 语法；本卷题面即印有参考答案（答案写在题面下划线上，本文以 $\underline{\ }$ 标注），「解答」为原卷【解】/【证】全文，评分标注（如"6 分"）为原卷评分点，均照录。

---

## 卷面结构

| 题号 | 一 | 二 | 三 | 四 | 五 | 六 | 总分 |
|---|---|---|---|---|---|---|---|
| 满分 | 30 | 14 | 14 | 14 | 14 | 14 | 100 |
| 形式 | 填空题 ×5（每小题 6 分） | 解答题 | 解答题 | 解答题 | 解答题 | 解答题 | |

---

## 一、填空题（本题满分 30 分，每小题 6 分）

**1、** 设 $x_0 = 1$，$x_n = \ln(1 + x_{n-1})\ (n \ge 1)$，则 $\lim\limits_{n\to+\infty} nx_n = \underline{2}$。

> **解答**：【解】 $x_n \in (0,1)$ 单调减少且 $\lim\limits_{n\to+\infty} x_n = 0$。由 Stolz 定理，得
> $$\lim_{n\to+\infty}\frac{1}{nx_n} = \lim_{n\to+\infty}\left(\frac{1}{x_{n+1}} - \frac{1}{x_n}\right) = \lim_{n\to+\infty}\frac{x_n - x_{n+1}}{x_nx_{n+1}}$$
> $$= \lim_{n\to+\infty}\frac{x_n - \ln(1+x_n)}{x_n\ln(1+x_n)} = \lim_{n\to+\infty}\frac{x_n - \left[x_n - \dfrac{1}{2}x_n^2 + o(x_n^2)\right]}{x_n^2} = \frac{1}{2}.$$

**2、** 积分 $\displaystyle\int_0^{\frac{\pi}{2}}\frac{\cos x}{1+\tan x}\,\mathrm{d}x = \underline{\dfrac{1}{\sqrt{2}}\ln(1+\sqrt{2})}$。

> **解答**：【解】 作变换 $x = \dfrac{\pi}{2} - t$，则 $\displaystyle\int_0^{\frac{\pi}{2}}\frac{\cos x}{1+\tan x}\mathrm{d}x = \int_0^{\frac{\pi}{2}}\frac{\sin t}{1+\cot t}\mathrm{d}t = \int_0^{\frac{\pi}{2}}\frac{\sin x}{1+\cot x}\mathrm{d}x$。
> 于是
> $$\int_0^{\frac{\pi}{2}}\frac{\cos x}{1+\tan x}\mathrm{d}x = \frac{1}{2}\left(\int_0^{\frac{\pi}{2}}\frac{\cos x}{1+\tan x}\mathrm{d}x + \int_0^{\frac{\pi}{2}}\frac{\sin x}{1+\cot x}\mathrm{d}x\right)$$
> $$= \frac{1}{2}\int_0^{\frac{\pi}{2}}\frac{1}{\cos x + \sin x}\mathrm{d}x$$
> $$= \frac{1}{2\sqrt{2}}\int_0^{\frac{\pi}{2}}\frac{1}{\sin\left(x + \frac{\pi}{4}\right)}\mathrm{d}x = \frac{1}{2\sqrt{2}}\int_0^{\frac{\pi}{2}}\csc\left(x + \frac{\pi}{4}\right)\mathrm{d}x$$
> $$= \frac{1}{2\sqrt{2}}\int_0^{\frac{\pi}{2}}\csc\left(x + \frac{\pi}{4}\right)\mathrm{d}\left(x + \frac{\pi}{4}\right)$$
> $$= \frac{1}{2\sqrt{2}}\ln\left[\csc\left(x + \frac{\pi}{4}\right) - \cot\left(x + \frac{\pi}{4}\right)\right]\Big|_0^{\frac{\pi}{2}}$$
> $$= \frac{1}{\sqrt{2}}\ln(1+\sqrt{2}).$$

**3、** 已知直线 $L$：$\begin{cases}2x - 4y + z = 0\\ 3x - y - 2z = 9\end{cases}$ 和平面 $\pi$：$4x - y + z = 1$，则直线 $L$ 在平面 $\pi$ 上的投影直线方程为 $\begin{cases}\underline{17x+31y-37z=117}\\ \underline{4x-y+z=1}\end{cases}$。

> **解答**：【解】 所求投影直线为过 $L$ 且垂直于 $\pi$ 的平面 $\pi_1$ 与 $\pi$ 的交线，因此需要先求出过 $L$ 且垂直于 $\pi$ 的平面 $\pi_1$ 的方程.
> 过 $L$ 的平面束方程为
> $$\lambda(2x - 4y + z) + \mu(3x - y - 2z - 9) = 0,$$
> 即
> $$(2\lambda + 3\mu)x - (4\lambda + \mu)y + (\lambda - 2\mu)z - 9\mu = 0 \qquad \cdots\cdots\cdots\cdots\cdots\cdots\cdots (1)$$
> 平面 $\pi$ 的法向量为
> $$\vec{n} = (4,\ -1,\ 1).$$
> 因平面 $\pi_1$ 与平面 $\pi$ 垂直，则必须有
> $$4(2\lambda + 3\mu) + (-1)(-4\lambda - \mu) + 1\cdot(\lambda - 2\mu) = 0$$
> 解之，得
> $$\frac{\lambda}{\mu} = -\frac{11}{13},$$
> 由 (1)，得到平面 $\pi_1$ 的方程
> $$17x + 31y - 37z - 117 = 0.$$
> 故所求投影直线为
> $$\begin{cases}17x + 31y - 37z - 117 = 0\\ 4x - y + z - 1 = 0\end{cases}$$

**4、** $\displaystyle\sum_{n=1}^{+\infty}\arctan\frac{2}{4n^2+4n+1} = \underline{\dfrac{\pi}{2} - \arctan 2}$。

> **解答**：【解】 由 $\tan(\alpha - \beta) = \dfrac{\tan\alpha - \tan\beta}{1 + \tan\alpha\tan\beta}$ 及 $\dfrac{2}{4n^2+4n+1} = \dfrac{(2n+2) - 2n}{1 + 2n(2n+2)}$，得
> $$\arctan\frac{2}{4n^2+4n+1} = \arctan(2n+2) - \arctan(2n).$$
> 故
> $$\sum_{n=1}^{+\infty}\arctan\frac{2}{4n^2+4n+1} = \lim_{N\to+\infty}\sum_{n=1}^{N}\left[\arctan(2n+2) - \arctan(2n)\right]$$
> $$= \lim_{N\to+\infty}\left[\arctan(2N+2) - \arctan 2\right] = \frac{\pi}{2} - \arctan 2.$$

**5、** 微分方程 $\begin{cases}(x+1)\dfrac{\mathrm{d}y}{\mathrm{d}x} + 1 = 2\mathrm{e}^{-y}\\ y(0) = 0\end{cases}$ 的解是 $\underline{\ln\dfrac{2x+1}{x+1}}$。

> **解答**：【解】 方程变形为：$\mathrm{e}^y\dfrac{\mathrm{d}y}{\mathrm{d}x} = -\dfrac{1}{x+1}\mathrm{e}^y + \dfrac{2}{x+1}$，
> 即，$\dfrac{\mathrm{d}\mathrm{e}^y}{\mathrm{d}x} = -\dfrac{1}{x+1}\mathrm{e}^y + \dfrac{2}{x+1}$，
> $$\mathrm{e}^y = \mathrm{e}^{\int\frac{-1}{x+1}\mathrm{d}x}\left[\int\frac{2}{x+1}\mathrm{e}^{-\int\frac{-1}{x+1}\mathrm{d}x}\mathrm{d}x + C\right] = \frac{1}{x+1}\left[\int\frac{2}{x+1}\cdot(x+1)\mathrm{d}x + C\right]$$
> $$= \frac{1}{x+1}[2x + C]$$
> 由 $y(0) = 0$，得到，$C = 1$，
> 所以 $\mathrm{e}^y = \dfrac{2x+1}{x+1}$，故，$y = \ln\dfrac{2x+1}{x+1}$。

---

## 二、（本题满分 14 分）

设 $f(x) = -\dfrac{1}{2}\left(1 + \dfrac{1}{\mathrm{e}}\right) + \displaystyle\int_{-1}^{1}|x - t|\mathrm{e}^{-t^2}\mathrm{d}t$。证明：在区间 $(-1,1)$ 内，$f(x)$ 有且仅有两个实根。

> **解答**：【证】
> $$f(x) = -\frac{1}{2}\left(1 + \frac{1}{\mathrm{e}}\right) + \int_{-1}^{1}|x - t|\mathrm{e}^{-t^2}\mathrm{d}t$$
> $$= -\frac{1}{2}\left(1 + \frac{1}{\mathrm{e}}\right) + \int_{-1}^{x}(x - t)\mathrm{e}^{-t^2}\mathrm{d}t + \int_{x}^{1}(t - x)\mathrm{e}^{-t^2}\mathrm{d}t$$
> $$= -\frac{1}{2}\left(1 + \frac{1}{\mathrm{e}}\right) + x\int_{-1}^{x}\mathrm{e}^{-t^2}\mathrm{d}t - \int_{-1}^{x}t\mathrm{e}^{-t^2}\mathrm{d}t$$
> $$+ \int_{x}^{1}t\mathrm{e}^{-t^2}\mathrm{d}t - x\int_{x}^{1}\mathrm{e}^{-t^2}\mathrm{d}t$$
> $$= -\frac{1}{2}\left(1 + \frac{1}{\mathrm{e}}\right) + x\int_{-1}^{0}\mathrm{e}^{-t^2}\mathrm{d}t + x\int_{0}^{x}\mathrm{e}^{-t^2}\mathrm{d}t + \frac{1}{2}\mathrm{e}^{-t^2}\Big|_{-1}^{x}$$
> $$- \frac{1}{2}\mathrm{e}^{-t^2}\Big|_{x}^{1} + x\int_{1}^{0}\mathrm{e}^{-t^2}\mathrm{d}t + x\int_{0}^{x}\mathrm{e}^{-t^2}\mathrm{d}t$$
> $$= -\frac{1}{2} - \frac{3}{2}\mathrm{e}^{-1} + \mathrm{e}^{-x^2} + x\int_{-1}^{0}\mathrm{e}^{-t^2}\mathrm{d}t$$
> $$+ x\int_{1}^{0}\mathrm{e}^{-t^2}\mathrm{d}t + 2x\int_{0}^{x}\mathrm{e}^{-t^2}\mathrm{d}t$$
> $$= -\frac{1}{2} - \frac{3}{2}\mathrm{e}^{-1} + \mathrm{e}^{-x^2} + 2x\int_{0}^{x}\mathrm{e}^{-t^2}\mathrm{d}t.$$
> ……（6 分）
> 显然，$f(x)$ 是偶函数，所以我们只需考察 $f(x)$ 在 $(0,1)$ 内的零点。由于
> $$f(0) = \frac{1}{2} - \frac{3}{2}\mathrm{e}^{-1} = \frac{\mathrm{e} - 3}{2\mathrm{e}} < 0,$$
> $$f(1) = -\frac{1}{2} - \frac{3}{2}\mathrm{e}^{-1} + \mathrm{e}^{-1} + 2\int_{0}^{1}\mathrm{e}^{-t^2}\mathrm{d}t$$
> $$> -\left(\frac{1}{2} + \frac{1}{2}\mathrm{e}^{-1}\right) + 2\int_{0}^{1}\mathrm{e}^{-t}\mathrm{d}t = \frac{3}{2} - \frac{5}{2}\mathrm{e}^{-1} > 0,$$
> 又 $f(x)$ 在 $[0,1]$ 上连续，由闭区间上连续函数的零点定理，一定存在 $\xi \in (0,1)$，使 $f(\xi) = 0$。
> 由于 $\forall x \in (0,1)$，$f'(x) = 2\displaystyle\int_0^x \mathrm{e}^{-t^2}\mathrm{d}t > 0$，则 $f(x)$ 在 $(0,1)$ 内严格单调递增，所以 $f(x)$ 在 $(0,1)$ 内仅有一个实根。……（6 分）
> 因为 $f(x)$ 是偶函数，它在 $(-1,0)$ 内也仅有一个实根。因此 $f(x)$ 在 $(-1,1)$ 内仅有两个实根。……（2 分）

---

## 三、（本题满分 14 分）

设函数 $f(x,y)$ 在闭区域 $D = \{(x,y) \mid x^2 + y^2 \le 1\}$ 上具有二阶连续偏导数，且 $\dfrac{\partial^2 f}{\partial x^2} + \dfrac{\partial^2 f}{\partial y^2} = x^2 + y^2$，求

$$\lim_{r\to 0^+}\frac{\displaystyle\iint_{x^2+y^2\le r^2}\left(x\frac{\partial f}{\partial x} + y\frac{\partial f}{\partial y}\right)\mathrm{d}x\mathrm{d}y}{(\tan r - \sin r)^2}.$$

> **解答**：【解】 对 $\forall 0 < r \le 1$，设 $D_r := \left\{(x,y) \in R^2 \mid x^2 + y^2 \le r^2\right\}$，由 Green 公式，得
> $$\iint_{D_r}\left(x\frac{\partial f}{\partial x} + y\frac{\partial f}{\partial y}\right)\mathrm{d}x\mathrm{d}y = -\frac{1}{2}\iint_{D_r}(x^2 + y^2)\left(\frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}\right)\mathrm{d}x\mathrm{d}y$$
> $$+ \frac{1}{2}\int_{\partial D_r} -(x^2 + y^2)\frac{\partial f}{\partial y}\mathrm{d}x + (x^2 + y^2)\frac{\partial f}{\partial x}\mathrm{d}y$$
> $$= \frac{r^2}{2}\iint_{D_r}\left(\frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}\right)\mathrm{d}x\mathrm{d}y - \frac{1}{2}\iint_{D_r}(x^2 + y^2)\left(\frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}\right)\mathrm{d}x\mathrm{d}y$$
> $$= \pi r^2\int_0^r s^3\mathrm{d}s - \pi\int_0^r s^5\mathrm{d}s = \frac{\pi}{4}r^6 - \frac{\pi}{6}r^6 = \frac{\pi}{12}r^6.$$
> ……（8 分）
> 因此，由 Taylor 公式，得
> $$\lim_{r\to 0^+}\frac{\displaystyle\iint_{D_r}\left(x\frac{\partial f}{\partial x} + y\frac{\partial f}{\partial y}\right)\mathrm{d}x\mathrm{d}y}{(\tan r - \sin r)^2} = \lim_{r\to 0^+}\frac{\dfrac{\pi}{12}r^6}{\left[\left(r + \dfrac{r^3}{3} + o(r^3)\right) - \left(r - \dfrac{r^3}{3!} + o(r^3)\right)\right]^2}$$
> $$= \lim_{r\to 0^+}\frac{\dfrac{\pi}{12}r^6}{\dfrac{r^6}{4} + o(r^6)} = \frac{1}{3}\pi.$$
> ……（6 分）

---

## 四、（本题满分 14 分）

若对于 $R^3$ 中半空间 $\{(x,y,z) \in R^3 \mid x > 0\}$ 内的任意有向光滑封闭曲面 $S$，都有：

$$\oiint_S xf'(x)\mathrm{d}y\mathrm{d}z + y\left(xf(x) - f'(x)\right)\mathrm{d}z\mathrm{d}x - xz\left(\sin x + f'(x)\right)\mathrm{d}x\mathrm{d}y = 0,$$

其中 $f$ 在 $(0,+\infty)$ 上二阶导数连续且 $\lim\limits_{x\to 0^+} f(x) = \lim\limits_{x\to 0^+} f'(x) = 0$，求 $f(x)$.

> **解答**：【解】 任取一定点 $P(x,y,z) \in \{(x,y,z) \in R^3 \mid x > 0\}$，对任意充分小 $\varepsilon > 0$，以 $P$ 点为中心半径为 $2\varepsilon$ 的有向球面 $S_{2\varepsilon}(P)$ 仍位于此半空间中。记 $B_{\varepsilon}(P)$ 为球面 $S_{\varepsilon}(P)$（取外侧）所围内部开球域。
> 由题设条件及 Gauss 公式，得：
> $$0 = \oiint_{S_{\varepsilon}(P)} xf'(x)\mathrm{d}y\mathrm{d}z + y(xf(x) - f'(x))\mathrm{d}z\mathrm{d}x - xz(\sin x + f'(x))\mathrm{d}x\mathrm{d}y = $$
> $$\iiint_{B_{\varepsilon}(P)}\left[f'(x) + xf''(x) + xf(x) - f'(x) - x\sin x - xf'(x)\right]\mathrm{d}x\mathrm{d}y\mathrm{d}z = $$
> $$\iiint_{B_{\varepsilon}(P)}\left[xf''(x) - xf'(x) + xf(x) - x\sin x\right]\mathrm{d}x\mathrm{d}y\mathrm{d}z = \rho\left[f''(\rho) - f'(\rho) + f(\rho) - \sin\rho\right]\cdot\frac{4}{3}\pi\varepsilon^3,$$
> 其中 $|\rho - x| \le \varepsilon$。
> 由此可得 $f''(\rho) - f'(\rho) + f(\rho) - \sin\rho = 0$。
> 令 $\varepsilon \to 0^+$，由 $f$ 在 $(0,+\infty)$ 上二阶导数连续得
> $$f''(x) - f'(x) + f(x) - \sin x = 0\ (\forall x > 0),$$
> 即
> $$f''(x) - f'(x) + f(x) = \sin x\ (\forall x > 0).$$
> ……（7 分）
> （以上方程也可通过反证法得到）。
> 求解此二阶方程，齐次方程通解为 $\mathrm{e}^{\frac{x}{2}}\left(c_1\cos\frac{\sqrt{3}}{2}x + c_2\sin\frac{\sqrt{3}}{2}x\right)$，非齐次方程特解为 $\cos x$，故可得：
> $$f(x) = \mathrm{e}^{\frac{x}{2}}\left(c_1\cos\frac{\sqrt{3}}{2}x + c_2\sin\frac{\sqrt{3}}{2}x\right) + \cos x, \quad \forall x > 0.$$
> 由 $\lim\limits_{x\to 0^+} f(x) = 0$ 可得：$c_1 = -1$。
> 再由 $\lim\limits_{x\to 0^+} f'(x) = 0$，得
> $$\lim_{x\to 0^+}\left[\frac{\mathrm{e}^{\frac{x}{2}}}{2}\left((c_1 + \sqrt{3}c_2)\cos\frac{\sqrt{3}}{2}x + (c_2 - \sqrt{3}c_1)\sin\frac{\sqrt{3}}{2}x\right) - \sin x\right] = \frac{c_1 + \sqrt{3}c_2}{2} = 0,$$
> 可得：$c_2 = \dfrac{\sqrt{3}}{3}$。
> 因此，$f(x) = \mathrm{e}^{\frac{x}{2}}\left(\dfrac{\sqrt{3}}{3}\sin\dfrac{\sqrt{3}}{2}x - \cos\dfrac{\sqrt{3}}{2}x\right) + \cos x, \quad \forall x > 0.$
> ……（7 分）

---

## 五、（本题满分 14 分）

设 $f(x) = \displaystyle\int_0^x\left(1 - \frac{[u]}{u}\right)\mathrm{d}u$，其中 $[x]$ 表示小于等于 $x$ 的最大整数. 试讨论

$$\int_1^{+\infty}\frac{\mathrm{e}^{f(x)}}{x^p}\cos\left(x^2 - \frac{1}{x^2}\right)\mathrm{d}x$$

的敛散性，其中 $p > 0$。

> **解答**：【解】 $\forall x \ge 1$，
> $$f(x) = \int_0^x\left(1 - \frac{[u]}{u}\right)\mathrm{d}u = \int_0^{[x]}\left(1 - \frac{[u]}{u}\right)\mathrm{d}u + \int_{[x]}^{x}\frac{u - [u]}{u}\mathrm{d}u$$
> $$= \sum_{k=0}^{[x]-1}\int_k^{k+1}\left(1 - \frac{k}{u}\right)\mathrm{d}u + \int_{[x]}^{x}\frac{u - [x]}{u}\mathrm{d}u = [x] - \sum_{k=1}^{[x]-1}k\ln\left(1 + \frac{1}{k}\right) + O\left(\frac{1}{x}\right)$$
> $$= [x] - \sum_{k=1}^{[x]-1}k\left[\frac{1}{k} - \frac{1}{2k^2} + \frac{1}{3k^3} + o\left(\frac{1}{k^3}\right)\right] + O\left(\frac{1}{x}\right) = 1 + \frac{1}{2}\sum_{k=1}^{[x]-1}\frac{1}{k} + O(1)$$
> $$= \frac{1}{2}\ln[x] + \frac{1}{2}\left(\sum_{k=1}^{[x]}\frac{1}{k} - \ln[x]\right) + O(1) = \frac{1}{2}\ln x + O(1).$$
> 故存在 $0 < C_1 \le C_2$，使得
> $$C_1\sqrt{x} \le \mathrm{e}^{f(x)} \le C_2\sqrt{x}, \quad \forall x \ge 1.$$
> ……（4 分）
> 若 $p > \dfrac{3}{2}$，$\left|\dfrac{\mathrm{e}^{f(x)}}{x^p}\cos\left(x^2 - \dfrac{1}{x^2}\right)\right| \le \dfrac{C_2}{x^{p-\frac{1}{2}}}$，故原积分绝对收敛。……（3 分）
> 再考虑 $0 < p \le \dfrac{3}{2}$。首先，注意到
> $$\frac{\mathrm{e}^{f(x)}}{x^p}\cos\left(x^2 - \frac{1}{x^2}\right) = \frac{\mathrm{e}^{f(x)}x^{3-p}}{2(x^4+1)}2\left(x + \frac{1}{x^3}\right)\cos\left(x^2 - \frac{1}{x^2}\right),$$
> 且对任意 $1 \le A < B < +\infty$，成立
> $$\left|\int_A^B 2\left(x + \frac{1}{x^3}\right)\cos\left(x^2 - \frac{1}{x^2}\right)\mathrm{d}x\right| = \left|\left.\sin\left(x^2 - \frac{1}{x^2}\right)\right|_A^B\right| \le 2.$$
> 其次，$\dfrac{\mathrm{e}^{f(x)}x^{3-p}}{x^4+1}$ 单调递减（对 $x$ 充分大）且趋于 $0$（当 $x \to +\infty$）。事实上，$\dfrac{x^{4-p}}{x^4+1}$ 单调递减（对 $x$ 充分大），$\dfrac{\mathrm{e}^{f(x)}}{x} = \mathrm{e}^{\int_0^x\left(1 - \frac{[u]}{u}\right)\mathrm{d}u - \ln x} = \mathrm{e}^{\int_1^x\left(1 - \frac{[u]+1}{u}\right)\mathrm{d}u + 1}$ 在 $[1,+\infty]$ 上单调递减。由 Dirichlet 判别法，原积分收敛。……（4 分）
> 注意到
> $$\left|\frac{\mathrm{e}^{f(x)}}{x^p}\cos\left(x^2 - \frac{1}{x^2}\right)\right| \ge \frac{\mathrm{e}^{f(x)}}{x^p}\cos^2\left(x^2 - \frac{1}{x^2}\right)$$
> $$= \frac{\mathrm{e}^{f(x)}}{2x^p}\left(\cos\left[2\left(x^2 - \frac{1}{x^2}\right)\right] + 1\right).$$
> 类似地可证 $\displaystyle\int_1^{+\infty}\frac{\mathrm{e}^{f(x)}}{x^p}\cos\left[2\left(x^2 - \frac{1}{x^2}\right)\right]\mathrm{d}x$ 收敛，但由于 $\dfrac{\mathrm{e}^{f(x)}}{x^p} \ge \dfrac{C_1}{x}$，故 $\displaystyle\int_1^{+\infty}\frac{\mathrm{e}^{f(x)}}{x^p}\mathrm{d}x$ 发散。因此，原积分当 $0 < p \le \dfrac{3}{2}$ 时条件收敛。……（3 分）

---

## 六、（本题满分 14 分）

设正数列 $\{a_n\}$ 单调减少且趋于零，$f(x) = \displaystyle\sum_{n=1}^{+\infty}a_n^n x^n$。证明：若级数 $\displaystyle\sum_{n=1}^{+\infty}a_n$ 发散，则积分 $\displaystyle\int_1^{+\infty}\frac{\ln f(x)}{x^2}\mathrm{d}x$ 也发散。

> **解答**：【证】 因为级数 $\displaystyle\sum_{n=1}^{\infty}a_n^n x^n$ 的收敛半径 $R = \lim\limits_{n\to\infty}\dfrac{1}{\sqrt[n]{a_n^n}} = \lim\limits_{n\to\infty}\dfrac{1}{a_n} = +\infty$。
> 所以函数 $f(x)$ 的定义域为 $(-\infty,+\infty)$。……（2 分）
> 若 $x \in \left[\dfrac{\mathrm{e}}{a_p},\ \dfrac{\mathrm{e}}{a_{p+1}}\right]$，则当 $k \le p$ 时，$a_kx \ge a_px \ge \mathrm{e}$（因为 $a_n$ 单调减少）。
> 因此，$f(x) \ge \displaystyle\sum_{k=1}^{p}(a_kx)^k \ge \sum_{k=1}^{p}\mathrm{e}^k \ge \mathrm{e}^p$。
> 于是，$\ln f(x) \ge p$，$\left(x \in \left[\dfrac{\mathrm{e}}{a_p},\ \dfrac{\mathrm{e}}{a_{p+1}}\right]\right)$。……（6 分）
> 又因为当 $x \ge 1$ 时，$f(x) \ge f(1) = \displaystyle\sum_{n=1}^{\infty}a_n^n > 0$。
> 对于固定的 $n$，当 $X > \dfrac{\mathrm{e}}{a_n}$ 时，
> $$\int_1^X\frac{\ln f(x)}{x^2}\mathrm{d}x = \int_1^{\frac{\mathrm{e}}{a_1}}\frac{\ln f(x)}{x^2}\mathrm{d}x + \sum_{p=1}^{n-1}\int_{\frac{\mathrm{e}}{a_p}}^{\frac{\mathrm{e}}{a_{p+1}}}\frac{\ln f(x)}{x^2}\mathrm{d}x + \int_{\frac{\mathrm{e}}{a_n}}^{X}\frac{\ln f(x)}{x^2}\mathrm{d}x$$
> $$\ge \sum_{p=1}^{n-1}p\int_{\frac{\mathrm{e}}{a_p}}^{\frac{\mathrm{e}}{a_{p+1}}}\frac{1}{x^2}\mathrm{d}x + n\int_{\frac{\mathrm{e}}{a_n}}^{X}\frac{1}{x^2}\mathrm{d}x$$
> 注：原卷由上一式到本式之间，略去了首项 $\displaystyle\int_1^{\mathrm{e}/a_1}\frac{\ln f(x)}{x^2}\mathrm{d}x$ 的估计（该项可负，但有与 $n$ 无关的有限下界，补上不影响结论）；此处照原卷转录。
> $$= \frac{1}{\mathrm{e}}\sum_{p=1}^{n}a_p - \frac{n}{X}.$$
> 于是当 $X > \max\left\{n,\ \dfrac{\mathrm{e}}{a_n}\right\}$ 时，$\displaystyle\int_1^X\frac{\ln f(x)}{x^2}\mathrm{d}x \ge \frac{1}{\mathrm{e}}\sum_{p=1}^{n}a_p - 1$。
> 因为级数 $\displaystyle\sum_{n=1}^{\infty}a_n$ 发散，所以 $\displaystyle\lim_{X\to+\infty}\int_1^X\frac{\ln f(x)}{x^2}\mathrm{d}x = +\infty$。……（6 分）

---

## 附：本卷考点分布速览

| 题号 | 分值 | 考点板块 | 具体考点 |
|---|---|---|---|
| 一(1) | 6 | 数列极限 | 迭代数列单调有界 + Stolz 定理 + Taylor 展开 |
| 一(2) | 6 | 定积分计算 | 区间再现换元 $x=\frac{\pi}{2}-t$ + 三角有理式积分 |
| 一(3) | 6 | 空间解析几何 | 直线在平面上的投影 + 过直线的平面束 |
| 一(4) | 6 | 级数求和 | arctan 差角公式裂项 + 望远镜求和 |
| 一(5) | 6 | 常微分方程 | 一阶线性方程（经 $\mathrm{e}^y$ 换元）+ 初值定常数 |
| 二 | 14 | 一元积分与零点 | 含绝对值定积分化为显式 + 偶函数 + 单调性 + 零点定理 |
| 三 | 14 | 多元积分与极限 | Green 公式 + 极坐标累次积分 + Taylor 展开求极限 |
| 四 | 14 | 曲面积分与微分方程 | Gauss 公式 + 球面中值 + 二阶常系数线性 ODE + 极限条件定常数 |
| 五 | 14 | 反常积分敛散性 | 取整函数积分估计（调和数展开）+ Dirichlet 判别法 + 条件收敛 |
| 六 | 14 | 级数与反常积分 | 幂级数收敛半径 + 一维分段下界估计 + 发散性传递 |
