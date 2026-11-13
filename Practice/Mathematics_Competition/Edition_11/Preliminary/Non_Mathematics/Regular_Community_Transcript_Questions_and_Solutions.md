<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC11%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6%E7%B1%BB-%E5%88%9D%E8%B5%9B-2019.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第十一届全国大学生数学竞赛（非数学类）初赛试题及参考答案

> **年份**：2019 年（第十一届；原 PDF 未标注年份，按届次推定）｜**类别**：非数学类
> **考试形式**：闭卷｜**满分**：100 分（填空题 5 × 6 分 + 解答题 5 × 14 分）｜**题量**：填空题 5 小题 + 解答题 5 题（原卷未印考试时长）
> **来源**：原卷扫描 PDF《第十一届全国大学生数学竞赛(非数学类)试题 参考解答及评分标准》｜原始文件：`../初赛/第11届非数学类-初赛(试题及参考答案).pdf`
> **转录说明**：原卷为「试题＋参考解答及评分标准」合一文档，本文件由视觉逐页转写，公式采用 KaTeX 语法；填空题题面按原卷照录（题面等式右端即原卷给出的答案），解答均来自原卷参考解，过程给分点（如"……（5 分）"）为原卷标注；页脚"大学生数学竞赛网"水印已略去。

---

## 卷面结构

| 题号 | 一 | 二 | 三 | 四 | 五 | 六 | 总分 |
|---|---|---|---|---|---|---|---|
| 满分 | 30 | 14 | 14 | 14 | 14 | 14 | 100 |
| 形式 | 填空题 ×5 | 解答题 | 解答题 | 解答题 | 解答题 | 解答题 | |

---

## 一、填空题（每小题 6 分）

**1.** 极限 $\lim\limits_{x\to 0}\dfrac{\ln(e^{\sin x}+\sqrt[3]{1-\cos x})-\sin x}{\arctan(4\sqrt[3]{1-\cos x})} = \underline{\qquad}$。

> **解答**：
> $$\lim_{x\to 0}\frac{\ln(e^{\sin x}+\sqrt[3]{1-\cos x})-\sin x}{\arctan(4\sqrt[3]{1-\cos x})} = \lim_{x\to 0}\frac{(e^{\sin x}-1)+\sqrt[3]{1-\cos x}}{4\sqrt[3]{1-\cos x}} - \lim_{x\to 0}\frac{\sin x}{4\sqrt[3]{1-\cos x}}$$
> $$= \lim_{x\to 0}\frac{e^{\sin x}-1}{4\left(\frac{x^2}{2}\right)^{1/3}} + \frac{1}{4} - \lim_{x\to 0}\frac{\sin x}{4\left(\frac{x^2}{2}\right)^{1/3}} = \frac{1}{4}.$$

**2.** 设隐函数 $y = y(x)$ 由方程 $y^2(x-y) = x^2$ 所确定，则 $\displaystyle\int\frac{\mathrm{d}x}{y^2} = \underline{\qquad}$。

> **解答**：令 $y = tx$，则 $x = \dfrac{1}{t^2(1-t)}$，$y = \dfrac{1}{t(1-t)}$，$\mathrm{d}x = \dfrac{-2+3t}{t^3(1-t)^2}\,\mathrm{d}t$，
> 这样，
> $$\int\frac{\mathrm{d}x}{y^2} = \int\frac{-2+3t}{t}\,\mathrm{d}t = 3t - 2\ln|t| + C = \frac{3y}{x} - 2\ln\left|\frac{y}{x}\right| + C.$$

**3.** 定积分 $\displaystyle\int_0^{\frac{\pi}{2}}\frac{e^x(1+\sin x)}{1+\cos x}\,\mathrm{d}x = \underline{\qquad}$。

