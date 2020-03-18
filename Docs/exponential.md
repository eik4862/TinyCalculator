# Class Exp

> Exponential and logarithm function toolbox.

> [!DANGER]
> This class is implemented as an [abstract class](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html) of JAVA.
That is, it cannot be initialized or instantiated.
If one tries to instantiate this class, it will throw `NotImplementedError` at `__init__`.
Since all methods are class method, one should use them as `Exp.chk_t`.

Class `Exp` supports following usual trigonometric functions and inverse of them.

| Function | Definition | Domain | Range |
| --- | --- | --- | --- |
| `Exp[x]` | $\exp(x) = \sum_{n=0}^\infty\frac{x^n}{n!}$ | $\mathbb{R}$ | $\mathbb{R}^+$ |
| `Log[x, y]` | $\log_y(x) = \frac{\log(x)}{\log(y)}$ | $\mathbb{R}^+\times(\mathbb{R}^+\setminus\{1\})$ | $\mathbb{R}$ |
| `Colog[x, y]` | $\mathrm{colog}_y(x) = -\log_y(x)$ | $\mathbb{R}^+\times(\mathbb{R}^+\setminus\{1\})$ | $\mathbb{R}$ |
| `Napierainlog[x]` | $\mathrm{NapLog}(x) = \log_{10^7/(10^7-1)}\left(\frac{10^7}{x}\right)$ | $\mathbb{R}^+$ | $\mathbb{R}$ |
| `Pow[x, y]` | $x^y = \exp(y\log(x))$ | Refer to the note | $\mathbb{R}$ |
| `Sqrt[x]` | $\sqrt{x}=x^{1/2}$ | $\mathbb{R}^+_0$ | $\mathbb{R}^+_0$ |
| `Root[x, n]` | $\sqrt[n]{x}=x^{1/n}$ | $\mathbb{R}^+_0\times2\mathbb{N}\cup\mathbb{R}\times(2\mathbb{N}-1)$ | $\mathbb{R}$ |
| `Log2[x]` | $\log_2(x)$ | $\mathbb{R}^+$ | $\mathbb{R}$ |
| `Log10[x]` | $\log_{10}(x)$ | $\mathbb{R}^+$ | $\mathbb{R}$ |
| `Tetra[x, n]` | $^nx = \underbrace{x^{x^{\cdot^{\cdot^x}}}}_n$ | $(\mathbb{Z}^-\cup\mathbb{R}^+_0)\times\mathbb{N}$ | Refer to the note |
| `Nestlog[x, n]` | $\log_n(x) = \underbrace{\log\cdots\log}_n(x)$ | Refer to the note | $\mathbb{R}$ |

> [!NOTE]
> 1. One can easily show that power series definition of exponential function have radius of convergence $\infty$ so that they are indeed well-defined.
2. In the definition of log function, $\log(x)$ is defined as the inverse function of $\exp$.
3. The given definition of power function is only valid for $(x,\,y)\in\mathbb{R}^+\times\mathbb{R}$.
    To expand this definition for $x\in\mathbb{R}^-_0$, we employ following (reasonable) rules.
    1. $x^0=1$ for any $x\in\mathbb{R}$. This means that we employ a convention $0^0=1$.
    2. $(-1)^y$ is $1$ if $y$ is even and is $-1$ if $y$ is odd. If $y$ is noninteger, it is not defined. (Note that this coincides with rule 1 since $(-1)^0=1$.)
    3. $0^y$ is $1$ if $y=0$ and is $0$ if $y>0$. If $y<0$, it is not defined.
    4. $x^y$ is $[\mathrm{sgn}(x)]^y|x|^y$ for $x\ne0$. This implies that for $x<0$, $y$ must be integer for $x^y$ to be defined.
    Here, $\mathrm{sgn}$ is sign function defined as
    $$
        \mathrm{sgn}(x)=\begin{dcases}
            1&\textrm{when }x>0\\
            0&\textrm{when }x=0\\
            -1&\textrm{ow.}
        \end{dcases}
    $$
    With this extended definition of power function, its domain will be $\mathbb{R}^+\times\mathbb{R}\cup\{0\}\times\mathbb{R}^+_0\cup\mathbb{R}^-\times\mathbb{Z}$.
    (Note that with this definition, $(-27)^{1/3}$ is not defined.)

