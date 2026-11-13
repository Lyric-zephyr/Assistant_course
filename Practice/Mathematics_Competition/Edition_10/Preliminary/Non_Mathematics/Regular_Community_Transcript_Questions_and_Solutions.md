<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC10%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6%E7%B1%BB-%E5%88%9D%E8%B5%9B-2018.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 2018 年第十届全国大学生数学竞赛初赛试题及参考答案（非数学类）

> **年份**：2018 年（第十届，卷面明确标注"2018 年"）｜**类别**：非数学类
> **满分**：100 分（卷面分值合计：24 + 8 + 14 + 12 + 14 + 14 + 14）｜**题量**：填空题 4 小题 + 解答题 6 题
> **来源**：试卷为微信公众号「考研竞赛数学」整理扫描版（原扫描页眉含该公众号推广信息，转录时省略）；参考答案为官网 PDF｜原始文件：`../初赛/第10届非数学类-初赛.pdf`、`../初赛/第10届非数学类-初赛(参考答案·官网).pdf`
> **转录说明**：原卷为单页扫描版（本 PDF 仅 1 页，全卷完整），本文件由视觉逐页转写，公式采用 KaTeX 语法；「答案／解答／证明」整合自参考答案 PDF，过程分标注（原为"----------5 分"）转录为"……（5 分）"。卷面未标注考试时间与考试形式，故未记录。参考答案文本与试卷题面个别措辞略有出入（题二"分段光滑（闭）曲线"、题四"空间图形／空心立体"），正文题面以试卷原文为准。

---

## 卷面结构

| 题号 | 一 | 二 | 三 | 四 | 五 | 六 | 七 | 总分 |
|---|---|---|---|---|---|---|---|---|
| 满分 | 24 | 8 | 14 | 12 | 14 | 14 | 14 | 100 |
| 形式 | 填空题 ×4（每小题 6 分） | 解答题 | 解答题 | 解答题 | 解答题 | 解答题 | 解答题 | |

---

## 一、填空题（本题满分 24 分，共 4 小题，每小题 6 分）

**(1)** 设 $\alpha \in (0,1)$，则 $\lim\limits_{n\to+\infty}\left[(n+1)^\alpha - n^\alpha\right] = \underline{\qquad}$。

> **答案**：$0$
>
> **解答**：由于 $\left(1+\dfrac{1}{n}\right)^\alpha < 1 + \dfrac{1}{n}$，则
> $$(n+1)^\alpha - n^\alpha = n^\alpha\left[\left(1+\frac{1}{n}\right)^\alpha - 1\right] < n^\alpha\left[\left(1+\frac{1}{n}\right) - 1\right] = \frac{1}{n^{1-\alpha}},$$
> 于是 $0 < (n+1)^\alpha - n^\alpha < \dfrac{1}{n^{1-\alpha}}$，应用两边夹法则，$\lim\limits_{n\to+\infty}\left[(n+1)^\alpha - n^\alpha\right] = 0$。

**(2)** 若曲线 $y = y(x)$ 由 $\begin{cases} x = t + \cos t \\ e^y + ty + \sin t = 1 \end{cases}$ 确定，则此曲线在 $t = 0$ 对应点处的切线方程为 $\underline{\qquad}$。

> **答案**：$y - 0 = -(x-1)$（即 $x + y = 1$）
>
> **解答**：当 $t = 0$ 时，$x = 1$，$y = 0$。对 $x = t + \cos t$ 两边关于 $t$ 求导：$\dfrac{\mathrm{d}x}{\mathrm{d}t} = 1 - \sin t$，$\left.\dfrac{\mathrm{d}x}{\mathrm{d}t}\right|_{t=0} = 1$；
> 对 $e^y + ty + \sin t = 1$ 两边关于 $t$ 求导：$e^y\dfrac{\mathrm{d}y}{\mathrm{d}t} + y + t\dfrac{\mathrm{d}y}{\mathrm{d}t} + \cos t = 0$，$\left.\dfrac{\mathrm{d}y}{\mathrm{d}t}\right|_{t=0} = -1$，则 $\left.\dfrac{\mathrm{d}y}{\mathrm{d}x}\right|_{t=0} = -1$。
> 所以，切线方程为 $y - 0 = -(x-1)$。

**(3)** $\displaystyle\int \frac{\ln\left(x + \sqrt{1+x^2}\right)}{(1+x^2)^{3/2}}\,\mathrm{d}x = \underline{\qquad}$。

