# Class SpecialFun

> Special function toolbox.

> [!DANGER]
> This class is implemented as an [abstract class](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html) of JAVA.
That is, it cannot be initialized or instantiated.
If one tries to instantiate this class, it will throw `NotImplementedError` at `__init__`.
Since all methods are class method, one should use them as `SpecialFun.chk_t`.

Class `SpecialFun` supports following special functions.

| Function | Definition | Domain | Range |
| --- | --- | --- | --- |
| `Erf[x]` | $\mathrm{erf}(x) = \frac{2}{\sqrt{\pi}}\int_0^xe^{-t^2}\,d\mu(t)$ | $\mathbb{R}$ | $(-1,\,1)$ |
| `Erfc[x]` | $\mathrm{erfc}(x) = 1-\mathrm{erf}(x)$ | $\mathbb{R}$ | $(0,\,2)$ |
| `Gamma[x]` | $\Gamma(x) = \int_0^\infty t^{x-1}e^{-t}\,d\mu(t)$ | $\mathbb{R}\setminus\mathbb{Z}^-_0$ | $\mathbb{R}\setminus\{0\}$ |
| `Lgamma[x]` | $\log\vert\Gamma(x)\vert$ | $\mathbb{R}\setminus\mathbb{Z}^-_0$ | $\mathbb{R}$ |
| `Recigamma[x]` | $\frac{1}{\Gamma(x)}$ | $\mathbb{R}$ | $\mathbb{R}$ |
| `Besselclifford[x]` | $\frac{1}{\Gamma(x + 1)}$ | $\mathbb{R}$ | $\mathbb{R}$ |
| `Beta[x, y]` | $\mathrm{B}(x,\,y) = \int_0^1t^{x-1}(1-t)^{y-1}\,d\mu(t)$ | $(\mathbb{R}\setminus\mathbb{Z}^-_0)^2$ | $\mathbb{R}$ |
| `Centralbeta[x]` | $\beta(x) = \mathrm{B}(x,\,x)$ | $\mathbb{R}\setminus\mathbb{Z}^-_0$ | $\mathbb{R}$ |
| `Sinc[x]` | $\mathrm{sinc}(x) = \frac{\sin(x)}{x}$ | $\mathbb{R}$ | $\approx[-0.217,\,1]$ |
| `Tanc[x]` | $\mathrm{tanc}(x) = \frac{\tan(x)}{x}$ | $\mathbb{R}\setminus(\pi\mathbb{Z}+\pi/2)$ | $\mathbb{R}$ |
| `Sinhc[x]` | $\mathrm{sinhc}(x) = \frac{\sinh(x)}{x}$ | $\mathbb{R}$ | $[1,\,\infty)$ |
| `Coshc[x]` | $\mathrm{coshc}(x) = \frac{\cosh(x)}{x}$ | $\mathbb{R}\setminus\{0\}$ | $\approx\mathbb{R}\setminus(-1.509,\,1.509)$ |
| `Tanhc[x]` | $\mathrm{tanhc}(x) = \frac{\tanh(x)}{x}$ | $\mathbb{R}$ | $(0,\,1]$ |
| `Dirichletkernel[x, n]` | $D_n(x) = \sum_{k=-n}^ne^{\mathbf{i}kx}$ | $\mathbb{R}\times\mathbb{N}_0$ | $\mathbb{R}$ | 
| `Fejerkernel[x, n]` | $F_n(x) = \sum_{k=0}^{n-1}D_k(x)$ | $\mathbb{R}\times\mathbb{N}$ | $\mathbb{R}^+_0$ |
| `Topologistsin[x]` | $\sin(1/x)$ | $\mathbb{R}^+$ | $[-1,\,1]$ |

