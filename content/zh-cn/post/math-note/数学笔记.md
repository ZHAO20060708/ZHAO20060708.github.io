---
title: 数学笔记
date: 2024-11-05
tags: 
    - math
categories:
    - learning
comments: true
---

## 例2
### 设$ \bm{X=\{1,2,...,n,...\},Y=\{1,3,.....2n-1,...\}} $, 对于任何一个$ \bm{n\in X} $ ,按照对应法则$ \bm{f} $得到$ \bm{2n-1\in Y} $,则映射$ \bm{f{:}X{\to}Y} $是一一映射.
#### 值得注意的是：$ \bm{Y} $是$ \bm{X} $ 的子集，$ \bm{Y} $中的元素似乎比$ \bm{X} $中的元素个数“少”,但实际是，在无限集合中，“部分可以等于整体”,这是无限集合的一个特性.$ \bm{\blacksquare} $
**并非所有的函数都有反函数**,如$ y=f(x)=x^2 $, 定义域为$ D_f=(-∞,+∞) $  
, 值域为$ R_f=[0,+∞) $,显然$ f $不是一一映射,所以该函数没有反函数.  
但如果函数$ y=f(x) $是单调函数,则相应的映射必为一一映射,而相应的反函数必存在,故有如下结论：  
**反函数存在定理**:单调函数$ f $必存在单调的反函数,且此反函数与$ f $具有相同的单调性。 

## 注意:
1. 不是任何两个的数都可以复合成一个复合函数的;  
例如，$ y = \arcsin u，u=2+x^2；y≠\arcsin(2+x^2) $
2. 复合函数可以由两个以上的函数经过复合构成。  
例如，$ y = \sqrt{\cot \frac x2}，y=\sqrt{u}，u=\cot v，v=\frac x2 $.

## 例9
### 判断函数 $ \bm{f(x)=\log_2\left(x+\sqrt{1+x^2}\right)} $的奇偶性.
### 解:
&emsp;&emsp;函数$ f(x) $的定义域为$ (-\infty,+\infty). $对$ \forall x $,由于

&emsp;&emsp;$ f(-x)=\log_{2}(-x+\sqrt{1+\left(-x\right)^{2}})=\log_{2}(\sqrt{1+x^{2}}-x)\\\\=\log_{2}\frac{1}{\sqrt{1+x^{2}}+x}=-\log_{2}(x+\sqrt{1+x^{2}})=-f(x), $

&emsp;&emsp;所以函数$ f(x)=\log_2(x+\sqrt{1+x^2}) $是奇函数

## 思考题1
### 已知$ \bm{f(x)} $是一个偶函数，且满足$ \bm{f(a+x)=f(a-x),} $则$ \bm{f(x)} $是不是一个周期函数？若是，则说明它的一个周期，若不是，请说明理由
### 思考题解答
由$ f(a+x)=f(a-x) $可知：

$ f(2a+x)=f[a+(a+x)]=f[a-(a+x)]=f\left(-x\right) $

又因为$ f(x) $是一个偶函数， 所以$ f(2a+x)=f(x) $

## 例1
### 求函数$ \bm{y=\sqrt{e^x+1}} $的反函数
### 解：
&emsp;&emsp;$ \because e^x=y^2-1 $  
&emsp;&emsp;$ \therefore x=\ln(y^2-1)\quad y=\sqrt{e^x+1}\gt1 $，即原函数的值域为$ (1,+\infty) $  
&emsp;&emsp;$ \therefore $反函数为$ y=\ln(x^2-1) $  
&emsp;&emsp;&emsp;$ \boldsymbol{D}_{f^{-1}}=(1,+\infty) $

## 例2
### 设$ \bm{f(\sin x)=\cos2x+1} $,求$ \bm{f(x)} $及$ \bm{f(\cos x).} $
### 解：
&emsp;&emsp;因为$ f(\sin x)=\cos2x+1=1-2\sin^2x+1=2-2\sin^2x, $  
&emsp;&emsp;所以$ f\left(x\right)=2-2x^{2},\quad f(\cos x)=2-2\cos^2x=2\sin^2x. $

## 例4
### 设函数 $ \bm{f(x)} $的定义域为$ \bm{(-l,l)} $, 证明必定存在$ \bm{(-l,l)} $上的偶函数$ \bm{g(x)} $及奇函数$ \bm{h(x)} $,使得$ \bm{f(x)=g(x)+h(x).} $
### 分析
&emsp;&emsp;如果这样的$ g(x) $和$ h(x) $存在，于是

