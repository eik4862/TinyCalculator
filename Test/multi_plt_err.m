function multi_plt_err(fname, size, main, argc, from, to)
    % Argument validation.        
    if nargin ~= 6
        error('Some arguments are missing. Terminate.')
    end
    
    range_flag = false;
    
    for i = 1:min([length(from) length(to)])
        if any(from{i} >= to{i})
            range_flag = true;
        end
    end
    
    if ~((length(fname) == length(size)) && (length(fname) == length(main)) && (length(fname) == length(argc)) && (length(fname) == length(from)) && (length(fname) == length(to)))
        error('Dimensions of input arguments does not match. Terminate.')
    elseif any(size <= 0) || any(mod(size, 1) ~= 0)
        error('The # of test outputs must be positive integer. Terminate.')
    elseif ~all(ismember(argc, [1 2]))
        error('The target functions must be univariate or bivariate. Terminate.')    
    elseif range_flag
        error('Plotting range is invalid. Terminate.')
    end
    
    % Report.
    fprintf('%s\n', f_title('MULTIPLE TEST DATA PROCESSOR'))
    fprintf('  @target: %d\n', length(fname))
    
    if all(size == size(1))
        fprintf('  @size  : %d\n', size(1))
    end

    fprintf('\n%s\n', f_title('START PROCESSING'))
    
     % Open files to read.
    fprintf('  Opening files.......[%06.2f%%', 0)
    tic
    
    in = cell(1, length(fname));
    ref = cell(1, length(fname));
    out = cell(1, length(fname));
    
    for i = 1:length(fname)
        in{i} = fopen(sprintf('In/%s.in', fname{i}), 'r');
        
        if in{i} == -1
            error('Cannot open test input file. Terminate.')
        end
        
        ref{i} = fopen(sprintf('Ref/%s.ref', fname{i}), 'r');
        
        if ref{i} == -1
            error('Cannot open reference output file. Terminate.')
        end
        
        out{i} = fopen(sprintf('Out/%s.out', fname{i}), 'r');
        
        if out{i} == -1
            error('Cannot open test output file. Terminate.')
        end
        
        prog_update(i, length(fname))
    end
    
    if ~exist('Plt', 'dir')
        mkdir('Plt')
    end
    
    % Process data and save it.
    fprintf(']\n  Processing data.....[%06.2f%%', 0)

    for i = 1:length(fname)
        fig = plt_err(in{i}, ref{i}, out{i}, size(i), main{i}, argc(i), double(from{i}), double(to{i}), false);
        tmp = split(fname{i}, '_');
        plt_name = [tmp{2} '_' tmp{3}];
        saveas(fig, sprintf('Plt/%s.eps', plt_name), 'epsc')
        close(fig)
        prog_update(i, length(fname))
    end
    
    % Close files.
    fprintf(']\n  Closing files.......[%06.2f%%', 0)
    
    for i = 1:length(fname)
        if fclose(in{i}) == -1
            error('Cannot close test input file. Terminate.')
        end
        
        if fclose(ref{i}) == -1
            error('Cannot close reference output file. Terminate.')
        end
        
        if fclose(out{i}) == -1
            error('Cannot close test output file. Terminate.')
        end
        
        prog_update(i, length(fname))
    end
    
    elapsed = toc;
    fprintf(']\n\n')

    % Report.
    fprintf('%s\n', f_title('PROCESSING FINISHED'))
    fprintf('  @elapsed: %.02fms\n\n', elapsed * 1000)
end