> [!NOTE]
> 1. Here, $\mu$ stands for [Lebesgue measure](https://en.wikipedia.org/wiki/Lebesgue_measure) on measure space $(\mathbb{R},\,\mathcal{M},\,\mu)$, $x^{\overline{n}}$ stands for [rising factorial](https://en.wikipedia.org/wiki/Falling_and_rising_factorials) which is defined by $x^{\overline{n}}=x\cdots(x+n-1)$, and $\mathbf{i}$ stands for imaginary unit.
2. For convenience, we employ convention $1/\pm\infty=0$.
3. One can show that integral in the definition of error function converges for all $x\in\mathbb{R}$ so that it is indeed well-defined.
4. One can show that integral in the definition of gamma function and beta function converges for all $x\in\mathbb{R}^+$ and $(x,\,y)\in(\mathbb{R}^+)^2$ so that they are indeed well-defined on $\mathbb{R}^+$ and $(\mathbb{R}^+)^2$, resp.
    Then we expand them using [analytic continuation](https://en.wikipedia.org/wiki/Analytic_continuation) to $\mathbb{R}\setminus\mathbb{Z}^-_0$ and $(\mathbb{R}\setminus\mathbb{Z}^-_0)^2$, resp.
5. In the definition of sinc, tanc, sinhc, and tanhc above, we define their value at $x=0$ as $1$, which is their limit value as $x\to0$.
6. One can show that although Dirichlet kernel is defined as a sum of complex numbers, its value always computes to real number.

We present some simple graph of functions above.
Following plots are computed and rendered by MATLAB and one can read detailed description on these code at ...

<center>
<!-- tabs:start -->
#### ** Erf **
![Erf_Graph](Figures/Erf_Graph.eps)

__Figure 1__. Graph of $\mathrm{erf}(x)$ on $[-3,\,3]$.<br/>
Gray dashes are asymptotic line of error function, $y=\pm1$.

#### ** Erfc **
![Erfc_Graph](Figures/Erfc_Graph.eps)

__Figure 2__. Graph of $\mathrm{erfc}(x)$ on $[-3,\,3]$.<br/>
Gray dash is asymptotic line of complementary error function, $y=2$ with $x$ axis.

#### ** Gamma **
![Gamma_Graph](Figures/Gamma_Graph.eps)

__Figure 3__. Graph of $\Gamma(x)$ on $[-4,\,4]$.<br/>
Gray dashes are asymptotic line of gamma function, $x=0,\,\cdots,\,-3$.

#### ** Lgamma **
![Lgamma_Graph](Figures/Lgamma_Graph.eps)

__Figure 4__. Graph of $\log|\Gamma(x)|$ on $[-4,\,4]$.<br/>
Gray dashes are asymptotic line of log gamma function, $x=0,\,\cdots,\,-3$.

#### ** Recigamma **
![Recigamma_Graph](Figures/Recigamma_Graph.eps)

__Figure 5__. Graph of $1/\Gamma(x)$ on $[-4,\,4]$.<br/>
Here, $x$ axis is asymptotic line of reciprocal gamma function.

#### ** Besselclifford **
![Besselclifford_Graph](Figures/Besselclifford_Graph.eps)

__Figure 6__. Graph of $1/\Gamma(x+1)$ on $[-4,\,4]$.<br/>
Here, $x$ axis is asymptotic line of Bessel-Clifford function.

#### ** Beta **
![Beta_Graph](Figures/Beta_Graph.eps)

__Figure 7__. Graph of $\mathrm{B}(x,\,y)$ on $[-3,\,3]\times[-3,\,3]$.<br/>
Here, $x=0,\,-1,\,-2$, $y=0,\,-1,\,-2$ and $z=0$ are asymptotic plane of beta function.

#### ** Centralbeta **
![Centralbeta_Graph](Figures/Centralbeta_Graph.eps)

__Figure 8__. Graph of $\beta(x)$ on $[-3,\,3]$.<br/>
Gray dashes are asymptotic line of central beta function, $x=0,\,-1,\,-2$.

#### ** Sinc **
![Sinc_Graph](Figures/Sinc_Graph.eps)

__Figure 9__. Graph of $\mathrm{sinc}(x)$ on $[-5\pi,\,5\pi]$.<br/>
Here, $x$ axis is asymptotic line of sinc function.

#### ** Tanc **
![Tanc_Graph](Figures/Tanc_Graph.eps)

__Figure 10__. Graph of $\mathrm{tanc}(x)$ on $[-5\pi/2,\,5\pi/2]$.<br/>
Gray dashes are asymptotic line of tanc function, $x=\pm3\pi/2$ and $x=\pm\pi/2$.

#### ** Sinhc **
![Sinhc_Graph](Figures/Sinhc_Graph.eps)

__Figure 11__. Graph of $\mathrm{sinhc}(x)$ on $[-5,\,5]$.

#### ** Coshc **
![Coshc_Graph](Figures/Coshc_Graph.eps)

__Figure 12__. Graph of $\mathrm{coshc}(x)$ on $[-5,\,5]$.<br/>
Gray dash is asymptotic line of coshc function, $x=0$.

#### ** Tanhc **
![Tanhc_Graph](Figures/Tanhc_Graph.eps)

__Figure 13__. Graph of $\mathrm{tanhc}(x)$ on $[-10,\,10]$.<br/>
Here, $x$ axis is asymptotic line of tanhc function.

#### ** Dirichletkernel **
![Dirichletkernel_Graph](Figures/Dirichletkernel_Graph.eps)

__Figure 14__. Graph of $D_n(x)$ on $[-3,\,3]$.

#### ** Fejerkernel **
![Fejerkernel_Graph](Figures/Fejerkernel_Graph.eps)

__Figure 15__. Graph of $F_n(x)$ on $[-3,\,3]$.

#### ** Topologistsin **
![Topologistsin_Graph](Figures/Topologistsin_Graph.eps)

__Figure 16__. Graph of $\sin(1/x)$ on $[0,\,3]$.<br/>
Here, $x$ axis is asymptotic line of topologist's sine function.
<!-- tabs:end -->
</center>

For more information on special functions, refer to following references.
- [http://mathworld.wolfram.com/Erf.html](http://mathworld.wolfram.com/Erf.html)
- [http://mathworld.wolfram.com/Erfc.html](http://mathworld.wolfram.com/Erfc.html)
- [http://mathworld.wolfram.com/GammaFunction.html](http://mathworld.wolfram.com/GammaFunction.html)
- [http://mathworld.wolfram.com/LogGammaFunction.html](http://mathworld.wolfram.com/LogGammaFunction.html)
- [https://en.wikipedia.org/wiki/Reciprocal_gamma_function](https://en.wikipedia.org/wiki/Reciprocal_gamma_function)
- [https://en.wikipedia.org/wiki/Bessel–Clifford_function](https://en.wikipedia.org/wiki/Bessel–Clifford_function)
- [http://mathworld.wolfram.com/BetaFunction.html](http://mathworld.wolfram.com/BetaFunction.html)
- [http://mathworld.wolfram.com/CentralBetaFunction.html](http://mathworld.wolfram.com/CentralBetaFunction.html)
- [http://mathworld.wolfram.com/SincFunction.html](http://mathworld.wolfram.com/SincFunction.html)
- [http://mathworld.wolfram.com/TancFunction.html](http://mathworld.wolfram.com/TancFunction.html)
- [http://mathworld.wolfram.com/SinhcFunction.html](http://mathworld.wolfram.com/SinhcFunction.html)
- [https://en.wikipedia.org/wiki/Coshc_function](https://en.wikipedia.org/wiki/Coshc_function)
- [http://mathworld.wolfram.com/TanhcFunction.html](http://mathworld.wolfram.com/TanhcFunction.html)
- [https://en.wikipedia.org/wiki/Dirichlet_kernel](https://en.wikipedia.org/wiki/Dirichlet_kernel)
- [https://en.wikipedia.org/wiki/Fejér_kernel](https://en.wikipedia.org/wiki/Fejér_kernel)
- [http://mathworld.wolfram.com/TopologistsSineCurve.html](http://mathworld.wolfram.com/TopologistsSineCurve.html)


## __sign
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-info">const</span> <span class="badge badge-pill badge-secondary">class variable</span>
- Type: `Final[Dict[FunT, List[Sign]]]`
- Value
```python
    {
        FunT.ERF: [Sign([T.NUM], T.NUM, FunT.ERF)],
        FunT.ERFC: [Sign([T.NUM], T.NUM, FunT.ERFC)],
        FunT.GAMMA: [Sign([T.NUM], T.NUM, FunT.GAMMA)],
        FunT.LGAMMA: [Sign([T.NUM], T.NUM, FunT.LGAMMA)],
        FunT.RECIGAMMA: [Sign([T.NUM], T.NUM, FunT.RECIGAMMA)],
        FunT.BESSELCLIFFORD: [Sign([T.NUM], T.NUM, FunT.BESSELCLIFFORD)],
        FunT.BETA: [Sign([T.NUM, T.NUM], T.NUM, FunT.BETA)],
        FunT.CENTRALBETA: [Sign([T.NUM], T.NUM, FunT.CENTRALBETA)],
        FunT.SINC: [Sign([T.NUM], T.NUM, FunT.SINC)],
        FunT.TANC: [Sign([T.NUM], T.NUM, FunT.TANC)],
        FunT.SINHC: [Sign([T.NUM], T.NUM, FunT.SINHC)],
        FunT.COSHC: [Sign([T.NUM], T.NUM, FunT.COSHC)],
        FunT.TANHC: [Sign([T.NUM], T.NUM, FunT.TANHC)],
        FunT.DIRICHLETKERNEL: [Sign([T.NUM, T.NUM], T.NUM, FunT.DIRICHLETKERNEL)],
        FunT.FEJERKERNEL: [Sign([T.NUM, T.NUM], T.NUM, FunT.FEJERKERNEL)],
        FunT.TOPOLOGISTSIN: [Sign([T.NUM], T.NUM, FunT.TOPOLOGISTSIN)]
    }
```

Function calling signatures of special functions for type checking.

## __erf(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where error function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of error function. |

It is simple helper for `simplify` computing `Erf[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Erf(x)` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: |
| `Erf(x)` | `nan` | $-1$ | $\mathrm{erf}(x)$ | $1$ |

The value of $\mathrm{erf}(x)$ is computed using `math.erf` in basic Python math package `math`.
The implementation of `math.erf` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `erf` function in `cmath` library.
Unfortunately, the implementation `erf` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Erf[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Erf_Small](Figures/Erf_Small.eps)

__Figure 1__. Error of `Erf[x]` on $[-1,\,1]$. Input points are drawn randomly from $\mathbf{U}(-1,\,1)$.

#### ** Medium input **
![Erf_Medium](Figures/Erf_Medium.eps)

__Figure 2__. Error of `Erf[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$.

#### ** Large input **
![Erf_Large](Figures/Erf_Large.eps)

__Figure 3__. Error of `Erf[x]` on $[-25,\,25]$. Input points are drawn randomly from $\mathbf{U}(-25,\,25)$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __erfc(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where complementary error function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of complementary error function. |

It is simple helper for `simplify` computing `Erfc[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Erfc(x)` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: |
| `Erfc(x)` | `nan` | $2$ | $\mathrm{erfc}(x)$ | $0$ |

The value of $\mathrm{erfc}(x)$ is computed using `math.erfc` in basic Python math package `math`.
The implementation of `math.erfc` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `erfc` function in `cmath` library.
Unfortunately, the implementation `erfc` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Erfc[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Erfc_Small](Figures/Erfc_Small.eps)

__Figure 1__. Error of `Erfc[x]` on $[-1,\,1]$. Input points are drawn randomly from $\mathbf{U}(-1,\,1)$.

#### ** Medium input **
![Erfc_Medium](Figures/Erfc_Medium.eps)

__Figure 2__. Error of `Erfc[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$.

#### ** Large input **
![Erfc_Large](Figures/Erfc_Large.eps)

__Figure 3__. Error of `Erfc[x]` on $[-25,\,25]$. Input points are drawn randomly from $\mathbf{U}(-25,\,25)$.
<!-- tabs:end -->

> [!NOTE]
> Theoretically, `Erfc[x]` is equivalent to `1 - Erf[x]`, but `Erfc[x]` is more accurate for large `x`.
Since `Erf[x]` for large `x` is very close to 1, rounding error in `1 - Erf[x]` is quite large.
For example, `1 - Erf[20]` gives `0` but `Erfc[20]` gives `5.395865611607901e-176` where the actual value is `5.539586561160790092893499916790e-176` (computed by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300).
The former has absolute error about `5.3959e-176` but the latter has absolute error about `2.4981e-192`.

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __gamma(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where gamma function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of gamma function. |

It is simple helper for `simplify` computing `Gamma[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Gamma[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}\setminus\mathbb{Z}^-_0$ | $\mathbb{Z}^-_0$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Gamma[x]` | `nan` | `nan` | $\Gamma(x)$ | `nan` | `inf` |

The value of $\Gamma(x)$ is computed using `math.gamma` in basic Python math package `math`.
The implementation of `math.gamma` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `gamma` function in `cmath` library.
Unfortunately, the implementation `gamma` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Gamma[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Gamma_Small](Figures/Gamma_Small.eps)

__Figure 1__. Error of `Gamma[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$.

#### ** Medium input **
![Gamma_Medium](Figures/Gamma_Medium.eps)

__Figure 2__. Error of `Gamma[x]` on $[-25,\,25]$. Input points are drawn randomly from $\mathbf{U}(-25,\,25)$.

#### ** Large input **
![Gamma_Large](Figures/Gamma_Large.eps)

__Figure 3__. Error of `Gamma[x]` on $[-125,\,125]$. Input points are drawn randomly from $\mathbf{U}(-125,\,125)$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __lgamma(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where log gamma function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of log gamma function. |

It is simple helper for `simplify` computing `Lgamma[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Lgamma[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}\setminus\mathbb{Z}^-_0$ | $\mathbb{Z}^-_0$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Lgamma[x]` | `nan` | `nan` | $\log\vert\Gamma(x)\vert$ | `nan` | `inf` |

The value of $\log\vert\Gamma(x)\vert$ is computed using `math.lgamma` in basic Python math package `math`.
The implementation of `math.lgamma` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `lgamma` function in `cmath` library.
Unfortunately, the implementation `lgamma` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Lgamma[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Lgamma_Small](Figures/Lgamma_Small.eps)

__Figure 1__. Error of `Lgamma[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$.

#### ** Medium input **
![Lgamma_Medium](Figures/Lgamma_Medium.eps)

__Figure 2__. Error of `Lgamma[x]` on $[-50,\,50]$. Input points are drawn randomly from $\mathbf{U}(-50,\,50)$.

#### ** Large input **
![Lgamma_Large](Figures/Lgamma_Large.eps)

__Figure 3__. Error of `Lgamma[x]` on $[-5\times10^5,\,5\times10^5]$. Input points are drawn randomly from $\mathbf{U}(-5\times10^5,\,5\times10^5)$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __recigamma(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where reciprocal function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of reciprocal function. |

It is simple helper for `simplify` computing `Recigamma[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Recigamma[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: | 
| `Recigamma[x]` | `nan` | `nan` | $1/\Gamma(x)$ | $0$ |

The implementation directly reflects the definition of reciprocal gamma function.
Thus error will depend on implementation of `math.gamma` which we described in detail [above](#__gammax).

Anyway, we present a thorough report on errors of `Recigamma[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Recigamma_Small](Figures/Recigamma_Small.eps)

__Figure 1__. Error of `Recigamma[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$.

#### ** Medium input **
![Recigamma_Medium](Figures/Recigamma_Medium.eps)

__Figure 2__. Error of `Recigamma[x]` on $[-25,\,25]$. Input points are drawn randomly from $\mathbf{U}(-25,\,25)$.

#### ** Large input **
![Recigamma_Large](Figures/Recigamma_Large.eps)

__Figure 3__. Error of `Recigamma[x]` on $[-125,\,125]$. Input points are drawn randomly from $\mathbf{U}(-125,\,125)$.
<!-- tabs:end -->

## __bessel_clifford(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where Bessel-Clifford function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of Bessel-Clifford function. |

It is simple helper for `simplify` computing `Besselclifford[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Besselclifford[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: | 
| `Besselclifford[x]` | `nan` | `nan` | $1/\Gamma(x+1)$ | $0$ |

The implementation directly reflects the definition of Bessel-Clifford function.
Thus error will depend on implementation of `math.gamma` which we described in detail [above](#__gammax).

Anyway, we present a thorough report on errors of `Besselclifford[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Besselclifford_Small](Figures/Besselclifford_Small.eps)

__Figure 1__. Error of `Besselclifford[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$.

#### ** Medium input **
![Besselclifford_Medium](Figures/Besselclifford_Medium.eps)

__Figure 2__. Error of `Besselclifford[x]` on $[-25,\,25]$. Input points are drawn randomly from $\mathbf{U}(-25,\,25)$.

#### ** Large input **
![Besselclifford_Large](Figures/Besselclifford_Large.eps)

__Figure 3__. Error of `Besselclifford[x]` on $[-125,\,125]$. Input points are drawn randomly from $\mathbf{U}(-125,\,125)$.
<!-- tabs:end -->

## __beta(x, y)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | First coordinate of point where beta function is to be computed. |
| `y` | `float` | Second coordinate of point where beta function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of beta function. |

It is simple helper for `simplify` computing `Beta[x, y]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Beta[x, y]` is as follows.

| `y\x` | `nan` | `-inf` | $\mathbb{R}^+\cup\bigcup_{n=1}^\infty(-2n,\,-2n+1)$ | $\bigcup_{n=0}^\infty(-2n-1,\,-2n)$ | $\mathbb{Z}^-_0$ | `inf` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| __`nan`__ | `nan` | `nan` | `nan` | `nan` | `nan` | `nan` |
| __`-inf`__ |  `nan` | `nan` | `nan` | `nan` | `nan` | `nan` |
| $\mathbb{R}^+\cup\bigcup_{n=1}^\infty(-2n,\,-2n+1)$ | `nan` | `nan` | $\mathrm{B}(x,\,y)$ | $\mathrm{B}(x,\,y)$ | `nan` | `inf` |
| $\bigcup_{n=0}^\infty(-2n-1,\,-2n)$ | `nan` | `nan` | $\mathrm{B}(x,\,y)$ | $\mathrm{B}(x,\,y)$ | `nan` | `-inf` |
| $\mathbb{Z}^-_0$ | `nan` | `nan` | `nan` | `nan` | `nan` | `nan` |
| __`inf`__ | `nan` | `nan` | `inf` | `-inf` | `nan` | $0$ |

The value of $\mathrm{B}(x,\,y)$ is computed as `math.exp(math.lgamma(x) + math.lgamma(y) - math.lgamma(x + y))` which comes from identity
$$
    \mathrm{B}(x,\,y)=\frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}.
$$
The sign of $\mathrm{B}(x,\,y)$ will be recovered later using following identity.
$$
\mathrm{sgn}(\Gamma(x))=
\begin{dcases}
1&\textrm{when }x>0\textrm{ or }x\in(2n,\,2n+1)\textrm{ for some }n\in\mathbb{Z}^-\\
-1&\textrm{ow.}
\end{dcases}
$$
Thus error will depend on implementation of `math.lgamma` which we described in detail [above](#__lgammax).
For more information on the identity we used, consult the reference below.

Anyway, we present a thorough report on errors of `Beta[x, y]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Beta_Small](Figures/Beta_Small.eps)

__Figure 1__. Error of `Beta[x, y]` on $[-3,\,3]^2$. Input points are drawn randomly from $\mathbf{U}([-3,\,3]^2)$.

#### ** Medium input **
![Beta_Medium](Figures/Beta_Medium.eps)

__Figure 2__. Error of `Beta[x, y]` on $[-30,\,30]$. Input points are drawn randomly from $\mathbf{U}([-30,\,30]^2)$.

#### ** Large input **
![Beta_Large](Figures/Beta_Large.eps)

__Figure 3__. Error of `Beta[x, y]` on $[-300,\,300]$. Input points are drawn randomly from $\mathbf{U}([-300,\,300]^2)$.
<!-- tabs:end -->

- References
    1. [https://en.wikipedia.org/wiki/Beta_function](https://en.wikipedia.org/wiki/Beta_function)

## __cenbeta(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where central beta function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of central beta function. |

It is simple helper for `simplify` computing `Centralbeta[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Centralbeta[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}\setminus\mathbb{Z}^-_0$ | $\mathbb{Z}^-_0$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: | 
| `Centralbeta[x]` | `nan` | `nan` | $\beta(x)$ | `nan` | $0$ |

The value of $\beta(x)$ is computed as `math.exp(2 * math.lgamma(x) - math.lgamma(2 * x))` which comes from identity $\beta(x)=\Gamma(x)^2/\Gamma(2x)$.
The sign of $\beta(x)$ will be recovered later using following identity.
$$
\mathrm{sgn}(\beta(x))=
\begin{dcases}
1&\textrm{when }x>0\textrm{ or }x\in(n,\,n+1/2)\textrm{ for some }n\in\mathbb{Z}^-\\
-1&\textrm{ow.}
\end{dcases}
$$
Thus error will depend on implementation of `math.lgamma` which we described in detail [above](#__lgammax).
For more information on the identity we used, consult the reference below.

Anyway, we present a thorough report on errors of `Centralbeta[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Centralbeta_Small](Figures/Centralbeta_Small.eps)

__Figure 1__. Error of `Centralbeta[x]` on $[-3,\,3]$. Input points are drawn randomly from $\mathbf{U}(-3,\,3)$.

#### ** Medium input **
![Centralbeta_Medium](Figures/Centralbeta_Medium.eps)

__Figure 2__. Error of `Centralbeta[x]` on $[-30,\,30]$. Input points are drawn randomly from $\mathbf{U}(-30,\,30)$.

#### ** Large input **
![Centralbeta_Large](Figures/Centralbeta_Large.eps)

__Figure 3__. Error of `Centralbeta[x]` on $[-300,\,300]$. Input points are drawn randomly from $\mathbf{U}(-300,\,300)$.
<!-- tabs:end -->

- References
    1. [https://en.wikipedia.org/wiki/Beta_function](https://en.wikipedia.org/wiki/Beta_function)

## __sinc(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where sinc function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of sinc function. |

It is simple helper for `simplify` computing `Sinc[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Sinc[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: |
| `Sinc[x]` | `nan` | $0$ | $\mathrm{sinc}(x)$ | $0$ |

The value of $\mathrm{sinc}(x)$ is computed as `math.sin(x) / x` if $x\ne0$ and `1` if $x=0$, which reflects its definition directly.
Thus error will depend on implementation of `math.sin` which we described in detail [here](trigonometric.md#__sinx).

Anyway, we present a thorough report on errors of `Sinc[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Sinc_Small](Figures/Sinc_Small.eps)

__Figure 1__. Error of `Sinc[x]` on $[-5\pi,\,5\pi]$. Input points are drawn randomly from $\mathbf{U}(-5\pi,\,5\pi)$.

#### ** Medium input **
![Sinc_Medium](Figures/Sinc_Medium.eps)

__Figure 2__. Error of `Sinc[x]` on $[-500\pi,\,500\pi]$. Input points are drawn randomly from $\mathbf{U}(-500\pi,\,500\pi)$.

#### ** Large input **
![Sinc_Large](Figures/Sinc_Large.eps)

__Figure 3__. Error of `Sinc[x]` on $[-5\times10^{10}\pi,\,5\times10^{10}\pi]$. Input points are drawn randomly from $\mathbf{U}(-5\times10^{10}\pi,\,5\times10^{10}\pi)$.
<!-- tabs:end -->

## __tanc(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where tanc function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of tanc function. |

It is simple helper for `simplify` computing `Tanc[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Tanc[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}\setminus(\pi\mathbb{Z}+\pi/2)$ | $\pi\mathbb{Z}+\pi/2$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Tanc[x]` | `nan` | `nan` | $\mathrm{tanc}(x)$ | `nan` | `nan` |

The value of $\mathrm{tanc}(x)$ is computed as `math.tan(x) / x` if $x\ne0$ and `1` if $x=0$ which reflects its definition directly.
Thus error will depend on implementation of `math.tan` which we described in detail [here](trigonometric.md#__tanx).

Anyway, we present a thorough report on errors of `Tanc[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.

<!-- tabs:start -->
#### ** Small input **
![Tanc_Small](Figures/Tanc_Small.eps)

__Figure 1__. Error of `Tanc[x]` on $[-5\pi,\,5\pi]$. Input points are drawn randomly from $\mathbf{U}(-5\pi,\,5\pi)$.

#### ** Medium input **
![Tanc_Medium](Figures/Tanc_Medium.eps)

__Figure 2__. Error of `Tanc[x]` on $[-250\pi,\,250\pi]$. Input points are drawn randomly from $\mathbf{U}(-250\pi,\,250\pi)$.

#### ** Large input **
![Tanc_Large](Figures/Tanc_Large.eps)

__Figure 3__. Error of `Tanc[x]` on $[-5\times10^{10}\pi/2,\,5\times10^{10}\pi/2]$. Input points are drawn randomly from $\mathbf{U}(-5\times10^{10}\pi/2,\,5\times10^{10}\pi/2)$.
<!-- tabs:end -->

## __sinhc(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where sinhc function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of sinhc function. |

It is simple helper for `simplify` computing `Sinhc[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Sinhc[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: |
| `Sinhc[x]` | `nan` | `inf` | $\mathrm{sinhc}(x)$ | `inf` |

The value of $\mathrm{sinhc}(x)$ is computed as `math.sinh(x) / x` if $x\ne0$ and `1` if $x=0$ which reflects its definition directly.
Thus error will depend on implementation of `math.sinh` which we described in detail [here](hyperbolic_trigonometric.md#__sinhx).

Anyway, we present a thorough report on errors of `Sinhc[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.

<!-- tabs:start -->
#### ** Small input **
![Sinhc_Small](Figures/Sinhc_Small.eps)

__Figure 1__. Error of `Sinhc[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$.

#### ** Medium input **
![Sinhc_Medium](Figures/Sinhc_Medium.eps)

__Figure 2__. Error of `Sinhc[x]` on $[-50,\,50]$. Input points are drawn randomly from $\mathbf{U}(-50,\,50)$.

#### ** Large input **
![Sinhc_Large](Figures/Sinhc_Large.eps)

__Figure 3__. Error of `Sinhc[x]` on $[-500,\,500]$. Input points are drawn randomly from $\mathbf{U}(-500,\,500)$.
<!-- tabs:end -->

## __coshc(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where coshc function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of coshc function. |

It is simple helper for `simplify` computing `Coshc[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Coshc[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}\setminus\{0\}$ | $0$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Coshc[x]` | `nan` | `-inf` | $\mathrm{coshc}(x)$ | `nan` | `inf` |

The value of $\mathrm{coshc}(x)$ is computed as `math.cosh(x) / x` if $x\ne0$ and `1` if $x=0$ which reflects its definition directly.
Thus error will depend on implementation of `math.cosh` which we described in detail [here](hyperbolic_trigonometric.md#__coshx).

Anyway, we present a thorough report on errors of `Coshc[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.

<!-- tabs:start -->
#### ** Small input **
![Coshc_Small](Figures/Coshc_Small.eps)

__Figure 1__. Error of `Coshc[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$.

#### ** Medium input **
![Coshc_Medium](Figures/Coshc_Medium.eps)

__Figure 2__. Error of `Coshc[x]` on $[-50,\,50]$. Input points are drawn randomly from $\mathbf{U}(-50,\,50)$.

#### ** Large input **
![Coshc_Large](Figures/Coshc_Large.eps)

__Figure 3__. Error of `Coshc[x]` on $[-500,\,500]$. Input points are drawn randomly from $\mathbf{U}(-500,\,500)$.
<!-- tabs:end -->

## __tanhc(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where tanhc function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of tanhc function. |

It is simple helper for `simplify` computing `Tanhc[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Tanhc[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: |
| `Tanhc[x]` | `nan` | $0$ | $\mathrm{tanhc}(x)$ | $0$ |

The value of $\mathrm{coshc}(x)$ is computed as `math.tanh(x) / x` if $x\ne0$ and `1` if $x=0$ which reflects its definition directly.
Thus error will depend on implementation of `math.tanh` which we described in detail [here](hyperbolic_trigonometric.md#__tanhx).

Anyway, we present a thorough report on errors of `Tanhc[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.

<!-- tabs:start -->
#### ** Small input **
![Tanhc_Small](Figures/Tanhc_Small.eps)

__Figure 1__. Error of `Tanhc[x]` on $[-3,\,3]$. Input points are drawn randomly from $\mathbf{U}(-3,\,3)$.

#### ** Medium input **
![Tanhc_Medium](Figures/Tanhc_Medium.eps)

__Figure 2__. Error of `Tanhc[x]` on $[-30,\,30]$. Input points are drawn randomly from $\mathbf{U}(-30,\,30)$.

#### ** Large input **
![Tanhc_Large](Figures/Tanhc_Large.eps)

__Figure 3__. Error of `Tanhc[x]` on $[-300,\,300]$. Input points are drawn randomly from $\mathbf{U}(-300,\,300)$.
<!-- tabs:end -->

## __dirichlet_ker(x, n)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | First coordinate of point where Dirichlet kernel is to be computed. |
| `n` | `int` | Second coordinate of point where Dirichlet kernel is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of Dirichlet kernel. |

It is simple helper for `simplify` computing `Dirichletkernel[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Dirichletkernel[x]` is as follows.

| `n\x` | `nan` | `-inf` | $\mathbb{R}\setminus2\pi\mathbb{Z}$ | $2\pi\mathbb{Z}$ | `inf` |
| :---: | :---: | :---: | :---: | :---: | :---: |
| __`nan`__ | `nan` | `nan` | `nan` | `nan` | `nan` |
| __`-inf`__ | `nan` | `nan` | `nan` | `nan` | `nan` |
| $0$ | `nan` | `nan` | $1$ | $1$ | `nan` |
| $\mathbb{N}$ | `nan` | `nan` | $D_n(x)$ | $2n+1$ | `nan` |
| $\mathbb{R}\setminus\mathbb{N}_0$ | `nan` | `nan` | `nan` | `nan` | `nan` |
| __`inf`__ | `nan` | `nan` | `nan` | `nan` | `nan` |

The value of $D_n(x)$ is computed as `math.sin((n + 0.5) * x) / math.sin(x / 2)` which comes from identity
$$
D_n(x)=\begin{dcases}
    \frac{\sin((n+1/2)x)}{\sin(x/2)}&\textrm{when }x\notin2\pi\mathbb{Z}\\
    2n+1&\textrm{when }x\in2\pi\mathbb{Z}.
\end{dcases}
$$
Thus error will depend on implementation of `math.sin` which we described in detail [here](trigonometric.md#__sinx).
For more information on the identity we used, consult the reference below.

Anyway, we present a thorough report on errors of `Dirichletkernel[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.

<!-- tabs:start -->
#### ** Small input **
![Dirichletkernel_Small](Figures/Dirichletkernel_Small.eps)

__Figure 1__. Error of `Dirichletkernel[x]` on $[-5,\,5]\times[1,\,5]$.
Input points are drawn randomly from $\mathbf{U}([-5,\,5]\times[0.5,\,5.5])$ and mapped by $(x,\,y)\mapsto(x,\,\mathrm{round}(y))$.

#### ** Medium input **
![Dirichletkernel_Medium](Figures/Dirichletkernel_Medium.eps)

__Figure 2__. Error of `Dirichletkernel[x]` on $[-500,\,500]\times[1,\,50]$.
Input points are drawn randomly from $\mathbf{U}([-500,\,500]\times[0.5,\,50.5])$ and mapped by $(x,\,y)\mapsto(x,\,\mathrm{round}(y))$.

#### ** Large input **
![Dirichletkernel_Large](Figures/Dirichletkernel_Large.eps)

__Figure 3__. Error of `Dirichletkernel[x]` on $[-5\times10^{10},\,5\times10^{10}]\times[1,\,500]$.
Input points are drawn randomly from $\mathbf{U}([-5\times10^{10},\,5\times10^{10}]\times[0.5,\,500.5])$ and mapped by $(x,\,y)\mapsto(x,\,\mathrm{round}(y))$.
<!-- tabs:end -->

- References
    1. [https://en.wikipedia.org/wiki/Dirichlet_kernel](https://en.wikipedia.org/wiki/Dirichlet_kernel)

## __fejer_ker(x, n)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | First coordinate of point where Fejer kernel is to be computed. |
| `n` | `int` | Second coordinate of point where Fejer kernel is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of Fejer kernel. |

It is simple helper for `simplify` computing `Fejerkernel[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Fejerkernel[x]` is as follows.

| `n\x` | `nan` | `-inf` | $\mathbb{R}\setminus2\pi\mathbb{Z}$ | $2\pi\mathbb{Z}$ | `inf` |
| :---: | :---: | :---: | :---: | :---: | :---: |
| __`nan`__ | `nan` | `nan` | `nan` | `nan` | `nan` |
| __`-inf`__ | `nan` | `nan` | `nan` | `nan` | `nan` |
| $1$ | `nan` | `nan` | $1$ | $1$ | `nan` |
| $\mathbb{N}\setminus\{1\}$ | `nan` | `nan` | $F_n(x)$ | $n$ | `nan` |
| $\mathbb{R}\setminus\mathbb{N}$ | `nan` | `nan` | `nan` | `nan` | `nan` |
| __`inf`__ | `nan` | `nan` | `nan` | `nan` | `nan` |

The value of $F_n(x)$ is computed as `(1 - math.cos(n * x)) / (1 - math.cos(x)) / n` which comes from identity
$$
F_n(x)=\begin{dcases}
    \frac{1}{n}\bigg[\frac{1-\cos(nx)}{1-\cos(x)}\bigg]&\textrm{when }x\notin2\pi\mathbb{Z}\\
    n&\textrm{when }x\in2\pi\mathbb{Z}.
\end{dcases}
$$
Thus error will depend on implementation of `math.cos` which we described in detail [here](trigonometric.md#__cosx).
For more information on the identity we used, consult the reference below.

Anyway, we present a thorough report on errors of `Fejerkernel[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.

<!-- tabs:start -->
#### ** Small input **
![Fejerkernel_Small](Figures/Fejerkernel_Small.eps)

__Figure 1__. Error of `Fejerkernel[x]` on $[-5,\,5]\times[2,\,5]$.
Input points are drawn randomly from $\mathbf{U}([-5,\,5]\times[1.5,\,5.5])$ and mapped by $(x,\,y)\mapsto(x,\,\mathrm{round}(y))$.

#### ** Medium input **
![Fejerkernel_Medium](Figures/Fejerkernel_Medium.eps)

__Figure 2__. Error of `Fejerkernel[x]` on $[-500,\,500]\times[2,\,50]$.
Input points are drawn randomly from $\mathbf{U}([-500,\,500]\times[1.5,\,50.5])$ and mapped by $(x,\,y)\mapsto(x,\,\mathrm{round}(y))$.

#### ** Large input **
![Fejerkernel_Large](Figures/Fejerkernel_Large.eps)

__Figure 3__. Error of `Fejerkernel[x]` on $[-5\times10^{10},\,5\times10^{10}]\times[2,\,500]$.
Input points are drawn randomly from $\mathbf{U}([-5\times10^{10},\,5\times10^{10}]\times[1.5,\,500.5])$ and mapped by $(x,\,y)\mapsto(x,\,\mathrm{round}(y))$.
<!-- tabs:end -->

- References
    1. [https://en.wikipedia.org/wiki/Fejér_kernel](https://en.wikipedia.org/wiki/Fejér_kernel)

## __topo_sin(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where topologist's sine function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of topologist's sine function. |

It is simple helper for `simplify` computing `Topologistsin[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Topologistsin[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}^-_0$ | $\mathbb{R}^+$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Topologistsin[x]` | `nan` | `nan` | `nan` | $\sin(1/x)$ | $0$ |

The implementation directly reflects the definition of topologist's sine function.
Thus error will depend on implementation of `math.sin` which we described in detail [here](trigonometric.md#__sinx).

Anyway, we present a thorough report on errors of `Topologistsin[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.

<!-- tabs:start -->
#### ** Small input **
![Topologistsin_Small](Figures/Topologistsin_Small.eps)

__Figure 1__. Error of `Topologistsin[x]` on $[0,\,3]$. Input points are drawn randomly from $\mathbf{U}(0,\,3)$.

#### ** Medium input **
![Topologistsin_Medium](Figures/Topologistsin_Medium.eps)

__Figure 2__. Error of `Topologistsin[x]` on $[0,\,300]$. Input points are drawn randomly from $\mathbf{U}(0,\,300)$.

#### ** Large input **
![Topologistsin_Large](Figures/Topologistsin_Large.eps)

__Figure 3__. Error of `Topologistsin[x]` on $[0,\,3\times10^{10}]$. Input points are drawn randomly from $\mathbf{U}(0,\,3\times10^{10})$.
<!-- tabs:end -->

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
Also, `rt`'s token value must be one of special functions listed [above](#class-specialfun).
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
    from Function.SpecialFuntion import SpecialFun
    
    # Input: Erf[2, "2"]
    line = input()
    AST = Parser.inst().parse(line)
    
    # Inferred signature: T.NUM Erf[T.NUM, T.STR]
    # Candidate signatures: T.NUM Erf[T.NUM]
    # Type error. Return candidate signatures [Sign([T.NUM], T.NUM, FunT.Erf)].
    cand = SpecialFun.chk_t(AST.rt)
    
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
Also, `rt`'s token value must be one of special functions listed [above](#class-specialfun).
After simplification, it returns the root token of simplified partial AST and list of warnings generated during simplification process.

> [!NOTE]
> Multiple warnings can be generated during one simplification.

For simplification, it branches flow by looking up the token value of `rt` and executes corresponding simplification logic.
Although simplification logic is quite complicated, we shall present in-depth description of these logic here.

### Erf
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Erf[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

- Constant folding

If `x` is numeric token, it just computes `Erf[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__erf`.
Thus, for detailed computation rules, refer to the documentation [above](#__erfx).

- Sign propagation

Since sine function is odd function, sign can be propagated using identity $\mathrm{erf}(-x)=-\mathrm{erf}(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this propagation is indeed safe.

### Erfc
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Erfc[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

- Constant folding

If `x` is numeric token, it just computes `Cos[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__erfc`.
Thus, for detailed computation rules, refer to the documentation [above](#__erfcx).

### Gamma
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Gamma[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is in $\mathbb{Z}^-_0$, it generates `POLE_DETECT` warning.

- Constant folding

If `x` is numeric token, it just computes `Gamma[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__gamma`.
Thus, for detailed computation rules, refer to the documentation [above](#__gammax).

### Lgamma
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Lgamma[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is in $\mathbb{Z}^-_0$, it generates `POLE_DETECT` warning.

- Constant folding

If `x` is numeric token, it just computes `Lgamma[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__lgamma`.
Thus, for detailed computation rules, refer to the documentation [above](#__lgammax).

### Recigamma
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Recigamma[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

- Constant folding

If `x` is numeric token, it just computes `Recigamma[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__recigamma`.
Thus, for detailed computation rules, refer to the documentation [above](#__recigammax).

### Besselclifford
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Besselclifford[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

- Constant folding

If `x` is numeric token, it just computes `Besselclifford[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__bessel_clifford`.
Thus, for detailed computation rules, refer to the documentation [above](#__bessel_cliffordx).

### Beta
- Warning check

If `x` and `y` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Beta[x, y]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `y` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `y` with `math.inf`.
6. If `y` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `y` with `-math.inf`.
7. If `y` is `math.nan`, it generates `NAN_DETECT` warning.
8. If `y` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
9. If `x` is in $\mathbb{Z}^-_0$ and `y` is finite, it generates `POLE_DETECT` warning.
10. If `x` is finite and `y` is in $\mathbb{Z}^-_0$, it generates `POLE_DETECT` warning.

- Constant folding

If `x` and `y` are numeric tokens, it just computes `Beta[x, y]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__beta`.
Thus, for detailed computation rules, refer to the documentation [above](#__betax-y).

- Dead expression stripping

From the computation table [above](#__betax-y), one can see that `Beta[x, y]` always computes to `nan` if `x` or `y` is `nan`, `+-inf` or in $\mathbb{Z}^-_0$.
Thus we can simply replace `Beta[x, y]` with `nan` safely in these cases.

> [!NOTE]
> The case of `x` or `y` being integer which is less than the minimum size of representable `float` should be treated as `x` or `y` being `-inf`.

### Centralbeta
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Centralbeta[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is in $\mathbb{Z}^-_0$, it generates `POLE_DETECT` warning.

- Constant folding

If `x` is numeric token, it just computes `Centralbeta[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__cenbeta`.
Thus, for detailed computation rules, refer to the documentation [above](#__cenbetax).

### Sinc
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Sinc[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

- Constant folding

If `x` is numeric token, it just computes `Sinc[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__sinc`.
Thus, for detailed computation rules, refer to the documentation [above](#__sincx).

- Dead expression stripping

Since sinc function is even function, minus sign inside of secant can be safely removed using identity $\mathrm{sinc}(-x)=\mathrm{sinc}(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this removal is indeed safe.

### Tanc
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Tanc[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is $(n+1/2)\pi$ for some $n\in\mathbb{Z}$, it generates `POLE_DETECT` warning.

> [!WARNING]
> Because of rounding error of floating point arithmetic, `POLE_DETECT` warning might not be generated even if rule 5 is met.
For example, `Tanc[100000.5 * Pi]` does not generate `POLE_DETECT` warning and gives result `87150.4519722597` instead of `nan`.

- Constant folding

If `x` is numeric token, it just computes `Tanc[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__tanc`.
Thus, for detailed computation rules, refer to the documentation [above](#__tancx).

- Dead expression stripping

Since tanc function is even function, minus sign inside of secant can be safely removed using identity $\mathrm{tanc}(-x)=\mathrm{tanc}(x)$.
Note that this identity holds not only for $x\in\mathbb{R}\setminus(\pi\mathbb{Z}+\pi/2)$, but also for `nan`, `+-inf` and $x\in\pi\mathbb{Z}+\pi/2$.
Thus this removal is indeed safe.

### Sinhc
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Sinhc[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

- Constant folding

If `x` is numeric token, it just computes `Sinhc[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__sinhc`.
Thus, for detailed computation rules, refer to the documentation [above](#__sinhcx).

- Dead expression stripping

Since sinhc function is even function, minus sign inside of secant can be safely removed using identity $\mathrm{sinhc}(-x)=\mathrm{sinhc}(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this removal is indeed safe.

### Coshc
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Sinhc[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is $0$, it generates `POLE_DETECT` warning.

- Constant folding

If `x` is numeric token, it just computes `Coshc[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__coshc`.
Thus, for detailed computation rules, refer to the documentation [above](#__coshcx).

- Sign propagation

Since coshc function is odd function, sign can be propagated using identity $\mathrm{coshc}(-x)=-\mathrm{coshc}(x)$.
Note that this identity holds not only for $x\in\mathbb{R}\setminus\{0\}$, but also for `nan`, `+-inf`, and $x=0$.
Thus this propagation is indeed safe.

### Tanhc
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Tanhc[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

- Constant folding

If `x` is numeric token, it just computes `Tanhc[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__tanhc`.
Thus, for detailed computation rules, refer to the documentation [above](#__tanhcx).

- Dead expression stripping

Since tanhc function is even function, minus sign inside of secant can be safely removed using identity $\mathrm{tanhc}(-x)=\mathrm{tanhc}(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this removal is indeed safe.

### Dirichletkernel
- Warning check

If `x` and `n` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Dirichletkernel[x, n]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `n` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `n` with `math.inf`.
6. If `n` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `n` with `-math.inf`.
7. If `n` is `math.nan`, it generates `NAN_DETECT` warning.
8. If `n` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
9. If `n` is in $\mathbb{R}^+_0\setminus\mathbb{N}_0$, it generates `DOMAIN_OUT` warning and replaces `n` with `round(n)`.
10. If `n` is in $\mathbb{R}^-$, it generates `DOMIAN_OUT` warning.

- Constant folding

If `x` and `n` are numeric tokens, it just computes `Dirichletkernel[x, n]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__dirichlet_ker`.
Thus, for detailed computation rules, refer to the documentation [above](#__dirichlet_kerx-n).

- Dead expression stripping

From the computation table [above](#__dirichlet_kerx-n), one can see that `Dirichletkernel[x, n]` always computes to `nan` in following cases.
1. `x` is `nan` or `+-inf`.
2. `n` is `nan`, `+-inf`, or in $\mathbb{R}^-$.
Thus we can simply replace `Dirichletkernel[x, n]` with `nan` safely in these cases.

> [!NOTE]
> By warning rule 9, there is no case of `n` being positive noninteger.
Thus it is enough to check whether `n` is negative.
Also, the case of `x` or `n` being integer which is greater or less than the maximum or minimum size of representable `float`, resp. should be treated as `x` or `n` being `+-inf`, resp.

Also, since Dirichlet kernel is even function wrt. the first paremeter, minus sign of the first parameter of Dirichlet kernel can be safely removed using identity $D_n(-x)=D_n(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this removal is indeed safe.

> [!NOTE]
> By dead expression stripping rule 2, there is no case of $n$ being `nan` or `+-inf` here.

### Fejerkernel
- Warning check

If `x` and `n` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Fejerkernel[x, n]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `n` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `n` with `math.inf`.
6. If `n` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `n` with `-math.inf`.
7. If `n` is `math.nan`, it generates `NAN_DETECT` warning.
8. If `n` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
9. If `n` is in $[0.5,\,\inf)\setminus\mathbb{N}$, it generates `DOMAIN_OUT` warning and replaces `n` with `round(n)`.
10. If `n` is in $(-inf,\,0.5)$, it generates `DOMIAN_OUT` warning.

- Constant folding

If `x` and `n` are numeric tokens, it just computes `Fejerkernel[x, n]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__fejer_ker`
Thus, for detailed computation rules, refer to the documentation [above](#__fejer_kerx-n).

- Dead expression stripping

From the computation table [above](#__fejer_kerx-n), one can see that `Fejerkernel[x, n]` always computes to `nan` in following cases.
1. `x` is `nan` or `+-inf`.
2. `n` is `nan`, `+-inf`, or less than 0.5.
Thus we can simply replace `Fejerkernel[x, n]` with `nan` safely in those cases.

> [!NOTE]
> By warning rule 9, there is no case of `n` being noninteger greater than 0.5.
Thus it is enough to check whether `n` is less than 0.5.
Also, the case of `x` or `n` being integer which is greater or less than the maximum or minimum size of representable `float`, resp. should be treated as `x` or `n` being `+-inf`, resp.

Also, since Fejer kernel is even function wrt. the first paremeter, minus sign of the first parameter of Fejer kernel can be safely removed using identity $F_n(-x)=F_n(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this removal is indeed safe.

> [!NOTE]
> By dead expression stripping rule 2, there is no case of $n$ being `nan` or `+-inf` here.

### Topologistsin
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Tanhc[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float`, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float`, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is nonpositive, it generates `DOMAIN_OUT` warning.

- Constant folding

If `x` is numeric token, it just computes `Topologistsin[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__topo_sin`.
Thus, for detailed computation rules, refer to the documentation [above](#__topo_sinx).

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
Each item in the list which is again list, will be passed to the target function using list unpacking operation `*`.

- Returns

| Type | Description |
| --- | --- |
| `List[Decimal]` | Test outputs. |

It simply computes test outputs of function indicated by `fun` at test input points `test_in`.
The value of `fun` must be one of special functions listed [above](#class-specialfun).
For accuracy, it takes `test_in` as `Decimal`, which is a class in `decimal` package that supports arbitrary precision arithmetic in Python.
By default, the precision (# of significant digits) is 300, but it can be customized.

For test output generation, it simply branches flow by looking up `fun` and computes outputs using the basic implementation of each `fun` described above.
After computing all test outputs, the result will be returned as `Decimal` again.

- Example
```python
    from decimal import Decimal
    from Core.Type import FunT
    from Function.SpecialFunction import SpecialFun
    
    # Uniform 100 test input points from [0, 100).
    test_in = [[Decimal(n)] for n in range(100)]
    # Computes value of math.erf(n) for n in test points.
    test_out = SpecialFun.test(FunT.ERF, test_in)
```