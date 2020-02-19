%% Sin test
% Plot graph
plt_grph(@sin, -2 * pi, 2 * pi, 'Sine function on [-2\pi, 2\pi]', 'sin(x)');
saveas(gcf, 'Sin_Graph', 'epsc')
close('all')

% [0, 2Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@sin, sym(0), sym(pi) * sym(2), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Sin[x] on [0, 2\pi]')
saveas(gcf, 'Sin_Small', 'epsc')
close('all')

% [-100Pi, 100Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@sin, sym(-100) * sym(pi), sym(100) * sym(pi), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Sin[x] on [-100\pi, 100\pi]')
saveas(gcf, 'Sin_Medium', 'epsc')
close('all')

% [-1e10Pi, 1e10Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@sin, sym(-1e10) * sym(pi), sym(1e10) * sym(pi), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Sin[x] on [-10^{10}\pi, 10^{10}\pi]')
saveas(gcf, 'Sin_Large', 'epsc')
close('all')

%% Cos test
% Plot graph
plt_grph(@cos, -2 * pi, 2 * pi, 'Cosine function on [-2\pi, 2\pi]', 'cos(x)');
saveas(gcf, 'Cos_Graph', 'epsc')
close('all')

% [0, 2Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@cos, sym(0), sym(pi) * sym(2), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Cos[x] on [0, 2\pi]')
saveas(gcf, 'Cos_Small', 'epsc')
close('all')

% [-100Pi, 100Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@cos, sym(-100) * sym(pi), sym(100) * sym(pi), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Cos[x] on [-100\pi, 100\pi]')
saveas(gcf, 'Cos_Medium', 'epsc')
close('all')

% [-1e10Pi, 1e10Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@cos, sym(-1e10) * sym(pi), sym(1e10) * sym(pi), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Cos[x] on [-10^{10}\pi, 10^{10}\pi]')
saveas(gcf, 'Cos_Large', 'epsc')
close('all')

%% Tan test
% Plot graph
plt_grph(@tan, -pi, pi, 'Tangent function on [-\pi, \pi]', 'tan(x)', [-3 3], [-pi / 2 pi / 2]);
saveas(gcf, 'Tan_Graph', 'epsc')
close('all')

% [-Pi/2, Pi/2] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@tan, sym(-pi) / sym(2), sym(pi) / sym(2), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Tan[x] on [-\pi/2, \pi/2]')
saveas(gcf, 'Tan_Small', 'epsc')
close('all')

% [-50Pi, 50Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@tan, sym(-50) * sym(pi), sym(50) * sym(pi), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Tan[x] on [-50\pi, 50\pi]')
saveas(gcf, 'Tan_Medium', 'epsc')
close('all')

% [-1e10Pi/2, 1e10Pi/2] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@tan, sym(-1e10) * sym(pi) / sym(2), sym(1e10) * sym(pi) / sym(2), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Tan[x] on [-10^{10}\pi/2, 10^{10}\pi/2]')
saveas(gcf, 'Tan_Large', 'epsc')
close('all')

%% Csc test
% Plot graph
plt_grph(@csc, -2 * pi, 2 * pi, 'Cosecant function on [-2\pi, 2\pi]', 'cosec(x)', [-3 3], [-pi 0 pi]);
saveas(gcf, 'Csc_Graph', 'epsc')
close('all')

% [0, 2Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@csc, sym(0), sym(2) * sym(pi), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Csc[x] on [0, 2\pi]')
saveas(gcf, 'Csc_Small', 'epsc')
close('all')

% [-100Pi, 100Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@csc, sym(-100) * sym(pi), sym(100) * sym(pi), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Csc[x] on [-100\pi, 100\pi]')
saveas(gcf, 'Csc_Medium', 'epsc')
close('all')

% [-1e10Pi, 1e10Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@csc, sym(-1e10) * sym(pi), sym(1e10) * sym(pi), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Csc[x] on [-10^{10}\pi, 10^{10}\pi]')
saveas(gcf, 'Csc_Large', 'epsc')
close('all')

%% Sec test
% Plot graph
plt_grph(@sec, -2 * pi, 2 * pi, 'Secant function on [-2\pi, 2\pi]', 'sec(x)' ,[-3 3], [-3 * pi / 2 -pi / 2 pi / 2 3 * pi / 2]);
saveas(gcf, 'Sec_Graph', 'epsc')
close('all')

% [0, 2Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@sec, sym(0), sym(2) * sym(pi), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Sec[x] on [0, 2\pi]')
saveas(gcf, 'Sec_Small', 'epsc')
close('all')

% [-100Pi, 100Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@sec, sym(-100) * sym(pi), sym(100) * sym(pi), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Sec[x] on [-100\pi, 100\pi]')
saveas(gcf, 'Sec_Medium', 'epsc')
close('all')

% [-1e10Pi, 1e10Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@sec, sym(-1e10) * sym(pi), sym(1e10) * sym(pi), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Sec[x] on [-10^{10}\pi, 10^{10}\pi]')
saveas(gcf, 'Sec_Large', 'epsc')
close('all')

%% Cot test
% Plot graph
plt_grph(@cot, -pi, pi, 'Cotagent function on [-\pi, \pi]', 'cot(x)', [-3 3], 0);
saveas(gcf, 'Cot_Graph', 'epsc')
close('all')

% [-Pi/2, Pi/2] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@cot, sym(-pi) / sym(2), sym(pi) / sym(2), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Cot[x] on [-\pi/2, \pi/2]')
saveas(gcf, 'Cot_Small', 'epsc')
close('all')

% [-50Pi, 50Pi] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@cot, sym(-50) * sym(pi), sym(50) * sym(pi), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Cot[x] on [-50\pi, 50\pi]')
saveas(gcf, 'Cot_Medium', 'epsc')
close('all')

% [-1e10Pi/2, 1e10Pi/2] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@cot, sym(-1e10) * sym(pi) / sym(2), sym(1e10) * sym(pi) / sym(2), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Cot[x] on [-10^{10}\pi/2, 10^{10}\pi/2]')
saveas(gcf, 'Cot_Large', 'epsc')
close('all')

%% Asin test
% Plot graph
plt_grph(@asin, -1, 1, 'Arcsine function on [-1, 1]', 'asin(x)', [-inf inf], [], [], [-1 -pi / 2;1 pi / 2]);
saveas(gcf, 'Asin_Graph', 'epsc')
close('all')

% [-1, 1] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@asin, sym(-1), sym(1), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Asin[x] on [-1, 1]')
saveas(gcf, 'Asin_Small', 'epsc')
close('all')

%% Acos test
% Plot graph
plt_grph(@acos, -1, 1, 'Arccosine function on [-1, 1]', 'acos(x)', [-inf inf], [], [], [-1 pi; 1 0]);
saveas(gcf, 'Acos_Graph', 'epsc')
close('all')

% [-1, 1] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@acos, sym(-1), sym(1), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Acos[x] on [-1, 1]')
saveas(gcf, 'Acos_Small', 'epsc')
close('all')

%% Atan test
% Plot graph
plt_grph(@atan, -5, 5, 'Arctangent function on [-5, 5]', 'atan(x)', [-inf inf], [], [-pi / 2 pi / 2]);
saveas(gcf, 'Atan_Graph', 'epsc')
close('all')

% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@atan, sym(-5), sym(5), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Atan[x] on [-5, 5]')
saveas(gcf, 'Atan_Small', 'epsc')
close('all')

% [-500, 500] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@atan, sym(-500), sym(500), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Atan[x] on [-500, 500]')
saveas(gcf, 'Atan_Medium', 'epsc')
close('all')

% [-5e10, 5e10] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@atan, sym(-5e10), sym(5e10), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Atan[x] on [-5\times10^{10}, 5\times10^{10}]')
saveas(gcf, 'Atan_Large', 'epsc')
close('all')

%% Acsc test
% Plot graph
fig = plt_grph(@acsc, -5, 5, 'Arccosecant function on [-5, 5]', 'acosec(x)', [-inf inf], [-0.99 0.99], [], [-1 -pi / 2; 1 pi / 2]);
fig.Children.XTick = -5:1:5;
fig.Children.Children(3).Visible = false;
fig.Children.Children(4).Visible = false;
fig.Children.Children(7).Visible = false;
fig.Children.Children(8).Visible = false;
saveas(gcf, 'Acsc_Graph', 'epsc')
close('all')

% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@acsc, sym(-4), sym(4), 1000, in, ref, {@(x) x + sign(x)})
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Acsc[x] on [-5, 5]')
saveas(gcf, 'Acsc_Small', 'epsc')
close('all')

% [-500, 500] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@acsc, sym(-499), sym(499), 1000, in, ref, {@(x) x + sign(x)})
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Acsc[x] on [-500, 500]')
saveas(gcf, 'Acsc_Medium', 'epsc')
close('all')

% [-5e10, 5e10] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@acsc, sym(-5e10) + sym(1), sym(5e10) - sym(1), 1000, in, ref, {@(x) x + sign(x)})
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Acsc[x] on [-5\times10^{10}, 5\times10^{10}]')
saveas(gcf, 'Acsc_Large', 'epsc')
close('all')

%% Asec test
% Plot graph
fig = plt_grph(@asec, -5, 5, 'Arcsecant function on [-5, 5]', 'asec(x)', [-inf inf], [-0.99 0.99], pi / 2, [-1 pi; 1 0]);
fig.Children.XTick = -5:1:5;
fig.Children.Children(4).Visible = false;
fig.Children.Children(5).Visible = false;
fig.Children.Children(8).Visible = false;
fig.Children.Children(9).Visible = false;
saveas(gcf, 'Asec_Graph', 'epsc')
close('all')

% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@asec, sym(-4), sym(4), 1000, in, ref, {@(x) x + sign(x)})
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Asec[x] on [-5, 5]')
saveas(gcf, 'Asec_Small', 'epsc')
close('all')

% [-500, 500] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@asec, sym(-499), sym(499), 1000, in, ref, {@(x) x + sign(x)})
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Asec[x] on [-500, 500]')
saveas(gcf, 'Asec_Medium', 'epsc')
close('all')

% [-5e10, 5e10] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@asec, sym(-5e10) + sym(1), sym(5e10) - sym(1), 1000, in, ref, {@(x) x + sign(x)})
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Asec[x] on [-5\times10^{10}, 5\times10^{10}]')
saveas(gcf, 'Asec_Large', 'epsc')
close('all')

%% Acot test
% Plot graph
fig = plt_grph(@acot, -5, 5, 'Arccotagent function on [-5, 5]', 'acot(x)', [-inf inf], 0, [], [0 pi / 2], [0 -pi / 2]);
fig.Children.XTick = -5:1:5;
fig.Children.Children(3).Visible = false;
saveas(gcf, 'Acot_Graph', 'epsc')
close('all')

% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@acot, sym(-5), sym(5), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Acot[x] on [-5, 5]')
saveas(gcf, 'Acot_Small', 'epsc')
close('all')

% [-500, 500] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@acot, sym(-500), sym(500), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Acot[x] on [-500, 500]')
saveas(gcf, 'Acot_Medium', 'epsc')
close('all')

% [-5e10, 5e10] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@acot, sym(-5e10), sym(5e10), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Acot[x] on [-5\times10^{10}, 5\times10^{10}]')
saveas(gcf, 'Acot_Large', 'epsc')
close('all')

%% math.sinh test
% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@sinh, sym(-5), sym(5), 1000, in, ref)
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
test_gen(@cosh, sym(-5), sym(5), 1000, in, ref)
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
test_gen(@tanh, sym(-5), sym(5), 1000, in, ref)
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
test_gen(@asinh, sym(-5), sym(5), 1000, in, ref)
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
test_gen(@acosh, sym(1), sym(5), 1000, in, ref)
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
test_gen(@atanh, sym(-1), sym(1), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.atanh on [-1, 1]')
saveas(gcf, 'Atanh_-1_1', 'epsc')
close('all')

%% Erf test
% Plot graph
fig = plt_grph(@erf, -3, 3, 'Error function on [-3, 3]', 'erf(x)', [-inf inf], [], [-1 1]);
fig.Children.YLim = [-1.5 1.5];
saveas(gcf, 'Erf_Graph', 'epsc')
close('all')

% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@erf, sym(-5), sym(5), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Erf[x] on [-5, 5]')
saveas(gcf, 'Erf_Small', 'epsc')
close('all')

% [-500, 500] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@erf, sym(-500), sym(500), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Erf[x] on [-500, 500]')
saveas(gcf, 'Erf_Medium', 'epsc')
close('all')

% [-5e10, 5e10] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@erf, sym(-5e10), sym(5e10), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Erf[x] on [-5\times10^{10}, 5\times10^{10}]')
saveas(gcf, 'Erf_Large', 'epsc')
close('all')

%% Erfc test
% Plot graph
fig = plt_grph(@erfc, -3, 3, 'Complementary error function on [-3, 3]', 'erfc(x)', [-inf inf], [], 2);
fig.Children.YLim = [0 2.5];
saveas(gcf, 'Erfc_Graph', 'epsc')
close('all')

% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@erfc, sym(-5), sym(5), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Erfc[x] on [-5, 5]')
saveas(gcf, 'Erfc_Small', 'epsc')
close('all')

% [-500, 500] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@erfc, sym(-500), sym(500), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Erfc[x] on [-500, 500]')
saveas(gcf, 'Erfc_Medium', 'epsc')
close('all')

% [-5e10, 5e10] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@erfc, sym(-5e10), sym(5e10), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Erfc[x] on [-5\times10^{10}, 5\times10^{10}]')
saveas(gcf, 'Erfc_Large', 'epsc')
close('all')

%% Gamma test
% Plot graph
plt_grph(@gamma, -4, 4, 'Gamma function on [-4, 4]', 'gamma(x)', [-5 7], [-4 -3 -2 -1 0], [], [], [], 0.001);
saveas(gcf, 'Gamma_Graph', 'epsc')
close('all')

% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@gamma, sym(-5), sym(5), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Gamma[x] on [-5, 5]')
saveas(gcf, 'Gamma_Small', 'epsc')
close('all')

% [-50, 50] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@gamma, sym(-50), sym(50), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Gamma[x] on [-50, 50]')
saveas(gcf, 'Gamma_Medium', 'epsc')
close('all')

%% Lgamma test
% Plot graph
plt_grph(@(x) log(abs(gamma(x))), -4, 4, 'Log gamma function on [-4, 4]', 'log gamma(x)', [-3 3], [-4 -3 -2 -1 0], [], [], [], 0.001);
saveas(gcf, 'Lgamma_Graph', 'epsc')
close('all')

% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@(x) log(abs(gamma(x))), sym(-5), sym(5), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Lgamma[x] on [-5, 5]')
saveas(gcf, 'Lgamma_Small', 'epsc')
close('all')

% [-50, 50] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@(x) log(abs(gamma(x))), sym(-50), sym(50), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of Lgamma[x] on [-50, 50]')
saveas(gcf, 'Lgamma_Medium', 'epsc')
close('all')

%% Beta test
% Plot graph
plt_grph3(@(x, y) gamma(x) .* gamma(y) ./ gamma(x + y), [-3 -3], [3 3], 'Beta function on [-3, 3]\times[-3, 3]', 'B(x, y)', 10, [-1.5 -0.5 0.5 1.5; -1.5 -0.5 1 2], [-6 6], [-3 -2 -1 0], [-3 -2 -1 0]);
saveas(gcf, 'Beta_Graph', 'epsc')
close('all')

% [-3, 3] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@(x, y) gamma(x) .* gamma(y) ./ gamma(x + y), sym([-3 3]), sym([-3 3]), 1000, in, ref)
close('all')

%% math.exp test
% [-5, 5] rand
in = fopen('Test.in', 'w');
ref = fopen('Test.ref', 'w');
test_gen(@exp, sym(-5), sym(5), 1000, in, ref)
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
test_gen(@sqrt, sym(0), sym(5), 1000, in, ref)
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
test_gen(@log, sym(0), sym(5), 1000, in, ref)
close('all')

in = fopen('Test.in', 'r');
ref = fopen('Test.ref', 'r');
out = fopen('Test.out', 'r');
plt_err(in, ref, out, 1000, 'Error of math.log on [0, 5]')
saveas(gcf, 'Log_0_5', 'epsc')
close('all')
