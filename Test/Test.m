%% PLOT
% Sin
fig = plt_grph(@sin, -2 * pi, 2 * pi, 'Sine function on [-2\pi, 2\pi]', 'sin(x)');
saveas(fig, './Plt/Sin_Graph', 'epsc')
close('all')

% Cos
fig = plt_grph(@cos, -2 * pi, 2 * pi, 'Cosine function on [-2\pi, 2\pi]', 'cos(x)');
saveas(fig, './Plt/Cos_Graph', 'epsc')
close('all')

% Tan
fig = plt_grph(@tan, -pi, pi, 'Tangent function on [-\pi, \pi]', 'tan(x)', [-3 3], [-pi / 2 pi / 2]);
saveas(fig, './Plt/Tan_Graph', 'epsc')
close('all')

% Csc
fig = plt_grph(@csc, -2 * pi, 2 * pi, 'Cosecant function on [-2\pi, 2\pi]', 'cosec(x)', [-3 3], [-pi 0 pi]);
saveas(fig, './Plt/Csc_Graph', 'epsc')
close('all')

% Sec
fig = plt_grph(@sec, -2 * pi, 2 * pi, 'Secant function on [-2\pi, 2\pi]', 'sec(x)' ,[-3 3], [-3 * pi / 2 -pi / 2 pi / 2 3 * pi / 2]);
saveas(fig, './Plt/Sec_Graph', 'epsc')
close('all')

% Cot
fig = plt_grph(@cot, -pi, pi, 'Cotagent function on [-\pi, \pi]', 'cot(x)', [-3 3], 0);
saveas(fig, './Plt/Cot_Graph', 'epsc')
close('all')

% Asin
fig = plt_grph(@asin, -1, 1, 'Arcsine function on [-1, 1]', 'asin(x)', [-inf inf], [], [], [-1 -pi / 2;1 pi / 2]);
saveas(fig, './Plt/Asin_Graph', 'epsc')
close('all')

% Acos
fig = plt_grph(@acos, -1, 1, 'Arccosine function on [-1, 1]', 'acos(x)', [-inf inf], [], [], [-1 pi; 1 0]);
saveas(fig, './Plt/Acos_Graph', 'epsc')
close('all')

% Atan
fig = plt_grph(@atan, -5, 5, 'Arctangent function on [-5, 5]', 'atan(x)', [-inf inf], [], [-pi / 2 pi / 2]);
saveas(fig, './Plt/Atan_Graph', 'epsc')
close('all')

% Acsc
fig = plt_grph(@acsc, -5, 5, 'Arccosecant function on [-5, 5]', 'acosec(x)', [-inf inf], [-0.99 0.99], [], [-1 -pi / 2; 1 pi / 2]);
fig.Children.XTick = -5:1:5;
fig.Children.Children(3).Visible = false;
fig.Children.Children(4).Visible = false;
fig.Children.Children(7).Visible = false;
fig.Children.Children(8).Visible = false;
saveas(fig, './Plt/Acsc_Graph', 'epsc')
close('all')

% Asec
fig = plt_grph(@asec, -5, 5, 'Arcsecant function on [-5, 5]', 'asec(x)', [-inf inf], [-0.99 0.99], pi / 2, [-1 pi; 1 0]);
fig.Children.XTick = -5:1:5;
fig.Children.Children(4).Visible = false;
fig.Children.Children(5).Visible = false;
fig.Children.Children(8).Visible = false;
fig.Children.Children(9).Visible = false;
saveas(fig, './Plt/Asec_Graph', 'epsc')
close('all')

% Acot
fig = plt_grph(@acot, -5, 5, 'Arccotagent function on [-5, 5]', 'acot(x)', [-inf inf], 0, [], [0 pi / 2], [0 -pi / 2]);
fig.Children.XTick = -5:1:5;
fig.Children.Children(3).Visible = false;
saveas(fig, './Plt/Acot_Graph', 'epsc')
close('all')

% Sinh
fig = plt_grph(@sinh, -5, 5, 'Sine hyperbolic function on [-5, 5]', 'sinh(x)', [-30 30]);
fig.Children.XTick = -5:1:5;
saveas(fig, './Plt/Sinh_Graph', 'epsc')
close('all')

% Cosh
fig = plt_grph(@cosh, -5, 5, 'Cosine hyperbolic function on [-5, 5]', 'cosh(x)', [0 30]);
fig.Children.XTick = -5:1:5;
saveas(fig, './Plt/Cosh_Graph', 'epsc')
close('all')

% Tanh
fig = plt_grph(@tanh, -3, 3, 'Tangent hyperbolic function on [-3, 3]', 'tanh(x)', [-inf inf], [], [-1 1]);
fig.Children.YLim = [-1.5 1.5];
saveas(fig, './Plt/Tanh_Graph', 'epsc')
close('all')

% Csch
fig = plt_grph(@csch, -5, 5, 'Cosecant hyperbolic function on [-5, 5]', 'csch(x)', [-5 5], 0);
fig.Children.XTick = -5:1:5;
saveas(fig, './Plt/Csch_Graph', 'epsc')
close('all')