> **解答**：
> $$\int_0^{\frac{\pi}{2}}\frac{e^x(1+\sin x)}{1+\cos x}\,\mathrm{d}x = \int_0^{\frac{\pi}{2}}\frac{e^x}{1+\cos x}\,\mathrm{d}x + \int_0^{\frac{\pi}{2}}\frac{\sin x}{1+\cos x}\,\mathrm{d}e^x$$
> $$= \int_0^{\frac{\pi}{2}}\frac{e^x}{1+\cos x}\,\mathrm{d}x + \left.\frac{\sin x\,e^x}{1+\cos x}\right|_0^{\frac{\pi}{2}} - \int_0^{\frac{\pi}{2}}e^x\frac{\cos x(1+\cos x)+\sin^2 x}{(1+\cos x)^2}\,\mathrm{d}x$$
> $$= \int_0^{\frac{\pi}{2}}\frac{e^x}{1+\cos x}\,\mathrm{d}x + \left.\frac{\sin x\,e^x}{1+\cos x}\right|_0^{\frac{\pi}{2}} - \int_0^{\frac{\pi}{2}}\frac{e^x}{1+\cos x}\,\mathrm{d}x = e^{\frac{\pi}{2}}.$$

**4.** 已知 $\mathrm{d}u(x,y) = \dfrac{y\,\mathrm{d}x - x\,\mathrm{d}y}{3x^2-2xy+3y^2}$，则 $u(x,y) = \underline{\qquad}$。

> **解答**：
> $$\mathrm{d}u(x,y) = \frac{y\,\mathrm{d}x - x\,\mathrm{d}y}{3x^2-2xy+3y^2} = \frac{\mathrm{d}\left(\frac{x}{y}\right)}{3\left(\frac{x}{y}\right)^2 - \frac{2x}{y} + 3} = \frac{1}{2\sqrt{2}}\,\mathrm{d}\arctan\frac{3}{2\sqrt{2}}\left(\frac{x}{y}-\frac{1}{3}\right).$$
> 所以，$u(x,y) = \dfrac{1}{2\sqrt{2}}\arctan\dfrac{3}{2\sqrt{2}}\left(\dfrac{x}{y}-\dfrac{1}{3}\right) + C$。

**5.** 设 $a,b,c,\mu>0$，曲面 $xyz = \mu$ 与曲面 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}+\dfrac{z^2}{c^2} = 1$ 相切，则 $\mu = \underline{\qquad}$。

> **解答**：根据题意有：$yz = \dfrac{2x}{a^2}\lambda$，$xz = \dfrac{2y}{b^2}\lambda$，$xy = \dfrac{2z}{c^2}\lambda$，以及
> $$\mu = 2\lambda\frac{x^2}{a^2},\qquad \mu = 2\lambda\frac{y^2}{b^2},\qquad \mu = 2\lambda\frac{z^2}{c^2},$$
> 从而得：$\mu = \dfrac{8\lambda^3}{a^2b^2c^2}$，$3\mu = 2\lambda$，
> 联立解得：$\mu = \dfrac{abc}{3\sqrt{3}}$。

---

## 二、（本题 14 分）

计算三重积分 $\displaystyle\iiint_\Omega \frac{xyz}{x^2+y^2}\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$，其中 $\Omega$ 是由曲面 $(x^2+y^2+z^2)^2 = 2xy$ 围成的区域在第一卦限部分。

> **解答**：采用"球面坐标"计算，并利用对称性，得
> $$I = 2\int_0^{\frac{\pi}{4}}\mathrm{d}\theta\int_0^{\frac{\pi}{2}}\mathrm{d}\varphi\int_0^{\sqrt{2}\sin\varphi\sqrt{\sin\theta\cos\theta}} \frac{\rho^3\sin^2\varphi\cos\theta\sin\theta\cos\varphi}{\rho^2\sin^2\varphi}\,\rho^2\sin\varphi\,\mathrm{d}\rho$$
> ……（5 分）
> $$= 2\int_0^{\frac{\pi}{4}}\sin\theta\cos\theta\,\mathrm{d}\theta\int_0^{\frac{\pi}{2}}\sin\varphi\cos\varphi\,\mathrm{d}\varphi\int_0^{\sqrt{2}\sin\varphi\sqrt{\sin\theta\cos\theta}}\rho^3\,\mathrm{d}\rho$$
> $$= 2\int_0^{\frac{\pi}{4}}\sin^3\theta\cos^3\theta\,\mathrm{d}\theta\int_0^{\frac{\pi}{2}}\sin^5\varphi\cos\varphi\,\mathrm{d}\varphi$$
> ……（10 分）
> $$= \frac{1}{4}\int_0^{\frac{\pi}{4}}\sin^3 2\theta\,\mathrm{d}\theta\int_0^{\frac{\pi}{2}}\sin^5\varphi\,\mathrm{d}(\sin\varphi)$$
> $$= \frac{1}{48}\int_0^{\frac{\pi}{2}}\sin^3 t\,\mathrm{d}t = \frac{1}{48}\cdot\frac{2}{3} = \frac{1}{72}.$$
> ……（14 分）

