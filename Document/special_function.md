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
| `Gamma[x]` | $\Gamma(x) = \lim_{n\to\infty}\frac{n!}{x^{\overline{n+1}}}n^x$ | $\mathbb{R}\setminus\mathbb{Z}^-_0$ | $\mathbb{R}\setminus\{0\}$ |
| `Lgamma[x]` | $\log\vert\Gamma(x)\vert$ | $\mathbb{R}\setminus\mathbb{Z}^-_0$ | $\mathbb{R}$ |
| `Recigamma[x]` | $\frac{1}{\Gamma(x)}$ | $\mathbb{R}$ | $\mathbb{R}$ |
| `Besselclifford[x]` | $\frac{1}{\Gamma(x + 1)}$ | $\mathbb{R}$ | $\mathbb{R}$ |
| `Beta[x, y]` | $\mathrm{B}(x,\,y) = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}$ | $(\mathbb{R}\setminus\mathbb{Z}^-_0)^2$ | $\mathbb{R}$ |

> [!NOTE]
> 1. Here, $\mu$ stands for [Lebesgue measure](https://en.wikipedia.org/wiki/Lebesgue_measure) on measure space $(\mathbb{R},\,\mathcal{M},\,\mu)$ and $x^{\overline{n}}$ stands for [rising factorial](https://en.wikipedia.org/wiki/Falling_and_rising_factorials) which is defined by $x^{\overline{n}}=x\cdots(x+n-1)$
2. For convenience, we employ convention $1/\pm\infty=0$.
3. One can show that integral in the definition of error function and limit in the definition of gamma function converges for all $x$ in each domain so that they are indeed well-defined.
4. One can show that other definitions of gamma function, like [analytic continuation](https://en.wikipedia.org/wiki/Analytic_continuation) of$$\int_0^\infty t^{x-1}e^{-x}\,d\mu(t)$$to $\mathbb{C}\setminus\mathbb{Z}^-_0$ by Euler or $$\frac{1}{xe^{\gamma x}}\prod_{n=1}^\infty\frac{e^{x/n}}{1+x/n}$$by Weierstrass coincide with the definition above. (Here, $\gamma$ is [Euler–Mascheroni constant](https://en.wikipedia.org/wiki/Euler–Mascheroni_constant).)
5. One cas easily show that the definition of beta function above coincides with the definition using [analytic continuation](https://en.wikipedia.org/wiki/Analytic_continuation) of$$\int_0^1t^{x-1}(1-t)^{y-1}\,d\mu(t)$$to $(\mathbb{R}\setminus\mathbb{Z}^-_0)^2$.

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

__Figure 5__. Graph of $1/\Gamma(x)$ on $[-4,\,4]$.

#### ** Besselclifford **
![Besselclifford_Graph](Figures/Besselclifford_Graph.eps)

__Figure 6__. Graph of $1/\Gamma(x+1)$ on $[-4,\,4]$.

#### ** Beta **
![Beta_Graph](Figures/Beta_Graph.eps)

__Figure 7__. Graph of $\mathrm{B}(x,\,y)$ on $[-3,\,3]\times[-3,\,3]$.
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
        FunT.BETA: [Sign([T.NUM, T.NUM], T.NUM, FunT.BETA)]
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

| `y\x` | `nan` | `-inf` | $\mathbb{R}\setminus\mathbb{Z}^-_0$ | $\mathbb{Z}^-_0$ | `inf` |
| :---: | :---: | :---: | :---: | :---: | :---: |
| __`nan`__ | `nan` | `nan` | `nan` | `nan` | `nan` |
| __`-inf`__ |  `nan` | `nan` | `nan` | `nan` | `nan` |
| $\mathbb{R}\setminus\mathbb{Z}^-_0$ | `nan` | `nan` | $\mathrm{B}(x,\,y)$ | `nan` | Refer to the note |
| $\mathbb{Z}^-_0$ | `nan` | `nan` | `nan` | `nan` | `nan` |
| __`inf`__ | `nan` | `nan` | Refer to the note | `nan` | $0$ |

> [!NOTE]
> If `y`is in $\mathbb{R}\setminus\mathbb{Z}^-_0$, then `Beta[inf, y]` is `inf` if `y` is positive or in $(2n,\,2n+1)$ for some $n\in\mathbb{Z}^-$. Otherwise, it is `-inf`. This holds symmetrically for `Beta[x, inf]` with `x` in $\mathbb{R}\setminus\mathbb{Z}^-_0$.

The value of $\mathrm{B}(x,\,y)$ is computed as `exp(math.lgamma(x) + math.lgamma(y) - math.lgamma(x + y))` which reflects its definition directly.
The sign of `Beta[x, y]` will be recovered later using following identity.
$$
\mathrm{sgn}(\Gamma(x))=
\begin{dcases}
1&\textrm{when }x>0\textrm{ or }x\in(2n,\,2n+1)\textrm{ for some }n\in\mathbb{Z}^-\\
-1&\textrm{ow.}
\end{dcases}
$$
Thus error will depend nd on implementation of `math.lgamma` which we described in detail [above](#__lgammax).

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
Also, `rt`'s token value must be one of special functions listed [above](#__sign).
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
| `BIG_INT` | Given parameter is greater than the maximum size of representable `float` size, `sys.float_info.max`.
| `SMALL_INT` | Given parameter is smaller than the minimum size of representable `float` size, `-sys.float_info.max`.

It simplifies partial AST rooted at `rt` using simplification strategies described at ...
Since it assumes that all children of `rt` is already simplified, simplification of `rt`'s children should be preceded before calling this method.
Also, `rt`'s token value must be one of special functions listed [above](#__sign).
After simplification, it returns the root token of simplified partial AST and list of warnings generated during simplification process.

> [!NOTE]
> Multiple warnings can be generated during one simplification.

For simplification, it branches flow by looking up the token value of `rt` and executes corresponding simplification logic.
Although simplification logic is quite complicated, we shall present in-depth description of these logic here.

### Erf
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Erf[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is smaller than the minimum size of representable `float` size, it generates `SMALL_INT` warning and replaces `x` with `-math.inf`.
3. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
4. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 4.

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
For computation, it just calls its helper `__erfc`.
Thus, for detailed computation rules, refer to the documentation [above](#__erfcx).

### Gamma
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Gamma[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
3. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
4. If `x` is in $\mathbb{Z}^-_0$, it generates `POLE_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 3.

- Constant folding

If `x` is numeric token, it just computes `Gamma[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__gamma`.
Thus, for detailed computation rules, refer to the documentation [above](#__gammax).

### Lgamma
- Warning check

If `x` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Lgamma[x]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
3. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
4. If `x` is in $\mathbb{Z}^-_0$, it generates `POLE_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 3.

- Constant folding

If `x` is numeric token, it just computes `Lgamma[x]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__lgamma`.
Thus, for detailed computation rules, refer to the documentation [above](#__lgammax).

### Beta
- Warning check

If `x` or `y` is numeric token, it checks warning conditions and generates warning if needed.
The warning generation rules for `Beta[x, y]` are as follows.
1. If `x` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `x` with `math.inf`.
2. If `x` is `math.nan`, it generates `NAN_DETECT` warning.
3. If `x` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
4. If `y` is greater than the maximum size of representable `float` size, it generates `BIG_INT` warning and replaces `y` with `math.inf`.
5. If `y` is `math.nan`, it generates `NAN_DETECT` warning.
6. If `y` is `math.inf` or `-math.inf`, it generates `INF_DETECT` warning.
7. If `x` is in $\mathbb{Z}^-_0$ and `y` is finite, it generates `POLE_DETECT` warning.
8. If `x` is finite and `y` is in $\mathbb{Z}^-_0$, it generates `POLE_DETECT` warning.

> [!NOTE]
> These rules are sequential. That is, the first rule is checked and then the second one will be checked.
Also, these rules are exclusive. That is, if one rule is applied, then rules after that will not be applied.
Thus even if `x` is replaced with `math.inf` by rule 1, generating `BIG_INT` warning, `INF_DETECT` warning will not be generated by rule 3.

> [!TIP]
> Trivially, the case of `x` or `y` being less than the minimum size of representable `float` size will be captured by rule 7 and 8, resp.
In these cases, it replaces `x` or `y` with `-1` for technical reason.
Note that this does not make any change in the result of computation.

- Constant folding

If `x` and `y` are numeric tokens, it just computes `Beta[x, y]` so that it can be simplified into one simple numeric token.
For computation, it just calls its helper `__beta`.
Thus, for detailed computation rules, refer to the documentation [above](#__betax-y).

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
The value of `fun` must be one of special functions listed [above](#__sign).
For accuracy, it takes `test_in` as `Decimal`, which is a class in `decimal` package that supports arbitrary precision arithmetic in Python.
By default, the precision (# of significant digits) is 300, but it can be customized.

For test output generation, it simply branches flow by looking up `fun` and computes outputs using the basic implementation of each `fun` described above.
Since there is no logic for error handling, `test_in` must be generated with care so that there is no chance of encountering erroneous situation like `math.asin(1, 2)` which causes `TypeError`.
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