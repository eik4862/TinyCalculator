%% PLOT
% Sin
fig = plt_grph(@sin, -2 * pi, 2 * pi, 'Sine function on [-2\pi, 2\pi]', 'sin(x)');
saveas(fig, 'Sin_Graph', 'epsc')
close('all')

% Cos
fig = plt_grph(@cos, -2 * pi, 2 * pi, 'Cosine function on [-2\pi, 2\pi]', 'cos(x)');
saveas(fig, 'Cos_Graph', 'epsc')
close('all')

% Tan
fig = plt_grph(@tan, -pi, pi, 'Tangent function on [-\pi, \pi]', 'tan(x)', [-3 3], [-pi / 2 pi / 2]);
saveas(fig, 'Tan_Graph', 'epsc')
close('all')

% Csc
fig = plt_grph(@csc, -2 * pi, 2 * pi, 'Cosecant function on [-2\pi, 2\pi]', 'cosec(x)', [-3 3], [-pi 0 pi]);
saveas(fig, 'Csc_Graph', 'epsc')
close('all')

% Sec
fig = plt_grph(@sec, -2 * pi, 2 * pi, 'Secant function on [-2\pi, 2\pi]', 'sec(x)' ,[-3 3], [-3 * pi / 2 -pi / 2 pi / 2 3 * pi / 2]);
saveas(fig, 'Sec_Graph', 'epsc')
close('all')

% Cot
fig = plt_grph(@cot, -pi, pi, 'Cotagent function on [-\pi, \pi]', 'cot(x)', [-3 3], 0);
saveas(fig, 'Cot_Graph', 'epsc')
close('all')

% Asin
fig = plt_grph(@asin, -1, 1, 'Arcsine function on [-1, 1]', 'asin(x)', [-inf inf], [], [], [-1 -pi / 2;1 pi / 2]);
saveas(fig, 'Asin_Graph', 'epsc')
close('all')

% Acos
fig = plt_grph(@acos, -1, 1, 'Arccosine function on [-1, 1]', 'acos(x)', [-inf inf], [], [], [-1 pi; 1 0]);
saveas(fig, 'Acos_Graph', 'epsc')
close('all')

% Atan
fig = plt_grph(@atan, -5, 5, 'Arctangent function on [-5, 5]', 'atan(x)', [-inf inf], [], [-pi / 2 pi / 2]);
saveas(fig, 'Atan_Graph', 'epsc')
close('all')

% Acsc
fig = plt_grph(@acsc, -5, 5, 'Arccosecant function on [-5, 5]', 'acosec(x)', [-inf inf], [-0.99 0.99], [], [-1 -pi / 2; 1 pi / 2]);
fig.Children.XTick = -5:1:5;
fig.Children.Children(3).Visible = false;
fig.Children.Children(4).Visible = false;
fig.Children.Children(7).Visible = false;
fig.Children.Children(8).Visible = false;
saveas(fig, 'Acsc_Graph', 'epsc')
close('all')

% Asec
fig = plt_grph(@asec, -5, 5, 'Arcsecant function on [-5, 5]', 'asec(x)', [-inf inf], [-0.99 0.99], pi / 2, [-1 pi; 1 0]);
fig.Children.XTick = -5:1:5;
fig.Children.Children(4).Visible = false;
fig.Children.Children(5).Visible = false;
fig.Children.Children(8).Visible = false;
fig.Children.Children(9).Visible = false;
saveas(fig, 'Asec_Graph', 'epsc')
close('all')

% Acot
fig = plt_grph(@acot, -5, 5, 'Arccotagent function on [-5, 5]', 'acot(x)', [-inf inf], 0, [], [0 pi / 2], [0 -pi / 2]);
fig.Children.XTick = -5:1:5;
fig.Children.Children(3).Visible = false;
saveas(fig, 'Acot_Graph', 'epsc')
close('all')

% math.sinh
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@sinh, sym(-5), sym(5), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
fig = plt_err(in, ref, out, 1000, 'Error of math.sinh on [-5, 5]')
saveas(fig, 'Sinh_-5_5', 'epsc')
close('all')

% math.cosh
% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@cosh, sym(-5), sym(5), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
fig = plt_err(in, ref, out, 1000, 'Error of math.cosh on [-5, 5]')
saveas(fig, 'Cosh_-5_5', 'epsc')
close('all')

% math.tanh
% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@tanh, sym(-5), sym(5), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
fig = plt_err(in, ref, out, 1000, 'Error of math.tanh on [-5, 5]')
saveas(fig, 'Tanh_-5_5', 'epsc')
close('all')