$ \begin{cases}f(x)=g(x)+h(x)\\\\f(-x)=g(-x)+h(-x)=g(x)-h(x)\end{cases} $

### 证明
&emsp;&emsp;设

$ \begin{cases}g(x)=\frac12[f(x)+f(-x)]\\\\h(x)=\frac12[f(x)-f(-x)]\end{cases} $

&emsp;&emsp;显然$ f\left(x\right)=g\left(x\right)+h\left(x\right). $  
&emsp;&emsp;$ g\left(-x\right)=\frac12|f\left(-x\right)+f\left(x\right)|=|f\left(x\right) $是偶函数，  
&emsp;&emsp;$ -h(x)=\frac12[f(-x)-f(x)]=h(-x) $是奇函数.

已知 $ f(\tan x)=\sec^2x+1 $,求 $ f(x). $  
解：  
&emsp;&emsp;$ f(\tan x)=\left(\tan^2x+1\right)+1 $  
&emsp;&emsp;$ \therefore f\left(x\right)=\left(x^{2}+1\right)+1=x^{2}+2 $

## 思考题
### 分段函数一定不是初等函数吗？
### 解答
&emsp;&emsp;不一定

$y=\begin{cases}x&x\geq0\\\\-x&x<0\end{cases}$

&emsp;&emsp;它是一个分段函数， 但是，$ y=\left|x\right|=\sqrt{x^{2}} $ 根据定义，它是一个初等函数。

---

$ \sin x+\sin y=2\sin\frac{x+y}2\cos\frac{x-y}2 $

$ \sin x-\sin y=2\cos\frac{x+y}2\sin\frac{x-y}2 $

$ \cos x+\cos y=2\cos\frac{x+y}{2}\cos\frac{x-y}{2} $

$ \cos x-\cos y=-2\sin\frac{x+y}{2}\sin\frac{x-y}{2} $

$ \sin x\sin y=-\frac{1}{2}[\cos(x+y)-\cos(x-y)] $

$ \cos x\cos y=\frac12[\cos(x+y)+\cos(x-y)] $

$ \sin x\cos y=\frac{1}{2}[\sin(x+y)+\sin(x-y)] $

$ \sin x=\cos(x-\frac{\pi}{2}) $

$ \cos x=\sin(x+\frac{\pi}{2}) $

$ \cos^{2}x-\sin^{2}x=\cos2x $

$ \sin^{2}x+\cos^{2}x=1 $

$ \tan^{2}x+1=\sec^{2}x $

$ \sin 2x=2\sin x\cos x $

$ \cot^{2}x+1=\csc^{2}x $

$ \sin(x\pm y)=\sin x\cos y\pm\cos x\sin y $

$ \cos\left(x\pm y\right)=\cos x\cos y\mp\sin x\sin y $

$ \sin x+\sin y=2\sin\frac{x+y}{2}\cos\frac{x-y}{2} $

---

注意:数列极限的定义未给出求极限的方法。

## 例1：证明$ \bm{\lim_{n\to\infty}\frac{n+(-1)^{n-1}}n=1.} $

证：  
&emsp;&emsp;$ |x_n-1|=\left|\frac{n+(-1)^{n-1}}n-1\right|=\frac1n $  
&emsp;&emsp;任给$ \varepsilon\gt0 $，要$ |x_n-1|\lt\varepsilon $,只要$ \frac1n\lt\varepsilon, $或$ n\gt\frac1\varepsilon $，  
&emsp;&emsp;给定$ \frac1{100} $, 由$ \frac1n<\frac1{100} $,只要 $ n>100 $时，有$ |x_n-1|<\frac1{100} $,  
&emsp;&emsp;给定$ \frac1{1000} $,只要 $ n>1000 $ 时，有$ |x_n-1|<\frac1{1000} $,  
&emsp;&emsp;给定$ \frac1{10000} $,只要$ n>10000 $时，有$ |x_n-1|<\frac1{10000} $,  
&emsp;&emsp;给定 $ \varepsilon > 0 $, 只要 $ n>N(=\begin{bmatrix} \frac1\varepsilon\end{bmatrix}) $时，有$ |x_n-1|<\varepsilon $成立.

## 例2 设$ \bm{x_n\equiv C} $（$ \bm{C} $为常数），证明$ \bm{\lim_{n\to\infty} x_n=C.} $

