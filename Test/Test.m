%% math.sin test
% [0, 2Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@sin, sym(0), sym(pi) * sym(2), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.sin on [0, 2\pi]')
saveas(gcf, 'Math_Sin_0_2Pi', 'epsc')
close('all')

%% math.cos test
% [0, 2Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@cos, sym(0), sym(pi) * sym(2), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.cos on [0, 2\pi]')
saveas(gcf, 'Math_Cos_0_2Pi', 'epsc')
close('all')

%% math.tan test
% [-Pi/2, Pi/2] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@tan, sym(-pi) / sym(2), sym(pi) / sym(2), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.tan on [-\pi/2, \pi/2]')
saveas(gcf, 'Math_Tan_-Pi%2_Pi%2', 'epsc')
close('all')

%% math.asin test
% [-1, 1] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@asin, sym(-1), sym(1), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.asin on [-1, 1]')
saveas(gcf, 'Math_Asin_-1_1', 'epsc')
close('all')

%% math.acos test
% [-1, 1] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@acos, sym(-1), sym(1), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.acos on [-1, 1]')
saveas(gcf, 'Math_Acos_-1_1', 'epsc')
close('all')

%% math.atan test
% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@atan, sym(-5), sym(5), 1000, in, ref, 'rand')
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.atan on [-5, 5]')
saveas(gcf, 'Math_Atan_-5_5', 'epsc')
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
saveas(gcf, 'Math_Sinh_-5_5', 'epsc')
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
saveas(gcf, 'Math_Cosh_-5_5', 'epsc')
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
saveas(gcf, 'Math_Tanh_-5_5', 'epsc')
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
saveas(gcf, 'Math_Asinh_-5_5', 'epsc')
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
saveas(gcf, 'Math_Acosh_1_5', 'epsc')
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
saveas(gcf, 'Math_Atanh_-1_1', 'epsc')
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
saveas(gcf, 'Math_Gamma_-5_5', 'epsc')
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
saveas(gcf, 'Math_Lgamma_-5_5', 'epsc')
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
saveas(gcf, 'Math_Erf_-5_5', 'epsc')
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
saveas(gcf, 'Math_Erfc_-5_5', 'epsc')
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
saveas(gcf, 'Math_Exp_-5_5', 'epsc')
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
saveas(gcf, 'Math_Sqrt_0_5', 'epsc')
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
saveas(gcf, 'Math_Log_0_5', 'epsc')
close('all')
