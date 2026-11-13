<!-- 来源：https://github.com/DREAMERhyh/ucas-cmc-2026/blob/dbcdece740d2dfaba8f3a008f175f996c7520d99/%E7%A0%94%E7%A9%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E7%9C%9F%E9%A2%98/%E8%BD%AC%E5%BD%95/%E7%AC%AC13%E5%B1%8A%E9%9D%9E%E6%95%B0%E5%AD%A6%E7%B1%BB-%E5%88%9D%E8%B5%9B-2021.md
整理者：DREAMERhyh/ucas-cmc-2026。获取日期：2026-11-11。
来源仓库对其原创整理部分声明 CC BY-NC-SA 4.0；试题与官方答案仍归原权利人，不能据此认定已取得再分发授权。
本地处理：仅添加本来源说明，保留转录正文。社区转录未由本项目逐题核对；第七届参考答案来源标为非官方。 -->

# 第十三届全国大学生数学竞赛初赛试题及参考答案（非数学类）

> **年份**：2021 年（第十三届）｜**类别**：非数学专业（非数学类）
> **考试形式**：闭卷｜**时间**：150 分钟｜**满分**：100 分
> **来源**：扫描版参考答案（水印为大学生数学竞赛网 cmathc.org.cn）｜原始文件：`../第十三届全国大学生数学竞赛初赛（非数学类）试题及参考答案.pdf`
> **转录说明**：原卷为扫描版，本文件由视觉逐页转写，公式采用 KaTeX 语法；题面与「答案/解答」均来自原卷参考答案；原卷以「---------- n 分」标注过程分点，此处记作「……（n 分）」；原卷个别明显笔误已照抄原文并以「注」说明。

---

## 卷面结构

| 题号 | 一 | 二 | 三 | 四 | 五 | 六 | 总分 |
|---|---|---|---|---|---|---|---|
| 满分 | 30 | 14 | 14 | 14 | 14 | 14 | 100 |
| 形式 | 填空题 ×5 | 解答题 | 解答题 | 解答题 | 解答题 | 解答题 | |

---

## 一、填空题（本题满分 30 分，每小题 6 分）

**(1)** 极限 $\lim\limits_{x\to+\infty}\sqrt{x^2+x+1}\,\dfrac{x-\ln(e^x+x)}{x}=\underline{\qquad}$。

> **答案**：$0$
>
> **解答**：原式 $=\lim\limits_{x\to+\infty}\sqrt{x^2+x+1}\,\dfrac{x-\ln(e^x+x)}{x}=-\lim\limits_{x\to+\infty}\sqrt{1+\dfrac{1}{x}+\dfrac{1}{x^2}}\,\ln\left(1+\dfrac{x}{e^x}\right)=0$。

**(2)** 设 $z=z(x,y)$ 是由方程 $2\sin(x+2y-3z)=x+2y-3z$ 所确定的二元隐函数，则 $\dfrac{\partial z}{\partial x}+\dfrac{\partial z}{\partial y}=\underline{\qquad}$。

> **答案**：$1$
>
> **解答**：将方程两边分别关于 $x$ 和 $y$ 求偏导，得
> $$\begin{cases}
> 2\cos(x+2y-3z)\left(1-3\dfrac{\partial z}{\partial x}\right)=1-3\dfrac{\partial z}{\partial x},\\[6pt]
> 2\cos(x+2y-3z)\left(2-3\dfrac{\partial z}{\partial y}\right)=2-3\dfrac{\partial z}{\partial y}.
> \end{cases}$$
> 按 $\cos(x+2y-3z)=\dfrac{1}{2}$ 和 $\neq\dfrac{1}{2}$ 两种情形，都可解得：
> $$\begin{cases}
> \dfrac{\partial z}{\partial x}=\dfrac{1}{3},\\[6pt]
> \dfrac{\partial z}{\partial y}=\dfrac{2}{3}.
> \end{cases}$$
> 因此 $\dfrac{\partial z}{\partial x}+\dfrac{\partial z}{\partial y}=1$。

