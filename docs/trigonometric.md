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
- Value:
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
        FunT.ATAN: [Sign([T.NUM], T.NUM, FunT.ATAN)]
    }
```

Function calling signatures of trigonometric functions and their inverses for type checking.
Note that all of them have identical and unique calling signature `T.NUM Fun[T.NUM]`.

## chk_t
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

## simplify
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
Computation table is as follows.

| `x` | $\mathrm{Nan}$ | $-\infty$ | $\mathbb{R}$ | $\infty$ |
| --- | :---: | :---: | :---: | :---: |
| `Sin[x]` | $\mathrm{Nan}$ | $\mathrm{Nan}$ | $\sin(x)$ | $\mathrm{Nan}$ |

The value of $\sin(x)$ is computed using `math.sin` in basic Python math package `math`.
The exact implementation of `math.sin` is not known.
But in case of CPython, it is suspected to use `sin` function in `cmath` library.
Unfortunately, the implementation `sin` in `cmath` depends heavily on the machine and C compiler you are using.
In case of my setting (LLVM with AMD Radeon Pro 555X GPU), it is implemented as [compiler intrinsic](https://en.wikipedia.org/wiki/Intrinsic_function) `__nv_sin` which is basically a single instruction that computes sine function.
And nowadays, most of circuit-level implementation of trigonometric functions use some optimized version of [CORDIC](https://en.wikipedia.org/wiki/CORDIC) (__CO__ordinate __R__otation __DI__gital __C__omputer) algorithm.

Anyway, we present a thorough report on errors of `Sin[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 100 significant digits.
Test output is computed by `test` method described [below](#test) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

<!-- tabs:start -->
#### ** English **
![Sin_Small](Figures/Sin_Small.eps)
__Figure 1__. Error of `Sin[x]` on $[0,\,2\pi]$.
Input points are drawn randomly from $\mathbf{U}(0,\,2\pi)$.
One can see that relative error of `Sin[x]` for small input is bounded by (about) $2\times10^{-16}$.

#### ** French **
![Sin_Small](Figures/Sin_Small.eps)
__Figure 1__. Error of `Sin[x]` on $[0,\,2\pi]$.
Input points are drawn randomly from $\mathbf{U}(0,\,2\pi)$.
One can see that relative error of `Sin[x]` for small input is bounded by (about) $2\times10^{-16}$.

#### ** Italian **
x
<!-- tabs:end -->

- Sign propagation

Since sine function is odd function, sign can be propagated using identity $\sin(-x)=-\sin(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and $\pm\infty$.
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
Computation table is as follows.

| `x` | $\mathrm{Nan}$ | $-\infty$ | $\mathbb{R}$ | $\infty$ |
| --- | :---: | :---: | :---: | :---: |
| `Cos[x]` | $\mathrm{Nan}$ | $\mathrm{Nan}$ | $\cos(x)$ | $\mathrm{Nan}$ |

The value of $\cos(x)$ is computed using `math.cos` in basic Python math package `math`.
The exact implementation of `math.cos` is not known.
But in case of CPython, it is suspected to use `cos` function in `cmath` library.
Unfortunately, the implementation `cos` in `cmath` depends heavily on the machine and C compiler you are using.
In case of my setting (LLVM with AMD Radeon Pro 555X GPU), it is implemented as [compiler intrinsic](https://en.wikipedia.org/wiki/Intrinsic_function) `__nv_cos` which is basically a single instruction that computes cosine function.
And nowadays, most of circuit-level implementation of trigonometric functions use some optimized version of [CORDIC](https://en.wikipedia.org/wiki/CORDIC) (__CO__ordinate __R__otation __DI__gital __C__omputer) algorithm.

Anyway, we present a thorough report on errors of `Cos[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 100 significant digits.
Test output is computed by `test` method described [below](#test) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

| ![Cos_Small](Figures/Cos_Small.eps) |
| --- |
| __Figure 1__. Error of `Cos[x]` on $[0,\,2\pi]$. Input points are drawn randomly from $\mathbf{U}(0,\,2\pi)$. One can see that relative error of `Cos[x]` for small input is bounded by (about) $2\times10^{-16}$.|

- Dead code stripping

Since cosine function is even function, minus sign inside of cosine can be safely removed using identity $\cos(-x)=\cos(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and $\pm\infty$.
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
Computation table is as follows.

| `x` | $\mathrm{Nan}$ | $-\infty$ | $\mathbb{R}\setminus(\pi\mathbb{Z}+\pi/2)$ | $\pi\mathbb{Z}+\pi/2$ | $\infty$ |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Tan[x]` | $\mathrm{Nan}$ | $\mathrm{Nan}$ | $\tan(x)$ | $\mathrm{Nan}$ | $\mathrm{Nan}$ |

The value of $\tan(x)$ is computed using `math.tan` in basic Python math package `math`.
The exact implementation of `math.tan` is not known.
But in case of CPython, it is suspected to use `tan` function in `cmath` library.
Unfortunately, the implementation `tan` in `cmath` depends heavily on the machine and C compiler you are using.
In case of my setting (LLVM with AMD Radeon Pro 555X GPU), it is implemented as [compiler intrinsic](https://en.wikipedia.org/wiki/Intrinsic_function) `__nv_tan` which is basically a single instruction that computes tangent function.
And nowadays, most of circuit-level implementation of trigonometric functions use some optimized version of [CORDIC](https://en.wikipedia.org/wiki/CORDIC) (__CO__ordinate __R__otation __DI__gital __C__omputer) algorithm.

Anyway, we present a thorough report on errors of `Tan[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 100 significant digits.
Test output is computed by `test` method described [below](#test) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

| ![Tan_Small](Figures/Tan_Small.eps) |
| --- |
| __Figure 1__. Error of `Tan[x]` on $[-\pi/2,\,\pi/2]$. Input points are drawn randomly from $\mathbf{U}(-\pi/2,\,\pi/2)$. One can see that relative error of `Tan[x]` for small input is bounded by (about) $3\times10^{-16}$. Also, since the value of tangent function diverges at $\pm\pi/2$, absolute error grows rapidly as input point approaches to $\pm\pi/2$.|

- Sign propagation

Since tangent function is odd function, sign can be propagated using identity $\tan(-x)=-\tan(x)$.
Note that this identity holds not only for $x\in\mathbb{R}\setminus(\pi\mathbb{Z}+\pi/2)$, but also for `nan`, $\pm\infty$, and $x\in\pi\mathbb{Z}+\pi/2$.
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
Computation table is as follows.

| `x` | $\mathrm{Nan}$ | $-\infty$ | $\mathbb{R}\setminus\pi\mathbb{Z}$ | $\pi\mathbb{Z}$ | $\infty$ |
| --- | :---: | :---: | :---: | :---: | :---: |
| `Csc[x]` | $\mathrm{Nan}$ | $\mathrm{Nan}$ | $\cosec(x)$ | $\mathrm{Nan}$ | $\mathrm{Nan}$ |

The value of $\cosec(x)$ is computed as `1 / math.sin(x)` which reflects its definition directly.
Thus error will depend on implementation of `math.sin` which we described in detail [above](#sin).

Anyway, we present a thorough report on errors of `Csc[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 100 significant digits.
Test output is computed by `test` method described [below](#test) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

| ![Scs_Small](Figures/Csc_Small.eps) |
| --- |
| __Figure 1__. Error of `Csc[x]` on $[0,\,2\pi]$. Input points are drawn randomly from $\mathbf{U}(0,\,2\pi)$. One can see that relative error of `Csc[x]` for small input is bounded by (about) $3\times10^{-16}$. Also, since the value of cosecant function diverges at $0$, $\pi$, and $2\pi$, absolute error grows rapidly as input point approaches to those points.|


- Sign propagation

Since cosecant function is odd function, sign can be propagated using identity $\cosec(-x)=-\cosec(x)$.
Note that this identity holds not only for $x\in\mathbb{R}\setminus\pi\mathbb{Z}$, but also for `nan`, $\pm\infty$, and $x\in\pi\mathbb{Z}$.
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
Computation table is as follows.

| `x` | $\mathrm{Nan}$ | $[-\infty,\,1)$ | $[-1,\,1]$ | $(1,\,\infty]$ |
| --- | :---: | :---: | :---: | :---: |
| `Asin[x]` | $\mathrm{Nan}$ | $\mathrm{Nan}$ | $\mathrm{asin}(x)$ | $\mathrm{Nan}$ |

The value of $\mathrm{asin}(x)$ is computed using `math.asin` in basic Python math package `math`.
The exact implementation of `math.asin` is not known.
But in case of CPython, it is suspected to use `asin` function in `cmath` library.
Unfortunately, the implementation `asin` in `cmath` depends heavily on the machine and C compiler you are using.
In case of my setting (LLVM with AMD Radeon Pro 555X GPU), it is implemented as [compiler intrinsic](https://en.wikipedia.org/wiki/Intrinsic_function) `__nv_asin` which is basically a single instruction that computes arcsine function.
And nowadays, most of circuit-level implementation of trigonometric functions use some optimized version of [CORDIC](https://en.wikipedia.org/wiki/CORDIC) (__CO__ordinate __R__otation __DI__gital __C__omputer) algorithm.

Anyway, we present a thorough report on errors of `Asin[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 100 significant digits.
Test output is computed by `test` method described [below](#test) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

| ![Asin_Small](Figures/Asin_Small.eps) |
| --- |
| __Figure 1__. Error of `Asin[x]` on $[-1,\,1]$. Input points are drawn randomly from $\mathbf{U}(-1,\,1)$. One can see that relative error of `Asin[x]` for small input is bounded by (about) $1.5\times10^{-16}$. |

- Sign propagation

Since arcsine function is odd function, sign can be propagated using identity $\mathrm{asin}(-x)=-\mathrm{asin}(x)$.
Note that this identity holds not only for $x\in[-1,\,1]$, but also for `nan`, $\pm\infty$, and $x\in\mathbb{R}\setminus[-1,\,1]$.
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
Computation table is as follows.

| `x` | $\mathrm{Nan}$ | $[-\infty,\,1)$ | $[-1,\,1]$ | $(1,\,\infty]$ |
| --- | :---: | :---: | :---: | :---: |
| `Acos[x]` | $\mathrm{Nan}$ | $\mathrm{Nan}$ | $\mathrm{acos}(x)$ | $\mathrm{Nan}$ |

The value of $\mathrm{acos}(x)$ is computed using `math.acos` in basic Python math package `math`.
The exact implementation of `math.acos` is not known.
But in case of CPython, it is suspected to use `acos` function in `cmath` library.
Unfortunately, the implementation `acos` in `cmath` depends heavily on the machine and C compiler you are using.
In case of my setting (LLVM with AMD Radeon Pro 555X GPU), it is implemented as [compiler intrinsic](https://en.wikipedia.org/wiki/Intrinsic_function) `__nv_acos` which is basically a single instruction that computes arccosine function.
And nowadays, most of circuit-level implementation of trigonometric functions use some optimized version of [CORDIC](https://en.wikipedia.org/wiki/CORDIC) (__CO__ordinate __R__otation __DI__gital __C__omputer) algorithm.

Anyway, we present a thorough report on errors of `Acos[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 100 significant digits.
Test output is computed by `test` method described [below](#test) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

| ![Acos_Small](Figures/Acos_Small.eps) |
| --- |
| __Figure 1__. Error of `Acos[x]` on $[-1,\,1]$. Input points are drawn randomly from $\mathbf{U}(-1,\,1)$. One can see that relative error of `Acos[x]` for small input is bounded by (about) $1.5\times10^{-16}$. |

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
Computation table is as follows.

| `x` | $\mathrm{Nan}$ | $-\infty$ | $\mathbb{R}$ | $\infty$ |
| --- | :---: | :---: | :---: | :---: |
| `Atan[x]` | $\mathrm{Nan}$ | $-\pi/2$ | $\mathrm{atan}(x)$ | $\pi/2$ |

The value of $\mathrm{atan}(x)$ is computed using `math.atan` in basic Python math package `math`.
The exact implementation of `math.atab` is not known.
But in case of CPython, it is suspected to use `atan` function in `cmath` library.
Unfortunately, the implementation `atan` in `cmath` depends heavily on the machine and C compiler you are using.
In case of my setting (LLVM with AMD Radeon Pro 555X GPU), it is implemented as [compiler intrinsic](https://en.wikipedia.org/wiki/Intrinsic_function) `__nv_atan` which is basically a single instruction that computes arctangent function.
And nowadays, most of circuit-level implementation of trigonometric functions use some optimized version of [CORDIC](https://en.wikipedia.org/wiki/CORDIC) (__CO__ordinate __R__otation __DI__gital __C__omputer) algorithm.

Anyway, we present a thorough report on errors of `Atan[x]`.
Test input and reference output (correct answer) is generated by [arbitrary precision arithmetic functionality](https://www.mathworks.com/help/symbolic/vpa.html) of MATLAB with precision of 100 significant digits.
Test output is computed by `test` method described [below](#test) and the result is analyzed using MATLAB again.
One can read detailed description on these MATLAB codes at ...

| ![Atan_Small](Figures/Atan_Small.eps) |
| --- |
| __Figure 1__. Error of `Atan[x]` on $[-5,\,5]$. Input points are drawn randomly from $\mathbf{U}(-5,\,5)$. One can see that relative error of `Atan[x]` for small input is bounded by (about) $1.5\times10^{-16}$. |

- Sign propagation

Since arctangent function is odd function, sign can be propagated using identity $\mathrm{atan}(-x)=-\mathrm{atan}(x)$.
Note that this identity holds not only for $x\in\mathbb{R}$, but also for `nan` and $\pm\infty$.
Thus this propagation is indeed safe.

## test
<span class="badge badge-pill badge-success">public</span> <span class="badge badge-pill badge-secondary">class method</span> <span class="badge badge-pill badge-warning">debug&analysis</span> 

> [!DANGER]
> This method is for analysis only. We recommend you to keep far from this.

- Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `fun` | `FunT` | Function to be tested. |
| `test_in` | `List[Decimal]` | Test inputs. |

- Returns

| Type | Description |
| --- | --- |
| `List[Decimal]` | Test outputs. |

It simply computes test outputs of function indicated by `fun` at test input points `test_in`.
The value of `fun` must be one of trigonometric functions and their inverses listed [above](#__sign).
For accuracy, it takes `test_in` as `Decimal`, which is a class in `decimal` package that supports arbitrary precision arithmetic in Python.
By default, the precision (# of significant digits) is 100, but it can be customized.

For test output generation, it simply branches flow by looking up `fun` and computes outputs using the basic implementation of each `fun` described [above](#simplify).
Since there is no logic for error handling, `test_in` must be generated with care so that there is no chance of encountering erroneous situation like `math.asin(2)` which causes `ValueError`.
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