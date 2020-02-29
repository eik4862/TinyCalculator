# Class HyperTri

> Hyperbolic trigonometric function toolbox.

> [!DANGER]
> This class is implemented as an [abstract class](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html) of JAVA.
That is, it cannot be initialized or instantiated.
If one tries to instantiate this class, it will throw `NotImplementedError` at `__init__`.
Since all methods are class method, one should use them as `HyperTri.chk_t`.

Class `Tri` supports following usual hyperbolic trigonometric functions and inverse of them.

| Function | Definition | Domain | Range |
| --- | --- | --- | --- |
| `Sinh[x]` | $\sinh(x) = \frac{e^x-e^{-x}}{2}$ | $\mathbb{R}$ | $\mathbb{R}$ |
| `Cosh[x]` | $\cosh(x) = \frac{e^x+e^{-x}}{2}$ | $\mathbb{R}$ | $[1,\,\infty)$ |
| `Tanh[x]` | $\tanh(x) = \frac{\sinh(x)}{\cosh(x)}$ | $\mathbb{R}$ | $(-1,\,1)$ |
| `Csch[x]` | $\mathrm{cosech}(x) = \frac{1}{\sinh(x)}$ | $\mathbb{R}\setminus\{0\}$ | $\mathbb{R}\setminus\{0\}$ |
| `Sech[x]` | $\mathrm{sech}(x) = \frac{1}{\cosh(x)}$ | $\mathbb{R}$ | $(0,\,1]$ |
| `Coth[x]` | $\coth(x) = \frac{1}{\tanh(x)}$ | $\mathbb{R}\setminus\{0\}$ | $\mathbb{R}\setminus[-1,\,1]$ |
| `Asinh[x]` | $\mathrm{asinh}(x) = \sinh^{-1}(x)$ | $\mathbb{R}$ | $\mathbb{R}$ |
| `Acosh[x]` | $\mathrm{acosh}(x) = \cosh\vert_{\mathbb{R}^+_0}^{-1}(x)$ | $[1,\,\infty)$ | $\mathbb{R}^+_0$ |
| `Atanh[x]` | $\mathrm{atanh}(x) = \tanh^{-1}(x)$ | $(-1,\,1)$ | $\mathbb{R}$ |
| `Acsch[x]` | $\mathrm{acosech}(x) = \mathrm{cosech}^{-1}(x)$ | $\mathbb{R}\setminus\{0\}$ | $\mathbb{R}\setminus\{0\}$ |
| `Asech[x]` | $\mathrm{asech}(x) = \mathrm{sech}\vert_{\mathbb{R}^+_0}^{-1}(x)$ | $(0,\,1]$ | $\mathbb{R}^+_0$ |
| `Acoth[x]` | $\mathrm{acoth}(x) = \coth^{-1}(x)$ | $\mathbb{R}\setminus[-1,\,1]$ | $\mathbb{R}\setminus\{0\}$ |