**(3)** 设函数 $f(x)$ 连续，且 $f(0)\neq 0$，则 $\lim\limits_{x\to 0}\dfrac{2\displaystyle\int_0^x (x-t)f(t)\,\mathrm{d}t}{x\displaystyle\int_0^x f(x-t)\,\mathrm{d}t}=\underline{\qquad}$。

> **答案**：$1$
>
> **解答**：原式 $=\lim\limits_{x\to 0}\dfrac{2x\displaystyle\int_0^x f(t)\,\mathrm{d}t-2\displaystyle\int_0^x tf(t)\,\mathrm{d}t}{x\displaystyle\int_0^x f(u)\,\mathrm{d}u}=\lim\limits_{x\to 0}\dfrac{2\displaystyle\int_0^x f(t)\,\mathrm{d}t+2xf(x)-2xf(x)}{\displaystyle\int_0^x f(u)\,\mathrm{d}u+xf(x)}$
> $$=\lim\limits_{x\to 0}\dfrac{2\displaystyle\int_0^x f(t)\,\mathrm{d}t}{\displaystyle\int_0^x f(u)\,\mathrm{d}u+xf(x)}=\lim\limits_{x\to 0}\dfrac{2xf(\xi)}{xf(\xi)+xf(x)}=1,$$
> 其中 $\xi$ 介于 $0,x$ 之间。

**(4)** 过三条直线 $L_1:\begin{cases}x=0,\\ y-z=2,\end{cases}$ $L_2:\begin{cases}x=0,\\ x+y-z+2=0,\end{cases}$ 与 $L_3:\begin{cases}x=\sqrt{2},\\ y-z=0\end{cases}$ 的圆柱面方程为 $\underline{\qquad}$。

> **答案**：$2x^2+y^2+z^2-2yz=4$
>
> **解答**：三条直线的对称式方程分别为
> $$L_1:\ \frac{x}{0}=\frac{y-1}{1}=\frac{z+1}{1},\qquad L_2:\ \frac{x}{0}=\frac{y-0}{1}=\frac{z-2}{1},\qquad L_2:\ \frac{x-\sqrt{2}}{0}=\frac{y-1}{1}=\frac{z-1}{1},$$
> 所以三条直线平行。
>
> 注：此处原卷疑为笔误，第三个对称式方程对应的应是直线 $L_3$（原卷标签印为 $L_2$）。
>
> 在 $L_1$ 上取点 $P_1(0,1,-1)$，过该点作与三直线都垂直的平面 $y+z=0$，分别交 $L_2$，$L_3$ 于点 $P_2(0,-1,1)$，$P_3(\sqrt{2},0,0)$。易知经过这三点的圆的圆心为 $O(0,0,0)$。这样，所求圆柱面的中心轴线方程为 $\dfrac{x}{0}=\dfrac{y}{1}=\dfrac{z}{1}$。
> 设圆柱面上任意点的坐标为 $Q(x,y,z)$，因为点 $Q$ 到轴线的距离均为 $\sqrt{2}$，所以有
> $$\frac{\left|(x,y,z)\times(0,1,1)\right|}{\sqrt{0^2+1^2+1^2}}=\sqrt{2},$$
> 化简即得所求圆柱面的方程为 $2x^2+y^2+z^2-2yz=4$。

**(5)** 记 $D=\{(x,y)\,|\,x^2+y^2\leq\pi\}$，则 $\displaystyle\iint_D\left(\sin x^2\cos y^2+x\sqrt{x^2+y^2}\right)\mathrm{d}x\mathrm{d}y=\underline{\qquad}$。

