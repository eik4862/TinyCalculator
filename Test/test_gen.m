function test_gen(f, from, to, cnt, in, ref, mode, prec)
% TEST_GEN generates test DB input and reference output.
%
% TEST_GEN(F, FROM, TO, CNT, IN, REF, 'step') generates CNT uniform test
% inputs which range [FROM, TO] and reference outputs from function F at
% generated input points. All results are calculated using arbitrary
% precision arithematic, with precision 100. Generated input and output
% will be stored at IN and REF, resp.
%
% TEST_GEN(F, FROM, TO, CNT, IN, REF, 'rand') generates CNT random test
% inputs from U(FROM, TO) and reference outputs from function F at
% generated input points. All results are calculated using arbitrary
% precision arithematic, with precision 100. Generated input and output
% will be stored at IN and REF, resp.
%
% TEST_GEN(F, FROM, TO, CNT, IN, REF, 'geostep') generates CNT
% geometrically uniform test inputs which range [FROM, TO] and reference
% outputs from function F at generated input points. All results are
% calculated using arbitrary precision arithematic, with precision 100.
% Generated input and output will be stored at IN and REF, resp.
%
% TEST_GEN(F, FROM, TO, CNT, IN, REF, 'georand') generates CNT random test
% inputs from exp(U(FROM, TO)) (flipped Gumbel distribution) and reference
% outputs from function F at generated input points. All results are
% calculated using arbitrary precision arithematic, with precision 100.
% Generated input and output will be stored at IN and REF, resp.
%
% TEST_GEN(F, FROM, TO, CNT, IN, REF, MODE, PREC) geneates CNT test inputs
% which ranges [FROM, TO] according to specified MODE and reference outputs
% from function F at generated input points . All results are calculated
% using arbitrary precision arithematic, with precision PREC. Generated
% input and output will be stored at IN and REF, resp.
%
% Inputs:
%   F    - Function which will be used to generate output.
%   FROM - Starting point of input points.
%   TO   - Ending point of input points.
%   CNT  - The # of test points.
%   IN   - File where generated input to be written.
%   REF  - File where generated output to be written.
%   MODE - Input generation mode. (step/rand/geostep/georand)
%
% Optional inputs:
%   PREC - Precision of floating point. (default = 100)
%
% Notes:
%   - FROM and TO must be symbolic type for arbitrary floating point
%     operation to be accurate.
%   - With geostep and georand mode, generation range [FROM, TO] must be
%     positive.
%   - Function F must be univariate function, like sin.
%   - Since it does not close files IN and REF after writing on them, one
%     must close them manually after this function call.

    % Argument validation.
    if nargin == 7
        prec = 100;
    elseif nargin ~= 8
        error('Some arguments are missing. Terminate.')
    end
    
    if from > to
        error('Generation range is invalid. Terminate.')
    elseif cnt < 2
        error('The # of test points must be at least 2. Terminate.')
    elseif mod(cnt, 1) ~= 0
        error('The # of test points must be integer. Terminate.')
    elseif ~strcmp(mode, 'step') && ~strcmp(mode, 'rand') && ~strcmp(mode, 'geostep') && ~strcmp(mode, 'georand')
        error('Invalid mode. Terminate.')
    elseif prec <= 0 || mod(prec, 1) ~= 0
        error('The # of test points must be positive integer. Terminate.')
    elseif strcmp(mode, 'geostep') && sign(from) ~= 1
        error('With geostep mode, the range of generation must be positive. Terminate.')
    end
    
    in_name = fopen(in);
    ref_name = fopen(ref);
    
    if in_name == -1
        error('Cannot open test input file to write on. Terminate.')
    elseif ref_name == -1
        error('Cannot open test reference output file to write on. Terminate.')
    end
    
    % Report.
    fprintf('%s\n', f_title('TEST DB GENERATOR'))
    fprintf('  @in   : %s\n', in_name)
    fprintf('  @out  : %s\n', ref_name)
    fprintf('  @mode : %s\n', mode)
    fprintf('  @range: [%.3g, %.3g]\n', from, to)
    
    if strcmp(mode, 'step')
        step = (to - from) / sym(cnt - 1);
        fprintf('  @step : %.3g\n', step(1)) 
    elseif strcmp(mode, 'geostep')
        step = nthroot(to / from, cnt - 1);
        fprintf('  @step : %.3g\n', step(1)) 
    end
    
    fprintf('  @size : %d\n', cnt)
    fprintf('  @prec : %d\n\n', prec)

    % Generate input.
    fprintf('%s\n', f_title('START GENERATION'))
    fprintf('  Generating input....[%06.2f%%', 0)
    tic
    
    if strcmp(mode, 'step')
        x = from + sym(0:cnt - 1) * step;        
    elseif strcmp(mode, 'rand')
        % Since random number generation uses bitwise operation, precision
        % may be compromised here.
        % But not a big deal!
        x= sym(unifrnd(double(from), double(to), 1, cnt));
    elseif strcmp(mode, 'geostep')
        x = from .* step.^sym(0:cnt - 1);
    else
        % Since random number generation uses bitwise operation, precision
        % may be compromised here.
        % But not a big deal!
        x = exp(sym(unifrnd(double(log(from)), double(log(to)), 1, cnt)));
    end
    
    for i = 1:cnt
        fprintf(in, '%s\n', string(vpa(x(i), prec)));            
        prog_update(i, cnt)
    end

    % Generate output.
    fprintf(']\n  Generating output...[%06.2f%%', 0)
    y = f(x);
    
    for i = 1:cnt
        fprintf(ref, '%s\n', string(vpa(y(i), prec)));
        prog_update(i, cnt)
    end
    
    elapsed = toc;
    fprintf(']\n\n')
    
    % Report.
    dir_in = dir(in_name);
    dir_ref = dir(ref_name);
    fprintf('%s\n', f_title('GENERATION FINISHED'))
    fprintf('  @in     : %s (%dbytes)\n', in_name, dir_in.bytes)
    fprintf('  @out    : %s (%dbytes)\n', ref_name, dir_ref.bytes)
    fprintf('  @elapsed: %.02fms\n\n', elapsed * 1000)
end