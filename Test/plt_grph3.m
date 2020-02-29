function fig = plt_grph3(f, from, to, main, ylab, level, margin, lim, x_asymp, y_asymp, mark_in, mark_out, step)
% PLT_GRPH3 plots the graph of bivariate function.
%
% PLT_GRPH3(F, FROM, TO, MAIN, YLAB, LEVEL, MARGIN, LIM, X_ASYMP, Y_ASYMP,
% MARK_IN, MARK_OUT, SETP) plots following graphs of bivariate function F
% on range [FROM, TO].
%   - Contour plot where LEVEL is the # of contours
%   - Density plot where LEVEL is the # of contours
%   - Marginal plot where MARGIN specifies x and y cutting potins and YLAB
%     is the label of z axis
% The sample points for plotting will be drawn uniformly with step size
% STEP and the title of the plot will be MAIN. Additionally, it draws
% asymptotic lines X_ASYMP and Y_ASYMP with inclusive markers MARK_IN and
% exclusive markers MARK_OUT at marginal plots.
%
% Inputs:
%   F      - Function to be plotted.
%   FROM   - Starting point of plotting range.
%   TO     - Ending point of plotting range.
%   MAIN   - The title of the plot.
%   YLAB   - The label of y axis of marginal plot.
%   LEVEL  - The # of contours to be plotted.
%   MARGIN - The # of marginal lines in one marginal plots.
%
% Optional inputs:
%   LIM      - Limit of function values. (default = [-inf inf])
%   X_ASYMP  - Points for asymptotic lines in x marginal plot.
%              (default = [])
%   Y_ASYMP  - Points for asymptotic lines in y marginal plot.
%              (default = [])
%   MARK_IN  - Coordinates for inclusive markers. (default = {[], []})
%   MARK_OUT - Coordinates for exclusive markers. (default = {[], []})
%   STEP     - Step size for sample points. (default = [0.01 0.01])
%
% Outputs:
%   FIG - Figure handle of the plot.
%
% Notes:
%   - Elements of X_ASYMP and Y_ASYMP must be sorted.
%   - Elements of X_ASYMP and Y_ASYMP which coincides with FROM or TO will
%     be ignored.

    % Argument validation.
    if nargin == 7
        lim = [-inf inf];
        x_asymp = [];
        y_asymp = [];
        mark_in = {[], []};
        mark_out = {[], []};
        step = [0.01 0.01];
    elseif nargin == 8
        x_asymp = [];
        y_asymp = [];
        mark_in = {[], []};
        mark_out = {[], []};
        step = [0.01 0.01];
    elseif nargin == 9
        y_asymp = [];
        mark_in = {[], []};
        mark_out = {[], []};
        step = [0.01 0.01];
    elseif nargin == 10
        mark_in = {[], []};
        mark_out = {[], []};
        step = [0.01 0.01];
    elseif nargin == 11
        mark_out = {[], []};
        step = [0.01 0.01];
    elseif nargin == 10
        step = [0.01 0.01];
    elseif nargin ~= 11
        error('Some arguments are missing. Terminate.')
    end
    
    if any(from >= to)
        error('Plotting range is invalid. Terminate.')
    elseif any(step <= 0) || any(step > (to - from))
        error('The size of step must be positive less than or equal to the range to be plotted. Terminate.')
    elseif lim(1) > lim(2)
        error('Axis limit is invalid. Terminate.')
    elseif level <= 0 || mod(level, 1) ~= 0
        error('The # of contours must be positive integer. Terminate.')
    end
    
    % Report.
    fprintf('%s\n', f_title('PLOTTING PROCEDURE'))
    fprintf('  @range : [%.3g, %.3g]*[%.3g, %.3g]\n', from(1), to(1), from(2), to(2))
    fprintf('  @level : %d\n', level)
    fprintf('  @zlim  : [%.3g, %.3g]\n', lim(1), lim(2)) 
    fprintf('  @step  : [%.3g, %.3g]\n\n', step(1), step(2))
    
    % Compute plotting points.
    fprintf('%s\n', f_title('START PLOTTING'))
    fprintf('  Computing points....[%06.2f%%', 0)
    tic
    
    part_x = length(x_asymp) + 1;
    part_y = length(y_asymp) + 1;
        
    % Contour/surface plot.
    [x, y] = meshgrid(from(1):step(1):to(1), from(2):step(2):to(2));
    prog_update(1, 2 * (part_x + part_y + 1))
    
    z = f(x, y);
    z(z < lim(1)) = lim(1);
    z(z > lim(2)) = lim(2);
    prog_update(2, 2 * (part_x + part_y + 1))
    
    % Marginal plot for x.
    [tmp_x, tmp_y] = meshgrid(from(1):step(1):to(1), margin(2,:));
    x_y = cell(1, part_x);
    y_y = cell(1, part_x);
    z_y = cell(1, part_x);
    
    if part_x == 1
       	x_y{1} = tmp_x;
        y_y{1} = tmp_y;
        prog_update(3, 2 * (part_x + part_y + 1))
        
        z_y{1} = f(x_y{1}, y_y{1});
        prog_update(4, 2 * (part_x + part_y + 1))
    else
        msk = tmp_x(1,:) < x_asymp(1);
        x_y{1} = tmp_x(:,msk);
        y_y{1} = tmp_y(:,msk);
        prog_update(3, 2 * (part_x + part_y + 1))
        
        for i = 2:(part_x - 1)
            msk = tmp_x(1,:) > x_asymp(i - 1) & tmp_x(1,:) < x_asymp(i);
            x_y{i} = tmp_x(:,msk);
            y_y{i} = tmp_y(:,msk);
            prog_update(2 + i, 2 * (part_x + part_y + 1))
        end
        
        msk = tmp_x(1,:) > x_asymp(end);
        x_y{end} = tmp_x(:,msk);
        y_y{end} = tmp_y(:,msk);
        prog_update(part_x + 2, 2 * (part_x + part_y + 1))
        
        for i = 1:part_x
            z_y{i} = f(x_y{i}, y_y{i});
            prog_update(part_x + 2 + i, 2 * (part_x + part_y + 1))
        end
    end
    
    leg_y = cell(1, length(margin(2,:)));
    
    for i = 1:length(margin(2,:))
        leg_y{i} = sprintf('y=%.3g', margin(2,i));
    end
    
    % Marginal plot for y.
    [tmp_x, tmp_y] = meshgrid(margin(1,:), from(2):step(2):to(2));
    x_x = cell(1, part_y);
    y_x = cell(1, part_y);
    z_x = cell(1, part_y);
    
    if part_y == 1
       	x_x{1} = tmp_x;
        y_x{1} = tmp_y;
        prog_update(2 * part_x + 3, 2 * (part_x + part_y + 1))
        
        z_x{1} = f(x_x{1}, y_x{1});
        prog_update(2 * part_x + 4, 2 * (part_x + part_y + 1))
    else
        msk = tmp_y(:,1) < y_asymp(1);
        x_x{1} = tmp_x(msk,:);
        y_x{1} = tmp_y(msk,:);
        prog_update(2 * part_x + 3, 2 * (part_x + part_y + 1))
        
        for i = 2:(part_y - 1)
            msk = tmp_y(:,1) > y_asymp(i - 1) & tmp_y(:,1) < y_asymp(i);
            x_x{i} = tmp_x(msk,:);
            y_x{i} = tmp_y(msk,:);
            prog_update(2 * part_x + 2 + i, 2 * (part_x + part_y + 1))
        end
        
        msk = tmp_y(:,1) > y_asymp(end);
        x_x{end} = tmp_x(msk,:);
        y_x{end} = tmp_y(msk,:);
        prog_update(2 * part_x + part_y + 2, 2 * (part_x + part_y + 1))
        
        for i = 1:part_y
            z_x{i} = f(x_x{i}, y_x{i});
            prog_update(2 * (part_x + part_y + 1), 2 * (part_x + part_y + 1))
        end
    end

    leg_x = cell(1, length(margin(1,:)));
    
    for i = 1:length(margin(1,:))
        leg_x{i} = sprintf('x=%.3g', margin(1,i));
    end
    
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
    colmap = cust_colmap();
    col_gray = [0.7 0.7 0.7];

    % Plot.
    fprintf(']\n  Plotting............[%06.2f%%', 0)
    fig = figure;
    set(fig, 'Position', [432 164 946 791])
    sgtitle(main, 'FontWeight', 'bold', 'FontSize', 15)    

    % Contour plot.
    sub1 = subplot(2, 2, 1);
    contour(x, y, z, level, 'Linewidth', 1.5);
    sub1.Colormap = colmap;
    title('Contour plot', 'FontWeight', 'bold')
    xlabel('x')
    ylabel('y')
    colorbar
    prog_update(1, 4)

    % Surface plot.
    sub2 = subplot(2, 2, 2);
    hold on

    surf(x, y, z, 'EdgeColor', 'none')
    contour3(x, y, z, level, 'LineColor', [0.7 0.7 0.7])

    hold off
    sub2.Colormap = colmap;
    sub2.View = [0 90];
    title('Density plot', 'FontWeight', 'bold')
    xlabel('x')
    ylabel('y')
    colorbar
    fig.Children(3).Limits = lim;
    prog_update(2, 4)
    
    % Marginal plot for x
    subplot(2, 2, 3)
    hold on
    grid on
    
    plot([from(1) to(1)], [0 0], '-k')
    
    for i = 1:part_x
        target_x = x_y{i};
        target_z = z_y{i};
        
        for j = 1:size(target_x, 1)
            patch([target_x(j,:) fliplr(target_x(j,:))], [target_z(j,:) zeros(1, length(target_x(j,:)))], col_fill(mod(j, size(col_fill, 1)) + 1,:), 'FaceAlpha', 0.5, 'LineStyle', 'none')
        end
    end
    
    for i = 1:part_x
        plt = plot(x_y{i}', z_y{i}', 'Linewidth', 1.5);
        
        for j = 1:length(plt)
            plt(j).Color = col_line(mod(j, size(col_line, 1)) + 1,:);
        end
    end
    
    fig.Children(1).YLim = [max(fig.Children(1).YLim(1), lim(1)) min(fig.Children(1).YLim(2), lim(2))];
    
    for i = 1:length(x_asymp)
        if x_asymp(i) ~= from(1) && x_asymp(i) ~= to(1)
            plot([x_asymp(i) x_asymp(i)], fig.Children(1).YLim, '--', 'Linewidth', 1.5, 'Color', col_gray)
        end
    end
   
    mark_in_y = mark_in{1};
    mark_out_y = mark_out{1};
    
    for i = 1:size(mark_in_y, 1)
        plot(mark_in_y(i,1), mark_in_y(i,2), 'Marker', 'o', 'MarkerEdgeColor', col, 'MarkerFaceColor', col)
    end
    
    for i = 1:size(mark_out_y, 1)
        plot(mark_out_y(i,1), mark_out_y(i,2), 'Marker', 'o', 'MarkerEdgeColor', col, 'MarkerFaceColor', 'w')
    end
    
    hold off
    xlim([from(1) to(1)])
    legend(plt, leg_y)
    title('Marginal plot of x', 'FontWeight', 'bold')
    xlabel('x')
    ylabel(ylab)
    prog_update(3, 4)
    
    % Marginal plot for y
    subplot(2, 2, 4)
    hold on
    grid on
    
    plot([from(2) to(2)], [0 0], '-k')
    
    for i = 1:part_y
        target_y = y_x{i};
        target_z = z_x{i};
        
        for j = 1:size(target_y, 2)
            patch([target_y(:,j)' fliplr(target_y(:,j)')], [target_z(:,j)' zeros(1, length(target_y(:,j)))], col_fill(mod(j, size(col_fill, 1)) + 1,:), 'FaceAlpha', 0.5, 'LineStyle', 'none')
        end
    end
    
    for i = 1:part_y
        plt = plot(y_x{i}, z_x{i}, 'Linewidth', 1.5);
        
        for j = 1:length(plt)
            plt(j).Color = col_line(mod(j, size(col_line, 1)) + 1,:);
        end
    end
    
    fig.Children(1).YLim = [max(fig.Children(1).YLim(1), lim(1)) min(fig.Children(1).YLim(2), lim(2))];
    
    for i = 1:length(y_asymp)
        if y_asymp(i) ~= from(2) && y_asymp(i) ~= to(2)
            plot([y_asymp(i) y_asymp(i)], fig.Children(1).YLim, '--', 'Linewidth', 1.5, 'Color', col_gray)
        end
    end
   
    mark_in_y = mark_in{2};
    mark_out_y = mark_out{2};
    
    for i = 1:size(mark_in_y, 1)
        plot(mark_in_y(i,1), mark_in_y(i,2), 'Marker', 'o', 'MarkerEdgeColor', col, 'MarkerFaceColor', col)
    end
    
    for i = 1:size(mark_out_y, 1)
        plot(mark_out_y(i,1), mark_out_y(i,2), 'Marker', 'o', 'MarkerEdgeColor', col, 'MarkerFaceColor', 'w')
    end
    
    hold off
    xlim([from(2) to(2)])
    legend(plt, leg_x)
    title('Marginal plot of y', 'FontWeight', 'bold')
    xlabel('y')
    ylabel(ylab)
    prog_update(4, 4)
    
    elapsed = toc;
    fprintf(']\n\n')

    % Report.
    fprintf('%s\n', f_title('PLOTTING FINISHED'))
    fprintf('  @elapsed: %.02fms\n\n', elapsed * 1000)
end