% math.asinh
% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@asinh, sym(-5), sym(5), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
fig = plt_err(in, ref, out, 1000, 'Error of math.asinh on [-5, 5]')
saveas(fig, 'Asinh_-5_5', 'epsc')
close('all')

% math.acosh
% [1, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@acosh, sym(1), sym(5), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
fig = plt_err(in, ref, out, 1000, 'Error of math.acosh on [1, 5]')
saveas(fig, 'Acosh_1_5', 'epsc')
close('all')

% math.atanh
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@atanh, sym(-1), sym(1), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
fig = plt_err(in, ref, out, 1000, 'Error of math.atanh on [-1, 1]')
saveas(fig, 'Atanh_-1_1', 'epsc')
close('all')

% Erf
fig = plt_grph(@erf, -3, 3, 'Error function on [-3, 3]', 'erf(x)', [-inf inf], [], [-1 1]);
fig.Children.YLim = [-1.5 1.5];
saveas(fig, 'Erf_Graph', 'epsc')
close('all')

% Erfc
fig = plt_grph(@erfc, -3, 3, 'Complementary error function on [-3, 3]', 'erfc(x)', [-inf inf], [], 2);
fig.Children.YLim = [0 2.5];
saveas(fig, 'Erfc_Graph', 'epsc')
close('all')

% Gamma
fig = plt_grph(@gamma, -4, 4, 'Gamma function on [-4, 4]', 'gamma(x)', [-5 7], [-4 -3 -2 -1 0], [], [], [], 0.001);
saveas(fig, 'Gamma_Graph', 'epsc')
close('all')

% Log gamma
fig = plt_grph(@(x) log(abs(gamma(x))), -4, 4, 'Log gamma function on [-4, 4]', 'log|gamma(x)|', [-3 3], [-4 -3 -2 -1 0], [], [], [], 0.001);
saveas(fig, 'Lgamma_Graph', 'epsc')
close('all')

% Reciprocal gamma
fig = plt_grph(@(x) 1 ./ gamma(x), -4, 4, 'Reciprocal gamma function on [-4, 4]', '1 / gamma(x)');
saveas(fig, 'Recigamma_Graph', 'epsc')
close('all')

% Bessel-Clifford function
fig = plt_grph(@(x) 1 ./ gamma(x + 1), -4, 4, 'Bessel-Clifford function on [-4, 4]', '1 / gamma(x + 1)');
saveas(fig, 'Besselclifford_Graph', 'epsc')
close('all')


% Beta
% Plot graph
fig = plt_grph3(@(x, y) gamma(x) .* gamma(y) ./ gamma(x + y), [-3 -3], [3 3], 'Beta function on [-3, 3]\times[-3, 3]', 'B(x, y)', 10, [-1.5 -0.5 0.5 1.5; -1.5 -0.5 1 2], [-6 6], [-3 -2 -1 0], [-3 -2 -1 0]);
saveas(fig, 'Beta_Graph', 'epsc')
close('all')

%% math.exp
% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@exp, sym(-5), sym(5), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
fig = plt_err(in, ref, out, 1000, 'Error of math.exp on [-5, 5]')
saveas(fig, 'Exp_-5_5', 'epsc')
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
saveas(fig, 'Sqrt_0_5', 'epsc')
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
saveas(fig, 'Log_0_5', 'epsc')
close('all')


%% TEST
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
    @(x, y) gamma(x) .* gamma(y) ./ gamma(x + y)
    @(x, y) gamma(x) .* gamma(y) ./ gamma(x + y)
    @(x, y) gamma(x) .* gamma(y) ./ gamma(x + y)
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
    sym(-1e10) * sym(pi) * sym(0.5);
    sym(0);
    sym(-100) * sym(pi);
    sym(-1e10) * sym(pi);
    sym(0);
    sym(-100) * sym(pi);
    sym(-1e10) * sym(pi);
    sym(-0.5) * sym(pi);
    sym(-50) * sym(pi);
    sym(-1e10) * sym(pi) * sym(0.5);
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
    sym(1e10) * sym(pi) * sym(0.5);
    sym(2) * sym(pi);
    sym(100) * sym(pi);
    sym(1e10) * sym(pi);
    sym(2) * sym(pi);
    sym(100) * sym(pi);
    sym(1e10) * sym(pi);
    sym(0.5) * sym(pi);
    sym(50) * sym(pi);
    sym(1e10) * sym(pi) * sym(0.5);
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
};
argc = [ones(length(f) - 3, 1); 2 * ones(3, 1)];
multi_test_gen(f, from, to, fname, argc, map)

size = 1000 * ones(length(f), 1);
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
};

multi_plt_err(fname, size, main, argc, from, to)