> **答案**：$\dfrac{x}{\sqrt{1+x^2}}\ln\left(x + \sqrt{1+x^2}\right) - \dfrac{1}{2}\ln(1+x^2) + C$
>
> **解法 1**（$x = \tan t$）：
> $$\int \frac{\ln(x+\sqrt{1+x^2})}{(1+x^2)^{3/2}}\,\mathrm{d}x \xrightarrow{\ x=\tan t\ } \int \frac{\ln(\tan t + \sec t)}{\sec t}\,\mathrm{d}t = \int \ln(\tan t + \sec t)\,\mathrm{d}\sin t$$
> $$= \sin t\ln(\tan t + \sec t) - \int \sin t\,\mathrm{d}\ln(\tan t + \sec t)$$
> $$= \sin t\ln(\tan t + \sec t) - \int \sin t\cdot\frac{1}{\tan t + \sec t}(\sec^2 t + \tan t\sec t)\,\mathrm{d}t$$
> $$= \sin t\ln(\tan t + \sec t) - \int \frac{\sin t}{\cos t}\,\mathrm{d}t$$
> $$= \sin t\ln(\tan t + \sec t) + \ln|\cos t| + C = \frac{x}{\sqrt{1+x^2}}\ln(x+\sqrt{1+x^2}) - \frac{1}{2}\ln(1+x^2) + C.$$
>
> **解法 2**（分部积分）：
> $$\int \frac{\ln(x+\sqrt{1+x^2})}{(1+x^2)^{3/2}}\,\mathrm{d}x = \int \ln(x+\sqrt{1+x^2})\,\mathrm{d}\frac{x}{\sqrt{1+x^2}}$$
> $$= \frac{x}{\sqrt{1+x^2}}\ln(x+\sqrt{1+x^2}) - \int \frac{x}{\sqrt{1+x^2}}\cdot\frac{1}{x+\sqrt{1+x^2}}\left(1 + \frac{x}{\sqrt{1+x^2}}\right)\mathrm{d}x$$
> $$= \frac{x}{\sqrt{1+x^2}}\ln(x+\sqrt{1+x^2}) - \int \frac{x}{1+x^2}\,\mathrm{d}x = \frac{x}{\sqrt{1+x^2}}\ln(x+\sqrt{1+x^2}) - \frac{1}{2}\ln(1+x^2) + C.$$

**(4)** $\lim\limits_{x\to 0}\dfrac{1 - \cos x\sqrt{\cos 2x}\sqrt[3]{\cos 3x}}{x^2} = \underline{\qquad}$。

> **答案**：$3$
>
> **解答**：
> $$\lim_{x\to 0}\frac{1-\cos x\sqrt{\cos 2x}\sqrt[3]{\cos 3x}}{x^2} = \lim_{x\to 0}\left[\frac{1-\cos x}{x^2} + \frac{\cos x\left(1-\sqrt{\cos 2x}\sqrt[3]{\cos 3x}\right)}{x^2}\right]$$
> $$= \frac{1}{2} + \lim_{x\to 0}\frac{1-\sqrt{\cos 2x}\sqrt[3]{\cos 3x}}{x^2} = \frac{1}{2} + \lim_{x\to 0}\left[\frac{1-\sqrt{\cos 2x}}{x^2} + \frac{\sqrt{\cos 2x}\left(1-\sqrt[3]{\cos 3x}\right)}{x^2}\right]$$
> $$= \frac{1}{2} + \lim_{x\to 0}\left[\frac{1-\sqrt{(\cos 2x - 1)+1}}{x^2} + \frac{1-\sqrt[3]{(\cos 3x - 1)+1}}{x^2}\right]$$
> $$= \frac{1}{2} + \lim_{x\to 0}\frac{1-\cos 2x}{2x^2} + \lim_{x\to 0}\frac{1-\cos 3x}{3x^2} = \frac{1}{2} + 1 + \frac{3}{2} = 3.$$

---

## 二、（本题满分 8 分）

设函数 $f(t)$ 在 $t \neq 0$ 时一阶连续可导，且 $f(1) = 0$，求函数 $f(x^2-y^2)$，使得曲线积分
$$\int_L y\left[2 - f(x^2-y^2)\right]\mathrm{d}x + xf(x^2-y^2)\,\mathrm{d}y$$
与路径无关，其中 $L$ 为任一不与直线 $y = \pm x$ 相交的分段光滑曲线。

