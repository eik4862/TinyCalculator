function plt_err(in_file, ref_file, out_file, size, main)
% PLT_ERR processes test output and plots the result.
% 
% PLT_ERR(IN, REF, OUT, SIZE) processes and plots test result using
% test input IN, test reference output REF and test output OUT where SIZE
% is the # of test outputs.
%
% PLT_ERR(IN, REF, OUT, SIZE, TITLE) processes and plots test result using
% test input IN, test reference output REF and test output OUT where SIZE
% is the # of test outputs and TITLE is the title of plots.
% 
% Inputs:
%   IN   - Test input file.
%   REF  - Test reference output file.
%   OUT  - Test output file.
%   SIZE - The # of test outputs.
%
% Optional inputs:
%   TITLE - The title of plot. (default = 'Error analysis report')
%   
% Notes:
%   - Since it does not close those files after reading them, one must
%     close them manually.

    % Argument validation.
    if nargin == 4
        main = 'Error analysis report';
    elseif nargin ~= 5
        error('Some arguments are missing. Terminate.')
    end
    
    if size < 0 || mod(size, 1) ~= 0
        error('The # of test outputs must be positive integer. Terminate.')
    end

    in.path = fopen(in_file);
    ref.path = fopen(ref_file);
    out.path = fopen(out_file);
    tmp = dir(in.path);
    in.bytes = tmp.bytes;
    tmp = dir(ref.path);
    ref.bytes = tmp.bytes;
    tmp = dir(out.path);
    out.bytes = tmp.bytes;
    
    % Report.
    fprintf('%s\n', f_title('TEST DATA PROCESSOR'))
    fprintf('  @in  : %s (%dbytes)\n', in.path, in.bytes)
    fprintf('  @ref : %s (%dbytes)\n', ref.path, ref.bytes)
    fprintf('  @out : %s (%dbytes)\n', out.path, out.bytes)
    fprintf('  @size: %d\n\n', size)
      
    % Read files
    fprintf('%s\n', f_title('START PROCESSING'))
    fprintf('  Reading files.......[%06.2f%%', 0)
    tic
    
    in.data = sym(nan([size 1]));
    ref = sym(nan([size 1]));
    out = sym(nan([size 1]));
    
    for i = 1:size
        in.data(i) = sym(fgetl(in_file));
        ref(i) = sym(fgetl(ref_file));
        out(i) = sym(fgetl(out_file));
        prog_update(i, size)
    end    
    
    % Compute abs/rel errors and stats.
    fprintf(']\n  Computing stats.....[%06.2f%%', 0)
    
    in.moving = smooth(double(in.data), 0.1, 'moving');
    prog_update(1, 39)
    in.loess = smooth(double(in.data), 0.1, 'loess');
    prog_update(2, 39)
    in.linear = polyval(double(polyfit(1:length(in.data), in.data', 1)), 1:length(in.data));
    prog_update(3, 39)
    in.mu = mean(in.data);
    prog_update(4, 39)
    in.sigma = std(in.data);
    prog_update(5, 39)
    in.band = [in.mu - in.sigma in.mu + in.sigma];
    prog_update(6, 39)
    in.pdf = fitdist(double(in.data), 'Kernel', 'Kernel', 'epanechnikov');
    prog_update(7, 39)
    in.col_deepdark = [0.3373 0 0.5882];	% #560096
    prog_update(8, 39)
    in.col_dark = [0.7373 0.3882 1];        % #bc63ff
    prog_update(9, 39)
    in.col = [0.8235 0.5882 1];             % #d296ff
    prog_update(10, 39)
    in.col_light = [0.9098 0.7882 1];       % #e8c9ff
    prog_update(11, 39)
    in.xlim = [1 size];
    prog_update(12, 39)

    tmp = sortrows([in.data abs(ref - out)]);
    abs_err.in = tmp(:,1);
    prog_update(13, 39)
    abs_err.data = tmp(:,2);
    prog_update(14, 39)
    abs_err.moving = smooth(abs_err.in, double(abs_err.data), 0.1, 'moving');
    prog_update(15, 39)
    abs_err.loess = smooth(abs_err.in, double(abs_err.data), 0.1, 'loess');
    prog_update(16, 39)
    abs_err.linear = polyval(double(polyfit(abs_err.in, abs_err.data, 1)), double(abs_err.in));
    prog_update(17, 39)
    abs_err.mu = mean(abs_err.data);
    prog_update(18, 39)
    abs_err.sigma = std(abs_err.data);
    prog_update(19, 39)
    abs_err.band = [abs_err.mu - abs_err.sigma abs_err.mu + abs_err.sigma];
    prog_update(20, 39)
    abs_err.pdf = fitdist(double(abs_err.data), 'Kernel', 'Kernel', 'epanechnikov');
    prog_update(21, 39)
    abs_err.col = [0.9725 0.4627 0.4275];           % #f8766d
    prog_update(22, 39)
    abs_err.col_deepdark = [0.6 0.0667 0.0275];     % #991107
    prog_update(23, 39)
    abs_err.col_dark = [0.9686 0.3725 0.3333];      % #f75f55
    prog_update(24, 39)
    abs_err.col_light = [0.9804 0.6431 0.6196];     % #faa49e
    prog_update(25, 39)
    abs_err.xlim = double([min(in.data) max(in.data)]);
    prog_update(26, 39)

    tmp = [in.data out ./ ref - 1];
    tmp = sortrows(tmp(isfinite(tmp(:,2)),:));
    rel_err.in = tmp(:,1);
    prog_update(27, 39)
    rel_err.data = tmp(:,2);
    prog_update(28, 39)
    rel_err.moving = smooth(rel_err.in, double(rel_err.data), 0.1, 'moving');
    prog_update(29, 39)
    rel_err.loess = smooth(rel_err.in, double(rel_err.data), 0.1, 'loess');
    prog_update(30, 39)
    rel_err.linear = polyval(double(polyfit(rel_err.in, rel_err.data, 1)), double(rel_err.in));
    prog_update(31, 39)
    rel_err.mu = mean(rel_err.data);
    prog_update(32, 39)
    rel_err.sigma = std(rel_err.data);
    prog_update(33, 39)
    rel_err.band = [rel_err.mu - rel_err.sigma rel_err.mu + rel_err.sigma];
    prog_update(34, 39)
    rel_err.pdf = fitdist(double(rel_err.data), 'Kernel', 'Kernel', 'epanechnikov');
    prog_update(35, 39)
    rel_err.col = [0.4873 0.6824 0];            % #7cae00
    prog_update(36, 39)
    rel_err.col_deepdark = [0.3216 0.451 0];    % #527300
    prog_update(37, 39)
    rel_err.col_light = [0.8549 0.9804 0.549];  % #dafa8c
    prog_update(38, 39)
    rel_err.xlim = abs_err.xlim;
    prog_update(39, 39)

    % Plot.
    fprintf(']\n  Plotting............')
    fig = figure;
    set(fig, 'Position', [400 58 1133 907])
    sgtitle(main, 'FontWeight', 'bold', 'FontSize', 15)    
    fprintf('[%06.2f%%', 0)
    
    % Trend of test input.
    sub_1 = subplot(3,10,1:3);
    hold on
    
    plt_lin = plot(in.linear, 'Linewidth', 1.5, 'Color', in.col_deepdark);
    plt_loess = plot(in.loess, 'Linewidth', 1.5, 'Color', in.col_dark);
    plt_mov = plot(in.moving, 'Linewidth', 1.5, 'Color', in.col_light);

    hold off
    legend([plt_lin, plt_loess, plt_mov], {'linear', 'LOESS', 'moving ave.'})
    title('Trend of test input', 'FontWeight', 'bold')
    ylabel('input')
    xlabel('count')
    xlim(in.xlim)
    prog_update(1, 12)
    
    % Box plot of test input.
    sub_2 = subplot(3,10,4);
    boxplot(double(in.data), 'Labels', 'input')
    sub_2.XLim = [0.8, 1.2];
    sub_2.Children.Children(1).Marker = 'o';
    sub_2.Children.Children(1).MarkerFaceColor = in.col;
    sub_2.Children.Children(1).MarkerEdgeColor = 'none';
    sub_2.Children.Children(2).Color = in.col_deepdark;
    sub_2.Children.Children(2).LineWidth = 1.5;
    
    for i = 3:7
        sub_2.Children.Children(i).Color = in.col;
        sub_2.Children.Children(i).LineWidth = 1.5;
    end
    
    prog_update(2, 12)
    
    % Scatter of test input.
    sub_3 = subplot(3,10,5:7);
    hold on
    
    plt_data = plot(in.data, 'o', 'LineStyle', 'none', 'MarkerEdgeColor','none', 'MarkerFaceColor', in.col);
    plt_mu = plot([1 length(in.data)], [in.mu in.mu], '--', 'Linewidth', 1.5, 'Color', in.col_deepdark);
    patch([in.xlim fliplr(in.xlim)], double([in.band(1) in.band(1) in.band(2) in.band(2)]), in.col_light, 'FaceAlpha', 0.5, 'LineStyle', 'none');
    
    hold off
    legend([plt_data, plt_mu], {'input', 'mean with one sd band'})
    title(sprintf('Test input (size: %d)', length(in.data)), 'FontWeight', 'bold')
    xlabel('count')
    xlim(in.xlim)
    in.ylim = sub_3.YLim;
    prog_update(3, 12)
    
    % Dist of test input.
    sub_4 = subplot(3,10,8:10);
    hold on
    
    hist = histogram(double(in.data), 10, 'FaceColor', in.col, 'Normalization', 'probability');
    x = sub_4.XLim(1):0.01:sub_4.XLim(2);
    y = pdf(in.pdf, x);
    y = y / max(y) * (sub_4.YLim(2) * 0.9);
    plt_pdf = plot(x, y, 'Linewidth', 1.5, 'Color', in.col_deepdark);
    patch([x fliplr(x)], [y zeros(1, length(x))], in.col_light, 'FaceAlpha', 0.5, 'LineStyle', 'none')
    
    for i = 1:hist.NumBins
        txt = text((hist.BinEdges(i) + hist.BinEdges(i + 1)) / 2, sub_4.YLim(2) * 0.035 + hist.Values(i), num2str(hist.BinCounts(i)));
        txt.HorizontalAlignment = 'center';
    end
    
    hold off
    legend([hist, plt_pdf], {'input', 'fitted dist. (scaled)'}, 'Location', 'southeast')
    title('Distribution of test input', 'FontWeight', 'bold')
    xlabel('input')
    ylabel('probability')
    ylim([0 sub_4.YLim(2) * 1.1])
    hist.Parent.YAxisLocation = 'right';
    
    sub_1.YLim = in.ylim;
    sub_2.YLim = in.ylim;
    prog_update(4, 12)
    
    % Trend of abs err.
    sub_1 = subplot(3,10,11:13);
    hold on
    
    plt_lin = plot(abs_err.in, abs_err.linear, 'Linewidth', 1.5, 'Color', abs_err.col_deepdark);
    plt_loess = plot(abs_err.in, abs_err.loess, 'Linewidth', 1.5, 'Color', abs_err.col_dark);
    plt_mov = plot(abs_err.in, abs_err.moving, 'Linewidth', 1.5, 'Color', abs_err.col_light);

    hold off
    legend([plt_lin, plt_loess, plt_mov], {'linear', 'LOESS', 'moving ave.'})
    title('Trend of absolute error', 'FontWeight', 'bold')
    ylabel('absolute error')
    xlabel('input')
    xlim(abs_err.xlim)
    prog_update(5, 12)
    
    % Box plot of abs err.
    sub_2 = subplot(3,10,14);
    boxplot(double(abs_err.data), 'Labels', 'abs. err.')
    sub_2.XLim = [0.8, 1.2];
    sub_2.Children.Children(1).Marker = 'o';
    sub_2.Children.Children(1).MarkerFaceColor = abs_err.col;
    sub_2.Children.Children(1).MarkerEdgeColor = 'none';
    sub_2.Children.Children(2).Color = abs_err.col_deepdark;
    sub_2.Children.Children(2).LineWidth = 1.5;
    
    for i = 3:7
        sub_2.Children.Children(i).Color = abs_err.col;
        sub_2.Children.Children(i).LineWidth = 1.5;
    end
    
    prog_update(6, 12)
    
    % Scatter of abs err.
    sub_3 = subplot(3,10,15:17);
    hold on
    
    plt_data = plot(abs_err.in, abs_err.data, 'o', 'LineStyle', 'none', 'MarkerEdgeColor','none', 'MarkerFaceColor', abs_err.col);
    plt_mu = plot(abs_err.xlim, [abs_err.mu abs_err.mu], '--', 'Linewidth', 1.5, 'Color', abs_err.col_deepdark);
    patch(double([abs_err.xlim fliplr(abs_err.xlim)]), double([abs_err.band(1) abs_err.band(1) abs_err.band(2) abs_err.band(2)]), abs_err.col_light, 'FaceAlpha', 0.5, 'LineStyle', 'none')
    
    hold off
    legend([plt_data, plt_mu], {'obs.', 'mean with one sd band'})
    title(sprintf('Absolute error (mean: %.02e)', abs_err.mu), 'FontWeight', 'bold')
    xlabel('input')
    xlim(abs_err.xlim)
    abs_err.ylim = sub_3.YLim;
    prog_update(7, 12)
    
    % Dist of abs err.
    sub_4 = subplot(3,10,18:20);
    hold on
    
    hist = histogram(double(abs_err.data * sym(1e16)), 10, 'FaceColor', abs_err.col, 'Normalization', 'probability');
    x = sub_4.XLim(1):0.01:sub_4.XLim(2);
    y = pdf(abs_err.pdf, x * 1e-16);
    y = y / max(y) * (sub_4.YLim(2) * 0.9);
    plt_pdf = plot(x, y, 'Linewidth', 1.5, 'Color', abs_err.col_deepdark);
    patch([x fliplr(x)], [y zeros(1, length(x))], abs_err.col_light, 'FaceAlpha', 0.5, 'LineStyle', 'none')
    
    for i = 1:hist.NumBins
        txt = text((hist.BinEdges(i) + hist.BinEdges(i + 1)) / 2, sub_4.YLim(2) * 0.035 + hist.Values(i), num2str(hist.BinCounts(i)));
        txt.HorizontalAlignment = 'center';
    end
    
    hold off
    legend([hist, plt_pdf], {'obs.', 'fitted dist. (scaled)'})
    title('Distribution of absolute error', 'FontWeight', 'bold')
    xlabel('absolute error (\times10^{16})')
    ylabel('probability')
    ylim([0 sub_4.YLim(2) * 1.1])
    hist.Parent.YAxisLocation = 'right';
    
    sub_1.YLim = abs_err.ylim;
    sub_2.YLim = abs_err.ylim;
    prog_update(8, 12)
    
    % Trend of rel err.
    sub_1 = subplot(3,10,21:23);
    hold on
    
    plt_lin = plot(rel_err.in, rel_err.linear, 'Linewidth', 1.5, 'Color', rel_err.col_deepdark);
    plt_loess = plot(rel_err.in, rel_err.loess, 'Linewidth', 1.5, 'Color', rel_err.col);
    plt_mov = plot(rel_err.in, rel_err.moving, 'Linewidth', 1.5, 'Color', rel_err.col_light);

    hold off
    legend([plt_lin, plt_loess, plt_mov], {'linear', 'LOESS', 'moving ave.'})
    title('Trend of relative error', 'FontWeight', 'bold')
    ylabel('relative error')
    xlabel('input')
    xlim(rel_err.xlim)
    prog_update(9, 12)
    
    % Box plot of rel err.
    sub_2 = subplot(3,10,24);
    boxplot(double(rel_err.data), 'Labels', 'rel. err.')
    sub_2.XLim = [0.8, 1.2];
    sub_2.Children.Children(1).Marker = 'o';
    sub_2.Children.Children(1).MarkerFaceColor = rel_err.col;
    sub_2.Children.Children(1).MarkerEdgeColor = 'none';
    sub_2.Children.Children(2).Color = rel_err.col_deepdark;
    sub_2.Children.Children(2).LineWidth = 1.5;
    
    for i = 3:7
        sub_2.Children.Children(i).Color = rel_err.col;
        sub_2.Children.Children(i).LineWidth = 1.5;
    end

    prog_update(10, 12)
    
    % Scatter of rel err.
    sub_3 = subplot(3,10,25:27);
    hold on
    
    plt_data = plot(rel_err.in, rel_err.data, 'o', 'LineStyle', 'none', 'MarkerEdgeColor','none', 'MarkerFaceColor', rel_err.col);
    plt_mu = plot(rel_err.xlim, [rel_err.mu rel_err.mu], '--', 'Linewidth', 1.5, 'Color', rel_err.col_deepdark);
    patch(double([rel_err.xlim fliplr(rel_err.xlim)]), double([rel_err.band(1) rel_err.band(1) rel_err.band(2) rel_err.band(2)]), rel_err.col_light, 'FaceAlpha', 0.5, 'LineStyle', 'none')
    
    hold off
    legend([plt_data, plt_mu], {'obs.', 'mean with one sd band'})
    title(sprintf('Relative error (mean: %.02e)', rel_err.mu), 'FontWeight', 'bold')
    xlabel('input')
    xlim(rel_err.xlim)
    rel_err.ylim = sub_3.YLim;
    prog_update(11, 12)
        
    % Dist of rel err.
    sub_4 = subplot(3,10,28:30);
    hold on
    
    hist = histogram(double(rel_err.data * sym(1e16)), 10, 'FaceColor', rel_err.col, 'Normalization', 'probability');
    x = sub_4.XLim(1):0.01:sub_4.XLim(2);
    y = pdf(rel_err.pdf, x * 1e-16);
    y = y / max(y) * (sub_4.YLim(2) * 0.9);
    plt_pdf = plot(x, y, 'Linewidth', 1.5, 'Color', rel_err.col_deepdark);
    patch([x fliplr(x)], [y zeros(1, length(x))], rel_err.col_light, 'FaceAlpha', 0.5, 'LineStyle', 'none')
    
    for i = 1:hist.NumBins
        txt = text((hist.BinEdges(i) + hist.BinEdges(i + 1)) / 2, sub_4.YLim(2) * 0.035 + hist.Values(i), num2str(hist.BinCounts(i)));
        txt.HorizontalAlignment = 'center';
    end
    
    hold off
    legend([hist, plt_pdf], {'obs.', 'fitted dist. (scaled)'})
    title('Distribution of relative error', 'FontWeight', 'bold')
    xlabel('relative error (\times10^{16})')
    ylabel('probability')
    ylim([0 sub_4.YLim(2) * 1.1])
    hist.Parent.YAxisLocation = 'right';

    sub_1.YLim = rel_err.ylim;
    sub_2.YLim = rel_err.ylim;
    prog_update(12, 12)
    elapsed = toc;
    
    % Report.
    fprintf(']\n\n%s\n', f_title('PROCESSING FINISHED'))
    fprintf('  @elapsed: %.02fms\n\n', elapsed * 1000)
    
end