% Sech
fig = plt_grph(@sech, -5, 5, 'Secant hyperbolic function on [-5, 5]', 'sech(x)');
fig.Children.XTick = -5:1:5;
saveas(fig, './Plt/Sech_Graph', 'epsc')
close('all')

% Coth
fig = plt_grph(@coth, -3, 3, 'Cotangent hyperbolic function on [-3, 3]', 'coth(x)', [-5 5], 0, [-1 1]);
saveas(fig, './Plt/Coth_Graph', 'epsc')
close('all')

% Asinh
fig = plt_grph(@asinh, -5, 5, 'Arcsine hyperbolic function on [-5, 5]', 'asinh(x)');
fig.Children.XTick = -5:1:5;
saveas(fig, './Plt/Asinh_Graph', 'epsc')
close('all')

% Acosh
fig = plt_grph(@acosh, 1, 5, 'Arccosine hyperbolic function on [1, 5]', 'acosh(x)', [-inf inf], [], [], [1 0]);
saveas(fig, './Plt/Acosh_Graph', 'epsc')
close('all')

% Atanh
fig = plt_grph(@atanh, -1, 1, 'Arctangent hyperbolic function on [-1, 1]', 'atanh(x)', [-3 3], [-1 1], [], [], [], 0.001);
saveas(fig, './Plt/Atanh_Graph', 'epsc')
close('all')

% Acsch
fig = plt_grph(@acsch, -5, 5, 'Arccosecant hyperbolic function on [-5, 5]', 'acsch(x)', [-3 3], 0);
fig.Children.XTick = -5:1:5;
saveas(fig, './Plt/Acsch_Graph', 'epsc')
close('all')

% Asech
fig = plt_grph(@asech, 0, 1, 'Arcsecant hyperbolic function on [0, 1]', 'asech(x)', [0 5], 0, [], [1 0], [], 0.001);
saveas(fig, './Plt/Asech_Graph', 'epsc')
close('all')

% Acoth
fig = plt_grph(@acoth, -5, 5, 'Arccotangent hyperbolic function on [-5, 5]', 'acoth(x)', [-2 2], [-1 1], [], [], [], 0.001);
fig.Children.Children(5).Visible = false;
fig.Children.Children(6).Visible = false;
fig.Children.XTick = -5:1:5;
saveas(fig, './Plt/Acoth_Graph', 'epsc')
close('all')

% Erf
fig = plt_grph(@erf, -3, 3, 'Error function on [-3, 3]', 'erf(x)', [-inf inf], [], [-1 1]);
fig.Children.YLim = [-1.5 1.5];
saveas(fig, './Plt/Erf_Graph', 'epsc')
close('all')

% Erfc
fig = plt_grph(@erfc, -3, 3, 'Complementary error function on [-3, 3]', 'erfc(x)', [-inf inf], [], 2);
fig.Children.YLim = [0 2.5];
saveas(fig, './Plt/Erfc_Graph', 'epsc')
close('all')

% Gamma
fig = plt_grph(@gamma, -4, 4, 'Gamma function on [-4, 4]', 'gamma(x)', [-5 7], [-4 -3 -2 -1 0], [], [], [], 0.001);
saveas(fig, './Plt/Gamma_Graph', 'epsc')
close('all')

% Log gamma
fig = plt_grph(@(x) log(abs(gamma(x))), -4, 4, 'Log gamma function on [-4, 4]', 'log|gamma(x)|', [-3 3], [-4 -3 -2 -1 0], [], [], [], 0.001);
saveas(fig, './Plt/Lgamma_Graph', 'epsc')
close('all')

% Reciprocal gamma
fig = plt_grph(@(x) 1 ./ gamma(x), -4, 4, 'Reciprocal gamma function on [-4, 4]', '1 / gamma(x)');
saveas(fig, './Plt/Recigamma_Graph', 'epsc')
close('all')

% Bessel-Clifford function
fig = plt_grph(@(x) 1 ./ gamma(x + 1), -4, 4, 'Bessel-Clifford function on [-4, 4]', '1 / gamma(x + 1)');
saveas(fig, './Plt/Besselclifford_Graph', 'epsc')
close('all')

% Beta
fig = plt_grph3(@(x, y) gamma(x) .* gamma(y) ./ gamma(x + y), [-3 -3], [3 3], 'Beta function on [-3, 3]\times[-3, 3]', 'B(x, y)', 10, [-1.5 -0.5 0.5 1.5; -1.5 -0.5 1 2], [-6 6], [-3 -2 -1 0], [-3 -2 -1 0]);
saveas(fig, './Plt/Beta_Graph', 'epsc')
close('all')

% Central beta
fig = plt_grph(@(x) gamma(x).^2 ./ gamma(2 * x), -3, 3, 'Central beta function on [-3, 3]', 'beta(x)', [-30 30], [-3 -2 -1 0]);
saveas(fig, './Plt/Centralbeta_Graph', 'epsc')
close('all')