> **解**：设 $P(x,y) = y\left(2 - f(x^2-y^2)\right)$，$Q(x,y) = xf(x^2-y^2)$，由题设可知，积分与路径无关，于是有 $\dfrac{\partial Q(x,y)}{\partial x} = \dfrac{\partial P}{\partial y}$，由此可知
> $$(x^2-y^2)f'(x^2-y^2) + f(x^2-y^2) = 1.$$
> ……（5 分）
>
> 记 $t = x^2-y^2$，则得微分方程 $tf'(t) + f(t) = 1$，即 $(tf(t))' = 1$，$tf(t) = t + C$。
> 又 $f(1) = 0$，可得 $C = -1$，$f(t) = 1 - \dfrac{1}{t}$，从而 $f(x^2-y^2) = 1 - \dfrac{1}{x^2-y^2}$。
> ……（8 分）

---

## 三、（本题满分 14 分）

设 $f(x)$ 在区间 $[0,1]$ 上连续，且 $1 \le f(x) \le 3$。证明：
$$1 \le \int_0^1 f(x)\,\mathrm{d}x\int_0^1\frac{1}{f(x)}\,\mathrm{d}x \le \frac{4}{3}.$$

> **证明**：由柯西不等式
> $$\int_0^1 f(x)\,\mathrm{d}x\int_0^1\frac{1}{f(x)}\,\mathrm{d}x \ge \left(\int_0^1\sqrt{f(x)}\sqrt{\frac{1}{f(x)}}\,\mathrm{d}x\right)^2 = 1.$$
> ……（4 分）
>
> 又由于 $(f(x)-1)(f(x)-3) \le 0$，则 $(f(x)-1)(f(x)-3)/f(x) \le 0$，
> 即 $f(x) + \dfrac{3}{f(x)} \le 4$，$\displaystyle\int_0^1\left(f(x) + \frac{3}{f(x)}\right)\mathrm{d}x \le 4$。
> ……（10 分）
>
> 由于 $\displaystyle\int_0^1 f(x)\,\mathrm{d}x\int_0^1\frac{3}{f(x)}\,\mathrm{d}x \le \frac{1}{4}\left(\int_0^1 f(x) + \int_0^1\frac{3}{f(x)}\,\mathrm{d}x\right)^2$，
> 故 $1 \le \displaystyle\int_0^1 f(x)\,\mathrm{d}x\int_0^1\frac{1}{f(x)}\,\mathrm{d}x \le \frac{4}{3}$。
> ……（14 分）

---

## 四、（本题满分 12 分）

计算三重积分 $\displaystyle\iiint_{(V)}\left(x^2+y^2\right)\mathrm{d}V$，其中 $(V)$ 是由
$$x^2+y^2+(z-2)^2 \ge 4,\quad x^2+y^2+(z-1)^2 \le 9$$
及 $z \ge 0$ 所围成的空间图形。

