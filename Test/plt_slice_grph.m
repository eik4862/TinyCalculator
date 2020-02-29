function fig = plt_slice_grph(f, from, to, main, ylab, slice_pt, lim, x_asymp, y_asymp, step)
    if nargin == 6
        lim = [-inf inf];
        x_asymp = [];
        y_asymp = [];
        step = 0.01;
    elseif nargin == 7
        x_asymp = [];
        y_asymp = [];
        step = 0.01;
    elseif nargin == 8
        y_asymp = [];
        step = 0.01;
    elseif nargin == 9
        step = 0.01;
    elseif nargin ~= 10
        error('Some arguments are missing. Terminate.')
    end

    if from >= to
        error('Plotting range is invalid. Terminate.')
    elseif step <= 0 || step > (to - from)
        error('The size of step must be positive less than or equal to the range to be plotted. Terminate.')
    elseif lim(1) > lim(2)
        error('Y limit is invalid. Terminate.')
    elseif isempty(slice_pt)
        error('There must be at least one slice point. Terminate.')
    end
    
    warning('off', 'all')
    
    fprintf('%s\n', f_title('PLOTTING PROCEDURE'))
    fprintf('  @range : [%.3g, %.3g]\n', from, to)
    fprintf('  @ylim  : [%.3g, %.3g]\n', lim(1), lim(2))
    fprintf('  @slice : %d\n', length(slice_pt))
    fprintf('  @step  : %.3g\n\n', step)
    
    fprintf('%s\n', f_title('START PLOTTING'))
    fprintf('  Computing points....[%06.2f%%', 0)
    tic
    
    tmp = from:step:to;
    part = length(x_asymp) + 1;
    leg = cell(1, length(slice_pt));
    
    for i = 1:length(slice_pt)
        leg{i} = sprintf('n=%.3g', slice_pt(i));
    end
    
    x = cell(1,part);
    y = cell(1,part);
    slice = cell(1,part);
    col_line = [hex2rgb('#ff4cc7');
                hex2rgb('#d296ff');
                hex2rgb('#f8766d');
                hex2rgb('#7cae00');
                hex2rgb('#529bff');
                hex2rgb('#eb63ff')];
    col_fill = [hex2rgb('#ffc2ec');
                hex2rgb('#e8c9ff');
                hex2rgb('#faa49e');
                hex2rgb('#dafa8c');
                hex2rgb('#cfe1ff');
                hex2rgb('#f8c5ff')];
    col_gray = [0.7 0.7 0.7];

    if part == 1
        [x{1}, slice{1}] = meshgrid(tmp, slice_pt);
        prog_update(1, 2)
        
        y{1} = f(x{1}, slice{1});
        prog_update(2, 2)
    else
        [x{1}, slice{1}] = meshgrid(tmp(tmp < x_asymp(1)), slice_pt);
        prog_update(1, 2 * part)
        
        for i = 2:(part - 1)
            [x{i}, slice{i}] = meshgrid(tmp(tmp > x_asymp(i - 1) & tmp < x_asymp(i)), slice_pt);
            prog_update(i, 2 * part)
        end
        
        [x{end}, slice{end}] = meshgrid(tmp(tmp > x_asymp(end)), slice_pt);
        prog_update(part, 2 * part)
        
        for i = 1:part
            y{i} = f(x{i}, slice{i});
            prog_update(part + i, 2 * part)
        end
    end
    
    fprintf(']\n  Plotting............[%06.2f%%', 0)
    fig = figure;
    set(fig, 'Position', [802 428 419 350])
    hold on
    grid on
    
    plot([from to], [0 0], '-k')
    
    for i = 1:part
        for j = 1:length(slice_pt)
            patch([x{i}(j,:) fliplr(x{i}(j,:))], [y{i}(j,:) zeros(1, length(x{i}(j,:)))], col_fill(mod(j, size(col_fill, 1)) + 1,:), 'FaceAlpha', 0.5, 'LineStyle', 'none')
        end
    end
    
    for i = 1:part
        plt = plot(x{i}', y{i}', 'Linewidth', 1.5);
        
        for j = 1:length(slice_pt)
            plt(j).Color = col_line(mod(j, size(col_line, 1)) + 1,:);
        end
    end
    
    for i = 1:length(x_asymp)
        if x_asymp(i) ~= from && x_asymp(i) ~= to
            plot([x_asymp(i) x_asymp(i)], fig.Children.YLim, '--', 'Linewidth', 1.5, 'Color', col_gray)
        end
    end
   
    for i = 1:length(y_asymp)
        plot([from to], [y_asymp(i) y_asymp(i)], '--', 'Linewidth', 1.5, 'Color', col_gray)
    end
    
    hold off
    title(main, 'FontWeight', 'bold')
    xlabel('x')
    ylabel(ylab)
    xlim([from to])
    legend(plt, leg)
    prog_update(1, 1)
    
    elapsed = toc;
    fprintf(']\n\n')
    
    % Report.
    fprintf('%s\n', f_title('PLOTTING FINISHED'))
    fprintf('  @elapsed: %.02fms\n\n', elapsed * 1000)
    
    % Turning on all warnings.
    warning('on', 'all')
end