% Sinc
fig = plt_grph(@(x) sinc(x / pi), -5 * pi, 5 * pi, 'Sinc function on [-5\pi, 5\pi]', 'sinc(x)');
saveas(fig, './Plt/Sinc_Graph', 'epsc')
close('all')

% Tanc
fig = plt_grph(@(x) tan(x) ./ x, -5 * pi / 2, 5 * pi / 2, 'Tanc function on [-5\pi/2, 5\pi/2]', 'tanc(x)', [-3 3], [-3 * pi / 2 -pi / 2 0 pi / 2 3 * pi / 2]);
fig.Children.Children(3).Visible = false;
saveas(fig, './Plt/Tanc_Graph', 'epsc')
close('all')

% Sinhc
fig = plt_grph(@(x) sinh(x) ./ x, -5, 5, 'Sinhc function on [-5, 5]', 'sinhc(x)', [-inf, 10], 0);
fig.Children.XTick = -5:1:5;
fig.Children.Children(1).Visible = false;
saveas(fig, './Plt/Sinhc_Graph', 'epsc')
close('all')

% Coshc
fig = plt_grph(@(x) cosh(x) ./ x, -5, 5, 'Coshc function on [-5, 5]', 'coshc(x)', [-10, 10], 0);
fig.Children.XTick = -5:1:5;
saveas(fig, './Plt/Coshc_Graph', 'epsc')
close('all')

% Tanhc
fig = plt_grph(@(x) tanh(x) ./ x, -10, 10, 'Tanhc function on [-10, 10]', 'tanhc(x)', [-inf inf], 0);
fig.Children.Children(1).Visible = false;
saveas(fig, './Plt/Tanhc_Graph', 'epsc')
close('all')

% Dirichlet kernel
fig = plt_slice_grph(@(x, n) sin((n + 1 / 2) .* x) ./ sin(x / 2), -5, 5, 'Dirichlet kernel on [-5, 5]', 'D_n(x)', [1 2 3 4], [-inf inf], 0);
fig.Children(2).XTick = -5:1:5;
fig.Children(2).Children(1).Visible = false;
saveas(fig, './Plt/Dirichletkernel_Graph', 'epsc')
close('all')

% Fejer kernel
fig = plt_slice_grph(@(x, n) (1 - cos(n .* x)) ./ (1 - cos(x)) ./ n, -5, 5, 'Fejer kernel on [-5, 5]', 'F_n(x)', [2 3 4 5], [-inf inf], 0);
fig.Children(2).XTick = -5:1:5;
fig.Children(2).Children(1).Visible = false;
saveas(fig, './Plt/Fejerkernel_Graph', 'epsc')
close('all')

% Topologist's sine
fig = plt_grph(@(x) sin(1 ./ x), 0.0001, 3, "Topologist's sine function on [0, 3]", 'sin(1 / x)', [-inf inf], [], [], [], [], 0.0001);
saveas(fig, './Plt/Topologistsin_Graph', 'epsc')
close('all')

