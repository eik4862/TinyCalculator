function multi_test_gen(f, from, to, fname, argc, map, cnt, prec)
    % Argument validation.    
    if nargin == 6
        cnt = 1000 * ones(length(f), 1);
        prec = 300 * ones(length(f), 1);
    elseif nargin == 7
        prec = 300 * ones(length(f), 1);
    elseif nargin ~= 8
        error('Some arguments are missing. Terminate.')
    end
    
    range_flag = false;
    
    for i = 1:min([length(from) length(to)])
        if any(from{i} >= to{i})
            range_flag = true;
        end
    end
    
    if ~((length(f) == length(from)) && (length(f) == length(to)) && (length(f) == length(fname)))
        error('Dimensions of input arguments does not match. Terminate.')
    elseif range_flag
        error('Generation range is invalid. Terminate.')
    elseif any(cnt < 2) || any(mod(cnt, 1) ~= 0)
        error('The # of test points must be integer greater than 1. Terminate.')
    elseif any(prec <= 0) || any(mod(prec, 1) ~= 0)
        error('The precision must be positive integer. Terminate.')
    elseif ~all(ismember(argc, [1 2]))
        error('The target functions must be univariate or bivariate. Terminate.')    
    end
    
    % Report.
    fprintf('%s\n', f_title('MULTIPLE TEST DB GENERATOR'))
    fprintf('  @target: %d\n', length(f))
    
    if all(cnt == cnt(1))
        fprintf('  @size  : %d\n', cnt(1))
    end
    
    if all(prec == prec(1))
        fprintf('  @prec  : %d\n', prec(1))
    end
    
    fprintf('\n%s\n', f_title('START GENERATION'))
    
    % Open files to write on.
    fprintf('  Opening files.......[%06.2f%%', 0)
    tic
    
    if ~exist('In', 'dir')
        mkdir('In')
    end
    
    if ~exist('Ref', 'dir')
        mkdir('Ref')
    end
    
    in = cell(1, length(f));
    ref = cell(1, length(f));
    
    for i = 1:length(f)
        in{i} = fopen(sprintf('In/%s.in', fname{i}), 'w');
        
        if in{i} == -1
            error('Cannot open test input file to write on. Terminate.')
        end
        
        ref{i} = fopen(sprintf('Ref/%s.ref', fname{i}), 'w');
        
        if ref{i} == 1
            error('Cannot open reference output file to write on. Terminate.')
        end
        
        prog_update(i, length(f))
    end
    
    % Generate test DBs.    
    for i = 1:length(f)
        fprintf(']\n  Generating DB %03d...[%06.2f%%', i, 0)
        test_gen(f{i}, from{i}, to{i}, cnt(i), in{i}, ref{i}, map{i}, prec(i), false)
    end
    
    % Close written files.
    fprintf(']\n  Closing files.......[%06.2f%%', 0)
    
    for i = 1:length(f)
        if fclose(in{i}) == -1
            error('Cannot close written test input file. Terminate.')
        end
        
        if fclose(ref{i}) == -1
            error('Cannot close written reference output file. Terminate.')
        end
        
        prog_update(i, length(f))
    end
    
    elapsed = toc;
    fprintf(']\n\n')

    % Report.
    fprintf('%s\n', f_title('GENERATION FINISHED'))
    fprintf('  @elapsed: %.02fms\n\n', elapsed * 1000)
end