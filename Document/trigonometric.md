# Class Tri

> Trigonometric function toolbox.

> [!DANGER]
> This class is implemented as an [abstract class](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html) of JAVA.
That is, it cannot be initialized or instantiated.
If one tries to instantiate this class, it will throw `NotImplementedError` at `__init__`.
Since all methods are class method, one should use them as `Tri.chk_t`.

Class `Tri` supports following usual trigonometric functions and inverse of them.

| Function | Definition | Domain | Range |
| --- | --- | --- | --- |
| `Sin[x]` | $\sin(x) = \sum_{n=0}^\infty\frac{(-1)^n}{(2n+1)!}x^{2n+1}$ | $\mathbb{R}$ | $[-1,\,1]$ |
| `Cos[x]` | $\cos(x) = \sum_{n=0}^\infty\frac{(-1)^n}{(2n)!}x^{2n}$ | $\mathbb{R}$ | $[-1,\,1]$ |
| `Tan[x]` | $\tan(x) = \frac{\sin(x)}{\cos(x)}$ | $\mathbb{R}\setminus(\pi\mathbb{Z}+\pi/2)$ | $\mathbb{R}$ |
| `Csc[x]` | $\cosec(x) = \frac{1}{\sin(x)}$ | $\mathbb{R}\setminus\pi\mathbb{Z}$ | $\mathbb{R}\setminus(-1,\,1)$ |
| `Sec[x]` | $\sec(x) = \frac{1}{\cos(x)}$ | $\mathbb{R}\setminus(\pi\mathbb{Z}+\pi/2)$ | $\mathbb{R}\setminus(-1,\,1)$ |
| `Cot[x]` | $\cot(x) = \frac{1}{\tan(x)}$ | $\mathbb{R}\setminus\pi\mathbb{Z}$ | $\mathbb{R}$ |
| `Asin[x]` | $\mathrm{asin}(x) = \sin\vert_{[-\pi/2,\,\pi/2]}^{-1}(x)$ | $[-1,\,1]$ | $[-\pi/2,\,\pi/2]$ |
| `Acos[x]` | $\mathrm{acos}(x) = \cos\vert_{[0,\,\pi]}^{-1}(x)$ | $[-1,\,1]$ | $[0,\,\pi]$ |
| `Atan[x]` | $\mathrm{atan}(x) = \tan\vert_{[-\pi/2,\,\pi/2]}^{-1}(x)$ | $\mathbb{R}$ | $[-\pi/2,\,\pi/2]$ |
| `Acsc[x]` | $\mathrm{acosec}(x) = \cosec\vert_{[-\pi/2,\,\pi/2]\setminus\{0\}}^{-1}(x)$ | $\mathbb{R}\setminus(-1,\,1)$ | $[-\pi/2,\,\pi/2]\setminus\{0\}$ |
| `Asec[x]` | $\mathrm{asec}(x) = \sec\vert_{[0,\,\pi]\setminus\{\pi/2\}}^{-1}(x)$ | $\mathbb{R}\setminus(-1,\,1)$ | $[0,\,\pi]\setminus\{\pi/2\}$ |
| `Acot[x]` | $\mathrm{acot}(x) = \cot\vert_{(-\pi/2,\,\pi/2]\setminus\{0\}}^{-1}(x)$ | $\mathbb{R}$ | $(-\pi/2,\,\pi/2]\setminus\{0\}$ |