---

## 三、（本题 14 分）

设 $f(x)$ 在 $[0,+\infty)$ 上可微，$f(0) = 0$，且存在常数 $A>0$，使得 $|f'(x)|\le A|f(x)|$ 在 $[0,+\infty)$ 上成立，试证明：在 $(0,+\infty)$ 上有 $f(x)\equiv 0$。

> **证明**：设 $x_0\in\left[0,\dfrac{1}{2A}\right]$，使得
> $$|f(x_0)| = \max\left\{|f(x)|\ \middle|\ x\in\left[0,\frac{1}{2A}\right]\right\},$$
> ……（5 分）
> $$|f(x_0)| = |f(0)+f'(\xi)x_0| \le A|f(x_0)|\frac{1}{2A} = \frac{1}{2}|f(x_0)|,$$
> 只有 $|f(x_0)| = 0$。
> 故当 $x\in\left[0,\dfrac{1}{2A}\right]$ 时，$f(x)\equiv 0$。……（12 分）
>
> 递推可得，对所有的 $x\in\left[\dfrac{k-1}{2A},\dfrac{k}{2A}\right]$，$k = 1,2,\cdots$，均有 $f(x)\equiv 0$。……（14 分）

---

## 四、（本题 14 分）

计算积分 $I = \displaystyle\int_0^{2\pi}\mathrm{d}\varphi\int_0^{\pi} e^{\sin\theta(\cos\varphi-\sin\varphi)}\sin\theta\,\mathrm{d}\theta$。

> **解答**：设球面 $\Sigma: x^2+y^2+z^2 = 1$，由球面参数方程
> $$x = \sin\theta\cos\varphi,\qquad y = \sin\theta\sin\varphi,\qquad z = \cos\theta$$
> 知 $\mathrm{d}S = \sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi$，所以，所求积分可化为第一型曲面积分
> $$I = \iint_\Sigma e^{x-y}\,\mathrm{d}S$$
> ……（4 分）
> 设平面 $P_t:\ \dfrac{x-y}{\sqrt{2}} = t$，$-1\le t\le 1$，其中 $t$ 为平面 $P_t$ 被球面截下部分中心到原点距离。用平面 $P_t$ 分割球面 $\Sigma$，球面在平面 $P_t$、$P_{t+\mathrm{d}t}$ 之间的部分形如圆台外表面状，记为 $\Sigma_{t,\mathrm{d}t}$。被积函数在其上为 $e^{x-y} = e^{\sqrt{2}t}$。……（8 分）
>
> 由于 $\Sigma_{t,\mathrm{d}t}$ 半径为 $r_t = \sqrt{1-t^2}$，半径的增长率为 $\mathrm{d}\sqrt{1-t^2} = \dfrac{-t\,\mathrm{d}t}{\sqrt{1-t^2}}$，就是 $\Sigma_{t,\mathrm{d}t}$ 上下底半径之差。记圆台外表面斜高为 $h_t$，则由微元法知 $\mathrm{d}t^2 + \left(\mathrm{d}\sqrt{1-t^2}\,\right)^2 = h_t^2$，得到 $h_t = \dfrac{\mathrm{d}t}{\sqrt{1-t^2}}$，所以 $\Sigma_{t,\mathrm{d}t}$ 的面积为 $\mathrm{d}S = 2\pi r_t h_t = 2\pi\,\mathrm{d}t$，……（12 分）
> $$I = \int_{-1}^{1} e^{\sqrt{2}t}\,2\pi\,\mathrm{d}t = \frac{2\pi}{\sqrt{2}}\left.e^{\sqrt{2}t}\right|_{-1}^{1} = \sqrt{2}\pi\left(e^{\sqrt{2}}-e^{-\sqrt{2}}\right).$$
> ……（14 分）

---

## 五、（本题 14 分）