> **答案**：$\pi$
>
> **解答**：根据重积分的对称性，得
> $$\text{原式}=\iint_D\sin x^2\cos y^2\,\mathrm{d}x\mathrm{d}y=\iint_D\sin y^2\cos x^2\,\mathrm{d}x\mathrm{d}y$$
> $$=\frac{1}{2}\iint_D\left(\sin x^2\cos y^2+\sin y^2\cos x^2\right)\mathrm{d}x\mathrm{d}y$$
> $$=\frac{1}{2}\iint_D\sin(x^2+y^2)\,\mathrm{d}x\mathrm{d}y=\frac{1}{2}\int_0^{2\pi}\mathrm{d}\theta\int_0^{\sqrt{\pi}}r\sin r^2\,\mathrm{d}r$$
> $$=\frac{\pi}{2}\left.(-\cos r^2)\right|_0^{\sqrt{\pi}}=\pi.$$

---

## 二、（14 分）

设 $x_1=2021$，$x_n^2-2(x_n+1)x_{n+1}+2021=0$（$n\geq1$），证明数列 $\{x_n\}$ 收敛，并求极限 $\lim\limits_{n\to\infty}x_n$。

> **解答**：记 $a=1011$，$y_n=1+x_n$，函数 $f(x)=\dfrac{x}{2}+\dfrac{a}{x}$（$x>0$），则 $y_1=2a$，且
> $$y_{n+1}=f(y_n)\quad(n\geq1).$$
> ……（5 分）
>
> 易知，当 $x>\sqrt{2a}$ 时，$x>f(x)>\sqrt{2a}$，所以 $\{y_n\}$ 是单调减少且有下界的数列，因而收敛。由此可知 $\{x_n\}$ 收敛 ……（5 分）
>
> 令 $\lim\limits_{n\to\infty}y_n=A$，则 $A>0$ 且 $A=f(A)$，解得 $A=\sqrt{2a}$。因此 $\lim\limits_{n\to\infty}x_n=\sqrt{2022}-1$。……（4 分）

---

## 三、（14 分）

设 $f(x)$ 在 $[0,+\infty)$ 上是有界连续函数，证明：方程 $y''+14y'+13y=f(x)$ 的每一个解在 $[0,+\infty)$ 上都是有界函数。