证：  
&emsp;&emsp;任给$ \varepsilon>0 $,对于一切正整数$ n $,  
&emsp;&emsp;$ |x_n-C|=|C-C|=0<\varepsilon $成立，  
&emsp;&emsp;所以，$ \lim_{n\to\infty} x_n=C. $  
&emsp;&emsp;说明：常数列的极限等于同一常数。 

_**小结：用定义证明数列极限存在时，关键是任意给定$ \bm{\varepsilon>0} $,寻找$ \bm{N} $,但不必要求最小的$ \bm{N} $.**_

## 例3：设$ \bm{|q|<1} $,证明等比数列$ \bm{\lim_{n\to\infty}q^n=0} $.
证：  
q=0时，等式显然成立。当$ 0<|q|<1 $,$ |x_n-0|=|q^n-0|=|q|^n $  
$ \forall\varepsilon\in(0,1) $，要使$ \left|x_n-0\right|<\varepsilon $，只要$ \left|q\right|^n<\varepsilon $，  
即  
$ n\ln | q| < \ln \varepsilon $,亦即$ n> \frac {\ln \varepsilon }{\ln | q| }. $  
因此，取  $ N= \begin{bmatrix} \frac {\ln \varepsilon }{\ln | q| }\end{bmatrix} $，则当$ n> N $时，就有$ |q^n-0|<\varepsilon $,故$ \lim_{n\to\infty}q^n=0 $.

## 例4 证明数列 $ \bm{x_n=(-1)^{n+1}} $是发散的 .
证：  
&emsp;&emsp;设$ \lim_n\to\infty x_n=a $, 由定义，对于$ \varepsilon=\frac12 $,则$ \exists N $,使得当$ n>N $时，有$ |x_n-a|<\frac12 $成立，  
&emsp;&emsp;即当$ n>N $时$ , x_n\in ( a- \frac 12, a+ \frac 12) $, 区间长度为1.  
&emsp;&emsp;而$ x_n $无休止地反复取1，-1两个数，不可能同时位于长度为1的区间内.  
&emsp;&emsp;事实上，$ \{x_n\} $是有界的 ,但却发散.

$ (a+b) (a²-ab+b²)=a³+b³ $

## 根据极限定义证明：函数$ f(x) $当$ x $趋近于$ x_0 $时 极限存在的充分必要条件是左极限、右极限各自存在并且相等
为了证明这个定理，我们需要分别从充分性和必要性两个  方面进行证明。

### 充分性
假设函数 $ f(x) $ 在点 $ x_0 $ 处的左极限和右极限都存在且相等，即：

$ \lim_{x \to x_0^-} f(x) = L \quad \text{和} \quad \lim_{x \to x_0^+} f(x) = L $

我们需要证明函数 $ f(x) $ 在点 $ x_0 $ 处的极限存在并且等于 $ L $。

根据极限的定义，对于任意给定的小正数$ \epsilon > 0 $，存在一个delta > 0，使得当$ 0 < |x - x_0| < \delta $ 时，有：

$ |f(x) - L| < \epsilon $

这个 delta 可以同时适用于左极限和右极限的定义。因为无论 $ x $ 是从左边还是右边接近$ x_0 $，只要 $ x $ 距离 $ x_0 $ 的距离小于$ \delta $，$ f(x) $ 都会靠近 $ L $ 并且与 $ L $的差小于 $ \epsilon $。

因此，当 $ x $ 趋近于 $ x_0 $ 时，无论从left 或 right，$ f(x) $ 的极限都是 $ L $。所以，函数 $ f(x) $ 在点 $ x_0 $ 处的极限存在并且等于 $ L $。

### 必要性
假设函数 $ f(x) $ 在点 $ x_0 $ 处的极限存在，记为  
$ L $，即：

$ \lim_{x \to x_0} f(x) = L $

我们需要证明函数 $ f(x) $ 在点 $ x_0 $ 处的左极限和右极限都存在并且相等。

由于 $ f(x) $ 的极限在 $ x_0 $ 存在，对于任意给定的小正数 $ \epsilon > 0 $，存在一个delta > 0，使得当$ 0 < |x - x_0| < \delta $ 时，有：

$ |f(x) - L| < \epsilon $

现在我们来分别考虑左极限和右极限。

1. **左极限**：对于任意 $ \epsilon > 0 $，存在  
$ \delta^- > 0 $ 使得当 $ 0 < x_0 - x < \delta^- $ 时，有：