> [!NOTE]
> 1. Here, $f\vert_{D'}$ for function $f:D\to R$ and subset $D'\subseteq D$ implies the restriction of function $f$ to $D'$.
2. For convenience, we employ convention $1/\pm\infty=0$.
3. One can easily show that power series definition of sine and cosine functions have radius of convergence $\infty$ so that they are indeed well-defined.

We present some simple graph of functions above.
Following plots are computed and rendered by MATLAB and one can read detailed description on these code at ...

<center>
<!-- tabs:start -->
#### ** Sin **
![Sin_Graph](Figures/Sin_Graph.eps)

__Figure 1__. Graph of $\sin(x)$ on $[-2\pi,\,2\pi]$.

#### ** Cos **
![Cos_Graph](Figures/Cos_Graph.eps)

__Figure 2__. Graph of $\cos(x)$ on $[-2\pi,\,2\pi]$.

#### ** Tan **
![Tan_Graph](Figures/Tan_Graph.eps)

__Figure 3__. Graph of $\tan(x)$ on $[-\pi,\,\pi]$.<br/>
Gray dashes are asymptotic line of tangent function, $x=\pm\pi/2$.

#### ** Csc **
![Csc_Graph](Figures/Csc_Graph.eps)

__Figure 4__. Graph of $\cosec(x)$ on $[-2\pi,\,2\pi]$.<br/>
Gray dashes are asymptotic line of cosecant function, $x=\pm\pi$ and $x=0$.

#### ** Sec **
![Sec_Graph](Figures/Sec_Graph.eps)

__Figure 5__. Graph of $\sec(x)$ on $[-2\pi,\,2\pi]$.<br/>
Gray dashes are asymptotic line of secant function, $x=\pm3\pi / 2$ and $x=\pm\pi/2$.

#### ** Cot **
![Cot_Graph](Figures/Cot_Graph.eps)

__Figure 6__. Graph of $\cot(x)$ on $[-\pi,\,\pi]$.<br/>
Gray dash is asymptotic line of cotangent function, $x=0$.

#### ** Asin **
![Asin_Graph](Figures/Asin_Graph.eps)

__Figure 7__. Graph of $\mathrm{asin}(x)$ on $[-1,\,1]$.

#### ** Acos **
![Acos_Graph](Figures/Acos_Graph.eps)

__Figure 8__. Graph of $\mathrm{acos}(x)$ on $[-1,\,1]$.

#### ** Atan **
![Atan_Graph](Figures/Atan_Graph.eps)

__Figure 9__. Graph of $\mathrm{atan}(x)$ on $[-5,\,5]$.<br/>
Gray dashes are asymptotic line of arctangent function, $y=\pm\pi/2$.

#### ** Acsc **
![Acsc_Graph](Figures/Acsc_Graph.eps)

__Figure 10__. Graph of $\mathrm{acosec}(x)$ on $[-5,\,5]$.<br/>
Here, $x$ axis is asymptotic line of arccosecant function.

#### ** Asec **
![Asec_Graph](Figures/Asec_Graph.eps)

__Figure 11__. Graph of $\mathrm{asec}(x)$ on $[-5,\,5]$.<br/>
Gray dash is asymptotic line of arcsecant function, $y=\pi/2$.

#### ** Acot **
![Acot_Graph](Figures/Acot_Graph.eps)

__Figure 12__. Graph of $\mathrm{acot}(x)$ on $[-5,\,5]$.<br/>
Here, $x$ axis is asymptotic line of arccotangent function.
<!-- tabs:end -->
</center>

For more information on trigonometric functions and their inverses, refer to following references.
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
        FunT.SIN: [Sign([T.NUM], T.NUM, FunT.SIN)],
        FunT.COS: [Sign([T.NUM], T.NUM, FunT.COS)],
        FunT.TAN: [Sign([T.NUM], T.NUM, FunT.TAN)],
        FunT.CSC: [Sign([T.NUM], T.NUM, FunT.CSC)],
        FunT.SEC: [Sign([T.NUM], T.NUM, FunT.SEC)],
        FunT.COT: [Sign([T.NUM], T.NUM, FunT.COT)],
        FunT.ASIN: [Sign([T.NUM], T.NUM, FunT.ASIN)],
        FunT.ACOS: [Sign([T.NUM], T.NUM, FunT.ACOS)],
        FunT.ATAN: [Sign([T.NUM], T.NUM, FunT.ATAN)],
        FunT.ACSC: [Sign([T.NUM], T.NUM, FunT.ACSC)],
        FunT.ASEC: [Sign([T.NUM], T.NUM, FunT.ASEC)],
        FunT.ACOT: [Sign([T.NUM], T.NUM, FunT.ACOT)]
    }
