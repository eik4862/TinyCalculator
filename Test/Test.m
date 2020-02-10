%% Sin test
% Plot graph
plt_grph(@sin, -2 * pi, 2 * pi, 'Sine function on [-2\pi, 2\pi]', 'sin(x)')
saveas(gcf, 'Sin_Graph', 'epsc')
close('all')

% [0, 2Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@sin, sym(0), sym(pi) * sym(2), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Sin[x] on [0, 2\pi]')
saveas(gcf, 'Sin_Small', 'epsc')
close('all')

%% Cos test
% Plot graph
plt_grph(@cos, -2 * pi, 2 * pi, 'Cosine function on [-2\pi, 2\pi]', 'cos(x)')
saveas(gcf, 'Cos_Graph', 'epsc')
close('all')

% [0, 2Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@cos, sym(0), sym(pi) * sym(2), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Cos[x] on [0, 2\pi]')
saveas(gcf, 'Cos_Small', 'epsc')
close('all')

%% Tan test
% Plot graph
plt_grph(@tan, -pi, pi, 'Tangent function on [-\pi, \pi]', 'tan(x)' ,[-3 3])
saveas(gcf, 'Tan_Graph', 'epsc')
close('all')

% [-Pi/2, Pi/2] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@tan, sym(-pi) / sym(2), sym(pi) / sym(2), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Tan[x] on [-\pi/2, \pi/2]')
saveas(gcf, 'Tan_Small', 'epsc')
close('all')

%% Csc test
% Plot graph
plt_grph(@csc, -2 * pi, 2 * pi, 'Cosecant function on [-2\pi, 2\pi]', 'cosec(x)', [-3 3])
saveas(gcf, 'Csc_Graph', 'epsc')
close('all')

% [0, 2Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@csc, sym(0), sym(2) * sym(pi), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Csc[x] on [0, 2\pi]')
saveas(gcf, 'Csc_Small', 'epsc')
close('all')

%% Sec test
% Plot graph
plt_grph(@sec, -2 * pi, 2 * pi, 'Secant function on [-2\pi, 2\pi]', 'sec(x)' ,[-3 3])
saveas(gcf, 'Sec_Graph', 'epsc')
close('all')

% [0, 2Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@sec, sym(0), sym(2) * sym(pi), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Sec[x] on [0, 2\pi]')
saveas(gcf, 'Sec_Small', 'epsc')
close('all')

%% Cot test
% Plot graph
plt_grph(@cot, -pi, pi, 'Cotagent function on [-\pi, \pi]', 'cot(x)', [-3 3])
saveas(gcf, 'Cot_Graph', 'epsc')
close('all')

% [-Pi/2, Pi/2] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@cot, sym(-pi) / sym(2), sym(pi) / sym(2), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Cot[x] on [-\pi/2, \pi/2]')
saveas(gcf, 'Cot_Small', 'epsc')
close('all')

%% Asin test
% Plot graph
plt_grph(@asin, -1, 1, 'Arcsine function on [-1, 1]', 'asin(x)')
saveas(gcf, 'Asin_Graph', 'epsc')
close('all')

% [-1, 1] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@asin, sym(-1), sym(1), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Asin[x] on [-1, 1]')
saveas(gcf, 'Asin_Small', 'epsc')
close('all')

%% Acos test
% Plot graph
plt_grph(@acos, -1, 1, 'Arccosine function on [-1, 1]', 'acos(x)')
saveas(gcf, 'Acos_Graph', 'epsc')
close('all')

% [-1, 1] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@acos, sym(-1), sym(1), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Acos[x] on [-1, 1]')
saveas(gcf, 'Acos_Small', 'epsc')
close('all')

%% Atan test
% Plot graph
plt_grph(@atan, -5, 5, 'Arctangent function on [-5, 5]', 'atan(x)')
saveas(gcf, 'Atan_Graph', 'epsc')
close('all')

% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@atan, sym(-5), sym(5), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Atan[x] on [-5, 5]')
saveas(gcf, 'Atan_Small', 'epsc')
close('all')

%% Acsc test
% Plot graph
plt_grph(@acsc, -5, 5, 'Arccosecant function on [-5, 5]\(-1, 1)', 'acosec(x)')
saveas(gcf, 'Acsc_Graph', 'epsc')
close('all')

% [-5, 5]\(-1, 1) rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@acsc, sym(-4), sym(4), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Acsc[x] on [-5, 5]\(-1, 1)')
saveas(gcf, 'Acsc_Small', 'epsc')
close('all')

%% Asec test
% Plot graph
plt_grph(@asec, -5, 5, 'Arcsecant function on [-5, 5]\(-1, 1)', 'asec(x)')
saveas(gcf, 'Asec_Graph', 'epsc')
close('all')

% [-5, 5]\(-1, 1) rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@asec, sym(-4), sym(4), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Asec[x] on [-5, 5]\(-1, 1)')
saveas(gcf, 'Asec_Small', 'epsc')
close('all')

%% Acot test
% Plot graph
plt_grph(@acot, -5, 5, 'Arccotagent function on [-5, 5]', 'acot(x)')
saveas(gcf, 'Acot_Graph', 'epsc')
close('all')

% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@acot, sym(-5), sym(5), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Acot[x] on [-5, 5]')
saveas(gcf, 'Acot_Small', 'epsc')
close('all')

%% math.sinh test
% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@sinh, sym(-5), sym(5), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.sinh on [-5, 5]')
saveas(gcf, 'Sinh_-5_5', 'epsc')
close('all')

%% math.cosh test
% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@cosh, sym(-5), sym(5), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.cosh on [-5, 5]')
saveas(gcf, 'Cosh_-5_5', 'epsc')
close('all')

%% math.tanh test
% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@tanh, sym(-5), sym(5), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.tanh on [-5, 5]')
saveas(gcf, 'Tanh_-5_5', 'epsc')
close('all')

%% math.asinh test
% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@asinh, sym(-5), sym(5), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.asinh on [-5, 5]')
saveas(gcf, 'Asinh_-5_5', 'epsc')
close('all')

%% math.acosh test
% [1, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@acosh, sym(1), sym(5), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.acosh on [1, 5]')
saveas(gcf, 'Acosh_1_5', 'epsc')
close('all')

%% math.atanh test
% [-1, 1] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@atanh, sym(-1), sym(1), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.atanh on [-1, 1]')
saveas(gcf, 'Atanh_-1_1', 'epsc')
close('all')

%% math.gamma test
% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@gamma, sym(-5), sym(5), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.gamma on [-5, 5]')
saveas(gcf, 'Gamma_-5_5', 'epsc')
close('all')

%% math.lgamma test
% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@(x) log(abs(gamma(x))), sym(-5), sym(5), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.lgamma on [-5, 5]')
saveas(gcf, 'Lgamma_-5_5', 'epsc')
close('all')

%% math.erf test
% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@erf, sym(-5), sym(5), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.erf on [-5, 5]')
saveas(gcf, 'Erf_-5_5', 'epsc')
close('all')

%% math.erfc test
% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@erfc, sym(-5), sym(5), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.erfc on [-5, 5]')
saveas(gcf, 'Erfc_-5_5', 'epsc')
close('all')

%% math.exp test
% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@exp, sym(-5), sym(5), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.exp on [-5, 5]')
saveas(gcf, 'Exp_-5_5', 'epsc')
close('all')

%% math.sqrt test
% [0, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@sqrt, sym(0), sym(5), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.sqrt on [0, 5]')
saveas(gcf, 'Sqrt_0_5', 'epsc')
close('all')

%% math.log test
% [0, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@log, sym(0), sym(5), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.log on [0, 5]')
saveas(gcf, 'Log_0_5', 'epsc')
close('all')