> **解**：（1）$(V_1): \begin{cases} x = r\sin\varphi\cos\theta,\ y = r\sin\varphi\sin\theta,\ z-1 = r\cos\varphi \\ 0 \le r \le 3,\ 0 \le \varphi \le \pi,\ 0 \le \theta \le 2\pi \end{cases}$
> $$\iiint_{(V_1)}\left(x^2+y^2\right)\mathrm{d}V = \int_0^{2\pi}\mathrm{d}\theta\int_0^\pi\mathrm{d}\varphi\int_0^3 r^2\sin^2\varphi\cdot r^2\sin\varphi\,\mathrm{d}r = \frac{8}{15}\cdot 3^5\cdot\pi$$
> ……（4 分）
>
> （2）$(V_2): \begin{cases} x = r\sin\varphi\cos\theta,\ y = r\sin\varphi\sin\theta,\ z-2 = r\cos\varphi \\ 0 \le r \le 2,\ 0 \le \varphi \le \pi,\ 0 \le \theta \le 2\pi \end{cases}$
> $$\iiint_{(V_2)}\left(x^2+y^2\right)\mathrm{d}V = \int_0^{2\pi}\mathrm{d}\theta\int_0^\pi\mathrm{d}\varphi\int_0^2 r^2\sin^2\varphi\cdot r^2\sin\varphi\,\mathrm{d}r = \frac{8}{15}\cdot 2^5\cdot\pi$$
> ……（8 分）
>
> （3）$(V_3): \begin{cases} x = r\cos\theta,\ y = r\sin\theta,\ 1-\sqrt{9-r^2} \le z \le 0 \\ 0 \le r \le 2\sqrt{2},\ 0 \le \theta \le 2\pi \end{cases}$
> $$\iiint_{(V_3)}\left(x^2+y^2\right)\mathrm{d}V = \iint_{r\le 2\sqrt{2}} r\,\mathrm{d}r\,\mathrm{d}\theta\int_{1-\sqrt{9-r^2}}^0 r^2\,\mathrm{d}z = \int_0^{2\pi}\mathrm{d}\theta\int_0^{2\sqrt{2}} r^3\left(\sqrt{9-r^2}-1\right)\mathrm{d}r = \left(124 - \frac{2}{5}\cdot 3^5 + \frac{2}{5}\right)\pi$$
>
> $$\iiint_{(V)}\left(x^2+y^2\right)\mathrm{d}V = \iiint_{(V_1)}\left(x^2+y^2\right)\mathrm{d}V - \iiint_{(V_2)}\left(x^2+y^2\right)\mathrm{d}V - \iiint_{(V_3)}\left(x^2+y^2\right)\mathrm{d}V = \frac{256}{3}\pi$$
> ……（12 分）

---

## 五、（本题满分 14 分）

设 $f(x,y)$ 在区域 $D$ 内可微，且
$$\sqrt{\left(\frac{\partial f}{\partial x}\right)^2 + \left(\frac{\partial f}{\partial y}\right)^2} \le M,$$
$A(x_1,y_1)$，$B(x_2,y_2)$ 是 $D$ 内两点，线段 $AB$ 包含在 $D$ 内。证明：
$$\left|f(x_1,y_1) - f(x_2,y_2)\right| \le M\left|AB\right|,$$
其中 $|AB|$ 表示线段 $AB$ 的长度。

> **证明**：作辅助函数 $\varphi(t) = f\left(x_1 + t(x_2-x_1),\ y_1 + t(y_2-y_1)\right)$，……（2 分）
>
> 显然 $\varphi(t)$ 在 $[0,1]$ 上可导。根据拉格朗日中值定理，存在 $c \in (0,1)$，使得
> $$\varphi(1) - \varphi(0) = \varphi'(c) = \frac{\partial f(u,v)}{\partial u}(x_2-x_1) + \frac{\partial f(u,v)}{\partial v}(y_2-y_1)$$
> ……（8 分）
>
> $$\left|\varphi(1)-\varphi(0)\right| = \left|f(x_2,y_2) - f(x_1,y_1)\right| = \left|\frac{\partial f(u,v)}{\partial u}(x_2-x_1) + \frac{\partial f(u,v)}{\partial v}(y_2-y_1)\right|$$
> $$\le \left[\left(\frac{\partial f(u,v)}{\partial u}\right)^2 + \left(\frac{\partial f(u,v)}{\partial v}\right)^2\right]^{1/2}\left[(x_2-x_1)^2 + (y_2-y_1)^2\right]^{1/2} \le M\left|AB\right|$$
> ……（14 分）

---

## 六、（本题满分 14 分）

证明：对于连续函数 $f(x) > 0$，有
$$\ln\int_0^1 f(x)\,\mathrm{d}x \ge \int_0^1\ln f(x)\,\mathrm{d}x.$$

> **证**：由于 $f(x)$ 在 $[0,1]$ 上连续，所以 $\displaystyle\int_0^1 f(x)\,\mathrm{d}x = \lim_{n\to+\infty}\frac{1}{n}\sum_{k=1}^n f(x_k)$，其中 $x_k \in \left[\frac{k-1}{n}, \frac{k}{n}\right]$。
> ……（4 分）
>
> 由不等式 $\left(f(x_1)f(x_2)\cdots f(x_n)\right)^{\frac{1}{n}} \le \dfrac{1}{n}\sum_{k=1}^n f(x_k)$，根据 $\ln x$ 的单调性
> $$\frac{1}{n}\sum_{k=1}^n \ln f(x_k) \le \ln\left(\frac{1}{n}\sum_{k=1}^n f(x_k)\right),$$
> ……（12 分）
>
> 根据 $\ln x$ 的连续性，两边取极限
> $$\lim_{n\to+\infty}\left(\frac{1}{n}\sum_{k=1}^n \ln f(x_k)\right) \le \lim_{n\to+\infty}\ln\left(\frac{1}{n}\sum_{k=1}^n f(x_k)\right)$$
> 得 $\displaystyle\int_0^1\ln f(x)\,\mathrm{d}x \le \ln\int_0^1 f(x)\,\mathrm{d}x$。
> ……（14 分）