$$|f(x) - L| < \epsilon$$

这说明当 $ x $ 从左边接近 $ x_0 $ 时，$ f(x) $ 趋近于$ L $。

2. **右极限**：对于任意 $ \epsilon > 0 $，存在$ \delta^+ > 0 $ 使得当 $ 0 < x - x_0 <\delta^+ $ 时，有：

$$|f(x) - L| < \epsilon$$

这说明当 $ x $ 从右边接近 $ x_0 $ 时，$ f(x) $ 趋近于$ L $。

由于上述两个条件对于任意的 $ \epsilon > 0 $ 都可以找到对应的 $ \delta^- > 0 $ 和 $ \delta^+ > 0 $，这意味着：

$ \lim_{x \to x_0^-} f(x) = L \quad \text{和}
\quad \lim_{x \to x_0^+} f(x) = L $

因此，函数 $ f(x) $ 在点 $ x_0 $ 处的左极限和右极限都存在并且相等。

### 结论
综上所述，我们证明了：

+ 如果函数 $ f(x) $ 在点 $ x_0 $ 处的左极限和右极限都存在且相等，那么函数 $ f(x) $ 在点 $ x_0 $ 处的极限存在，并且等于这两个极限的共同值。
+ 反之，如果函数 $ f(x) $ 在点 $ x_0 $ 处的极限存在，那么它的左极限和右极限也一定存在并且相等。

所以，函数 $ f(x) $ 在点 $ x_0 $ 处的极限存在的充分必要条件是其左极限和右极限都存在且相等。

根据复合函数求导法则，
$ \frac{d}{dx} f(u) = f^\prime(u) \cdot u^\prime $

当 $ x \to 0 $ 时，  
$ x \sim \sin x \sim \tan x \sim \arcsin x \sim \arctan x \sim \ln(1 + x) \sim e^x - 1 $;  
$ 1 - \cos x \sim \frac{x^2}{2} $;  
$ (1 + x)^a - 1 \sim ax\ (a \neq 0) $;  
$ a^x - 1 \sim x \ln a(a > 0, a \neq 1) $.

## 基本初等函数的求导公式
(1) $ (C)&#39;= 0 $$ (C为常数)

(2) $(x<sup>\mu)' = \mu x</sup>{\mu - 1}$ 

(3)  $(\sin x)' = \cos x$ 

(4)  $(\cos x)' = - \sin x$ 

(5)  $(\tan x)' = \sec^2 x$ 

(6)  $(\cot x)' = - \csc^2 x$ 

(7)  $(\sec x)' = \sec x \tan x$ 

(8)  $(\csc x)' = - \csc x \cot x$ 

(9)  $(a<sup>x)' = a</sup>x \ln a$ 

(10)  $(e<sup>x)' = e</sup>x$ 

(11)  $(\log_a x)' = \frac{1}{x \ln a}$ 

(12)  $(\ln x)' = \frac{1}{x}$ 

(13)  $(\arcsin x)' = \frac{1}{\sqrt{1 - x^2}}$ 

(14)  $(\arccos x)' = \frac{-1}{\sqrt{1 - x^2}}$ 

(15)  $(\arctan x)' = \frac{1}{1 + x^2}$ 

(16)  $(\text{arccot } x)' = \frac{-1}{1 + x^2}$

## 基本初等函数的微分公式
(1) $ \mathrm{d}C = 0 $ (c为常数)  

(2) $ \mathrm{d}x^\mu = \mu x^{\mu - 1} \mathrm{d}x $  

(3) $ \mathrm{d} \sin x = \cos x \mathrm{d}x $  

(4) $ \mathrm{d} \cos x = - \sin x \mathrm{d}x $  

(5) $ \mathrm{d} \tan x = \sec^2 x \mathrm{d}x $  

(6) $ \mathrm{d} \cot x = - \csc^2 x \mathrm{d}x $  

(7) $ \mathrm{d} \sec x = \sec x \tan x \mathrm{d}x $  

(8) $ \mathrm{d} \csc x = - \csc x \cot x \mathrm{d}x $  

(9) $ \mathrm{d}a^x = a^x \ln a \mathrm{d}x $  

(10) $ \mathrm{d}e^x = e^x \mathrm{d}x $  

(11) $ \mathrm{d} \log_a x = \frac{1}{x \ln a} \mathrm{d}x $  