设 $f(x)$ 是仅有正实根的多项式函数，满足 $\dfrac{f'(x)}{f(x)} = -\displaystyle\sum_{n=0}^{+\infty}c_nx^n$。试证：$c_n>0$（$n\ge 0$），极限 $\lim\limits_{n\to+\infty}\dfrac{1}{\sqrt[n]{c_n}}$ 存在，且等于 $f(x)$ 的最小根。

> **证明**：由 $f(x)$ 为仅有正实根的多项式，不妨设 $f(x)$ 的全部根为
> $$0 < a_1 < a_2 < \cdots < a_k,$$
> 这样，
> $$f(x) = A(x-a_1)^{r_1}\cdots(x-a_k)^{r_k},$$
> 其中 $r_i$ 为对应根 $a_i$ 的重数（$i = 1,\cdots,k$，$r_k\ge 1$）。……（2 分）
> $$f'(x) = Ar_1(x-a_1)^{r_1-1}\cdots(x-a_k)^{r_k} + \cdots + Ar_k(x-a_1)^{r_1}\cdots(x-a_k)^{r_k-1},$$
> 所以，$f'(x) = f(x)\left(\dfrac{r_1}{x-a_1}+\cdots+\dfrac{r_k}{x-a_k}\right)$，从而
> $$-\frac{f'(x)}{f(x)} = \frac{r_1}{a_1}\cdot\frac{1}{1-\frac{x}{a_1}} + \cdots + \frac{r_k}{a_k}\cdot\frac{1}{1-\frac{x}{a_k}}.$$
> ……（6 分）
> 若 $|x| < a_1$，则
> $$-\frac{f'(x)}{f(x)} = \frac{r_1}{a_1}\cdot\sum_{n=0}^{\infty}\left(\frac{x}{a_1}\right)^n + \cdots + \frac{r_k}{a_k}\cdot\sum_{n=0}^{\infty}\left(\frac{x}{a_k}\right)^n = \sum_{n=0}^{\infty}\left(\frac{r_1}{a_1^{n+1}}+\cdots+\frac{r_k}{a_k^{n+1}}\right)x^n.$$
> 而 $-\dfrac{f'(x)}{f(x)} = \displaystyle\sum_{n=0}^{\infty}c_nx^n$，由幂级数的唯一性知
> $$c_n = \frac{r_1}{a_1^{n+1}}+\cdots+\frac{r_k}{a_k^{n+1}} > 0,$$
> ……（9 分）
> $$\frac{c_n}{c_{n+1}} = \frac{\frac{r_1}{a_1^{n+1}}+\cdots+\frac{r_k}{a_k^{n+1}}}{\frac{r_1}{a_1^{n+2}}+\cdots+\frac{r_k}{a_k^{n+2}}} = a_1\cdot\frac{r_1+\cdots+\left(\frac{a_1}{a_k}\right)^{n+1}r_k}{r_1+\cdots+\left(\frac{a_1}{a_k}\right)^{n+2}r_k},$$
> $$\lim_{n\to\infty}\frac{c_n}{c_{n+1}} = a_1\cdot\frac{r_1+0+\cdots+0}{r_1+0+\cdots+0} = a_1 > 0,\qquad \lim_{n\to\infty}\frac{c_{n+1}}{c_n} = \frac{1}{a_1},$$
> ……（12 分）
> $$\lim_{n\to\infty}\frac{1}{n}\cdot\left(\ln\frac{c_2}{c_1}+\cdots+\ln\frac{c_{n+1}}{c_n}\right) = \ln\frac{1}{a_1},$$
> $$\sqrt[n]{c_n} = e^{\frac{\ln c_n}{n}} = e^{\frac{\ln c_1}{n}+\frac{1}{n}\left(\ln\frac{c_2}{c_1}+\cdots+\ln\frac{c_{n+1}}{c_n}\right)} \to e^{\ln\frac{1}{a_1}} = \frac{1}{a_1}.$$
> 从而，$\lim\limits_{n\to\infty}\dfrac{1}{\sqrt[n]{c_n}} = a_1$，即 $f(x)$ 的最小正根。……（14 分）

---

## 六、（本题 14 分）

设函数 $f(x)$ 在 $[0,+\infty)$ 上具有连续导数，满足
$$3\left[3+f^2(x)\right]f'(x) = 2\left[1+f^2(x)\right]^2e^{-x^2},$$
且 $f(0)\le 1$。证明：存在常数 $M>0$，使得 $x\in[0,+\infty)$ 时，恒有 $|f(x)|\le M$。

> **证明**：由于 $f'(x)>0$，所以 $f(x)$ 是 $[0,+\infty)$ 上的严格增函数，故 $\lim\limits_{x\to+\infty}f(x) = L$（有限或为 $+\infty$）。下面证明 $L\ne+\infty$。……（2 分）
>
> 记 $y = f(x)$，将所给等式分离变量并积分得
> $$\int\frac{3+y^2}{(1+y^2)^2}\,\mathrm{d}y = \frac{2}{3}\int e^{-x^2}\,\mathrm{d}x,$$
> 即
> $$\frac{y}{1+y^2}+2\arctan y = \frac{2}{3}\int_0^x e^{-t^2}\,\mathrm{d}t + C,$$
> ……（6 分）
> 其中 $C = \dfrac{f(0)}{1+f^2(0)}+2\arctan f(0)$。……（8 分）
>
> 若 $L = +\infty$，则对上式取极限 $x\to+\infty$，并利用 $\displaystyle\int_0^{+\infty}e^{-t^2}\,\mathrm{d}t = \frac{\sqrt{\pi}}{2}$，得 $C = \pi-\dfrac{\sqrt{\pi}}{3}$。……（10 分）
>
> 另一方面，令 $g(u) = \dfrac{u}{1+u^2}+2\arctan u$，则 $g'(u) = \dfrac{3+u^2}{(1+u^2)^2}>0$，所以函数 $g(u)$ 在 $(-\infty,+\infty)$ 上严格单调增加。因此，当 $f(0)\le 1$ 时，$C = g(f(0))\le g(1) = \dfrac{1+\pi}{2}$，但
> $$C > \frac{2\pi-\sqrt{\pi}}{2} > \frac{1+\pi}{2},$$
> 矛盾，这就证明了 $\lim\limits_{x\to+\infty}f(x) = L$ 为有限数。
>
> 最后，取 $M = \max\{|f(0)|,|L|\}$，则 $|f(x)|\le M$，$\forall x\in[0,+\infty)$。……（14 分）

---

## 附：本卷考点分布速览

| 题号 | 分值 | 考点板块 | 具体考点 |
|---|---|---|---|
| 一（1） | 6 | 极限 | 等价无穷小替换（$\sqrt[3]{1-\cos x}\sim\left(\frac{x^2}{2}\right)^{1/3}$）+ 极限拆分 |
| 一（2） | 6 | 不定积分 | 隐函数 $y^2(x-y)=x^2$ 下求 $\int\frac{\mathrm{d}x}{y^2}$（令 $y=tx$ 有理化换元） |
| 一（3） | 6 | 定积分 | 分部积分：$\int\frac{\sin x}{1+\cos x}\mathrm{d}e^x$ 与 $\int\frac{e^x}{1+\cos x}\mathrm{d}x$ 互消 |
| 一（4） | 6 | 全微分 | 由全微分求原函数（凑 $\mathrm{d}(x/y)$、配方后用 arctan 积分公式） |
| 一（5） | 6 | 空间解析几何 | 两曲面相切（Lagrange 乘子法）求参数 $\mu$ |
| 二 | 14 | 三重积分 | 球面坐标 + 对称性（曲面 $(x^2+y^2+z^2)^2=2xy$ 第一卦限部分） |
| 三 | 14 | 微分学证明 | 最大值点估计 + 拉格朗日中值定理 + 区间递推证 $f\equiv 0$ |
| 四 | 14 | 曲面积分 | 第一型曲面积分 + 球面按平面族分割（圆台面积微元 $\mathrm{d}S=2\pi\,\mathrm{d}t$） |
| 五 | 14 | 级数 | $-f'/f$ 的幂级数展开：证 $c_n>0$ 及 $\lim\frac{1}{\sqrt[n]{c_n}}=a_1$（最小正根，根值 + 对数平均化） |
| 六 | 14 | 常微分方程 | 可分离变量方程 + 反证法（$g$ 单调性导出 $C$ 的矛盾，证明解全局有界） |