---

## 七、（本题满分 14 分）

已知 $\{a_k\}$，$\{b_k\}$ 是正数数列，且 $b_{k+1} - b_k \ge \delta > 0$，$k = 1,2,\cdots$，$\delta$ 为一常数。证明：若级数 $\displaystyle\sum_{k=1}^{+\infty} a_k$ 收敛，则级数
$$\sum_{k=1}^{+\infty}\frac{k\sqrt[k]{(a_1a_2\cdots a_k)(b_1b_2\cdots b_k)}}{b_{k+1}b_k}$$
收敛。

> **证明**：令 $S_k = \displaystyle\sum_{i=1}^k a_ib_i$，$a_kb_k = S_k - S_{k-1}$，$S_0 = 0$，$a_k = \dfrac{S_k - S_{k-1}}{b_k}$，$k = 1,2,\cdots$。
> ……（4 分）
>
> $$\sum_{k=1}^N a_k = \sum_{k=1}^N \frac{S_k - S_{k-1}}{b_k} = \sum_{k=1}^{N-1}\left(\frac{S_k}{b_k} - \frac{S_k}{b_{k+1}}\right) + \frac{S_N}{b_N} = \sum_{k=1}^{N-1}\frac{b_{k+1}-b_k}{b_kb_{k+1}}S_k + \frac{S_N}{b_N} \ge \sum_{k=1}^{N-1}\frac{\delta}{b_kb_{k+1}}S_k$$
>
> 所以 $\displaystyle\sum_{k=1}^{+\infty}\frac{S_k}{b_kb_{k+1}}$ 收敛，……（10 分）
>
> 由不等式 $\sqrt[k]{(a_1a_2\cdots a_k)(b_1b_2\cdots b_k)} \le \dfrac{a_1b_1 + a_2b_2 + \cdots + a_kb_k}{k} = \dfrac{S_k}{k}$ 知
> $$\sum_{k=1}^{+\infty}\frac{k\sqrt[k]{(a_1a_2\cdots a_k)(b_1b_2\cdots b_k)}}{b_{k+1}b_k} \le \sum_{k=1}^{+\infty}\frac{S_k}{b_{k+1}b_k},$$
> 故结论成立。……（14 分）

---

## 附：本卷考点分布速览

| 题号 | 分值 | 考点板块 | 具体考点 |
|---|---|---|---|
| 一(1) | 6 | 极限 | 数列极限：幂函数差的两边夹法则估计（$0<\alpha<1$） |
| 一(2) | 6 | 微分学 | 参数方程（含隐式 $e^y+ty+\sin t=1$）求导 + 切线方程 |
| 一(3) | 6 | 不定积分 | 三角代换与分部积分两种解法（$\ln(x+\sqrt{1+x^2})$ 结构） |
| 一(4) | 6 | 极限 | 连乘式极限 + 等价无穷小（$\sqrt{1+x}-1\sim\frac{x}{2}$、$\sqrt[3]{1+x}-1\sim\frac{x}{3}$） |
| 二 | 8 | 曲线积分 | 路径无关条件（$\partial Q/\partial x=\partial P/\partial y$）+ 凑微分（$(tf(t))'$）解微分方程 |
| 三 | 14 | 积分不等式 | 柯西不等式（下界）+ 均值不等式（上界）双向估计 |
| 四 | 12 | 三重积分 | 两球体交叠区域：$V_1 - V_2 - V_3$ 分解，球面坐标 + 柱面坐标 |
| 五 | 14 | 多元微分/不等式 | 构造一元辅助函数用拉格朗日中值定理 + 柯西不等式证 Lipschitz 估计 |
| 六 | 14 | 积分不等式 | 定积分定义（Riemann 和）+ 均值不等式 + $\ln$ 连续性取极限 |
| 七 | 14 | 级数 | 级数收敛性证明：Abel 分部求和 + 均值不等式放缩 |
