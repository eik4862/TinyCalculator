function test_gen(f, from, to, cnt, in, ref, map, prec)
% TEST_GEN generates test DB input and reference output.
%
% TEST_GEN(F, FROM, TO, CNT, IN, REF, MAP, PREC) geneates CNT random test
% inputs from U(FROM, TO) and reference outputs from function F at
% generated input points. Before computing reference output, the input
% points are mapped by MAP. All results are calculated using arbitrary
% precision arithematic, with precision PREC. Generated input and output
% will be stored at IN and REF, resp.
%
% Inputs:
%   F    - Function which will be used to generate output.
%   FROM - Starting point of input generation range.
%   TO   - Ending point of input generation range.
%   CNT  - The # of test points.
%   IN   - File where generated input to be written.
%   REF  - File where generated output to be written.
%
% Optional inputs:
%   MAP  - Mapping for input points. (default = {@(x) x})
%   PREC - Precision of floating point. (default = 100)
%
% Notes:
%   - FROM and TO must be symbolic type for arbitrary floating point
%     operation to be accurate.
%   - Dimension of FROM and TO have to conincide with the # of arguments F
%     takes.
%   - Function F must be either univariate or bivariate function.
%   - Since it does not close files IN and REF after writing on them, one
%     must close them manually after this function call.

    % Argument validation.
    if nargin == 6
        map = {@(x) x};
        prec = 100;
    elseif nargin == 7
        prec = 100;
    elseif nargin ~= 8
        error('Some arguments are missing. Terminate.')
    end
    
    argc = length(from);
    
    if length(from) ~= length(to) || any(double(from) >= double(to))
        error('Generation range is invalid. Terminate.')
    elseif cnt < 2
        error('The # of test points must be at least 2. Terminate.')
    elseif mod(cnt, 1) ~= 0
        error('The # of test points must be integer. Terminate.')
    elseif prec <= 0 || mod(prec, 1) ~= 0
        error('The # of test points must be positive integer. Terminate.')
    elseif ~ismember(argc, [1 2])
        error('The target function must be univariate or bivariate. Terminate.')    
    end
    
    in_name = fopen(in);
    ref_name = fopen(ref);
    
    if in_name == -1
        error('Cannot open test input file to write on. Terminate.')
    elseif ref_name == -1
        error('Cannot open test reference output file to write on. Terminate.')
    end
    
    % Turning off all warnings.
    warning('off', 'all')
    
    % Report.
    fprintf('%s\n', f_title('TEST DB GENERATOR'))
    fprintf('  @in   : %s\n', in_name)
    fprintf('  @out  : %s\n', ref_name)
    
    if argc == 1
        fprintf('  @range: [%.3g, %.3g]\n', from, to)
        fprintf('  @size : %d\n', cnt)
    else
        fprintf('  @range: [%.3g, %.3g]*[%.3g, %.3g]\n', from(1), to(1), from(2), to(2))
        fprintf('  @size : %d\n', cnt^2)
    end
    
    fprintf('  @argc : %d\n', argc)
    fprintf('  @prec : %d\n\n', prec)

    % Generate input.
    fprintf('%s\n', f_title('START GENERATION'))
    fprintf('  Generating input....[%06.2f%%', 0)
    tic
    
    if argc == 1
        % Since random number generation uses bitwise operation, precision
        % may be compromised here.
        % But not a big deal!
        x = map{1}(sym(unifrnd(double(from), double(to), 1, cnt)));

        for i = 1:cnt
            fprintf(in, '%s\n', string(vpa(x(i), prec)));            
            prog_update(i, cnt)
        end

        % Generate output.
        fprintf(']\n  Generating output...[%06.2f%%', 0)
        y = f(x);
    else
        % Since random number generation uses bitwise operation, precision
        % may be compromised here.
        % But not a big deal!
        x = sym([map{1}(unifrnd(double(from(1)), double(to(1)), 1, cnt));
                 map{1}(unifrnd(double(from(2)), double(to(2)), 1, cnt))]);

        for i = 1:cnt
            fprintf(in, '%s\n%s\n', string(vpa(x(1,i), prec)), string(vpa(x(2,i), prec)));            
            prog_update(i, cnt)
        end

        % Generate output.
        fprintf(']\n  Generating output...[%06.2f%%', 0)
        y = f(x(1,:), x(2,:));
    end
    
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
    
    % Turning on all warnings.
    warning('on', 'all')
end