We present some simple graph of functions above.
Following plots are computed and rendered by MATLAB and one can read detailed description on these code at ...

<center>
<!-- tabs:start -->
#### ** Exp **
![Exp_Graph](Figures/Exp_Graph.eps)

__Figure 1__. Graph of $\exp(x)$ on $[-3,\,3]$.<br/>
Here, $x$ axis is asymptotic line of exponential function.

#### ** Log **
![Log_Graph](Figures/Log_Graph.eps)

__Figure 2__. Graph of $\log_y(x)$ on $[0,\,3]^2$.<br/>
Here, $x=0$, $y=1$, and $z=0$ are asymptotic plane of log function.

#### ** Pow **
![Pow_Graph](Figures/Pow_Graph.eps)

__Figure 3__. Graph of $x^y$ on $[0,\,3]\times[-3,\,3]$.<br/>
Here, $x=0$,and $z=0$ are asymptotic plane of power function.

#### ** Pow (integer exponent) **
![Pow2_Graph](Figures/Pow2_Graph.eps)

__Figure 4__. Graph of $x^y$ where $y\in\mathbb{Z}$ on $[-3,\,3]$.<br/>
Gray dashe is asymptotic line of power function with integer exponent, $x=0$ with $x$ axis.

#### ** Sqrt **
![Sqrt_Graph](Figures/Sqrt_Graph.eps)

__Figure 5__. Graph of $\sqrt{x}$ on $[0,\,5]$.

#### ** Log2 **
![Log2_Graph](Figures/Log2_Graph.eps)

__Figure 6__. Graph of $\log_2(x)$ on $[0,\,5]$.<br/>
Here, $x$ axis and $y$ axis are asymptotic line of log function with base 2.

#### ** Log10 **
![Log10_Graph](Figures/Log10_Graph.eps)

__Figure 7__. Graph of $\log_{10}(x)$ on $[0,\,5]$.<br/>
Here, $x$ axis and $y$ axis are asymptotic line of log function with base 10.
<!-- tabs:end -->
</center>