> [!NOTE]
> Here, $f\vert_{D'}$ for function $f:D\to R$ and subset $D'\subseteq D$ implies the restriction of function $f$ to $D'$.

We present some simple graph of functions above.
Following plots are computed and rendered by MATLAB and one can read detailed description on these code at ...

<center>
<!-- tabs:start -->
#### ** Sinh **
![Sinh_Graph](Figures/Sinh_Graph.eps)

__Figure 1__. Graph of $\sinh(x)$ on $[-5,\,5]$.

#### ** Cosh **
![Cosh_Graph](Figures/Cosh_Graph.eps)

__Figure 2__. Graph of $\cosh(x)$ on $[-5,\,5]$.

#### ** Tanh **
![Tanh_Graph](Figures/Tanh_Graph.eps)

__Figure 3__. Graph of $\tanh(x)$ on $[-3,\,3]$.<br/>
Gray dashes are asymptotic line of tangent hyperbolic function, $y=\pm1$.

#### ** Csch **
![Csch_Graph](Figures/Csch_Graph.eps)

__Figure 4__. Graph of $\mathrm{cosech}(x)$ on $[-5,\,5]$.<br/>
Gray dash is asymptotic line of cosecant hyperbolic function, $x=0$ with $x$ axis.

#### ** Sech **
![Sech_Graph](Figures/Sech_Graph.eps)

__Figure 5__. Graph of $\mathrm{sech}(x)$ on $[-5,\,5]$.<br/>
Here, $x$ axis is asymptotic line of secant hyperbolic function.

#### ** Coth **
![Coth_Graph](Figures/Coth_Graph.eps)

__Figure 6__. Graph of $\coth(x)$ on $[-3,\,3]$.<br/>
Gray dashes are asymptotic line of cotangent hyperbolic function, $x=0$ and $y=\pm1$.

#### ** Asinh **
![Asinh_Graph](Figures/Asinh_Graph.eps)

__Figure 7__. Graph of $\mathrm{asinh}(x)$ on $[-5,\,5]$.

#### ** Acos **
![Acosh_Graph](Figures/Acosh_Graph.eps)

__Figure 8__. Graph of $\mathrm{acosh}(x)$ on $[1,\,5]$.

#### ** Atanh **
![Atanh_Graph](Figures/Atanh_Graph.eps)

__Figure 9__. Graph of $\mathrm{atanh}(x)$ on $[-1,\,1]$.<br/>
Here, $x=\pm1$ is asymptotic line of arctangent hyperbolic function.

#### ** Acsch **
![Acsch_Graph](Figures/Acsch_Graph.eps)

__Figure 10__. Graph of $\mathrm{acosech}(x)$ on $[-5,\,5]$.<br/>
Gray dash is asymptotic line of arccosecant hyperbolic function, $x=0$ with $x$ axis.

#### ** Asech **
![Asech_Graph](Figures/Asech_Graph.eps)

__Figure 11__. Graph of $\mathrm{asech}(x)$ on $[0,\,1]$.<br/>
Here, $y$ axis is asymptotic line of arcsecant hyperbolic function.

#### ** Acoth **
![Acoth_Graph](Figures/Acoth_Graph.eps)

__Figure 12__. Graph of $\mathrm{acoth}(x)$ on $[-5,\,5]$.<br/>
Gray dashes are asymptotic line of arccotangent hyperbolic function, $x=\pm1$ with $x$ axis.
<!-- tabs:end -->
</center>

For more information on hyperbolic trigonometric functions and their inverses, refer to following references.
- [http://mathworld.wolfram.com/HyperbolicSine.html](http://mathworld.wolfram.com/HyperbolicSine.html)
- [http://mathworld.wolfram.com/HyperbolicCosine.html](http://mathworld.wolfram.com/HyperbolicCosine.html)
- [http://mathworld.wolfram.com/HyperbolicTangent.html](http://mathworld.wolfram.com/HyperbolicTangent.html)
- [http://mathworld.wolfram.com/HyperbolicCosecant.html](http://mathworld.wolfram.com/HyperbolicCosecant.html)
- [http://mathworld.wolfram.com/HyperbolicSecant.html](http://mathworld.wolfram.com/HyperbolicSecant.html)
- [http://mathworld.wolfram.com/HyperbolicCotangent.html](http://mathworld.wolfram.com/HyperbolicCotangent.html)
- [http://mathworld.wolfram.com/InverseHyperbolicSine.html](http://mathworld.wolfram.com/InverseHyperbolicSine.html)
- [http://mathworld.wolfram.com/InverseHyperbolicCosine.html](http://mathworld.wolfram.com/InverseHyperbolicCosine.html)
- [http://mathworld.wolfram.com/InverseHyperbolicTangent.html](http://mathworld.wolfram.com/InverseHyperbolicTangent.html)
- [http://mathworld.wolfram.com/InverseHyperbolicCosecant.html](http://mathworld.wolfram.com/InverseHyperbolicCosecant.html)
- [http://mathworld.wolfram.com/InverseHyperbolicSecant.html](http://mathworld.wolfram.com/InverseHyperbolicSecant.html)
- [http://mathworld.wolfram.com/InverseHyperbolicCotangent.html](http://mathworld.wolfram.com/InverseHyperbolicCotangent.html)

## __sign
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-info">const</span> <span class="badge badge-pill badge-secondary">class variable</span>
- Type: `Final[Dict[FunT, List[Sign]]]`
- Value
```python
    {
        FunT.SINH: [Sign([T.NUM], T.NUM, FunT.SINH)],
        FunT.COSH: [Sign([T.NUM], T.NUM, FunT.COSH)],
        FunT.TANH: [Sign([T.NUM], T.NUM, FunT.TANH)],
        FunT.CSCH: [Sign([T.NUM], T.NUM, FunT.CSCH)],
        FunT.SECH: [Sign([T.NUM], T.NUM, FunT.SECH)],
        FunT.COTH: [Sign([T.NUM], T.NUM, FunT.COTH)],
        FunT.ASINH: [Sign([T.NUM], T.NUM, FunT.ASINH)],
        FunT.ACOSH: [Sign([T.NUM], T.NUM, FunT.ACOSH)],
        FunT.ATANH: [Sign([T.NUM], T.NUM, FunT.ATANH)],
        FunT.ACSCH: [Sign([T.NUM], T.NUM, FunT.ACSCH)],
        FunT.ASECH: [Sign([T.NUM], T.NUM, FunT.ASECH)],
        FunT.ACOTH: [Sign([T.NUM], T.NUM, FunT.ACOTH)]
    }
```

Function calling signatures of hyperbolic trigonometric functions and their inverses for type checking.
Note that all of them have identical and unique calling signature `T.NUM Fun[T.NUM]`.

## __sinh(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where sine hyperbolic function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of sine hyperbolic function. |

It is simple helper for `simplify` computing `Sinh[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Sinh[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: |
| `Sinh[x]` | `nan` | `-inf` | $\sinh(x)$ | `inf` |

The value of $\sinh(x)$ is computed using `math.sinh` in basic Python math package `math`.
The implementation of `math.sinh` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `sinh` function in `cmath` library.
Unfortunately, the implementation `sinh` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Sinh[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Sinh_Small](Figures/Sinh_Small.eps)

__Figure 1__. Error of `Sinh[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$.

#### ** Medium input **
![Sinh_Medium](Figures/Sinh_Medium.eps)

__Figure 2__. Error of `Sinh[x]` on $[-50,\,50]$. Input points are drawn randomly from $\mathbf{U}(-50,\,50)$.

#### ** Large input **
![Sinh_Large](Figures/Sinh_Large.eps)

__Figure 3__. Error of `Sinh[x]` on $[-500,\,500]$. Input points are drawn randomly from $\mathbf{U}(-500,\,500)$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __cosh(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where cosine hyperbolic function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of cosine hyperbolic function. |

It is simple helper for `simplify` computing `Cosh[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Cosh[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: |
| `Cosh[x]` | `nan` | `inf` | $\cosh(x)$ | `inf` |

The value of $\cos(x)$ is computed using `math.cosh` in basic Python math package `math`.
The implementation of `math.cosh` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `cosh` function in `cmath` library.
Unfortunately, the implementation `cosh` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Cosh[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Cosh_Small](Figures/Cosh_Small.eps)

__Figure 1__. Error of `Cosh[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$.

#### ** Medium input **
![Cosh_Medium](Figures/Cosh_Medium.eps)

__Figure 2__. Error of `Cosh[x]` on $[-50,\,50]$. Input points are drawn randomly from $\mathbf{U}(-50,\,50)$.

#### ** Large input **
![Cosh_Large](Figures/Cosh_Large.eps)

__Figure 3__. Error of `Cosh[x]` on $[-500,\,500]$. Input points are drawn randomly from $\mathbf{U}(-500,\,500)$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __tanh(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where tangent hyperbolic function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of tangent hyperbolic function. |

It is simple helper for `simplify` computing `Tanh[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Tanh[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: |
| `Tanh[x]` | `nan` | $-1$ | $\tanh(x)$ | $1$ |

The value of $\tan(x)$ is computed using `math.tanh` in basic Python math package `math`.
The implementation of `math.tanh` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `tanh` function in `cmath` library.
Unfortunately, the implementation `tanh` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Tanh[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Tanh_Small](Figures/Tanh_Small.eps)

__Figure 1__. Error of `Tanh[x]` on $[-3,\,3]$. Input points are drawn randomly from $\mathbf{U}(-3,\,3)$.

#### ** Medium input **
![Tanh_Medium](Figures/Tanh_Medium.eps)

__Figure 2__. Error of `Tanh[x]` on $[-30,\,30]$. Input points are drawn randomly from $\mathbf{U}(-30,\,30)$.

#### ** Large input **
![Tanh_Large](Figures/Tanh_Large.eps)

__Figure 3__. Error of `Tanh[x]` on $[-300,\,300]$. Input points are drawn randomly from $\mathbf{U}(-300,\,300)$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __csch(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where cosecant hyperbolic function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of cosecant hyperbolic function. |

It is simple helper for `simplify` computing `Csch[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Csch[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}\setminus\{0\}$ | $\{0\}$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Csch[x]` | `nan` | $0$ | $\mathrm{cosech}(x)$ | `nan` | $0$ |

The value of $\cosec(x)$ is computed as `1 / math.sinh(x)` which reflects its definition directly.
Thus error will depend on implementation of `math.sinh` which we described in detail [above](#__sinhx).

Anyway, we present a thorough report on errors of `Csch[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Csch_Small](Figures/Csch_Small.eps)

__Figure 1__. Error of `Csch[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$.

#### ** Medium input **
![Csch_Medium](Figures/Csch_Medium.eps)

__Figure 2__. Error of `Csch[x]` on $[-50,\,50]$. Input points are drawn randomly from $\mathbf{U}(-50,\,50)$.

#### ** Large input **
![Csch_Large](Figures/Csch_Large.eps)

__Figure 3__. Error of `Csch[x]` on $[-500,\,500]$. Input points are drawn randomly from $\mathbf{U}(-500,\,500)$.
<!-- tabs:end -->

## __sech(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where secant hyperbolic function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of secant hyperbolic function. |

It is simple helper for `simplify` computing `Sech[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Sech[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: |
| `Sech[x]` | `nan` | $0$ | $\mathrm{sech}(x)$ | $0$ |

The value of $\mathrm{sech}(x)$ is computed as `1 / math.cosh(x)` which reflects its definition directly.
Thus error will depend on implementation of `math.cosh` which we described in detail [above](#__coshx).

Anyway, we present a thorough report on errors of `Sech[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Sech_Small](Figures/Sech_Small.eps)

__Figure 1__. Error of `Sech[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$.

#### ** Medium input **
![Sech_Medium](Figures/Sech_Medium.eps)

__Figure 2__. Error of `Sech[x]` on $[-50,\,50]$. Input points are drawn randomly from $\mathbf{U}(-50,\,50)$.

#### ** Large input **
![Sech_Large](Figures/Sech_Large.eps)

__Figure 3__. Error of `Sech[x]` on $[-500,\,500]$. Input points are drawn randomly from $\mathbf{U}(-500,\,500)$.
<!-- tabs:end -->

## __coth(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where cotangent hyperbolic function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of cotangent hyperbolic function. |

It is simple helper for `simplify` computing `Coth[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Coth[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}\setminus\{0\}$ | $\{0\}$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Coth[x]` | `nan` | $-1$ | $\coth(x)$ | `nan` | $1$ |

The value of $\coth(x)$ is computed as `1 / math.tanh(x)` which reflects its definition directly.
Thus error will depend on implementation of `math.tanh` which we described in detail [above](#__tanhx).

Anyway, we present a thorough report on errors of `Coth[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Coth_Small](Figures/Coth_Small.eps)

__Figure 1__. Error of `Coth[x]` on $[-3,\,3]$. Input points are drawn randomly from $\mathbf{U}(-3,\,3)$.

#### ** Medium input **
![Coth_Medium](Figures/Coth_Medium.eps)

__Figure 2__. Error of `Coth[x]` on $[-30,30]$. Input points are drawn randomly from $\mathbf{U}(-30,\,30)$.

#### ** Large input **
![Coth_Large](Figures/Coth_Large.eps)

__Figure 3__. Error of `Coth[x]` on $[-300,\,300]$. Input points are drawn randomly from $\mathbf{U}(-300,\,300)$.
<!-- tabs:end -->

## __asinh(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where arcsine hyperbolic function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of arcsine hyperbolic function. |

It is simple helper for `simplify` computing `Asinh[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Asinh[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: |
| `Asinh[x]` | `nan` | `-inf` | $\mathrm{asinh}(x)$ | `inf` |

The value of $\mathrm{asinh}(x)$ is computed using `math.asinh` in basic Python math package `math`.
The implementation of `math.asinh` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `asinh` function in `cmath` library.
Unfortunately, the implementation `asinh` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Asinh[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Asinh_Small](Figures/Asinh_Small.eps)

__Figure 1__. Error of `Asinh[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$.

#### ** Medium input **
![Asinh_Medium](Figures/Asinh_Medium.eps)

__Figure 2__. Error of `Asinh[x]` on $[-500,\,500]$. Input points are drawn randomly from $\mathbf{U}(-500,\,500)$.

#### ** Large input **
![Asinh_Large](Figures/Asinh_Large.eps)

__Figure 3__. Error of `Asinh[x]` on $[-5\times10^{10},\,5\times10^{10}]$. Input points are drawn randomly from $\mathbf{U}(-5\times10^{10},\,5\times10^{10})$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __acosh(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where arccosine hyperbolic function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of arccosine hyperbolic function. |

It is simple helper for `simplify` computing `Acosh[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Acosh[x]` is as follows.

| `x` | `nan` | `-inf` | $[1,\,\infty)$ | $(-\infty,\,1)$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Acosh[x]` | `nan` | `nan` | $\mathrm{acosh}(x)$ | `nan` | `inf` |

The value of $\mathrm{acosh}(x)$ is computed using `math.acosh` in basic Python math package `math`.
The implementation of `math.acosh` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `acosh` function in `cmath` library.
Unfortunately, the implementation `acosh` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Acosh[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Acosh_Small](Figures/Acosh_Small.eps)

__Figure 1__. Error of `Acosh[x]` on $[1,\,5]$. Input points are drawn randomly from $\mathbf{U}(1,\,5)$.

#### ** Medium input **
![Acosh_Medium](Figures/Acosh_Medium.eps)

__Figure 2__. Error of `Acosh[x]` on $[1,\,500]$. Input points are drawn randomly from $\mathbf{U}(1,\,500)$.

#### ** Large input **
![Acosh_Large](Figures/Acosh_Large.eps)

__Figure 3__. Error of `Acosh[x]` on $[1,\,5\times10^{10}]$. Input points are drawn randomly from $\mathbf{U}(1,\,5\times10^{10})$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __atanh(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where arctangent hyperbolic function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of arctangent hyperbolic function. |

It is simple helper for `simplify` computing `Atanh[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Atanh[x]` is as follows.

| `x` | `nan` | `-inf` | $-1$ | $(-1,\,1)$ | $1$ | $\mathbb{R}\setminus[-1,\,1]$ |  `inf` |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `Atanh[x]` | `nan` | `nan` | `-inf` | $\mathrm{atanh}(x)$ | `inf` | `nan` | `nan` |

The value of $\mathrm{atanh}(x)$ is computed using `math.atanh` in basic Python math package `math`.
The implementation of `math.atanh` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `atan` function in `cmath` library.
Unfortunately, the implementation `atanh` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Atanh[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Atanh_Small](Figures/Atanh_Small.eps)

__Figure 1__. Error of `Atan[x]` on $[-1,\,1]$. Input points are drawn randomly from $\mathbf{U}(-1,\,1)$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __acsch(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where arccosecant hyperbolic function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of arccosecant hyperbolic function. |

It is simple helper for `simplify` computing `Acsch[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Acsch[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}\setminus\{0\}$ | $\{0\}$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Acsch[x]` | `nan` | $0$ | $\mathrm{acosech}(x)$ | `nan` | $0$ | 

The value of $\mathrm{acosech}(x)$ is computed as `math.asinh(1 / x)` which comes from identity $\mathrm{acosech}(x)=\mathrm{asinh}(1/x)$.
Thus error will depend on implementation of `math.asinh` which we described in detail [above](#__asinhx).
For more information on the identity we used, consult to the reference below.

Anyway, we present a thorough report on errors of `Acsch[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Acsch_Small](Figures/Acsch_Small.eps)

__Figure 1__. Error of `Acsch[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$.

#### ** Medium input **
![Acsch_Medium](Figures/Acsch_Medium.eps)

__Figure 2__. Error of `Acsch[x]` on $[-500,\,500]$. Input points are drawn randomly from $\mathbf{U}(-500,\,500)$.

#### ** Large input **
![Acsch_Large](Figures/Acsch_Large.eps)

__Figure 3__. Error of `Acsch[x]` on $[-5\times10^{10},\,5\times10^{10}]$. Input points are drawn randomly from $\mathbf{U}(-5\times10^{10},\,5\times10^{10})$.
<!-- tabs:end -->

- References
    1. [https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions](https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions)

## __asech(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where arcsecant hyperbolic function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of arcsecant hyperbolic function. |

It is simple helper for `simplify` computing `Asech[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Asech[x]` is as follows.

| `x` | `nan` | `-inf`| $0$ | $(0,\,1]$ | $\mathbb{R}\setminus[0,\,1]$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| `Asech[x]` | `nan` | `nan` | `inf` | $\mathrm{asech}(x)$ | `nan` | `nan` | 

The value of $\mathrm{asec}(x)$ is computed as `math.acosh(1 / x)` which comes from identity $\mathrm{asech}(x)=\mathrm{acosh}(1/x)$.
Thus error will depend on implementation of `math.acosh` which we described in detail [above](#__acoshx).
For more information on the identity we used, consult to the reference below.

Anyway, we present a thorough report on errors of `Asech[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Asech_Small](Figures/Asech_Small.eps)

__Figure 1__. Error of `Asech[x]` on $[0,\,1]$. Input points are drawn randomly from $\mathbf{U}(0,\,1)$.
<!-- tabs:end -->

- References
    1. [https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions](https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions)

## __acoth(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where arccotangent hyperbolic function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of arccotagent hyperbolic function. |

It is simple helper for `simplify` computing `Acoth[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Acoth[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}\setminus[-1,\,1]$ | $-1$ | $(-1,\,1)$ | $1$ |`inf` |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `Acoth[x]` | `nan` | $0$ | $\mathrm{acoth}(x)$ | `-inf` | `nan` | `inf` |  $0$ |

The value of $\mathrm{acoth}(x)$ is computed as `math.atanh(1 / x)` which comes from identity $\mathrm{acoth}(x)=\mathrm{atanh}(1/x)$.
Thus error will depend on implementation of `math.atanh` which we described in detail [above](#__atanhx).
For more information on the identity we used, consult to the reference below.

Anyway, we present a thorough report on errors of `Acoth[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Acoth_Small](Figures/Acoth_Small.eps)

__Figure 1__. Error of `Acoth[x]` on $[-5,\,5]$.
Input points are drawn randomly from $\mathbf{U}(-4,\,4)$ and mapped by $x\mapsto (x-1)\mathbf{1}_{\mathbb{R}^-}(x)+(x+1)\mathbf{1}_{\mathbb{R}^+}(x)$.

#### ** Medium input **
![Acoth_Medium](Figures/Acoth_Medium.eps)

__Figure 2__. Error of `Acoth[x]` on $[-500,\,500]$.
Input points are drawn randomly from $\mathbf{U}(-499,\,499)$ and mapped by $x\mapsto (x-1)\mathbf{1}_{\mathbb{R}^-}(x)+(x+1)\mathbf{1}_{\mathbb{R}^+}(x)$.

#### ** Large input **
![Acoth_Large](Figures/Acoth_Large.eps)

__Figure 3__. Error of `Acoth[x]` on $[-5\times10^{10},\,5\times10^{10}]$.
Input points are drawn randomly from $\mathbf{U}(-5\times10^{10}+1,\,5\times10^{10}-1)$ and mapped by $x\mapsto (x-1)\mathbf{1}_{\mathbb{R}^-}(x)+(x+1)\mathbf{1}_{\mathbb{R}^+}(x)$.
<!-- tabs:end -->

- References
    1. [https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions](https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions)

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
Also, `rt`'s token value must be one of hyperbolic trigonometric functions and their inverses listed [above](#__sign).
After type checking, it will fill in `t` field of `rt` with inferred return type in case of no type error.

For type checking, it first constructs _inferred signature_ of `rt` using its children's inferred type and `__sign`.
Then it finds _candidate signatures_ of `rt` from `__sign` which is basically a list of all possible valid calling signatures.
Since all hyperbolic trigonometric functions and their inverses have unique calling signature, candidate signature will be always a list of size 1.
With this inferred signature and candidate signatures, it can simply determine whether the user input is valid or not.
If there is a matching signature among candidates, it is valid. Otherwise, it is not.
If there is match, then it fills in `t` field of `rt` with return type of inferred signature (which will be `T.NUM` always) and terminates by returning `None`.
Otherwise, it immediately terminates by returning the list of candidate signatures.
Caller of this method can tell the existence of type error by inspecting its return value and use returned candidate signature information for error handling.

- Example
```python
    # Not runnable! Just for conceptual understanding.
    from Core.Parser import Parser
    from Function.HyperbolicTrigonometric import HyperTri
    
    # Input: Sinh[2, "2"]
    line = input()
    AST = Parser.inst().parse(line)
    
    # Inferred signature: T.NUM Sinh[T.NUM, T.STR]
    # Candidate signatures: T.NUM Sinh[T.NUM]
    # Type error. Return candidate signatures [Sign([T.NUM], T.NUM, FunT.SINH)].
    cand = HyperTri.chk_t(AST.rt)
    
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
| `BIG_INT` | Given parameter is greater than the maximum size of representable `float` size, `sys.float_info.max`.
| `SMALL_INT` | Given parameter is smaller than the minimum size of representable `float` size, `-sys.float_info.max`.

It simplifies partial AST rooted at `rt` using simplification strategies described at ...
Since it assumes that all children of `rt` is already simplified, simplification of `rt`'s children should be preceded before calling this method.
Also, `rt`'s token value must be one of hyperbolic trigonometric functions and their inverses listed [above](#__sign).
After simplification, it returns the root token of simplified partial AST and list of warnings generated during simplification process.

> [!NOTE]
> Multiple warnings can be generated during one simplification.

For simplification, it branches flow by looking up the token value of `rt` and executes corresponding simplification logic.
Although simplification logic is quite complicated, we shall present in-depth description of these logic here.

### Sinh
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Sinh[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

- Constant folding

If `x` is numeric token, it just computes `Sinh[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__sinh`.
Thus, for detailed computation rules, refer to the documentation [above](#__sinhx).

- Sign propagation

Since sine hyperbolic function is odd function, sign can be propagated using identity $\sinh(-x)=-\sinh(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this propagation is indeed safe.

### Cosh
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Cosh[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

- Constant folding

If `x` is numeric token, it just computes `Cosh[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__cosh`.
Thus, for detailed computation rules, refer to the documentation [above](#__coshx).

- Dead expression stripping

Since cosine hyperbolic function is even function, minus sign inside of cosine can be safely removed using identity $\cosh(-x)=\cosh(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this removal is indeed safe.

### Tanh
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Tanh[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

- Constant folding

If `x` is numeric token, it just computes `Tanh[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__tanh`.
Thus, for detailed computation rules, refer to the documentation [above](#__tanhx).

- Sign propagation

Since tangent hyperbolic function is odd function, sign can be propagated using identity $\tanh(-x)=-\tanh(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this propagation is indeed safe.

### Csch
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Csch[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is $0$, it generates `POLE_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

- Constant folding

If `x` is numeric token, it just computes `Csch[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__csch`.
Thus, for detailed computation rules, refer to the documentation [above](#__cschx).

- Sign propagation

Since cosecant hyperbolic function is odd function, sign can be propagated using identity $\mathrm{cosech}(-x)=-\mathrm{cosech}(x)$.
Note that this identity holds not only for $x\in\mathbb{R}\setminus\{0\}$, but also for `nan`, `+-inf`, and $x=0$.
Thus this propagation is indeed safe.

### Sech
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Sech[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

- Constant folding

If `x` is numeric token, it just computes `Sech[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__sech`.
Thus, for detailed computation rules, refer to the documentation [above](#__sechx).

- Dead expression stripping

Since secant hyperbolic function is even function, minus sign inside of secant can be safely removed using identity $\mathrm{sech}(-x)=\mathrm{sech}(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this removal is indeed safe.

### Coth
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Coth[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is $0$, it generates `POLE_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

- Constant folding

If `x` is numeric token, it just computes `Coth[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__coth`.
Thus, for detailed computation rules, refer to the documentation [above](#__cothx).

- Sign propagation

Since cotangent function is odd function, sign can be propagated using identity $\coth(-x)=-\coth(x)$.
Note that this identity holds not only for $x\in\mathbb{R}\setminus\{0\}$, but also for `nan`, `+-inf`, and $x=0$.
Thus this propagation is indeed safe.

### Asinh
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Asinh[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

- Constant folding

If `x` is numeric token, it just computes `Asinh[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__asinh`.
Thus, for detailed computation rules, refer to the documentation [above](#__asinhx).

- Sign propagation

Since arcsine hyperbolic function is odd function, sign can be propagated using identity $\mathrm{asinh}(-x)=-\mathrm{asinh}(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this propagation is indeed safe.

### Acosh
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Acosh[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
3. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
4. If `x` is not in $[1,\,\infty)$, it generates `DOMAIN_OUT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `INF_DETECT` is generated by rule 3, `DOMAIN_OUT` warning will not be generated by rule 4.

> [!TIP]
> Trivially, the case of `x` being smaller than the minimum size of representable `float` size will be captured by rule 4.
In this case, it replaces `x` with `0` for technical reason.
Note that this does not make any change in the result of computation.

- Constant folding

If `x` is numeric token, it just computes `Acosh[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__acosh`.
Thus, for detailed computation rules, refer to the documentation [above](#__acoshx).

### Atanh
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Atan[x]` are as follows.
1. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
2. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
3. If `x` is $1$ or $-1$, it generates `POLE_DETECT` warning.
4. If `x` is not in $(-1,\,1)$, it generates `DOMAIN_OUT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `INF_DETECT` is generated by rule 2, `DOMAIN_OUT` warning will not be generated by rule 4.

> [!TIP]
> Trivially, the case of `x` being greater than the maximum size of representable `float` size or less than the minimum size of representable `float` size will be captured by rule 4.
In these cases, it replaces `x` with `2` for technical reason.
Note that this does not make any change in the result of computation.

- Constant folding

If `x` is numeric token, it just computes `Atanh[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__atanh`.
Thus, for detailed computation rules, refer to the documentation [above](#__atanhx).

- Sign propagation

Since arctangent hyperbolic function is odd function, sign can be propagated using identity $\mathrm{atanh}(-x)=-\mathrm{atanh}(x)$.
Note that this identity holds not only for $x\in(-1,\,1)$, but also for `nan`, `+-inf` and $x\in\mathbb{R}\setminus(-1,\,1)$.
Thus this propagation is indeed safe.

### Acsch
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Acsch[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is $0$, it generates `POLE_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

- Constant folding

If `x` is numeric token, it just computes `Acsch[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__acsch`.
Thus, for detailed computation rules, refer to the documentation [above](#__acschx).

- Sign propagation

Since arccosecant function is odd function, sign can be propagated using identity $\mathrm{acosech}(-x)=-\mathrm{acosech}(x)$.
Note that this identity holds not only for $x\in\mathbb{R}\setminus\{0\}$, but also for `nan`,`+-inf`, and $x=0$.
Thus this propagation is indeed safe.

### Asech
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Asech[x]` are as follows.
1. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
2. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
3. If `x` is $0$, it generates `POLE_DETECT` warning.
4. If `x` is not in $(0,\,1]$, it generates `DOMAIN_OUT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `INF_DETECT` is generated by rule 2, `DOMAIN_OUT` warning will not be generated by rule 4.

> [!TIP]
> Trivially, the case of `x` being greater than the maximum size of representable `float` size or less than the minimum size of representable `float` size will be captured by rule 4.
In these cases, it replaces `x` with `2` for technical reason.
Note that this does not make any change in the result of computation.

- Constant folding

If `x` is numeric token, it just computes `Asech[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__asech`.
Thus, for detailed computation rules, refer to the documentation [above](#__asechx).

### Acoth
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Acoth[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is $-1$ or $1$, it generates `POLE_DETECT` warning.
6. If `x` is in $(-1,\,1)$, it generates `DOMAIN_OUT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

- Constant folding

If `x` is numeric token, it just computes `Acoth[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__acoth`.
Thus, for detailed computation rules, refer to the documentation [above](#__acothx).

- Sign propagation

Since arccotangent function is odd function, sign can be propagated using identity $\mathrm{acoth}(-x)=-\mathrm{acoth}(x)$.
Note that this identity holds not only for $x\in\mathbb{R}\setminus[-1,\,1]$, but also for `nan`,`+-inf`, and $x\in[-1,\,1]$.
Thus this propagation is indeed safe.

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
Since all hyperbolic trigonometric functions and their inverses have unique calling signature `T.NUM fun(T.NUM)`, parameter `test_in` must have form of `[[arg], [arg], ...]`.

- Returns

| Type | Description |
| --- | --- |
| `List[Decimal]` | Test outputs. |

It simply computes test outputs of function indicated by `fun` at test input points `test_in`.
The value of `fun` must be one of trigonometric functions and their inverses listed [above](#__sign).
For accuracy, it takes `test_in` as `Decimal`, which is a class in `decimal` package that supports arbitrary precision arithmetic in Python.
By default, the precision (# of significant digits) is 300, but it can be customized.

For test output generation, it simply branches flow by looking up `fun` and computes outputs using the basic implementation of each `fun` described above.
Since there is no logic for error handling, `test_in` must be generated with care so that there is no chance of encountering erroneous situation like `math.asin(math.factorial(200))` which causes `OverflowError`.
After computing all test outputs, the result will be returned as `Decimal` again.

- Example
```python
    from decimal import Decimal
    from Core.Type import FunT
    from Function.HyperbolicTrigonometric import HyperTri
    
    # Uniform 100 test input points from [0, 100).
    test_in = [Decimal(n) for n in range(100)]
    # Computes value of math.tanh(n) for n in test points.
    test_out = HyperTri.test(FunT.TANH, test_in)
```