%% math.exp
% [-5, 5] rand
in = fopen('./In/Test_Sinh_Small.in', 'w');
ref = fopen('./Ref/Test_Sinh_Small.ref', 'w');
test_gen(@sinh, sym(-5), sym(5), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
fig = plt_err(in, ref, out, 1000, 'Error of math.exp on [-5, 5]')
saveas(fig, './Plt/Exp_-5_5', 'epsc')
close('all')

%% math.sqrt
% [0, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@sqrt, sym(0), sym(5), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
fig = plt_err(in, ref, out, 1000, 'Error of math.sqrt on [0, 5]')
saveas(fig, './Plt/Sqrt_0_5', 'epsc')
close('all')

%% math.log
% [0, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@log, sym(0), sym(5), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
fig = plt_err(in, ref, out, 1000, 'Error of math.log on [0, 5]')
saveas(fig, './Plt/Log_0_5', 'epsc')
close('all')

%% TEST DB GENERATION
f = {
    @sin;
    @sin;
    @sin;
    @cos;
    @cos;
    @cos;
    @tan;
    @tan;
    @tan;
    @csc;
    @csc;
    @csc;
    @sec;
    @sec;
    @sec;
    @cot;
    @cot;
    @cot;
    @asin;
    @acos;
    @atan;
    @atan;
    @atan;
    @acsc;
    @acsc;
    @acsc;
    @asec;
    @asec;
    @asec;
    @acot;
    @acot;
    @acot;
    @erf;
    @erf;
    @erf;
    @erfc;
    @erfc;
    @erfc;
    @gamma;
    @gamma;
    @gamma;
    @(x) log(abs(gamma(x)));
    @(x) log(abs(gamma(x)));
    @(x) log(abs(gamma(x)));
    @(x, y) gamma(x) .* gamma(y) ./ gamma(x + y);
    @(x, y) gamma(x) .* gamma(y) ./ gamma(x + y);
    @(x, y) gamma(x) .* gamma(y) ./ gamma(x + y);
    @sinh;
    @sinh;
    @sinh;
    @cosh;
    @cosh;
    @cosh;
    @tanh;
    @tanh;
    @tanh;
    @csch;
    @csch;
    @csch;
    @sech;
    @sech;
    @sech;
    @coth;
    @coth;
    @coth;
    @asinh;
    @asinh;
    @asinh;
    @acosh;
    @acosh;
    @acosh;
    @atanh;
    @acsch;
    @acsch;
    @acsch;
    @asech;
    @acoth;
    @acoth;
    @acoth;
};
from = {
    sym(0);
    sym(-100) * sym(pi);
    sym(-1e10) * sym(pi);
    sym(0);
    sym(-100) * sym(pi);
    sym(-1e10) * sym(pi);
    sym(-0.5) * sym(pi);
    sym(-50) * sym(pi);
    sym(-0.5e10) * sym(pi);
    sym(0);
    sym(-100) * sym(pi);
    sym(-1e10) * sym(pi);
    sym(0);
    sym(-100) * sym(pi);
    sym(-1e10) * sym(pi);
    sym(-0.5) * sym(pi);
    sym(-50) * sym(pi);
    sym(-0.5e10) * sym(pi);
    sym(-1);
    sym(-1);
    sym(-5);
    sym(-500);
    sym(-5e10);
    sym(-4);
    sym(-499);
    sym(-5e10) + sym(1);
    sym(-4);
    sym(-499);
    sym(-5e10) + sym(1);
    sym(-5);
    sym(-500);
    sym(-5e10);
    sym(-1);
    sym(-5);
    sym(-25);
    sym(-1);
    sym(-5);
    sym(-25);
    sym(-5);
    sym(-25);
    sym(-125);
    sym(-5);
    sym(-50);
    sym(-5e5);
    sym([-3 -3]);
    sym([-30 -30]);
    sym([-300 -300]);
    sym(-5);
    sym(-50);
    sym(-500);
    sym(-5);
    sym(-50);
    sym(-500);
    sym(-3);
    sym(-30);
    sym(-300);
    sym(-5);
    sym(-50);
    sym(-500);
    sym(-5);
    sym(-50);
    sym(-500);
    sym(-3);
    sym(-30);
    sym(-300);
    sym(-5);
    sym(-500);
    sym(-5e10);
    sym(1);
    sym(1);
    sym(1);
    sym(-1);
    sym(-5);
    sym(-500);
    sym(-5e10);
    sym(0);
    sym(-4);
    sym(-499);
    sym(-5e10) + sym(1);
};
to = {
    sym(2) * sym(pi);
    sym(100) * sym(pi);
    sym(1e10) * sym(pi);
    sym(2) * sym(pi);
    sym(100) * sym(pi);
    sym(1e10) * sym(pi);
    sym(0.5) * sym(pi);
    sym(50) * sym(pi);
    sym(0.5e10) * sym(pi);
    sym(2) * sym(pi);
    sym(100) * sym(pi);
    sym(1e10) * sym(pi);
    sym(2) * sym(pi);
    sym(100) * sym(pi);
    sym(1e10) * sym(pi);
    sym(0.5) * sym(pi);
    sym(50) * sym(pi);
    sym(0.5e10) * sym(pi);
    sym(1);
    sym(1);
    sym(5);
    sym(500);
    sym(5e10);
    sym(4);
    sym(499);
    sym(5e10) - sym(1);
    sym(4);
    sym(499);
    sym(5e10) - sym(1);
    sym(5);
    sym(500);
    sym(5e10);
    sym(1);
    sym(5);
    sym(25);
    sym(1);
    sym(5);
    sym(25);
    sym(5);
    sym(25);
    sym(125);
    sym(5);
    sym(50);
    sym(5e5);
    sym([3 3]);
    sym([30 30]);
    sym([300 300]);
    sym(5);
    sym(50);
    sym(500);
    sym(5);
    sym(50);
    sym(500);
    sym(3);
    sym(30);
    sym(300);
    sym(5);
    sym(50);
    sym(500);
    sym(5);
    sym(50);
    sym(500);
    sym(3);
    sym(30);
    sym(300);
    sym(5);
    sym(500);
    sym(5e10);
    sym(5);
    sym(500);
    sym(5e10);
    sym(1);
    sym(5);
    sym(500);
    sym(5e10);
    sym(1);
    sym(4);
    sym(499);
    sym(5e10) - sym(1);
};
fname = {
    'Test_Sin_Small';
    'Test_Sin_Medium';
    'Test_Sin_Large';
    'Test_Cos_Small';
    'Test_Cos_Medium';
    'Test_Cos_Large';
    'Test_Tan_Small';
    'Test_Tan_Medium';
    'Test_Tan_Large';
    'Test_Csc_Small';
    'Test_Csc_Medium';
    'Test_Csc_Large';
    'Test_Sec_Small';
    'Test_Sec_Medium';
    'Test_Sec_Large';
    'Test_Cot_Small';
    'Test_Cot_Medium';
    'Test_Cot_Large';
    'Test_Asin_Small';
    'Test_Acos_Small';
    'Test_Atan_Small';
    'Test_Atan_Medium';
    'Test_Atan_Large';
    'Test_Acsc_Small';
    'Test_Acsc_Medium';
    'Test_Acsc_Large';
    'Test_Asec_Small';
    'Test_Asec_Medium';
    'Test_Asec_Large';
    'Test_Acot_Small';
    'Test_Acot_Medium';
    'Test_Acot_Large';
    'Test_Erf_Small';
    'Test_Erf_Medium';
    'Test_Erf_Large';
    'Test_Erfc_Small';
    'Test_Erfc_Medium';
    'Test_Erfc_Large';
    'Test_Gamma_Small';
    'Test_Gamma_Medium';
    'Test_Gamma_Large';
    'Test_Lgamma_Small';
    'Test_Lgamma_Medium';
    'Test_Lgamma_Large';
    'Test_Beta_Small';
    'Test_Beta_Medium';
    'Test_Beta_Large';
    'Test_Sinh_Small';
    'Test_Sinh_Medium';
    'Test_Sinh_Large';
    'Test_Cosh_Small';
    'Test_Cosh_Medium';
    'Test_Cosh_Large';
    'Test_Tanh_Small';
    'Test_Tanh_Medium';
    'Test_Tanh_Large';
    'Test_Csch_Small';
    'Test_Csch_Medium';
    'Test_Csch_Large';
    'Test_Sech_Small';
    'Test_Sech_Medium';
    'Test_Sech_Large';
    'Test_Coth_Small';
    'Test_Coth_Medium';
    'Test_Coth_Large';
    'Test_Asinh_Small';
    'Test_Asinh_Medium';
    'Test_Asinh_Large';
    'Test_Acosh_Small';
    'Test_Acosh_Medium';
    'Test_Acosh_Large';
    'Test_Atanh_Small';
    'Test_Acsch_Small';
    'Test_Acsch_Medium';
    'Test_Acsch_Large';
    'Test_Asech_Small';
    'Test_Acoth_Small';
    'Test_Acoth_Medium';
    'Test_Acoth_Large';
};
map = {
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x + sign(x)};
    {@(x) x + sign(x)};
    {@(x) x + sign(x)};
    {@(x) x + sign(x)};
    {@(x) x + sign(x)};
    {@(x) x + sign(x)};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x; @(x) x};
    {@(x) x; @(x) x};
    {@(x) x; @(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x + sign(x)};
    {@(x) x + sign(x)};
    {@(x) x + sign(x)};
};
argc = [
    ones(44, 1);
    2 * ones(3, 1);
    ones(32, 1);
];
multi_test_gen(f, from, to, fname, argc, map)

%% PLOT ERROR
fname = {
    'Test_Sin_Small';
    'Test_Sin_Medium';
    'Test_Sin_Large';
    'Test_Cos_Small';
    'Test_Cos_Medium';
    'Test_Cos_Large';
    'Test_Tan_Small';
    'Test_Tan_Medium';
    'Test_Tan_Large';
    'Test_Csc_Small';
    'Test_Csc_Medium';
    'Test_Csc_Large';
    'Test_Sec_Small';
    'Test_Sec_Medium';
    'Test_Sec_Large';
    'Test_Cot_Small';
    'Test_Cot_Medium';
    'Test_Cot_Large';
    'Test_Asin_Small';
    'Test_Acos_Small';
    'Test_Atan_Small';
    'Test_Atan_Medium';
    'Test_Atan_Large';
    'Test_Acsc_Small';
    'Test_Acsc_Medium';
    'Test_Acsc_Large';
    'Test_Asec_Small';
    'Test_Asec_Medium';
    'Test_Asec_Large';
    'Test_Acot_Small';
    'Test_Acot_Medium';
    'Test_Acot_Large';
    'Test_Erf_Small';
    'Test_Erf_Medium';
    'Test_Erf_Large';
    'Test_Erfc_Small';
    'Test_Erfc_Medium';
    'Test_Erfc_Large';
    'Test_Gamma_Small';
    'Test_Gamma_Medium';
    'Test_Gamma_Large';
    'Test_Lgamma_Small';
    'Test_Lgamma_Medium';
    'Test_Lgamma_Large';
    'Test_Beta_Small';
    'Test_Beta_Medium';
    'Test_Beta_Large';
    'Test_Sinh_Small';
    'Test_Sinh_Medium';
    'Test_Sinh_Large';
    'Test_Cosh_Small';
    'Test_Cosh_Medium';
    'Test_Cosh_Large';
    'Test_Tanh_Small';
    'Test_Tanh_Medium';
    'Test_Tanh_Large';
    'Test_Csch_Small';
    'Test_Csch_Medium';
    'Test_Csch_Large';
    'Test_Sech_Small';
    'Test_Sech_Medium';
    'Test_Sech_Large';
    'Test_Coth_Small';
    'Test_Coth_Medium';
    'Test_Coth_Large';
    'Test_Asinh_Small';
    'Test_Asinh_Medium';
    'Test_Asinh_Large';
    'Test_Acosh_Small';
    'Test_Acosh_Medium';
    'Test_Acosh_Large';
    'Test_Atanh_Small';
    'Test_Acsch_Small';
    'Test_Acsch_Medium';
    'Test_Acsch_Large';
    'Test_Asech_Small';
    'Test_Acoth_Small';
    'Test_Acoth_Medium';
    'Test_Acoth_Large';
};
size = 1000 * ones(length(fname), 1);
main = {
    'Error of Sin[x] on [0, 2\pi]';
    'Error of Sin[x] on [-100\pi, 100\pi]';
    'Error of Sin[x] on [-10^{10}\pi, 10^{10}\pi]';
    'Error of Cos[x] on [0, 2\pi]';
    'Error of Cos[x] on [-100\pi, 100\pi]';
    'Error of Cos[x] on [-10^{10}\pi, 10^{10}\pi]';
    'Error of Tan[x] on [-\pi/2, \pi/2]';
    'Error of Tan[x] on [-50\pi, 50\pi]';
    'Error of Tan[x] on [-10^{10}\pi/2, 10^{10}\pi/2]';
    'Error of Csc[x] on [0, 2\pi]';
    'Error of Csc[x] on [-100\pi, 100\pi]';
    'Error of Csc[x] on [-10^{10}\pi, 10^{10}\pi]';
    'Error of Sec[x] on [0, 2\pi]';
    'Error of Sec[x] on [-100\pi, 100\pi]';
    'Error of Sec[x] on [-10^{10}\pi, 10^{10}\pi]';
    'Error of Cot[x] on [-\pi/2, \pi/2]';
    'Error of Cot[x] on [-50\pi, 50\pi]';
    'Error of Cot[x] on [-10^{10}\pi/2, 10^{10}\pi/2]';
    'Error of Asin[x] on [-1, 1]';
    'Error of Acos[x] on [-1, 1]';
    'Error of Atan[x] on [-5, 5]';
    'Error of Atan[x] on [-50, 50]';
    'Error of Atan[x] on [-5\times10^{10}, 5\times10^{10}]';
    'Error of Acsc[x] on [-5, 5]';
    'Error of Acsc[x] on [-50, 50]';
    'Error of Acsc[x] on [-5\times10^{10}, 5\times10^{10}]';
    'Error of Asec[x] on [-5, 5]';
    'Error of Asec[x] on [-50, 50]';
    'Error of Asec[x] on [-5\times10^{10}, 5\times10^{10}]';
    'Error of Acot[x] on [-5, 5]';
    'Error of Acot[x] on [-50, 50]';
    'Error of Acot[x] on [-5\times10^{10}, 5\times10^{10}]';
    'Error of Erf[x] on [-1, 1]';
    'Error of Erf[x] on [-5, 5]';
    'Error of Erf[x] on [-25, 25]';
    'Error of Erfc[x] on [-1, 1]';
    'Error of Erfc[x] on [-5, 5]';
    'Error of Erfc[x] on [-25, 25]';
    'Error of Gamma[x] on [-5, 5]';
    'Error of Gamma[x] on [-25, 25]';
    'Error of Gamma[x] on [-125, 125]';
    'Error of Lgamma[x] on [-5, 5]';
    'Error of Lgamma[x] on [-50, 50]';
    'Error of Lgamma[x] on [-5\times10^5, 5\times10^5]';
    'Error of Beta[x, y] on [-3, 3]^2';
    'Error of Beta[x, y] on [-30, 30]^2';
    'Error of Beta[x, y] on [-300, 300]^2';
    'Error of Sinh[x] on [-5, 5]';
    'Error of Sinh[x] on [-50, 50]';
    'Error of Sinh[x] on [-500, 500]';
    'Error of Cosh[x] on [-5, 5]';
    'Error of Cosh[x] on [-50, 50]';
    'Error of Cosh[x] on [-500, 500]';
    'Error of Tanh[x] on [-3, 3]';
    'Error of Tanh[x] on [-30, 30]';
    'Error of Tanh[x] on [-300, 300]';
    'Error of Csch[x] on [-5, 5]';
    'Error of Csch[x] on [-50, 50]';
    'Error of Csch[x] on [-500, 500]';
    'Error of Sech[x] on [-5, 5]';
    'Error of Sech[x] on [-50, 50]';
    'Error of Sech[x] on [-500, 500]';
    'Error of Coth[x] on [-3, 3]';
    'Error of Coth[x] on [-30, 30]';
    'Error of Coth[x] on [-300, 300]';
    'Error of Asinh[x] on [-5, 5]';
    'Error of Asinh[x] on [-500, 500]';
    'Error of Asinh[x] on [-5\times10^{10}, 5\times10^{10}]';
    'Error of Acosh[x] on [1, 5]';
    'Error of Acosh[x] on [1, 500]';
    'Error of Acosh[x] on [1, 5\times10^{10}]';
    'Error of Atanh[x] on [-1, 1]';
    'Error of Acsch[x] on [-5, 5]';
    'Error of Acsch[x] on [-500, 500]';
    'Error of Acsch[x] on [-5\times10^{10}, 5\times10^{10}]';
    'Error of Asech[x] on [0, 1]';
    'Error of Acoth[x] on [-5, 5]';
    'Error of Acoth[x] on [-500, 500]';
    'Error of Acoth[x] on [-5\times10^{10}, 5\times10^{10}]';
};
argc = [
    ones(44, 1);
    2 * ones(3, 1);
    ones(32, 1);
];
from = {
    sym(0);
    sym(-100) * sym(pi);
    sym(-1e10) * sym(pi);
    sym(0);
    sym(-100) * sym(pi);
    sym(-1e10) * sym(pi);
    sym(-0.5) * sym(pi);
    sym(-50) * sym(pi);
    sym(-0.5e10) * sym(pi);
    sym(0);
    sym(-100) * sym(pi);
    sym(-1e10) * sym(pi);
    sym(0);
    sym(-100) * sym(pi);
    sym(-1e10) * sym(pi);
    sym(-0.5) * sym(pi);
    sym(-50) * sym(pi);
    sym(-0.5e10) * sym(pi);
    sym(-1);
    sym(-1);
    sym(-5);
    sym(-500);
    sym(-5e10);
    sym(-5);
    sym(-500);
    sym(-5e10);
    sym(-5);
    sym(-500);
    sym(-5e10);
    sym(-5);
    sym(-500);
    sym(-5e10);
    sym(-1);
    sym(-5);
    sym(-25);
    sym(-1);
    sym(-5);
    sym(-25);
    sym(-5);
    sym(-25);
    sym(-125);
    sym(-5);
    sym(-50);
    sym(-5e5);
    sym([-3 -3]);
    sym([-30 -30]);
    sym([-300 -300]);
    sym(-5);
    sym(-50);
    sym(-500);
    sym(-5);
    sym(-50);
    sym(-500);
    sym(-3);
    sym(-30);
    sym(-300);
    sym(-5);
    sym(-50);
    sym(-500);
    sym(-5);
    sym(-50);
    sym(-500);
    sym(-3);
    sym(-30);
    sym(-300);
    sym(-5);
    sym(-500);
    sym(-5e10);
    sym(1);
    sym(1);
    sym(1);
    sym(-1);
    sym(-5);
    sym(-500);
    sym(-5e10);
    sym(0);
    sym(-5);
    sym(-500);
    sym(-5e10);
};
to = {
    sym(2) * sym(pi);
    sym(100) * sym(pi);
    sym(1e10) * sym(pi);
    sym(2) * sym(pi);
    sym(100) * sym(pi);
    sym(1e10) * sym(pi);
    sym(0.5) * sym(pi);
    sym(50) * sym(pi);
    sym(0.5e10) * sym(pi);
    sym(2) * sym(pi);
    sym(100) * sym(pi);
    sym(1e10) * sym(pi);
    sym(2) * sym(pi);
    sym(100) * sym(pi);
    sym(1e10) * sym(pi);
    sym(0.5) * sym(pi);
    sym(50) * sym(pi);
    sym(0.5e10) * sym(pi);
    sym(1);
    sym(1);
    sym(5);
    sym(500);
    sym(5e10);
    sym(5);
    sym(500);
    sym(5e10);
    sym(5);
    sym(500);
    sym(5e10);
    sym(5);
    sym(500);
    sym(5e10);
    sym(1);
    sym(5);
    sym(25);
    sym(1);
    sym(5);
    sym(25);
    sym(5);
    sym(25);
    sym(125);
    sym(5);
    sym(50);
    sym(5e5);
    sym([3 3]);
    sym([30 30]);
    sym([300 300]);
    sym(5);
    sym(50);
    sym(500);
    sym(5);
    sym(50);
    sym(500);
    sym(3);
    sym(30);
    sym(300);
    sym(5);
    sym(50);
    sym(500);
    sym(5);
    sym(50);
    sym(500);
    sym(3);
    sym(30);
    sym(300);
    sym(5);
    sym(500);
    sym(5e10);
    sym(5);
    sym(500);
    sym(5e10);
    sym(1);
    sym(5);
    sym(500);
    sym(5e10);
    sym(1);
    sym(5);
    sym(500);
    sym(5e10);
};
multi_plt_err(fname, size, main, argc, from, to)

%%
f = {
    @(x) 1 ./ gamma(x);
    @(x) 1 ./ gamma(x);
    @(x) 1 ./ gamma(x);
    @(x) 1 ./ gamma(x + 1);
    @(x) 1 ./ gamma(x + 1);
    @(x) 1 ./ gamma(x + 1);
    @(x) gamma(x).^2 ./ gamma(2 * x);
    @(x) gamma(x).^2 ./ gamma(2 * x);
    @(x) gamma(x).^2 ./ gamma(2 * x);
    @(x) sinc(x / pi);
    @(x) sinc(x / pi);
    @(x) sinc(x / pi);
    @(x) tan(x) ./ x;
    @(x) tan(x) ./ x;
    @(x) tan(x) ./ x;
    @(x) sinh(x) ./ x;
    @(x) sinh(x) ./ x;
    @(x) sinh(x) ./ x;
    @(x) cosh(x) ./ x;
    @(x) cosh(x) ./ x;
    @(x) cosh(x) ./ x;
    @(x) tanh(x) ./ x;
    @(x) tanh(x) ./ x;
    @(x) tanh(x) ./ x;
    @(x, n) sin((n + 1 / 2) .* x) ./ sin(x / 2);
    @(x, n) sin((n + 1 / 2) .* x) ./ sin(x / 2);
    @(x, n) sin((n + 1 / 2) .* x) ./ sin(x / 2);
    @(x, n) (1 - cos(n .* x)) ./ (1 - cos(x)) ./ n;
    @(x, n) (1 - cos(n .* x)) ./ (1 - cos(x)) ./ n;
    @(x, n) (1 - cos(n .* x)) ./ (1 - cos(x)) ./ n;
    @(x) sin(1 ./ x);
    @(x) sin(1 ./ x);
    @(x) sin(1 ./ x);
};
from = {
    sym(-5);
    sym(-25);
    sym(-125);
    sym(-5);
    sym(-25);
    sym(-125);
    sym(-3);
    sym(-30);
    sym(-300);
    sym(-5) * sym(pi);
    sym(-500) * sym(pi);
    sym(-5e10) * sym(pi);
    sym(-2.5) * sym(pi);
    sym(-250) * sym(pi);
    sym(-2.5e10) * sym(pi);
    sym(-5);
    sym(-50);
    sym(-500);
    sym(-5);
    sym(-50);
    sym(-500);
    sym(-3);
    sym(-30);
    sym(-300);
    sym([-5 -0.5]);
    sym([-500 -0.5]);
    sym([-5e10 -0.5]);
    sym([-5 0.5]);
    sym([-500 0.5]);
    sym([-5e10, 0.5]);
    sym(0);
    sym(0);
    sym(0);
};
to = {
    sym(5);
    sym(25);
    sym(125);
    sym(5);
    sym(25);
    sym(125);
    sym(3);
    sym(30);
    sym(300);
    sym(5) * sym(pi);
    sym(500) * sym(pi);
    sym(5e10) * sym(pi);
    sym(2.5) * sym(pi);
    sym(250) * sym(pi);
    sym(2.5e10) * sym(pi);
    sym(5);
    sym(50);
    sym(500);
    sym(5);
    sym(50);
    sym(500);
    sym(3);
    sym(30);
    sym(300);
    sym([5 5.5]);
    sym([500 50.5]);
    sym([5e10 500.5]);
    sym([5 5.5]);
    sym([500 50.5]);
    sym([5e10, 500.5]);
    sym(3);
    sym(300);
    sym(3e10);
};
fname = {
    'Test_Recigamma_Small';
    'Test_Recigamma_Medium';
    'Test_Recigamma_Large';
    'Test_Besselclifford_Small';
    'Test_Besselclifford_Medium';
    'Test_Besselclifford_Large';
    'Test_Centralbeta_Small';
    'Test_Centralbeta_Medium';
    'Test_Centralbeta_Large';
    'Test_Sinc_Small';
    'Test_Sinc_Medium';
    'Test_Sinc_Large';
    'Test_Tanc_Small';
    'Test_Tanc_Medium';
    'Test_Tanc_Large';
    'Test_Sinhc_Small';
    'Test_Sinhc_Medium';
    'Test_Sinhc_Large';
    'Test_Coshc_Small';
    'Test_Coshc_Medium';
    'Test_Coshc_Large';
    'Test_Tanhc_Small';
    'Test_Tanhc_Medium';
    'Test_Tanhc_Large';
    'Test_Dirichletkernel_Small';
    'Test_Dirichletkernel_Medium';
    'Test_Dirichletkernel_Large';
    'Test_Fejerkernel_Small';
    'Test_Fejerkernel_Medium';
    'Test_Fejerkernel_Large';
    'Test_Topologistsin_Small';
    'Test_Topologistsin_Medium';
    'Test_Topologistsin_Large';
};
argc = [
    ones(24, 1);
    2 * ones(6, 1);
    ones(3, 1);
];
map = {
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x};
    {@(x) x; @(x) round(x)};
    {@(x) x; @(x) round(x)};
    {@(x) x; @(x) round(x)};
    {@(x) x; @(x) round(x)};
    {@(x) x; @(x) round(x)};
    {@(x) x; @(x) round(x)};
    {@(x) x};
    {@(x) x};
    {@(x) x};
};
multi_test_gen(f, from, to, fname, argc, map)

%%