```

Function calling signatures of trigonometric functions and their inverses for type checking.
Note that all of them have identical and unique calling signature `T.NUM Fun[T.NUM]`.

## __sin(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where sine function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of sine function. |

It is simple helper for `simplify` computing `Sin[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Sin[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: |
| `Sin[x]` | `nan` | `nan` | $\sin(x)$ | `nan` |

The value of $\sin(x)$ is computed using `math.sin` in basic Python math package `math`.
The implementation of `math.sin` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `sin` function in `cmath` library.
Unfortunately, the implementation `sin` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Sin[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Sin_Small](Figures/Sin_Small.eps)

__Figure 1__. Error of `Sin[x]` on $[0,\,2\pi]$. Input points are drawn randomly from $\mathbf{U}(0,\,2\pi)$.

#### ** Medium input **
![Sin_Medium](Figures/Sin_Medium.eps)

__Figure 2__. Error of `Sin[x]` on $[-100\pi,\,100\pi]$. Input points are drawn randomly from $\mathbf{U}(-100\pi,\,100\pi)$.

#### ** Large input **
![Sin_Large](Figures/Sin_Large.eps)

__Figure 3__. Error of `Sin[x]` on $[-10^{10}\pi,\,10^{10}\pi]$. Input points are drawn randomly from $\mathbf{U}(-10^{10}\pi,\,10^{10}\pi)$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __cos(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where cosine function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of cosine function. |

It is simple helper for `simplify` computing `Cos[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Cos[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: |
| `Cos[x]` | `nan` | `nan` | $\cos(x)$ | `nan` |

The value of $\cos(x)$ is computed using `math.cos` in basic Python math package `math`.
The implementation of `math.cos` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `cos` function in `cmath` library.
Unfortunately, the implementation `cos` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Cos[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Cos_Small](Figures/Cos_Small.eps)

__Figure 1__. Error of `Cos[x]` on $[0,\,2\pi]$. Input points are drawn randomly from $\mathbf{U}(0,\,2\pi)$.

#### ** Medium input **
![Cos_Medium](Figures/Cos_Medium.eps)

__Figure 2__. Error of `Cos[x]` on $[-100\pi,\,100\pi]$. Input points are drawn randomly from $\mathbf{U}(-100\pi,\,100\pi)$.

#### ** Large input **
![Cos_Large](Figures/Cos_Large.eps)

__Figure 3__. Error of `Cos[x]` on $[-10^{10}\pi,\,10^{10}\pi]$. Input points are drawn randomly from $\mathbf{U}(-10^{10}\pi,\,10^{10}\pi)$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __tan(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where tangent function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of tangent function. |

It is simple helper for `simplify` computing `Tan[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Tan[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}\setminus(\pi\mathbb{Z}+\pi/2)$ | $\pi\mathbb{Z}+\pi/2$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Tan[x]` | `nan` | `nan` | $\tan(x)$ | `nan` | `nan` |

The value of $\tan(x)$ is computed using `math.tan` in basic Python math package `math`.
The implementation of `math.tan` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `tan` function in `cmath` library.
Unfortunately, the implementation `tan` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Tan[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Tan_Small](Figures/Tan_Small.eps)

__Figure 1__. Error of `Tan[x]` on $[-\pi/2,\,\pi/2]$. Input points are drawn randomly from $\mathbf{U}(-\pi/2,\,\pi/2)$.

#### ** Medium input **
![Tan_Medium](Figures/Tan_Medium.eps)

__Figure 2__. Error of `Tan[x]` on $[-50\pi,\,50\pi]$. Input points are drawn randomly from $\mathbf{U}(-50\pi,\,50\pi)$.

#### ** Large input **
![Tan_Large](Figures/Tan_Large.eps)

__Figure 3__. Error of `Tan[x]` on $[-10^{10}\pi/2,\,10^{10}\pi/2]$. Input points are drawn randomly from $\mathbf{U}(-10^{10}\pi/2,\,10^{10}\pi/2)$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __csc(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where cosecant function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of cosecant function. |

It is simple helper for `simplify` computing `Csc[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Csc[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}\setminus\pi\mathbb{Z}$ | $\pi\mathbb{Z}$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Csc[x]` | `nan` | `nan` | $\cosec(x)$ | `nan` | `nan` |

The value of $\cosec(x)$ is computed as `1 / math.sin(x)` which reflects its definition directly.
Thus error will depend on implementation of `math.sin` which we described in detail [above](#__sinx).

Anyway, we present a thorough report on errors of `Csc[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Csc_Small](Figures/Csc_Small.eps)

__Figure 1__. Error of `Csc[x]` on $[0,\,2\pi]$. Input points are drawn randomly from $\mathbf{U}(0,\,2\pi)$.

#### ** Medium input **
![Csc_Medium](Figures/Csc_Medium.eps)

__Figure 2__. Error of `Csc[x]` on $[-100\pi,\,100\pi]$. Input points are drawn randomly from $\mathbf{U}(-100\pi,\,100\pi)$.

#### ** Large input **
![Csc_Large](Figures/Csc_Large.eps)

__Figure 3__. Error of `Csc[x]` on $[-10^{10}\pi,\,10^{10}\pi]$. Input points are drawn randomly from $\mathbf{U}(-10^{10}\pi,\,10^{10}\pi)$.
<!-- tabs:end -->

## __sec(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where secant function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of secant function. |

It is simple helper for `simplify` computing `Sec[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Sec[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}\setminus(\pi\mathbb{Z}+\pi/2)$ | $\pi\mathbb{Z}+\pi/2$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Sec[x]` | `nan` | `nan` | $\sec(x)$ | `nan` | `nan` |

The value of $\sec(x)$ is computed as `1 / math.cos(x)` which reflects its definition directly.
Thus error will depend on implementation of `math.cos` which we described in detail [above](#__cosx).

Anyway, we present a thorough report on errors of `Sec[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Sec_Small](Figures/Sec_Small.eps)

__Figure 1__. Error of `Sec[x]` on $[0,\,2\pi]$. Input points are drawn randomly from $\mathbf{U}(0,\,2\pi)$.

#### ** Medium input **
![Sec_Medium](Figures/Sec_Medium.eps)

__Figure 2__. Error of `Sec[x]` on $[-100\pi,\,100\pi]$. Input points are drawn randomly from $\mathbf{U}(-100\pi,\,100\pi)$.

#### ** Large input **
![Sec_Large](Figures/Sec_Large.eps)

__Figure 3__. Error of `Sec[x]` on $[-10^{10}\pi,\,10^{10}\pi]$. Input points are drawn randomly from $\mathbf{U}(-10^{10}\pi,\,10^{10}\pi)$.
<!-- tabs:end -->

## __cot(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where cotangent function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of cotangent function. |

It is simple helper for `simplify` computing `Cot[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Cot[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}\setminus\pi\mathbb{Z}$ | $\pi\mathbb{Z}$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Cot[x]` | `nan` | `nan` | $\cot(x)$ | `nan` | `nan` |

The value of $\cot(x)$ is computed as `1 / math.tan(x)` which reflects its definition directly.
Thus error will depend on implementation of `math.tan` which we described in detail [above](#__tanx).

Anyway, we present a thorough report on errors of `Cot[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Cot_Small](Figures/Cot_Small.eps)

__Figure 1__. Error of `Cot[x]` on $[-\pi/2,\,\pi/2]$. Input points are drawn randomly from $\mathbf{U}(-\pi/2,\,\pi/2)$.

#### ** Medium input **
![Cot_Medium](Figures/Cot_Medium.eps)

__Figure 2__. Error of `Cot[x]` on $[-50\pi,\,50\pi]$. Input points are drawn randomly from $\mathbf{U}(-50\pi,\,50\pi)$.

#### ** Large input **
![Cot_Large](Figures/Cot_Large.eps)

__Figure 3__. Error of `Cot[x]` on $[-10^{10}\pi/2,\,10^{10}\pi/2]$. Input points are drawn randomly from $\mathbf{U}(-10^{10}\pi/2,\,10^{10}\pi/2)$.
<!-- tabs:end -->

## __asin(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where arcsine function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of arcsine function. |

It is simple helper for `simplify` computing `Asin[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Asin[x]` is as follows.

| `x` | `nan` | `-inf` | $[-1,\,1]$ | $\mathbb{R}\setminus[-1,\,1]$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Asin[x]` | `nan` | `nan` | $\mathrm{asin}(x)$ | `nan` | `nan` |

The value of $\mathrm{asin}(x)$ is computed using `math.asin` in basic Python math package `math`.
The implementation of `math.asin` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `asin` function in `cmath` library.
Unfortunately, the implementation `asin` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Asin[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Asin_Small](Figures/Asin_Small.eps)

__Figure 1__. Error of `Asin[x]` on $[-1,\,1]$. Input points are drawn randomly from $\mathbf{U}(-1,\,1)$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __acos(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where arccosine function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of arccosine function. |

It is simple helper for `simplify` computing `Acos[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Acos[x]` is as follows.

| `x` | `nan` | `-inf` | $[-1,\,1]$ | $\mathbb{R}\setminus[-1,\,1]$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Acos[x]` | `nan` | `nan` | $\mathrm{acos}(x)$ | `nan` | `nan` |

The value of $\mathrm{acos}(x)$ is computed using `math.acos` in basic Python math package `math`.
The implementation of `math.acos` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `acos` function in `cmath` library.
Unfortunately, the implementation `acos` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Acos[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Acos_Small](Figures/Acos_Small.eps)

__Figure 1__. Error of `Acos[x]` on $[-1,\,1]$. Input points are drawn randomly from $\mathbf{U}(-1,\,1)$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __atan(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where arctangent function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of arctangent function. |

It is simple helper for `simplify` computing `Atan[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Atan[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: |
| `Atan[x]` | `nan` | $-\pi/2$ | $\mathrm{atan}(x)$ | $\pi/2$ |

The value of $\mathrm{atan}(x)$ is computed using `math.atan` in basic Python math package `math`.
The implementation of `math.atan` depends on Python interpreter.
In case of CPython, it is implemented as a thin wrapper wrapping `atan` function in `cmath` library.
Unfortunately, the implementation `atan` in `cmath` depends heavily on the machine and C compiler you are using.
For more information on implementation, refer to the reference below.

Anyway, we present a thorough report on errors of `Atan[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Atan_Small](Figures/Atan_Small.eps)

__Figure 1__. Error of `Atan[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$.

#### ** Medium input **
![Atan_Medium](Figures/Atan_Medium.eps)

__Figure 2__. Error of `Atan[x]` on $[-500,\,500]$. Input points are drawn randomly from $\mathbf{U}(-500,\,500)$.

#### ** Large input **
![Atan_Large](Figures/Atan_Large.eps)

__Figure 3__. Error of `Atan[x]` on $[-5\times10^{10},\,5\times10^{10}]$. Input points are drawn randomly from $\mathbf{U}(-5\times10^{10},\,5\times10^{10})$.
<!-- tabs:end -->

- References
    1. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## __acsc(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where arccosecant function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of arccosecant function. |

It is simple helper for `simplify` computing `Acsc[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Acsc[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}\setminus(-1,\,1)$ | $(-1,\,1)$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Acsc[x]` | `nan` | $0$ | $\mathrm{acosec}(x)$ | `nan` | $0$ | 

The value of $\mathrm{acosec}(x)$ is computed as `math.asin(1 / x)` which comes from identity $\mathrm{acosec}(x)=\mathrm{asin}(1/x)$.
Thus error will depend on implementation of `math.asin` which we described in detail [above](#__asinx).
For more information on the identity we used, consult to the reference below.

Anyway, we present a thorough report on errors of `Acsc[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Acsc_Small](Figures/Acsc_Small.eps)

__Figure 1__. Error of `Acsc[x]` on $[-5,\,5]$.
Input points are drawn randomly from $\mathbf{U}(-4,\,4)$ and mapped by $x\mapsto (x-1)\mathbf{1}_{\mathbb{R}^-}(x)+(x+1)\mathbf{1}_{\mathbb{R}^+}(x)$.

#### ** Medium input **
![Acsc_Medium](Figures/Acsc_Medium.eps)

__Figure 2__. Error of `Acsc[x]` on $[-500,\,500]$.
Input points are drawn randomly from $\mathbf{U}(-499,\,499)$ and mapped by $x\mapsto (x-1)\mathbf{1}_{\mathbb{R}^-}(x)+(x+1)\mathbf{1}_{\mathbb{R}^+}(x)$.

#### ** Large input **
![Acsc_Large](Figures/Acsc_Large.eps)

__Figure 3__. Error of `Acsc[x]` on $[-5\times10^{10},\,5\times10^{10}]$.
Input points are drawn randomly from $\mathbf{U}(-5\times10^{10}+1,\,5\times10^{10}-1)$ and mapped by $x\mapsto (x-1)\mathbf{1}_{\mathbb{R}^-}(x)+(x+1)\mathbf{1}_{\mathbb{R}^+}(x)$.
<!-- tabs:end -->

- References
    1. [https://en.wikipedia.org/wiki/Inverse_trigonometric_functions](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)

## __asec(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where arcsecant function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of arcsecant function. |

It is simple helper for `simplify` computing `Asec[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Asec[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}\setminus(-1,\,1)$ | $(-1,\,1)$ | `inf` |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Asec[x]` | `nan` | $0$ | $\mathrm{asec}(x)$ | `nan` | $0$ | 

The value of $\mathrm{asec}(x)$ is computed as `math.acos(1 / x)` which comes from identity $\mathrm{asec}(x)=\mathrm{acos}(1/x)$.
Thus error will depend on implementation of `math.acos` which we described in detail [above](#__acosx).
For more information on the identity we used, consult to the reference below.

Anyway, we present a thorough report on errors of `Asec[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Asec_Small](Figures/Asec_Small.eps)

__Figure 1__. Error of `Asec[x]` on $[-5,\,5]$.
Input points are drawn randomly from $\mathbf{U}(-4,\,4)$ and mapped by $x\mapsto (x-1)\mathbf{1}_{\mathbb{R}^-}(x)+(x+1)\mathbf{1}_{\mathbb{R}^+}(x)$.

#### ** Medium input **
![Asec_Medium](Figures/Asec_Medium.eps)

__Figure 2__. Error of `Asec[x]` on $[-500,\,500]$.
Input points are drawn randomly from $\mathbf{U}(-499,\,499)$ and mapped by $x\mapsto (x-1)\mathbf{1}_{\mathbb{R}^-}(x)+(x+1)\mathbf{1}_{\mathbb{R}^+}(x)$.

#### ** Large input **
![Asec_Large](Figures/Asec_Large.eps)

__Figure 3__. Error of `Asec[x]` on $[-5\times10^{10},\,5\times10^{10}]$.
Input points are drawn randomly from $\mathbf{U}(-5\times10^{10}+1,\,5\times10^{10}-1)$ and mapped by $x\mapsto (x-1)\mathbf{1}_{\mathbb{R}^-}(x)+(x+1)\mathbf{1}_{\mathbb{R}^+}(x)$.
<!-- tabs:end -->

- References
    1. [https://en.wikipedia.org/wiki/Inverse_trigonometric_functions](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)

## __acot(x)
<span class="badge badge-pill badge-danger">private</span> <span class="badge badge-pill badge-secondary">class method</span>
- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `float` | Point where arccotangent function is to be computed. |

- Returns

| Type | Description |
| --- | --- |
| `float` | Computed value of arccotagent function. |

It is simple helper for `simplify` computing `Acot[x]`.
For detailed simplification logic, refer to the documentation [below](#simplifyrt).
Computation table for `Acot[x]` is as follows.

| `x` | `nan` | `-inf` | $\mathbb{R}$ | `inf` |
| --- | :---: | :---: | :---: | :---: |
| `Acot[x]` | `nan` | $0$ | $\mathrm{acot}(x)$ | $0$ |

The value of $\mathrm{acot}(x)$ is computed as `-math.pi / 2 - math.atan(x)` for negative `x` and `math.pi / 2 - math.atan(x)` for non-negative `x`.
This comes from identity
$$
\mathrm{acot}(x)=\begin{cases}
    -\pi/2-\mathrm{atan}(x) & \text{when }x<0 \\
    \pi/2-\mathrm{atan}(x) & \text{ow.}
\end{cases}
$$
Thus error will depend on implementation of `math.atan` which we described in detail [above](#atan).
For more information on the identity we used, consult to the reference below.

Anyway, we present a thorough report on errors of `Acot[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 300 significant digits.
Test output is computed by `test` method described [below](#testfun-test_in) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** Small input **
![Acot_Small](Figures/Acot_Small.eps)

__Figure 1__. Error of `Acot[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$.

#### ** Medium input **
![Acot_Medium](Figures/Acot_Medium.eps)

__Figure 2__. Error of `Acot[x]` on $[-500,\,500]$. Input points are drawn randomly from $\mathbf{U}(-500,\,500)$.

#### ** Large input **
![Acot_Large](Figures/Acot_Large.eps)

__Figure 3__. Error of `Acot[x]` on $[-5\times10^{10},\,5\times10^{10}]$. Input points are drawn randomly from $\mathbf{U}(-5\times10^{10},\,5\times10^{10})$.
<!-- tabs:end -->

- References
    1. [https://en.wikipedia.org/wiki/Inverse_trigonometric_functions](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)

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
Also, `rt`'s token value must be one of trigonometric functions and their inverses listed [above](#__sign).
After type checking, it will fill in `t` field of `rt` with inferred return type in case of no type error.

For type checking, it first constructs _inferred signature_ of `rt` using its children's inferred type and `__sign`.
Then it finds _candidate signatures_ of `rt` from `__sign` which is basically a list of all possible valid calling signatures.
Since all trigonometric functions and their inverses have unique calling signature, candidate signature will be always a list of size 1.
With this inferred signature and candidate signatures, it can simply determine whether the user input is valid or not.
If there is a matching signature among candidates, it is valid. Otherwise, it is not.
If there is match, then it fills in `t` field of `rt` with return type of inferred signature (which will be `T.NUM` always) and terminates by returning `None`.
Otherwise, it immediately terminates by returning the list of candidate signatures.
Caller of this method can tell the existence of type error by inspecting its return value and use returned candidate signature information for error handling.

- Example
```python
    # Not runnable! Just for conceptual understanding.
    from Core.Parser import Parser
    from Function.Trigonometric import Tri
    
    # Input: Sin[2, "2"]
    line = input()
    AST = Parser.inst().parse(line)
    
    # Inferred signature: T.NUM Sin[T.NUM, T.STR]
    # Candidate signatures: T.NUM Sin[T.NUM]
    # Type error. Return candidate signatures [Sign([T.NUM], T.NUM, FunT.SIN)].
    cand = Tri.chk_t(AST.rt)
    
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
Also, `rt`'s token value must be one of trigonometric functions and their inverses listed [above](#__sign).
After simplification, it returns the root token of simplified partial AST and list of warnings generated during simplification process.

> [!NOTE]
> Multiple warnings can be generated during one simplification.

For simplification, it branches flow by looking up the token value of `rt` and executes corresponding simplification logic.
Although simplification logic is quite complicated, we shall present in-depth description of these logic here.

### Sin
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Sin[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

- Constant folding

If `x` is numeric token, it just computes `Sin[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__sin`.
Thus, for detailed computation rules, refer to the documentation [above](#__sinx).

- Sign propagation

Since sine function is odd function, sign can be propagated using identity $\sin(-x)=-\sin(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this propagation is indeed safe.

### Cos
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Cos[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

- Constant folding

If `x` is numeric token, it just computes `Cos[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__cos`.
Thus, for detailed computation rules, refer to the documentation [above](#__cosx).

- Dead expression stripping

Since cosine function is even function, minus sign inside of cosine can be safely removed using identity $\cos(-x)=\cos(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this removal is indeed safe.

### Tan
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Tan[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is $(n+1/2)\pi$ for some $n\in\mathbb{Z}$, it generates `POLE_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

> [!WARNING]
> Because of rounding error of floating point arithmetic, `POLE_DETECT` warning might not be generated even if rule 5 is met.
For example, `Tan[100000.5 * Pi]` does not generate `POLE_DETECT` warning and gives result `27379258862.917953` instead of `nan`.

- Constant folding

If `x` is numeric token, it just computes `Tan[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__tan`.
Thus, for detailed computation rules, refer to the documentation [above](#__tanx).

- Sign propagation

Since tangent function is odd function, sign can be propagated using identity $\tan(-x)=-\tan(x)$.
Note that this identity holds not only for $x\in\mathbb{R}\setminus(\pi\mathbb{Z}+\pi/2)$, but also for `nan`, `+-inf`, and $x\in\pi\mathbb{Z}+\pi/2$.
Thus this propagation is indeed safe.

### Csc
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Csc[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is $n\pi$ for some $n\in\mathbb{Z}$, it generates `POLE_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

> [!WARNING]
> Because of rounding error of floating point arithmetic, `POLE_DETECT` warning might not be generated even if rule 5 is met.
For example, `Csc[100000 * Pi]` does not generate `POLE_DETECT` warning and gives result `-29445840474.947422` instead of `nan`.

- Constant folding

If `x` is numeric token, it just computes `Csc[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__csc`.
Thus, for detailed computation rules, refer to the documentation [above](#__cscx).

- Sign propagation

Since cosecant function is odd function, sign can be propagated using identity $\cosec(-x)=-\cosec(x)$.
Note that this identity holds not only for $x\in\mathbb{R}\setminus\pi\mathbb{Z}$, but also for `nan`, `+-inf`, and $x\in\pi\mathbb{Z}$.
Thus this propagation is indeed safe.

### Sec
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Sec[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is $(n+1/2)\pi$ for some $n\in\mathbb{Z}$, it generates `POLE_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

> [!WARNING]
> Because of rounding error of floating point arithmetic, `POLE_DETECT` warning might not be generated even if rule 5 is met.
For example, `Sec[100000.5 * Pi]` does not generate `POLE_DETECT` warning and gives result `27379258862.917953` instead of `nan`.

- Constant folding

If `x` is numeric token, it just computes `Sec[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__sec`.
Thus, for detailed computation rules, refer to the documentation [above](#__secx).

- Dead expression stripping

Since secant function is even function, minus sign inside of secant can be safely removed using identity $\sec(-x)=\sec(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this removal is indeed safe.

### Cot
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Cot[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is $n\pi$ for some $n\in\mathbb{Z}$, it generates `POLE_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

> [!WARNING]
> Because of rounding error of floating point arithmetic, `POLE_DETECT` warning might not be generated even if rule 5 is met.
For example, `Cot[100000 * Pi]` does not generate `POLE_DETECT` warning and gives result `-29445840474.947422` instead of `nan`.

- Constant folding

If `x` is numeric token, it just computes `Cot[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__cot`.
Thus, for detailed computation rules, refer to the documentation [above](#__cotx).

- Sign propagation

Since cotangent function is odd function, sign can be propagated using identity $\cot(-x)=-\cot(x)$.
Note that this identity holds not only for $x\in\mathbb{R}\setminus\pi\mathbb{Z}$, but also for `nan`, `+-inf`, and $x\in\pi\mathbb{Z}$.
Thus this propagation is indeed safe.

### Asin
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Asin[x]` are as follows.
1. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
2. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
3. If `x` is not in $[-1,\,1]$, it generates `DOMAIN_OUT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `INF_DETECT` is generated by rule 2, `DOMAIN_OUT` warning will not be generated by rule 3.

> [!TIP]
> Trivially, the case of `x` being greater than the maximum size of representable `float` size or less than the minimum size of representable `float` size will be captured by rule 3.
In these cases, it replaces `x` with `2` for technical reason.
Note that this does not make any change in the result of computation.

- Constant folding

If `x` is numeric token, it just computes `Asin[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__asin`.
Thus, for detailed computation rules, refer to the documentation [above](#__asinx).

- Sign propagation

Since arcsine function is odd function, sign can be propagated using identity $\mathrm{asin}(-x)=-\mathrm{asin}(x)$.
Note that this identity holds not only for $x\in[-1,\,1]$, but also for `nan`, `+-inf`, and $x\in\mathbb{R}\setminus[-1,\,1]$.
Thus this propagation is indeed safe.

### Acos
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Acos[x]` are as follows.
1. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
2. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
3. If `x` is not in $[-1,\,1]$, it generates `DOMAIN_OUT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `INF_DETECT` is generated by rule 2, `DOMAIN_OUT` warning will not be generated by rule 3.

> [!TIP]
> Trivially, the case of `x` being greater than the maximum size of representable `float` size or less than the minimum size of representable `float` size will be captured by rule 3.
In these cases, it replaces `x` with `2` for technical reason.
Note that this does not make any change in the result of computation.

- Constant folding

If `x` is numeric token, it just computes `Acos[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__acos`.
Thus, for detailed computation rules, refer to the documentation [above](#__acosx).

### Atan
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Atan[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

- Constant folding

If `x` is numeric token, it just computes `Atan[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__atan`.
Thus, for detailed computation rules, refer to the documentation [above](#__atanx).

- Sign propagation

Since arctangent function is odd function, sign can be propagated using identity $\mathrm{atan}(-x)=-\mathrm{atan}(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and `+-inf`.
Thus this propagation is indeed safe.

### Acsc
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Acsc[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is in $(-1,\,1)$, it generates `DOMAIN_OUT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

- Constant folding

If `x` is numeric token, it just computes `Acsc[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__acsc`.
Thus, for detailed computation rules, refer to the documentation [above](#__acscx).

- Sign propagation

Since arccosecant function is odd function, sign can be propagated using identity $\mathrm{acosec}(-x)=-\mathrm{acosec}(x)$.
Note that this identity holds not only for $x\in\mathbb{R}\setminus(-1,\,1)$, but also for `nan`,`+-inf`, and $x\in(-1,\,1)$.
Thus this propagation is indeed safe.

### Asec
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Asec[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
5. If `x` is in $(-1,\,1)$, it generates `DOMAIN_OUT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

- Constant folding

If `x` is numeric token, it just computes `Asec[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__asec`.
Thus, for detailed computation rules, refer to the documentation [above](#__asecx).

### Acot
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Acot[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

- Constant folding

If `x` is numeric token, it just computes `Acot[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__acot`.
Thus, for detailed computation rules, refer to the documentation [above](#__acotx).

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
Since all trigonometric functions and their inverses have unique calling signature `T.NUM fun(T.NUM)`, parameter `test_in` must have form of `[[arg], [arg], ...]`.

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
    from Function.Trigonometric import Tri
    
    # Uniform 100 test input points from [0, 100).
    test_in = [Decimal(n) for n in range(100)]
    # Computes value of math.sin(n) for n in test points.
    test_out = Tri.test(FunT.SIN, test_in)
```