> **证明**：易得对应的齐次方程 $y''+14y'+13y=0$ 的通解为
> $$y=C_1e^{-x}+C_2e^{-13x}.$$
> ……（4 分）
>
> 又由 $y''+14y'+13y=f(x)$，得 $(y''+y')+13(y'+y)=f(x)$。令 $y_1=y'+y$，则 $y_1'+13y_1=f(x)$，解得 $y_1=e^{-13x}\left(\displaystyle\int_0^x f(t)e^{13t}\,\mathrm{d}t+C_3\right)$。
>
> 同理，由 $y''+14y'+13y=f(x)$，得 $(y''+13y')+(y'+13y)=f(x)$。令 $y_2=y'+13y$，则 $y_2'+y_2=f(x)$，解得 $y_2=e^{-x}\left(\displaystyle\int_0^x f(t)e^t\,\mathrm{d}t+C_4\right)$。
>
> 取 $C_3=C_4=0$，得
> $$\begin{cases}
> y'+y=e^{-13x}\displaystyle\int_0^x f(t)e^{13t}\,\mathrm{d}t,\\
> y'+13y=e^{-x}\displaystyle\int_0^x f(t)e^t\,\mathrm{d}t,
> \end{cases}$$
> 由此解得原方程的一个特解为
> $$y^*=\frac{1}{12}e^{-x}\int_0^x f(t)e^t\,\mathrm{d}t-\frac{1}{12}e^{-13x}\int_0^x f(t)e^{13t}\,\mathrm{d}t.$$
> 因此，原方程的通解为
> $$y=C_1e^{-x}+C_2e^{-13x}+\frac{1}{12}e^{-x}\int_0^x f(t)e^t\,\mathrm{d}t-\frac{1}{12}e^{-13x}\int_0^x f(t)e^{13t}\,\mathrm{d}t.$$
> ……（6 分）
>
> 因为 $f(x)$ 在 $[0,+\infty)$ 上有界，所以，存在 $M>0$，使得 $|f(x)|\leq M$，$0\leq x<+\infty$，注意到当 $x\in[0,+\infty)$ 时，$0<e^{-x}\leq1$，$0<e^{-13x}\leq1$，所以
> $$|y|\leq|C_1|e^{-x}+|C_2|e^{-13x}+\frac{1}{12}e^{-x}\left|\int_0^x f(t)e^t\,\mathrm{d}t\right|+\frac{1}{12}e^{-13x}\left|\int_0^x f(t)e^{13t}\,\mathrm{d}t\right|$$
> $$\leq|C_1|+|C_2|+\frac{M}{12}e^{-x}\int_0^x e^t\,\mathrm{d}t+\frac{M}{12}e^{-13x}\int_0^x e^{13t}\,\mathrm{d}t$$
> $$\leq|C_1|+|C_2|+\frac{M}{12}\left(1-e^{-x}\right)+\frac{M}{12\times13}\left(1-e^{-13x}\right)$$
> $$\leq|C_1|+|C_2|+\frac{M}{12}+\frac{M}{12\times13}=|C_1|+|C_2|+\frac{7M}{78}.$$
> 对于方程的每一个确定的解，常数 $C_1$、$C_2$ 是固定的，所以，原方程的每一个解都是有界的。……（4 分）

---

## 四、（14 分）

对于 4 次齐次函数
$$f(x,y,z)=a_1x^4+a_2y^4+a_3z^4+3a_4x^2y^2+3a_5y^2z^2+3a_6x^2z^2,$$
计算曲面积分 $\displaystyle\oiint_\Sigma f(x,y,z)\,\mathrm{d}S$，其中 $\Sigma:\ x^2+y^2+z^2=1$。

> **解答**：因为 $f(x,y,z)$ 为 4 次齐次函数，所以对 $\forall t\in R$，恒有
> $$f(tx,ty,tz)=t^4f(x,y,z).$$
> 对上式两边关于 $t$ 求导，得
> $$xf_1'(tx,ty,tz)+yf_2'(tx,ty,tz)+zf_3'(tx,ty,tz)=4t^3f(x,y,z).$$
> 取 $t=1$，得
> $$xf_x'(x,y,z)+yf_y'(x,y,z)+zf_z'(x,y,z)=4f(x,y,z).$$
> ……（5 分）
>
> 设曲面 $\Sigma$ 上点 $(x,y,z)$ 处的外法线方向的方向余弦为 $(\cos\alpha,\cos\beta,\cos\gamma)$，则 $\cos\alpha=x,\cos\beta=y,\cos\gamma=z$，因此 ……（2 分）
> $$\oiint_\Sigma f(x,y,z)\,\mathrm{d}S=\frac{1}{4}\oiint_\Sigma\left(xf_x'(x,y,z)+yf_y'(x,y,z)+zf_z'(x,y,z)\right)\mathrm{d}S$$
> $$=\frac{1}{4}\oiint_\Sigma\left[\cos\alpha f_x'(x,y,z)+\cos\beta f_y'(x,y,z)+\cos\gamma f_z'(x,y,z)\right]\mathrm{d}S$$
> $$=\frac{1}{4}\oiint_\Sigma f_x'(x,y,z)\,\mathrm{d}y\,\mathrm{d}z+f_y'(x,y,z)\,\mathrm{d}z\,\mathrm{d}x+f_z'(x,y,z)\,\mathrm{d}x\,\mathrm{d}y$$
> $$=\frac{1}{4}\iiint_{x^2+y^2+z^2\leq1}\left[f_{xx}''(x,y,z)+f_{yy}''(x,y,z)+f_{zz}''(x,y,z)\right]\mathrm{d}x\mathrm{d}y\mathrm{d}z\quad\text{（利用高斯公式）}$$
> $$=\frac{3}{2}\iiint_{x^2+y^2+z^2\leq1}\left[x^2(2a_1+a_4+a_6)+y^2(2a_2+a_4+a_5)+z^2(2a_3+a_5+a_6)\right]\mathrm{d}x\mathrm{d}y\mathrm{d}z$$
> （利用轮换对称性）
> $$=\sum_{i=1}^6 a_i\iiint_{x^2+y^2+z^2\leq1}(x^2+y^2+z^2)\,\mathrm{d}x\mathrm{d}y\mathrm{d}z=\sum_{i=1}^6 a_i\int_0^{2\pi}\mathrm{d}\theta\int_0^{\pi}\mathrm{d}\varphi\int_0^1\rho^2\cdot\rho^2\sin\varphi\,\mathrm{d}\rho$$
> $$=\frac{4\pi}{5}\sum_{i=1}^6 a_i.$$
> ……（7 分）

---

## 五、（14 分）

设函数 $f(x)$ 在闭区间 $[a,b]$ 上有连续的二阶导数，证明：
$$\lim_{n\to\infty}n^2\left[\int_a^b f(x)\,\mathrm{d}x-\frac{b-a}{n}\sum_{k=1}^n f\left(a+\frac{2k-1}{2n}(b-a)\right)\right]=\frac{(b-a)^2}{24}\left[f'(b)-f'(a)\right].$$

> **证明**：记 $x_k=a+\dfrac{k(b-a)}{n}$，$\xi_k=a+\dfrac{(2k-1)(b-a)}{2n}$，$k=1,2,\cdots,n$。将 $f(x)$ 在 $[x_{k-1},x_k]$ 上展开成泰勒公式，得
> $$f(x)=f(\xi_k)+f'(\xi_k)(x-\xi_k)+\frac{f''(\eta_k)}{2}(x-\xi_k)^2,$$
> 其中 $x\in[x_{k-1},x_k]$，$\eta_k$ 介于 $0$ 和 $x$ 之间。
>
> 注：此处原卷疑为笔误，按泰勒公式的余项，$\eta_k$ 应介于 $\xi_k$ 和 $x$ 之间。
>
> 于是 ……（4 分）
> $$B_n=\int_a^b f(x)\,\mathrm{d}x-\frac{b-a}{n}\sum_{k=1}^n f\left(a+\frac{2k-1}{2n}(b-a)\right)=\sum_{k=1}^n\int_{x_{k-1}}^{x_k}\left(f(x)-f(\xi_k)\right)\mathrm{d}x$$
> $$=\sum_{k=1}^n\int_{x_{k-1}}^{x_k}\left[f'(\xi_k)(x-\xi_k)+\frac{f''(\eta_k)}{2}(x-\xi_k)^2\right]\mathrm{d}x=\frac{1}{2}\sum_{k=1}^n\int_{x_{k-1}}^{x_k}f''(\eta_k)(x-\xi_k)^2\,\mathrm{d}x.$$
> 设 $f''(x)$ 在 $[x_{k-1},x_k]$ 上的最大值和最小值分别为 $M_k$，$m_k$，因为
> $$\int_{x_{k-1}}^{x_k}(x-\xi_k)^2\,\mathrm{d}x=\frac{(b-a)^3}{12n^3},$$
> 所以
> $$\frac{(b-a)^2}{24}\sum_{k=1}^n m_k\frac{b-a}{n}\leq n^2B_n\leq\frac{(b-a)^2}{24}\sum_{k=1}^n M_k\frac{b-a}{n}.$$
> ……（6 分）
>
> 因为 $f''(x)$ 在 $[a,b]$ 上连续，所以 $f''(x)$ 在 $[a,b]$ 上可积。根据定积分 $\displaystyle\int_0^1 f''(x)\,\mathrm{d}x$ 的定义，及牛顿-莱布尼兹公式，得
>
> 注：此处原卷疑为笔误，结合上下文应为「根据定积分 $\displaystyle\int_a^b f''(x)\,\mathrm{d}x$ 的定义」。
>
> $$\lim_{n\to\infty}\sum_{k=1}^n m_k\frac{b-a}{n}=\lim_{n\to\infty}\sum_{k=1}^n M_k\frac{b-a}{n}=\int_a^b f''(x)\,\mathrm{d}x=f'(b)-f'(a).$$
> 再根据夹逼准则，得
> $$\lim_{n\to\infty}n^2B_n=\frac{(b-a)^2}{24}\left[f'(b)-f'(a)\right].$$
> ……（4 分）

---

## 六、（14 分）

设 $\{a_n\}$ 与 $\{b_n\}$ 均为正实数列，满足：$a_1=b_1=1$，且 $b_n=a_nb_{n-1}-2$，$n=2,3,\cdots$。又设 $\{b_n\}$ 为有界数列，证明级数 $\displaystyle\sum_{n=1}^{\infty}\frac{1}{a_1a_2\cdots a_n}$ 收敛，并求该级数的和。

> **解答**：首先，注意到 $a_1=b_1=1$，且 $a_n=\left(1+\dfrac{2}{b_n}\right)\dfrac{b_n}{b_{n-1}}$，所以当 $n\geq2$ 时，有
> $$a_1a_2\cdots a_n=\left(1+\frac{2}{b_2}\right)\left(1+\frac{2}{b_3}\right)\cdots\left(1+\frac{2}{b_n}\right)b_n.$$
> ……（4 分）
>
> 由于 $\{b_n\}$ 有界，故存在 $M>0$，使得当 $n\geq1$ 时，恒有 $0<b_n\leq M$。因此
> $$0<\frac{b_n}{a_1a_2\cdots a_n}=\left(1+\frac{2}{b_2}\right)^{-1}\left(1+\frac{2}{b_3}\right)^{-1}\cdots\left(1+\frac{2}{b_n}\right)^{-1}\leq\left(1+\frac{2}{M}\right)^{-n+1}\to 0,\quad n\to\infty$$
> 根据夹逼准则，$\lim\limits_{n\to\infty}\dfrac{b_n}{a_1a_2\cdots a_n}=0$。……（4 分）
>
> 考虑级数 $\displaystyle\sum_{n=1}^{\infty}\frac{1}{a_1a_2\cdots a_n}$ 的部分和 $S_n$，当 $n\geq2$ 时，有
> $$S_n=\sum_{k=1}^n\frac{1}{a_1a_2\cdots a_k}=\frac{1}{a_1}+\sum_{k=2}^n\frac{1}{a_1a_2\cdots a_k}\cdot\frac{a_kb_{k-1}-b_k}{2}$$
> $$=1+\frac{1}{2}\sum_{k=2}^n\left(\frac{b_{k-1}}{a_1a_2\cdots a_{k-1}}-\frac{b_k}{a_1a_2\cdots a_k}\right)$$
> $$=\frac{3}{2}-\frac{b_n}{2a_1a_2\cdots a_n},$$
> 所以 $\lim\limits_{n\to\infty}S_n=\dfrac{3}{2}$，这就证明了级数 $\displaystyle\sum_{n=1}^{\infty}\frac{1}{a_1a_2\cdots a_n}$ 收敛，且其和为 $\dfrac{3}{2}$。……（6 分）

---

## 附：本卷考点分布速览

| 题号 | 分值 | 考点板块 | 具体考点 |
|---|---|---|---|
| 一(1) | 6 | 极限 | 趋于无穷的极限、$\ln(e^x+x)$ 对数变形 |
| 一(2) | 6 | 多元微分 | 隐函数（含 $\sin$ 的方程）求偏导、分情形讨论 |
| 一(3) | 6 | 极限 | 变限积分求导、洛必达法则、积分中值定理 |
| 一(4) | 6 | 空间解析几何 | 过三条平行直线的圆柱面方程 |
| 一(5) | 6 | 二重积分 | 对称性化简、极坐标下 $\sin(x^2+y^2)$ 积分 |
| 二 | 14 | 数列极限 | 递推数列单调有界收敛、不动点法求极限 |
| 三 | 14 | 常微分方程 | 二阶常系数线性方程、解的有界性估计 |
| 四 | 14 | 曲面积分 | 齐次函数欧拉定理、高斯公式、轮换对称性 |
| 五 | 14 | 定积分 | 泰勒展开、黎曼和型渐近估计、夹逼准则 |
| 六 | 14 | 级数 | 正项级数收敛性判定与求和、裂项相消 |
