function fig = plt_grph(f, from, to, main, ylab, lim, x_asymp, y_asymp, mark_in, mark_out, step)
% PLT_GRPH plots the graph of univariate function.
%
% PLT_GRPH(F, FROM, TO, MAIN, YLAB, LIM, X_ASYMP, Y_ASYMP, MARK_IN,
% MARK_OUT, SETP) plots graph of univariate function F on range [FROM, TO].
% The sample points for plotting will be drawn uniformly with step size
% STEP. Computed value which is not in LIM will be truncated. The title of
% the graph will be MAIN and label of y axis will be YLAB. Additionally, it
% draws vertical asymptotic lines X_ASYMP and horizontal asymptotic lines
% Y_ASYMP with inclusive markers MARK_IN and exclusive markers MARK_OUT.
% 
% Inputs:
%   F    - Function to be plotted.
%   FROM - Starting point of plotting range.
%   TO   - Ending point of plotting range.
%   MAIN - The title of the plot.
%   YLAB - The label of y axis.
%
% Optional inputs:
%   LIM      - Limit of function values. (default = [-inf inf])
%   X_ASYMP  - Points for vertical asymptotic lines. (default = [])
%   Y_ASYMP  - Points for horizontal asymptotic lines. (default = [])
%   MARK_IN  - Coordinates for inclusive markers. (default = [])
%   MARK_OUT - Coordinates for exclusive markers. (default = [])
%   STEP     - Step size for sample points. (default = 0.01)
%
% Outputs:
%   FIG - Figure handle of the plot.
%
% Notes:
%   - Elements of X_ASYMP and Y_ASYMP must be sorted.
%   - Elements of X_ASYMP which coincides with FROM or TO will be ignored.

    % Argument validation.
    if nargin == 5
        lim = [-inf inf];
        x_asymp = [];
        y_asymp = [];
        mark_in = [];
        mark_out = [];
        step = 0.01;
    elseif nargin == 6
        x_asymp = [];
        y_asymp = [];
        mark_in = [];
        mark_out = [];
        step = 0.01;
    elseif nargin == 7
        y_asymp = [];
        mark_in = [];
        mark_out = [];
        step = 0.01;
    elseif nargin == 8
        mark_in = [];
        mark_out = [];
        step = 0.01; 
    elseif nargin == 9
        mark_out = [];
        step = 0.01; 
    elseif nargin == 10
        step = 0.01; 
    elseif nargin ~= 11
        error('Some arguments are missing. Terminate.')
    end
    
    if from >= to
        error('Plotting range is invalid. Terminate.')
    elseif step <= 0 || step > (to - from)
        error('The size of step must be positive less than or equal to the range to be plotted. Terminate.')
    elseif lim(1) > lim(2)
        error('Y limit is invalid. Terminate.')
    end
    
    % Turning off all warnings.
    warning('off', 'all')
    
    % Report.
    fprintf('%s\n', f_title('PLOTTING PROCEDURE'))
    fprintf('  @range : [%.3g, %.3g]\n', from, to)
    fprintf('  @ylim  : [%.3g, %.3g]\n', lim(1), lim(2))
    fprintf('  @step  : %.3g\n\n', step)
    
    % Compute plotting points.
    fprintf('%s\n', f_title('START PLOTTING'))
    fprintf('  Computing points....[%06.2f%%', 0)
    tic
    
    tmp = from:step:to;
    part = length(x_asymp) + 1;
    x = cell(1,part);
    y = cell(1,part);

    if part == 1
        x{1} = tmp;
        prog_update(1, 2)
        
        y{1} = f(x{1});
        prog_update(2, 2)
    else
        x{1} = tmp(tmp < x_asymp(1));
        prog_update(1, 2 * part)
        
        for i = 2:(part - 1)
            x{i} = tmp(tmp > x_asymp(i - 1) & tmp < x_asymp(i));
            prog_update(i, 2 * part)
        end
        
        x{end} = tmp(tmp > x_asymp(end));
        prog_update(part, 2 * part)
        
        for i = 1:part
            y{i} = f(x{i});
            prog_update(part + i, 2 * part)
        end
    end
    
    col = hex2rgb('#f8766d');
    col_light = hex2rgb('#faa49e');
    col_gray = [0.7 0.7 0.7];

    % Plot.
    fprintf(']\n  Plotting............[%06.2f%%', 0)
    fig = figure;
    set(fig, 'Position', [802 428 419 350])
    hold on
    grid on

    plot([from to], [0 0], '-k')
    
    for i = 1:part
        plot(x{i}, y{i}, 'Linewidth', 1.5, 'Color', col)
        patch([x{i} fliplr(x{i})], [y{i} zeros(1, length(x{i}))], col_light, 'FaceAlpha', 0.5, 'LineStyle', 'none')
    end
    
    fig.Children.YLim = [max(fig.Children.YLim(1), lim(1)) min(fig.Children.YLim(2), lim(2))];
    
    for i = 1:length(x_asymp)
        if x_asymp(i) ~= from && x_asymp(i) ~= to
            plot([x_asymp(i) x_asymp(i)], fig.Children.YLim, '--', 'Linewidth', 1.5, 'Color', col_gray)
        end
    end
   
    for i = 1:length(y_asymp)
        plot([from to], [y_asymp(i) y_asymp(i)], '--', 'Linewidth', 1.5, 'Color', col_gray)
    end
    
    for i = 1:size(mark_in, 1)
        plot(mark_in(i,1), mark_in(i,2), 'Marker', 'o', 'MarkerEdgeColor', col, 'MarkerFaceColor', col)
    end
    
    for i = 1:size(mark_out, 1)
        plot(mark_out(i,1), mark_out(i,2), 'Marker', 'o', 'MarkerEdgeColor', col, 'MarkerFaceColor', 'w')
    end

    hold off
    title(main, 'FontWeight', 'bold')
    xlabel('x')
    ylabel(ylab)
    xlim([from to])
    prog_update(1, 1)
    
    elapsed = toc;
    fprintf(']\n\n')
    
    % Report.
    fprintf('%s\n', f_title('PLOTTING FINISHED'))
    fprintf('  @elapsed: %.02fms\n\n', elapsed * 1000)
    
    % Turning on all warnings.
    warning('on', 'all')
end