(12) $ \mathrm{d} \ln x = \frac{1}{x} \mathrm{d}x $

(13)  $\mathrm{d} \arcsin x = \frac{1}{\sqrt{1 - x^2}} \mathrm{d}x$ 

(14)  $\mathrm{d} \arccos x = \frac{-1}{\sqrt{1 - x^2}} \mathrm{d}x$ 

(15)  $\mathrm{d} \arctan x = \frac{1}{1 + x^2} \mathrm{d}x$ 

(16)  $\mathrm{d} \text{ arccot } x = \frac{-1}{1 + x^2} \mathrm{d}x$


## 一些需要注意的点
* 存在原函数的偶函数其原函数不一定是奇函数。只有当原函数中的常数项为 0 时，原函数才是奇函数。
* 收敛数列的性质
    1. 收敛数列极限唯一
    2. 收敛数列必有界
    * 推论
        * 无界数列必发散（2.的逆否命题）
        * 有界数列未必收敛
    3. 保号性
    * 若$x_n→a,y_n→b$，则$\exists N \in \bold{N^+}$，当$n > N$ 时，有$x_n>y_n$.
    * 若$x_n→a$，且$a < 0(a > 0)$，则$\exists N \in \bold{N^+}$，当$n > N$ 时，有$x_n<0(x_n>0)$.
    * 推论：
        * $x_n→a,y_n→b$，若$x_n \geq y_n$，则$a\geq b$.
        * $x_n→a,y_n→b$，若$x_n \geq y_n$，则$a\geq b$.

## 麦克劳林级数
### 几何级数
$\frac{1}{1 - x} = \sum_{n=0}^{\infty} x^n = 1 + x + x^2 + x^3 + ... + x^n + ... \qquad \forall x:|x| < 1$
### 二项式级数
$\sum_{n=0}^{\infty} \binom{n}{k} x^n = (1 + x)^k=1 + kx + \frac{k(k-1)}{2!}x^2 + \frac{k(k-1)(k-2)}{3!}x^3 + ... + \frac{k(k-1)...(k-n+1)}{n!}x^n + ... \qquad \forall x: |x| < 1, \forall k: k \in \mathbb{C}$
### 指数函数
$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + ... + \frac{x^n}{n!} + ... \qquad \forall x$
### 自然对数
$\ln(1 - x) = \sum_{n=1}^{\infty} \frac{x^n}{n} = -x + \frac{x^2}{2} - \frac{x^3}{3} + ... + (-1)^{n+1} \frac{x^n}{n} + ... \qquad \forall x: |x| < 1$

$\ln(1 + x) = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - ... + (-1)^{n+1} \frac{x^n}{n} + ... \qquad \forall x: |x| < 1$
### 三角函数
$\sin x = \sum_{n = 0}^{\infty} \frac{(-1)^n x^{2n + 1}}{(2n + 1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots \quad \forall x$

$\cos x = \sum_{n = 0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots \quad \forall x$

$\tan x = \sum_{n = 1}^{\infty} \frac{B_{2n} (-4)^n (1 - 4^n)}{(2n)!} x^{2n - 1} = x + \frac{2x^5}{15} + \cdots \quad \forall x : |x| < \frac{\pi}{2}$

$\sec x = \sum_{n = 0}^{\infty} \frac{(-1)^n E_{2n} x^{2n}}{(2n)!} = 1 + \frac{x^2}{2} + \frac{5x^4}{24} + \cdots \quad \forall x : |x| < \frac{\pi}{2}$

$\arcsin x = \sum_{n = 0}^{\infty} \frac{(2n)!}{4^n (n!)^2 (2n + 1)} x^{2n + 1} = x + \frac{x^3}{6} + \frac{3x^5}{40} + \cdots \quad \forall x : |x| \leq 1$

$\arccos x = \frac{\pi}{2} - \arcsin x = \frac{\pi}{2} - \sum_{n = 0}^{\infty} \frac{(2n)!}{4^n (n!)^2 (2n + 1)} x^{2n + 1} = \frac{\pi}{2} - x - \frac{x^3}{6} - \frac{3x^5}{40} + \cdots \quad \forall x : |x| \leq 1$

$\arctan x = \sum_{n = 0}^{\infty} \frac{(-1)^n x^{2n + 1}}{2n + 1} = x - \frac{x^3}{3} + \frac{x^5}{5} - \cdots \quad \forall x : |x| \leq 1, x \neq \pm i$