For more information on exponential and logarithm functions, refer to following references.
- [http://mathworld.wolfram.com/Sine.html](http://mathworld.wolfram.com/Sine.html)
- [http://mathworld.wolfram.com/Cosine.html](http://mathworld.wolfram.com/Cosine.html)
- [http://mathworld.wolfram.com/Tangent.html](http://mathworld.wolfram.com/Tangent.html)
- [http://mathworld.wolfram.com/Cosecant.html](http://mathworld.wolfram.com/Cosecant.html)
- [http://mathworld.wolfram.com/Secant.html](http://mathworld.wolfram.com/Secant.html)
- [http://mathworld.wolfram.com/Cotangent.html](http://mathworld.wolfram.com/Cotangent.html)
- [http://mathworld.wolfram.com/InverseSine.html](http://mathworld.wolfram.com/InverseSine.html)
- [http://mathworld.wolfram.com/InverseCosine.html](http://mathworld.wolfram.com/InverseCosine.html)
- [http://mathworld.wolfram.com/InverseTangent.html](http://mathworld.wolfram.com/InverseTangent.html)
- [http://mathworld.wolfram.com/InverseCosecant.html](http://mathworld.wolfram.com/InverseCosecant.html)
- [http://mathworld.wolfram.com/InverseSecant.html](http://mathworld.wolfram.com/InverseSecant.html)
- [http://mathworld.wolfram.com/InverseCotangent.html](http://mathworld.wolfram.com/InverseCotangent.html)

## __sign
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-info">const</span> <span class="badge badge-pill badge-secondary">class variable</span>
- Type: `Final[Dict[FunT, List[Sign]]]`
- Value
```python
    {
        FunT.EXP: [Sign([T.NUM], T.NUM, FunT.EXP)],
        FunT.LOG: [Sign([T.NUM], T.NUM, FunT.LOG),
                        Sign([T.NUM, T.NUM], T.NUM, FunT.LOG)],
        FunT.POW: [Sign([T.NUM, T.NUM], T.NUM, FunT.POW)],
        FunT.SQRT: [Sign([T.NUM], T.NUM, FunT.SQRT)],
        FunT.LOG2: [Sign([T.NUM], T.NUM, FunT.LOG2)],
        FunT.LOG10: [Sign([T.NUM], T.NUM, FunT.LOG10)]
    }
```

Function calling signatures of trigonometric functions and their inverses for type checking.

## __exp(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where exponential function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of exponential function. |

It is simple helper for `simplify` computing `Exp[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Exp[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: |
| `Exp[x]` | `nan` | $0$ | $\exp(x)$ | `inf` |

The value of $\exp(x)$ is computed using `math.exp` in basic Python math package `math`.
The implementation of `math.exp` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `exp` function in `cmath` library.
Unfortunately, the implementation `exp` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Exp[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Exp_Small](Figures/Exp_Small.eps)

__Figure 1__. Error of `Exp[x]` on $[0,\,2\pi]$. Input points are drawn randomly from $\mathbf{U}(0,\,2\pi)$.

#### ** Medium input **
![Exp_Medium](Figures/Exp_Medium.eps)

__Figure 2__. Error of `Exp[x]` on $[-100\pi,\,100\pi]$. Input points are drawn randomly from $\mathbf{U}(-100\pi,\,100\pi)$.

#### ** Large input **
![Exp_Large](Figures/Exp_Large.eps)

__Figure 3__. Error of `Exp[x]` on $[-10^{10}\pi,\,10^{10}\pi]$. Input points are drawn randomly from $\mathbf{U}(-10^{10}\pi,\,10^{10}\pi)$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

> [!NOTE]
> Theoretically, `Exp[x]` is equivalent to `Pow[E, x]`, but `Exp[x]` is more accurate.
For example, `Pow[E, Pi]` gives `23.140692632779263249176437966525` but `Exp[Pi]` gives `23.140692632779266801890116767026` where the actual value is `23.140692632779269005729086367948` (computed by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300).
The former has absolute error about `5.7566e-15` but the latter has absolute error about `2.2038e-15`.

## __log(x, y)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Exponent where log function is to be computed. |
| `y` | `float` | Base where log function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of cosine function. |

It is simple helper for `simplify` computing `Log[x, y]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Log[x, y]` is as follows.

| `y\x` | `nan` | `-inf` | $\mathbb{R}^-$ | $0$ | $\mathbb{R}^+$ | `inf` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| __`nan`__ | `nan` | `nan` | `nan` | `nan` | `nan` | `nan` |
| __`-inf`__ | `nan` | `nan` | `nan` | `nan` | `nan` | `nan` |
| $\mathbb{R}^-$ | `nan` | `nan` | `nan` | `nan` | `nan` | `nan` |
| $0$ | `nan` | `nan` | `nan` | `nan` | $0$ | `nan` |
| $(0,\,1)$ | `nan` | `nan` | `nan` | `inf` | $\log_y(x)$ | `-inf` |
| $1$ | `nan` | `nan` | `nan` | `nan` | `nan` | `nan` |
| $(1,\,\infty)$ | `nan` | `nan` | `nan` | `-inf` | $\log_y(x)$ | `inf` |
| __`inf`__ | `nan` | `nan` | `nan` | `nan` | $0$ | `nan` |

The value of $\log_y(x)$ is computed using `math.log` in basic Python math package `math`.
The implementation of `math.log` depends on Python interpreter.
In case of CPython, it is implemented as `log(x) / log(y)` where `log` is a thin wrapper wrapping `log` function in `cmath` library.
Unfortunately, the implementation `log` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Log[x, y]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Log_Small](Figures/Log_Small.eps)

__Figure 1__. Error of `Log[x, y]` on $[0,\,2\pi]$. Input points are drawn randomly from $\mathbf{U}(0,\,2\pi)$.

#### ** Medium input **
![Log_Medium](Figures/Log_Medium.eps)

__Figure 2__. Error of `Log[x, y]` on $[-100\pi,\,100\pi]$. Input points are drawn randomly from $\mathbf{U}(-100\pi,\,100\pi)$.

#### ** Large input **
![Log_Large](Figures/Log_Large.eps)

__Figure 3__. Error of `Log[x, y]` on $[-10^{10}\pi,\,10^{10}\pi]$. Input points are drawn randomly from $\mathbf{U}(-10^{10}\pi,\,10^{10}\pi)$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __pow(x, y)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Base where power function is to be computed. |
| `y` | `float` | Exponent where power function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of power function. |

It is simple helper for `simplify` computing `Pow[x, y]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Pow[x, y]` is as follows.

| `y\x` | `nan` | `-inf` | $(-\infty,\,-1)$ | $-1$ | $(-1,\,0)$ | $0$ | $(0,\,1)$ | $1$ | $(1,\,\infty)$ | `inf` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| __`nan`__ | `nan` | `nan` | `nan` | `nan` | `nan` | `nan` | `nan` | `nan` | `nan` | `nan` |
| __`-inf`__ | `nan` | $0$ | $0$ | `nan` | `nan` | `nan` | `inf` | $1$ | $0$ | $0$ |
| $\mathbb{Z}^-$ | `nan` | $0$ | $x^y$ | $(-1)^y$ | $x^y$ | `nan` | $x^y$ | $1$ | $x^y$ | $0$ |
| $\mathbb{R}^-\setminus\mathbb{Z}^-$ | `nan` | `nan` | `nan` | `nan` | `nan` | `nan` | $x^y$ | $1$ | $x^y$ | $0$ |
| $0$ | `nan` | `nan` | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | `nan` |
| $\mathbb{R}^+\setminus\mathbb{N}$ | `nan` | `nan` | `nan` | `nan` | `nan` | $0$ | $x^y$ | $1$ | $x^y$ | `inf` |
| $2\mathbb{N}$ | `nan` | `inf` | $x^y$ | $1$ | $x^y$ | $0$ | $x^y$ | $1$ | $x^y$ | `inf` |
| $2\mathbb{N}-1$ | `nan` | `-inf` | $x^y$ | $-1$ | $x^y$ | $0$ | $x^y$ | $1$ | $x^y$ | `inf` |
| __`inf`__ | `nan` | `nan` | `nan` | `nan` | $0$ | $0$ | $0$ | $1$ | `inf` | `inf` |

The value of $x^y$ is computed using `math.pow` in basic Python math package `math`.
The implementation of `math.pow` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `pow` function in `cmath` library.
Unfortunately, the implementation `pow` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Pow[x, y]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Pow_Small](Figures/Pow_Small.eps)

__Figure 1__. Error of `Pow[x, y]` on $[-\pi/2,\,\pi/2]$. Input points are drawn randomly from $\mathbf{U}(-\pi/2,\,\pi/2)$.

#### ** Medium input **
![Pow_Medium](Figures/Pow_Medium.eps)

__Figure 2__. Error of `Pow[x, y]` on $[-50\pi,\,50\pi]$. Input points are drawn randomly from $\mathbf{U}(-50\pi,\,50\pi)$.

#### ** Large input **
![Pow_Large](Figures/Pow_Large.eps)

__Figure 3__. Error of `Pow[x, y]` on $[-10^{10}\pi/2,\,10^{10}\pi/2]$. Input points are drawn randomly from $\mathbf{U}(-10^{10}\pi/2,\,10^{10}\pi/2)$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __sqrt(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where square root function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of square root function. |

It is simple helper for `simplify` computing `Sqrt[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Sqrt[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}^-$ | $\mathbb{R}^+_0$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Sqrt[x]` | `nan` | `nan` | `nan` | $\sqrt{x}$ | `nan` |

The value of $x^y$ is computed using `math.sqrt` in basic Python math package `math`.
The implementation of `math.sqrt` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `sqrt` function in `cmath` library.
Unfortunately, the implementation `sqrt` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Sqrt[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Sqrt_Small](Figures/Sqrt_Small.eps)

__Figure 1__. Error of `Sqrt[x]` on $[0,\,2\pi]$. Input points are drawn randomly from $\mathbf{U}(0,\,2\pi)$.

#### ** Medium input **
![Sqrt_Medium](Figures/Sqrt_Medium.eps)

__Figure 2__. Error of `Sqrt[x]` on $[-100\pi,\,100\pi]$. Input points are drawn randomly from $\mathbf{U}(-100\pi,\,100\pi)$.

#### ** Large input **
![Sqrt_Large](Figures/Sqrt_Large.eps)

__Figure 3__. Error of `Sqrt[x]` on $[-10^{10}\pi,\,10^{10}\pi]$. Input points are drawn randomly from $\mathbf{U}(-10^{10}\pi,\,10^{10}\pi)$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __log2(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where log function with base 2 is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of log function with base 2. |

It is simple helper for `simplify` computing `Log2[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Log2[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}^-$ | $0$ | $\mathbb{R}^+$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| `Log2[x]` | `nan` | `nan` | `nan` | `-inf` | $\log_2(x)$ | `inf` |

The value of $\log_2(x)$ is computed using `math.log2` in basic Python math package `math`.
The implementation of `math.log2` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `log2` function in `cmath` library.
Unfortunately, the implementation `log2` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Log2[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Log2_Small](Figures/Log2_Small.eps)

__Figure 1__. Error of `Log2[x]` on $[0,\,2\pi]$. Input points are drawn randomly from $\mathbf{U}(0,\,2\pi)$.

#### ** Medium input **
![Log2_Medium](Figures/Log2_Medium.eps)

__Figure 2__. Error of `Log2[x]` on $[-100\pi,\,100\pi]$. Input points are drawn randomly from $\mathbf{U}(-100\pi,\,100\pi)$.

#### ** Large input **
![Log2_Large](Figures/Log2_Large.eps)

__Figure 3__. Error of `Log2[x]` on $[-10^{10}\pi,\,10^{10}\pi]$. Input points are drawn randomly from $\mathbf{U}(-10^{10}\pi,\,10^{10}\pi)$.
<!-- tabs:end -->

> [!NOTE]
> Theoretically, `Log2[x]` is equivalent to `Log[x, 2]`, but `Log2[x]` is more accurate.
For example, `Log[Pi, 2]` gives `1.651496129472319` but `Log2[Pi]` gives `1.6514961294723187` where the actual value is `1.651496129472318798043279295108` (computed by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300).
The former has absolute error about `1.4307e-16` but the latter has absolute error about `7.8976e-17`.

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __log10(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where log function with base 10 is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of log function with base 10. |

It is simple helper for `simplify` computing `Log10[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Log10[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}^-$ | $0$ | $\mathbb{R}^+$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| `Log10[x]` | `nan` | `nan` | `nan` | `-inf` | $\log_{10}(x)$ | `inf` |

The value of $\log_{10}(x)$ is computed using `math.log10` in basic Python math package `math`.
The implementation of `math.log10` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `log10` function in `cmath` library.
Unfortunately, the implementation `log10` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Log10[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Log10_Small](Figures/Log10_Small.eps)

__Figure 1__. Error of `Log10[x]` on $[-\pi/2,\,\pi/2]$. Input points are drawn randomly from $\mathbf{U}(-\pi/2,\,\pi/2)$.

#### ** Medium input **
![Log10_Medium](Figures/Log10_Medium.eps)

__Figure 2__. Error of `Log10[x]` on $[-50\pi,\,50\pi]$. Input points are drawn randomly from $\mathbf{U}(-50\pi,\,50\pi)$.

#### ** Large input **
![Log10_Large](Figures/Log10_Large.eps)

__Figure 3__. Error of `Log10[x]` on $[-10^{10}\pi/2,\,10^{10}\pi/2]$. Input points are drawn randomly from $\mathbf{U}(-10^{10}\pi/2,\,10^{10}\pi/2)$.
<!-- tabs:end -->

> [!NOTE]
> Theoretically, `Log10[x]` is equivalent to `Log[x, 10]`, but `Log10[x]` is more accurate.
For example, `Log[Pi, 10]` gives `0.4971498726941338` but `Log10[Pi]` gives `0.49714987269413385` where the actual value is `0.497149872694133854351268288290` (computed by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300).
The former has absolute error about `5.5684e-17` but the latter has absolute error about `1.7278e-19`.

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## chk_t(rt)
<span class="badge badge-pill badge-success">public</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `rt` | `FunTok` | Root token of partial AST to be type checked. |

- Returns

| Type | Description |
| --- | --- |
| `Optional[List[Sign]]` | `None` if type check is successful. Candidate signatures if not. |

It takes the root token of partial AST `rt` and do type check for `rt` token.
Since it uses the inferred type of children of `rt`, type checking of `rt`'s children should be preceded before calling this method.
Also, `rt`'s token value must be one of exponential or logarithm functions listed [above](#class-exp).
After type checking, it will fill in `t` field of `rt` with inferred return type in case of no type error.

For type checking, it first constructs _inferred signature_ of `rt` using its children's inferred type and `__sign`.
Then it finds _candidate signatures_ of `rt` from `__sign` which is basically a list of all possible valid calling signatures.
With this inferred signature and candidate signatures, it can simply determine whether the user input is valid or not.
If there is a matching signature among candidates, it is valid. Otherwise, it is not.
If there is match, then it fills in `t` field of `rt` with return type of inferred signature (which will be `T.NUM` always) and terminates by returning `None`.
Otherwise, it immediately terminates by returning the list of candidate signatures.
Caller of this method can tell the existence of type error by inspecting its return value and use returned candidate signature information for error handling.

- Example
```python
    # Not runnable! Just for conceptual understanding.
    from Core.Parser import Parser
    from Function.Exponential import ExpFun
    
    # Input: Exp[2, "2"]
    line = input()
    AST = Parser.inst().parse(line)
    
    # Inferred signature: T.NUM Exp[T.NUM, T.STR]
    # Candidate signatures: T.NUM Exp[T.NUM]
    # Type error. Return candidate signatures [Sign([T.NUM], T.NUM, FunT.Exp)].
    cand = ExpFun.chk_t(AST.rt)
    
    # Output: Oops! Check it again.
    if not cand:
        print('Well-done!')
    else:
        print('Oops! Check it again.')
```

## simplify(rt)
<span class="badge badge-pill badge-success">public</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `rt` | `FunTok` | Root token of partial AST to be simplified. |

- Returns

| Type | Description |
| --- | --- |
| `Token.Tok` | Root token of simplified partial AST. |
| `List[InterpWarn]` | List of generated warnings during simplification. |

- Warnings

| Warning | Description |
| --- | --- |
| `NAN_DETECT` | `math.nan` is detected as a parameter of function. |
| `INF_DETECT` | `math.inf` or `-math.inf` is detected as a parameter of function. |
| `POLE_DETECT` | Mathematical pole is detected at given parameter of function. |
| `DOMAIN_OUT` | Given parameter is not in the domain of function. |
| `BIG_INT` | Given parameter is greater than the maximum size of representable `float`, `sys.float_info.max`.
| `SMALL_INT` | Given parameter is smaller than the minimum size of representable `float`, `-sys.float_info.max`.

It simplifies partial AST rooted at `rt` using simplification strategies described at ...
Since it assumes that all children of `rt` is already simplified, simplification of `rt`'s children should be preceded before calling this method.
Also, `rt`'s token value must be one of exponential or logarithm functions listed [above](#class-exp).
After simplification, it returns the root token of simplified partial AST and list of warnings generated during simplification process.

> [!NOTE]
> Multiple warnings can be generated during one simplification.

For simplification, it branches flow by looking up the token value of `rt` and executes corresponding simplification logic.
Although simplification logic is quite complicated, we shall present in-depth description of these logic here.

### Exp
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Exp[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

- Constant folding

If `x` is numeric token, it just computes `Exp[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__exp`.
Thus, for detailed computation rules, refer to the documentation [above](#__expx).

### Log
- Warning check

If `x` (or `x` and `y`) is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Log[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is in $\mathbb{R}^-$, it generates `DOMAIN_OUT` warning.
6. If `x` is $0$, it generates `POLE_DETECT` warning.

The warning generation rules for `Log[x, y]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `y` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `y` with `math.inf`.
6. If `y` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `y` with `-math.inf`.
7. If `y` is `math.nan`, it generates `NAN_DETECT` warning.
8. If `y` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
9. If `x` or `y` is in $\mathbb{R}^-$, it generates `DOMAIN_OUT` warning.
10. If `x` is $0$ and `y` is in $\mathbb{R}^+_0$, it generates `POLE_DETECT` warning.
11. If `x` is in $\mathbb{R}^+$ and `y` is $0$ or $1$, it generates `POLE_DETECT` warning.

- Constant folding

If `x` (or `x` and `y`) is numeric token, it just computes `Log[x]` (or `Log[x, y]`) so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__log`.
Thus, for detailed computation rules, refer to the documentation [above](#__logx-y).

- Dead expression stripping

From the computation table [above](#__logx-y), one can see that `Log[x, y]` always computes to `nan` if `x` or `y` is `nan`, `-inf` or in $\mathbb{R}^-$.
Thus we can simply replace `Log[x, y]` with `nan` safely in these cases.

> [!NOTE]
> The case of `x` or `y` being integer which is less than the minimum size of representable `float` should be treated as `x` or `y` being `-inf`.

### Pow
- Warning check

If `x` and `y` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Pow[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
6. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
7. If `y` is `math.nan`, it generates `NAN_DETECT` warning.
8. If `y` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
9. If `x` is in $\mathbb{R}^-$ and `y` is in $\mathbb{R}\setminus\mathbb{Z}$, it generates `DOMAIN_OUT` warning.
10. If `x` is $0$ and `y` is in $\mathbb{R}^-_0$, it generates `POLE_DETECT` warning.

- Constant folding

If `x` and `y` are numeric tokens, it just computes `Pow[x, y]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__pow`.
Thus, for detailed computation rules, refer to the documentation [above](#__powx-y).

- Dead expression stripping

From the computation table [above](#__powx-y), one can see that `Pow[x, y]` always computes to `nan` if `x` or `y` is `nan`.
Thus we can simply replace `Pow[x, y]` with `nan` safely in these cases.

Also, since power function with even exponent is even function wrt. base, minus sign of base can be safely removed using identity $(-x)^y=x^y$ given that $y$ is even.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this removal is indeed safe.

- Sign propagation

Since power function with odd exponent is odd function wrt. base, minus sign of base can be propagated using identity $(-x)^y=-(x^y)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this propagation is indeed safe.

### Sqrt
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Sqrt[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is in $\mathbb{R}^-$, it generates `DOMAIN_OUT` warning.

- Constant folding

If `x` is numeric token, it just computes `Sqrt[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__sqrt`.
Thus, for detailed computation rules, refer to the documentation [above](#__sqrtx).

### Log2
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Log2[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
4. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
5. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
6. If `x` is 0, it generates `POLE_DETECT` warning.
7. If `x` is in $\mathbb{R}^-$, it generates `DOMAIN_OUT` warning.

- Constant folding

If `x` is numeric token, it just computes `Log2[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__log2`.
Thus, for detailed computation rules, refer to the documentation [above](#__log2x).

### Log10
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Log10[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is 0, it generates `POLE_DETECT` warning.
6. If `x` is in $\mathbb{R}^-$, it generates `DOMAIN_OUT` warning.

- Constant folding

If `x` is numeric token, it just computes `Log10[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__log10`.
Thus, for detailed computation rules, refer to the documentation [above](#__log10x).

## test(fun, test_in)
<span class="badge badge-pill badge-success">public</span> <span class="badge badge-pill badge-secondary">class method</span> <span class="badge badge-pill badge-warning">debug&analysis</span> 

> [!DANGER]
> This method is for analysis only. We recommend you to keep far from this.

- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `fun` | `FunT` | Function to be tested. |
| `test_in` | `List[List[Decimal]]` | Test inputs. |

> [!NOTE]
> Test input `test_in` has form of `List[List[Decimal]]`, not  `List[Decimal]`.
For example, if the function to be tested accepts `n` arguments, then the `test_in` must have form of `[[arg1, arg2, ..., argn], ...]`.

- Returns

| Type | Description |
| --- | --- |
| `List[Decimal]` | Test outputs. |

It simply computes test outputs of function indicated by `fun` at test input points `test_in`.
The value of `fun` must be one of exponential or logarithm functions listed [above](#class-exp).
For accuracy, it takes `test_in` as `Decimal`, which is a class in `decimal` package that supports arbitrary precision arithmetic in Python.
By default, the precision (# of significant digits) is 300, but it can be customized.

For test output generation, it simply branches flow by looking up `fun` and computes outputs using the basic implementation of each `fun` described above.
After computing all test outputs, the result will be returned as `Decimal` again.

- Example
```python
    from decimal import Decimal
    from Core.Type import FunT
    from Function.Exponential import ExpFun
    
    # Uniform 100 test input points from [1, 100].
    test_in = [Decimal(n + 1) for n in range(100)]
    # Computes value of math.log(n) for n in test points.
    test_out = ExpFun.test(FunT.Log, test_in)
```