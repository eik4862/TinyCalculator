function fig = plt_err(in_file, ref_file, out_file, size, main, argc, from, to, verbose)
% PLT_ERR processes test output and plots the result.
% 
% PLT_ERR(IN, REF, OUT, SIZE, TITLE) processes and plots test result using
% test input IN, test reference output REF and test output OUT where SIZE
% is the # of test outputs and MAIN is the title of plots. The plot
% includes the followings.
%   - Trend of input points/abs error/rel error estimated using
%     OLS/LOESS/moving ave
%   - Scatter plot of input points/abs error/rel error with mean and one sd
%     band
%   - Histogram of input points/abs error/rel error with fitted dist using
%     Epanechnikov kernel.
% 
% Inputs:
%   IN   - Test input file.
%   REF  - Test reference output file.
%   OUT  - Test output file.
%   SIZE - The # of test outputs.
%   MAIN - The title of the plot.
%
% Outputs:
%   FIG - Figure handle of the plot.
%
% Notes:
%   - Since it does not close those files after reading them, one must
%     close them manually.

    % Argument validation.
    if nargin == 8
        verbose = true;
    elseif nargin ~= 9
        error('Some arguments are missing. Terminate.')
    end
    
    if size <= 0 || mod(size, 1) ~= 0
        error('The # of test outputs must be positive integer. Terminate.')
    elseif ~((length(from) == argc) && (length(to) == argc)) || any(from >= to)
        error('Plotting range is invalid. Terminate.')
    end

    % Turning off all warnings and set 100 as float precision.
    warning('off', 'all')
    digitOld = digits(300);
    
    in.path = fopen(in_file);
    ref.path = fopen(ref_file);
    out.path = fopen(out_file);
    tmp = dir(in.path);
    in.bytes = tmp.bytes;
    tmp = dir(ref.path);
    ref.bytes = tmp.bytes;
    tmp = dir(out.path);
    out.bytes = tmp.bytes;
    
    if verbose
        % Report.
        fprintf('%s\n', f_title('TEST DATA PROCESSOR'))
        fprintf('  @in  : %s (%dbytes)\n', in.path, in.bytes)
        fprintf('  @ref : %s (%dbytes)\n', ref.path, ref.bytes)
        fprintf('  @out : %s (%dbytes)\n', out.path, out.bytes)
        fprintf('  @size: %d\n', size)
        fprintf('  @argc: %d\n\n', argc)

        % Read files
        fprintf('%s\n', f_title('START PROCESSING'))
        fprintf('  Reading files.......[%06.2f%%', 0)
        tic
    end
       
    if argc == 1
        in.data = sym(nan([size 1]));
        ref = sym(nan([size 1]));
        out = sym(nan([size 1]));

        if verbose
            for i = 1:size
                in.data(i) = sym(fgetl(in_file));
                ref(i) = sym(fgetl(ref_file));
                out(i) = sym(fgetl(out_file));
                prog_update(i, size)
            end   
        else
            for i = 1:size
                in.data(i) = sym(fgetl(in_file));
                ref(i) = sym(fgetl(ref_file));
                out(i) = sym(fgetl(out_file));
            end 
        end
    else
        in.data = sym(nan([size 2]));
        ref = sym(nan([size 1]));
        out = sym(nan([size 1]));
        
        if verbose
            for i = 1:size
                in.data(i,:) = [sym(fgetl(in_file)) sym(fgetl(in_file))];
                ref(i) = sym(fgetl(ref_file));
                out(i) = sym(fgetl(out_file));
                prog_update(i, size)
            end 
        else
            for i = 1:size
                in.data(i,:) = [sym(fgetl(in_file)) sym(fgetl(in_file))];
                ref(i) = sym(fgetl(ref_file));
                out(i) = sym(fgetl(out_file));
            end 
        end
    end
    
    % Compute abs/rel errors and stats.
    if verbose
        fprintf(']\n  Computing stats.....[%06.2f%%', 0)
    end
        
    if argc == 1
        in.moving = smooth(double(in.data), 0.1, 'moving');
        in.loess = smooth(double(in.data), 0.1, 'loess');
        in.linear = polyval(double(polyfit(1:length(in.data), in.data', 1)), 1:length(in.data));
        in.mu = mean(in.data);
        in.sigma = std(in.data);
        in.band = [in.mu - in.sigma in.mu + in.sigma];
        in.pdf = fitdist(double(in.data), 'Kernel', 'Kernel', 'epanechnikov');
        in.col_deepdark = hex2rgb('#560096');
        in.col_dark = hex2rgb('#bc63ff');
        in.col = hex2rgb('#d296ff');
        in.col_light = hex2rgb('#e8c9ff');
        in.xlim = [1 size];
        in.ylim = [from to];
        
        if verbose
            prog_update(1, 3)
        end

        tmp = sortrows([in.data abs(ref - out)]);
        abs_err.in = tmp(:,1);
        abs_err.data = tmp(:,2);
        abs_err.logdata = log10(abs_err.data);
        tmp_quant = quantile(abs_err.logdata, 3);
        tmp_iqr = tmp_quant(3) - tmp_quant(1);
        tmp_msk = (abs_err.logdata > tmp_quant(1) - 3 * tmp_iqr) & (abs_err.logdata < tmp_quant(1) + 3 * tmp_iqr);
        abs_err.x = abs_err.in(tmp_msk);
        abs_err.y = abs_err.logdata(tmp_msk);
        abs_err.x_out = abs_err.in(~tmp_msk);
        abs_err.moving = smooth(abs_err.x, double(abs_err.y), 0.1, 'moving');
        abs_err.loess = smooth(abs_err.x, double(abs_err.y), 0.1, 'loess');
        abs_err.linear = polyval(double(polyfit(abs_err.x, abs_err.y, 1)), double(abs_err.x));
        abs_err.mu = mean(abs_err.data);
        abs_err.sigma = std(abs_err.data);
        abs_err.band = log10([max(abs_err.mu - abs_err.sigma, 1e-300) abs_err.mu + abs_err.sigma]);
        abs_err.pdf = fitdist(double(abs_err.y), 'Kernel', 'Kernel', 'epanechnikov');
        abs_err.col = hex2rgb('#f8766d');
        abs_err.col_deepdark = hex2rgb('#991107');
        abs_err.col_dark = hex2rgb('#f75f55');
        abs_err.col_light = hex2rgb('#faa49e');
        abs_err.xlim = in.ylim;

        if verbose
            prog_update(2, 3)
        end

        tmp = [in.data abs(out ./ ref - 1)];
        tmp = sortrows(tmp(isfinite(tmp(:,2)),:));
        rel_err.in = tmp(:,1);
        rel_err.data = tmp(:,2);
        rel_err.logdata = log10(rel_err.data);
        tmp_quant = quantile(rel_err.logdata, 3);
        tmp_iqr = tmp_quant(3) - tmp_quant(1);
        tmp_msk = (rel_err.logdata > tmp_quant(1) - 3 * tmp_iqr) & (rel_err.logdata < tmp_quant(1) + 3 * tmp_iqr);
        rel_err.x = rel_err.in(tmp_msk);
        rel_err.y = rel_err.logdata(tmp_msk);
        rel_err.x_out = rel_err.in(~tmp_msk);
        rel_err.moving = smooth(rel_err.x, double(rel_err.y), 0.1, 'moving');
        rel_err.loess = smooth(rel_err.x, double(rel_err.y), 0.1, 'loess');
        rel_err.linear = polyval(double(polyfit(rel_err.x, rel_err.y, 1)), double(rel_err.x));
        rel_err.mu = mean(rel_err.data);
        rel_err.sigma = std(rel_err.data);
        rel_err.band = log10([max(rel_err.mu - rel_err.sigma, 1e-300) rel_err.mu + rel_err.sigma]);
        rel_err.pdf = fitdist(double(rel_err.y), 'Kernel', 'Kernel', 'epanechnikov');
        rel_err.col = hex2rgb('#7cae00');
        rel_err.col_deepdark = hex2rgb('#527300');
        rel_err.col_light = hex2rgb('#dafa8c');
        rel_err.xlim = in.ylim;

        if verbose
            prog_update(3, 3)
        end
    else
        [Z, Xedge, Yedge] = histcounts2(double(in.data(:,1)), double(in.data(:,2)), [10 10]);
        in.cnt_xy = nan([(length(Xedge) - 1) * (length(Yedge) - 1) 2]);
        tmp_mid = nan([(length(Yedge) - 1) 1]);
        
        for i = 1:(length(Yedge) - 1)
            tmp_mid(i) = (Yedge(i) + Yedge(i + 1)) / 2;
        end

        for i = 1:(length(Xedge) - 1)
            in.cnt_xy(((length(Yedge) - 1) * (i - 1) + 1):((length(Yedge) - 1) * i),1) = (Xedge(i) + Xedge(i + 1)) / 2;
            in.cnt_xy(((length(Yedge) - 1) * (i - 1) + 1):((length(Yedge) - 1) * i),2) = tmp_mid; 
        end
        
        in.cnt_z = reshape(Z', [(length(Xedge) - 1) * (length(Yedge) - 1) 1]);
        tmp_loess = fit(in.cnt_xy, in.cnt_z, 'loess');
        [in.X, in.Y] = meshgrid(linspace(min(double(in.data(:,1))), max(double(in.data(:,1))), 250), linspace(min(double(in.data(:,2))), max(double(in.data(:,2))), 250));
        in.Z = tmp_loess(in.X, in.Y);
        in.xlim = [from(1) to(1)];
        in.ylim = [from(2) to(2)];
        in.colmap = cust_colmap('#3f006f', '#d296ff' ,'#f4e4ff');
        in.col = hex2rgb('#d296ff');
        in.col_gray = [0.7 0.7 0.7];

        if verbose
            prog_update(1, 3)
        end
        
        abs_err.in = in.data;
        abs_err.data = abs(ref - out);
        abs_err.logdata = log10(abs_err.data);
        tmp_quant = quantile(abs_err.logdata, 3);
        tmp_iqr = tmp_quant(3) - tmp_quant(1);
        tmp_msk = (abs_err.logdata > tmp_quant(1) - 3 * tmp_iqr) & (abs_err.logdata < tmp_quant(1) + 3 * tmp_iqr);
        abs_err.xy = abs_err.in(tmp_msk,:);
        abs_err.z = abs_err.logdata(tmp_msk);
        abs_err.xy_out = abs_err.in(~tmp_msk,:);
        abs_err.mu = mean(abs_err.data);
        tmp_loess = fit(double(abs_err.xy), double(abs_err.z), 'loess');
        [abs_err.X, abs_err.Y] = meshgrid(linspace(min(double(abs_err.in(:,1))), max(double(abs_err.in(:,1))), 250), linspace(min(double(abs_err.in(:,2))), max(double(abs_err.in(:,2))), 250));
        abs_err.loess = tmp_loess(abs_err.X, abs_err.Y);
        abs_err.pdf = fitdist(double(abs_err.z), 'Kernel', 'Kernel', 'epanechnikov');
        abs_err.xlim = in.xlim;
        abs_err.ylim = in.ylim;
        abs_err.colmap = cust_colmap('#740d06', '#f8766d', '#fddfdd');
        abs_err.col = hex2rgb('#f8766d');
        abs_err.col_deepdark = hex2rgb('#991107');
        abs_err.col_light = hex2rgb('#faa49e');
        abs_err.col_gray = [0.7 0.7 0.7];
        
        if verbose
            prog_update(2, 3)
        end
        
        rel_err.in = in.data;
        rel_err.data = abs(out ./ ref - 1);
        rel_err.data = rel_err.data(isfinite(rel_err.data));
        rel_err.logdata = log10(rel_err.data);
        tmp_quant = quantile(rel_err.logdata, 3);
        tmp_iqr = tmp_quant(3) - tmp_quant(1);
        tmp_msk = (rel_err.logdata > tmp_quant(1) - 3 * tmp_iqr) & (rel_err.logdata < tmp_quant(1) + 3 * tmp_iqr);
        rel_err.xy = rel_err.in(tmp_msk,:);
        rel_err.z = rel_err.logdata(tmp_msk);
        rel_err.xy_out = rel_err.in(~tmp_msk,:);
        rel_err.mu = mean(rel_err.data);
        tmp_loess = fit(double(rel_err.xy), double(rel_err.z), 'loess');
        [rel_err.X, rel_err.Y] = meshgrid(linspace(min(double(rel_err.in(:,1))), max(double(rel_err.in(:,1))), 250), linspace(min(double(rel_err.in(:,2))), max(double(rel_err.in(:,2))), 250));
        rel_err.loess = tmp_loess(rel_err.X, rel_err.Y);
        rel_err.pdf = fitdist(double(rel_err.z), 'Kernel', 'Kernel', 'epanechnikov');
        rel_err.xlim = in.xlim;
        rel_err.ylim = in.ylim;
        rel_err.colmap = cust_colmap('#283800', '#7cae00', '#f3ffd5');
        rel_err.col = hex2rgb('#7cae00');
        rel_err.col_deepdark = hex2rgb('#527300');
        rel_err.col_light = hex2rgb('#dafa8c');
        rel_err.col_gray = [0.7 0.7 0.7];
        
        if verbose
            prog_update(3, 3)
        end

    end
    
    % Plot.
    if verbose
        fprintf(']\n  Plotting............[%06.2f%%', 0)
    end
    
    if argc == 1
        fig = figure;
        sgtitle(main, 'FontWeight', 'bold', 'FontSize', 15)    
        set(fig, 'Position', [400 58 1133 907])

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
        ylim(in.ylim)
        
        if verbose
            prog_update(1, 12)
        end

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
        
        if verbose
            prog_update(2, 12)
        end


        % Scatter of test input.
        subplot(3,10,5:7)
        hold on

        scatter(1:size, in.data, 'o', 'MarkerEdgeColor','none', 'MarkerFaceColor', in.col)
        plt_mu = plot([1 length(in.data)], [in.mu in.mu], '--', 'Linewidth', 1.5, 'Color', in.col_deepdark);
        patch([in.xlim fliplr(in.xlim)], double([in.band(1) in.band(1) in.band(2) in.band(2)]), in.col_light, 'FaceAlpha', 0.5, 'LineStyle', 'none');

        hold off
        box on
        grid on
        legend(plt_mu, 'mean with one sd band')
        title(sprintf('Test input (size: %d)', size), 'FontWeight', 'bold')
        xlabel('count')
        xlim(in.xlim)
        ylim(in.ylim)
        
        if verbose
            prog_update(3, 12)
        end

        % Dist of test input.
        sub_4 = subplot(3,10,8:10);
        hold on

        hist = histogram(double(in.data), 10, 'FaceColor', in.col, 'Normalization', 'probability');
        x = sub_4.XLim(1):(sub_4.XLim(2) - sub_4.XLim(1)) / 100:sub_4.XLim(2);
        y = pdf(in.pdf, x);
        y = y / max(y) * (sub_4.YLim(2) * 0.9);
        plt_pdf = plot(x, y, 'Linewidth', 1.5, 'Color', in.col_deepdark);
        patch([x fliplr(x)], [y zeros(1, length(x))], in.col_light, 'FaceAlpha', 0.5, 'LineStyle', 'none')

        for i = 1:hist.NumBins
            txt = text((hist.BinEdges(i) + hist.BinEdges(i + 1)) / 2, sub_4.YLim(2) * 0.035 + hist.Values(i), num2str(hist.BinCounts(i)));
            txt.HorizontalAlignment = 'center';
        end

        hold off
        legend(plt_pdf, 'fitted dist. (scaled)')
        title('Distribution of test input', 'FontWeight', 'bold')
        xlabel('input')
        ylabel('probability')
        ylim([0 sub_4.YLim(2) * 1.2])
        hist.Parent.YAxisLocation = 'right';

        sub_1.YLim = in.ylim;
        
        if verbose
            prog_update(4, 12)
        end

        % Trend of abs err.
        sub_1 = subplot(3,10,11:13);
        hold on

        plt_lin = plot(abs_err.x, abs_err.linear, 'Linewidth', 1.5, 'Color', abs_err.col_deepdark);
        plt_loess = plot(abs_err.x, abs_err.loess, 'Linewidth', 1.5, 'Color', abs_err.col_dark);
        plt_mov = plot(abs_err.x, abs_err.moving, 'Linewidth', 1.5, 'Color', abs_err.col_light);

        hold off
        legend([plt_lin, plt_loess, plt_mov], {'linear', 'LOESS', 'moving ave.'})
        title('Trend of absolute error', 'FontWeight', 'bold')
        ylabel('log of absolute error')
        xlabel('input')
        xlim(abs_err.xlim)
        
        if verbose
            prog_update(5, 12)
        end

        % Box plot of abs err.
        sub_2 = subplot(3,10,14);
        boxplot(double(abs_err.logdata), 'Labels', 'abs. err.')
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
        
        if verbose
            prog_update(6, 12)
        end

        % Scatter of abs err.
        sub_3 = subplot(3,10,15:17);
        hold on

        scatter(abs_err.x, abs_err.y, 'o', 'MarkerEdgeColor', 'none', 'MarkerFaceColor', abs_err.col)
        abs_err.ylim = sub_3.YLim;
        plt_out = plot(abs_err.x_out, sub_3.YLim(1) * ones(length(abs_err.x_out), 1), '*', 'LineStyle', 'none', 'MarkerEdgeColor', abs_err.col_deepdark);
        plt_mu = plot(abs_err.xlim, log10([abs_err.mu abs_err.mu]), '--', 'Linewidth', 1.5, 'Color', abs_err.col_deepdark);
        patch(double([abs_err.xlim fliplr(abs_err.xlim)]), double([abs_err.band(1) abs_err.band(1) abs_err.band(2) abs_err.band(2)]), abs_err.col_light, 'FaceAlpha', 0.5, 'LineStyle', 'none')
        
        hold off
        box on
        grid on
        legend([plt_mu, plt_out], {'mean with one sd band', 'outlier'}, 'Location', 'southeast')
        title(sprintf('Absolute error (mean: %.02e)', abs_err.mu), 'FontWeight', 'bold')
        xlabel('input')
        xlim(abs_err.xlim)
        
        if verbose
            prog_update(7, 12)
        end

        % Dist of abs err.
        sub_4 = subplot(3,10,18:20);
        hold on

        hist = histogram(double(abs_err.y), 10, 'FaceColor', abs_err.col, 'Normalization', 'probability');
        x = sub_4.XLim(1):(sub_4.XLim(2) - sub_4.XLim(1)) / 100:sub_4.XLim(2);
        y = pdf(abs_err.pdf, x);
        y = y / max(y) * (sub_4.YLim(2) * 0.9);
        plt_pdf = plot(x, y, 'Linewidth', 1.5, 'Color', abs_err.col_deepdark);
        patch([x fliplr(x)], [y zeros(1, length(x))], abs_err.col_light, 'FaceAlpha', 0.5, 'LineStyle', 'none')

        for i = 1:hist.NumBins
            txt = text((hist.BinEdges(i) + hist.BinEdges(i + 1)) / 2, sub_4.YLim(2) * 0.035 + hist.Values(i), num2str(hist.BinCounts(i)));
            txt.HorizontalAlignment = 'center';
        end

        hold off
        legend(plt_pdf, 'fitted dist. (scaled)')
        title('Distribution of absolute error', 'FontWeight', 'bold')
        xlabel('log of absolute error')
        ylabel('probability')
        ylim([0 sub_4.YLim(2) * 1.2])
        hist.Parent.YAxisLocation = 'right';

        sub_1.YLim = abs_err.ylim;
        sub_3.YLim = abs_err.ylim;
        
        if verbose
            prog_update(8, 12)
        end

        % Trend of rel err.
        sub_1 = subplot(3,10,21:23);
        hold on

        plt_lin = plot(rel_err.x, rel_err.linear, 'Linewidth', 1.5, 'Color', rel_err.col_deepdark);
        plt_loess = plot(rel_err.x, rel_err.loess, 'Linewidth', 1.5, 'Color', rel_err.col);
        plt_mov = plot(rel_err.x, rel_err.moving, 'Linewidth', 1.5, 'Color', rel_err.col_light);

        hold off
        legend([plt_lin, plt_loess, plt_mov], {'linear', 'LOESS', 'moving ave.'})
        title('Trend of relative error', 'FontWeight', 'bold')
        ylabel('log of relative error')
        xlabel('input')
        xlim(rel_err.xlim)
        
        if verbose
            prog_update(9, 12)
        end

        % Box plot of rel err.
        sub_2 = subplot(3,10,24);
        boxplot(double(rel_err.logdata), 'Labels', 'rel. err.')
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

        if verbose
            prog_update(10, 12)
        end

        % Scatter of rel err.
        sub_3 = subplot(3,10,25:27);
        hold on

        scatter(rel_err.x, rel_err.y, 'o', 'MarkerEdgeColor', 'none', 'MarkerFaceColor', rel_err.col)
        rel_err.ylim = sub_3.YLim;
        plt_out = plot(rel_err.x_out, sub_3.YLim(1) * ones(length(rel_err.x_out), 1), '*', 'LineStyle', 'none', 'MarkerEdgeColor', rel_err.col_deepdark);
        plt_mu = plot(rel_err.xlim, log10([rel_err.mu rel_err.mu]), '--', 'Linewidth', 1.5, 'Color', rel_err.col_deepdark);
        patch(double([rel_err.xlim fliplr(rel_err.xlim)]), double([rel_err.band(1) rel_err.band(1) rel_err.band(2) rel_err.band(2)]), rel_err.col_light, 'FaceAlpha', 0.5, 'LineStyle', 'none')
        
        hold off
        box on
        grid on
        legend([plt_mu, plt_out], {'mean with one sd band', 'outlier'}, 'Location', 'southeast')
        title(sprintf('Relative error (mean: %.02e)', rel_err.mu), 'FontWeight', 'bold')
        xlabel('input')
        xlim(rel_err.xlim)
        
        if verbose
            prog_update(11, 12)
        end

        % Dist of rel err.
        sub_4 = subplot(3,10,28:30);
        hold on

        hist = histogram(double(rel_err.y), 10, 'FaceColor', rel_err.col, 'Normalization', 'probability');
        x = sub_4.XLim(1):(sub_4.XLim(2) - sub_4.XLim(1)) / 100:sub_4.XLim(2);
        y = pdf(rel_err.pdf, x);
        y = y / max(y) * (sub_4.YLim(2) * 0.9);
        plt_pdf = plot(x, y, 'Linewidth', 1.5, 'Color', rel_err.col_deepdark);
        patch([x fliplr(x)], [y zeros(1, length(x))], rel_err.col_light, 'FaceAlpha', 0.5, 'LineStyle', 'none')

        for i = 1:hist.NumBins
            txt = text((hist.BinEdges(i) + hist.BinEdges(i + 1)) / 2, sub_4.YLim(2) * 0.035 + hist.Values(i), num2str(hist.BinCounts(i)));
            txt.HorizontalAlignment = 'center';
        end

        hold off
        legend(plt_pdf, 'fitted dist. (scaled)')
        title('Distribution of relative error', 'FontWeight', 'bold')
        xlabel('log of relative error')
        ylabel('probability')
        ylim([0 sub_4.YLim(2) * 1.2])
        hist.Parent.YAxisLocation = 'right';

        sub_1.YLim = rel_err.ylim;
        sub_3.YLim = rel_err.ylim;
        
        if verbose
            prog_update(12, 12)
        end
    else
        fig = figure;
        sgtitle(main, 'FontWeight', 'bold', 'FontSize', 15)    
        set(fig, 'Position', [400 58 1133 907])

        % Trend of test input.
        sub_1 = subplot(3,10,1:3);
        hold on
        
        surf(in.X, in.Y, in.Z, 'EdgeColor', 'none')
        contour3(in.X, in.Y, in.Z, 10, 'LineColor', in.col_gray)
        
        hold off
        sub_1.Colormap = in.colmap;
        sub_1.View = [0 90];
        sub_1.Box = 'on';
        sub_1.BoxStyle = 'full';
        title('Trend of test input (LOESS)', 'FontWeight', 'bold')
        xlabel('x')
        ylabel('y')
        xlim(in.xlim)
        ylim(in.ylim)
        
        if verbose
            prog_update(1, 11)
        end

        % Scatter of test input.
        subplot(3,10,5:7)
        plot(in.data(:,1), in.data(:,2), 'Linestyle', 'none', 'Marker', 'o', 'MarkerEdgeColor', 'none', 'MarkerFaceColor', in.col)
        box on
        grid on
        title(sprintf('Test input (size: %d)', size), 'FontWeight', 'bold')
        xlabel('x')
        xlim(in.xlim)
        ylim(in.ylim)
        
        if verbose
            prog_update(2, 11)
        end

        % Dist of test input.
        sub_3 = subplot(3,10,8:10);
        hist3(double(in.data), [10 10], 'CDataMode','auto','FaceColor','interp')
        sub_3.Colormap = in.colmap;
        sub_3.View = [0 90];
        sub_3.Box = 'on';
        sub_3.BoxStyle = 'full';
        title('Distribution of test input', 'FontWeight', 'bold')
        xlabel('x')
        c = colorbar;
        c.Label.String = 'count';
        
        tmp_1 = fig.Children(4).CLim;
        tmp_2 = fig.Children(2).CLim;
        fig.Children(2).CLim = [min(tmp_1(1), tmp_2(1)) max(tmp_1(2), tmp_2(2))];
        fig.Children(4).CLim = [min(tmp_1(1), tmp_2(1)) max(tmp_1(2), tmp_2(2))];
                
        if verbose
            prog_update(3, 11)
        end
        
        % Trend of abs err.
        sub_1 = subplot(3,10,11:13);
        hold on
        
        surf(abs_err.X, abs_err.Y, abs_err.loess, 'EdgeColor', 'none')
        contour3(abs_err.X, abs_err.Y, abs_err.loess, 10, 'LineColor', abs_err.col_gray)
        plt_out = scatter3(abs_err.xy_out(:,1), abs_err.xy_out(:,2), sub_1.ZLim(2) * ones(1, length(abs_err.xy_out(:,1))), 'Marker', '*', 'MarkerEdgeColor', abs_err.col_deepdark);
        
        hold off
        sub_1.Colormap = abs_err.colmap;
        sub_1.View = [0 90];
        sub_1.Box = 'on';
        sub_1.BoxStyle = 'full';
        title('Trend of absolute error (LOESS)', 'FontWeight', 'bold')
        xlabel('x')
        ylabel('y')
        legend(plt_out, 'outlier')
        xlim(abs_err.xlim)
        ylim(abs_err.ylim)
        
        if verbose
            prog_update(4, 11)
        end
        
        % Box plot of abs err.
        sub_2 = subplot(3,10,14);
        boxplot(double(abs_err.logdata), 'Labels', 'abs. err.')
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
                
        if verbose
            prog_update(5, 11)
        end
        
        % Scatter of abs err.
        sub_3 = subplot(3,10,15:17);
        hold on
        
        scatter(abs_err.xy(:,1), abs_err.xy(:,2), [], abs_err.z, 'filled', 'MarkerEdgeColor', 'none')
        plt_out = scatter(abs_err.xy_out(:,1), abs_err.xy_out(:,2), 'Marker', '*', 'MarkerEdgeColor', abs_err.col_deepdark);
        
        hold off
        sub_3.Colormap = abs_err.colmap;
        box on
        grid on
        title(sprintf('Absolute error (mean: %.02e)', abs_err.mu), 'FontWeight', 'bold')
        xlabel('x')
        legend(plt_out, 'outlier')
        xlim(abs_err.xlim)
        ylim(abs_err.ylim)
        c = colorbar;
        c.Label.String = 'log of absolute error';
        
        tmp_1 = fig.Children(5).CLim;
        tmp_2 = fig.Children(8).CLim;
        fig.Children(5).CLim = [min(tmp_1(1), tmp_2(1)) max(tmp_1(2), tmp_2(2))];
        fig.Children(8).CLim = [min(tmp_1(1), tmp_2(1)) max(tmp_1(2), tmp_2(2))];
        
        if verbose
            prog_update(6, 11)
        end
        
        % Dist of abs err.
        sub_4 = subplot(3,10,18:20);
        hold on

        hist = histogram(double(abs_err.z), 10, 'FaceColor', abs_err.col, 'Normalization', 'probability');
        x = sub_4.XLim(1):(sub_4.XLim(2) - sub_4.XLim(1)) / 100:sub_4.XLim(2);
        y = pdf(abs_err.pdf, x);
        y = y / max(y) * (sub_4.YLim(2) * 0.9);
        plt_pdf = plot(x, y, 'Linewidth', 1.5, 'Color', abs_err.col_deepdark);
        patch([x fliplr(x)], [y zeros(1, length(x))], abs_err.col_light, 'FaceAlpha', 0.5, 'LineStyle', 'none')

        for i = 1:hist.NumBins
            txt = text((hist.BinEdges(i) + hist.BinEdges(i + 1)) / 2, sub_4.YLim(2) * 0.035 + hist.Values(i), num2str(hist.BinCounts(i)));
            txt.HorizontalAlignment = 'center';
        end

        hold off
        legend(plt_pdf, 'fitted dist. (scaled)')
        title('Distribution of absolute error', 'FontWeight', 'bold')
        xlabel('log of absolute error')
        ylabel('probability')
        ylim([0 sub_4.YLim(2) * 1.2])
        hist.Parent.YAxisLocation = 'right';
        
        if verbose
            prog_update(7, 11)
        end
        
        % Trend of rel err.
        sub_1 = subplot(3,10,21:23);
        hold on
        
        surf(rel_err.X, rel_err.Y, rel_err.loess, 'EdgeColor', 'none')
        contour3(rel_err.X, rel_err.Y, rel_err.loess, 10, 'LineColor', rel_err.col_gray)
        plt_out = scatter3(rel_err.xy_out(:,1), rel_err.xy_out(:,2), sub_1.ZLim(2) * ones(1, length(rel_err.xy_out(:,1))), 'Marker', '*', 'MarkerEdgeColor', rel_err.col_deepdark);
        
        hold off
        sub_1.Colormap = rel_err.colmap;
        sub_1.View = [0 90];
        sub_1.Box = 'on';
        sub_1.BoxStyle = 'full';
        title('Trend of relative error (LOESS)', 'FontWeight', 'bold')
        xlabel('x')
        ylabel('y')
        legend(plt_out, 'outlier')
        xlim(rel_err.xlim)
        ylim(rel_err.ylim)
        
        if verbose
            prog_update(8, 11)
        end
        
        % Box plot of rel err.
        sub_2 = subplot(3,10,24);
        boxplot(double(rel_err.logdata), 'Labels', 'rel. err.')
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
                
        if verbose
            prog_update(9, 11)
        end
        
        % Scatter of rel err.
        sub_3 = subplot(3,10,25:27);
        hold on
        
        scatter(rel_err.xy(:,1), rel_err.xy(:,2), [], rel_err.z, 'filled', 'MarkerEdgeColor', 'none')
        plt_out = scatter(rel_err.xy_out(:,1), rel_err.xy_out(:,2), 'Marker', '*', 'MarkerEdgeColor', rel_err.col_deepdark);
        
        hold off
        sub_3.Colormap = rel_err.colmap;
        box on
        grid on
        title(sprintf('Relative error (mean: %.02e)', rel_err.mu), 'FontWeight', 'bold')
        xlabel('x')
        legend(plt_out, 'outlier')
        xlim(rel_err.xlim)
        ylim(rel_err.ylim)
        c = colorbar;
        c.Label.String = 'log of relative error';
        
        tmp_1 = fig.Children(5).CLim;
        tmp_2 = fig.Children(8).CLim;
        fig.Children(5).CLim = [min(tmp_1(1), tmp_2(1)) max(tmp_1(2), tmp_2(2))];
        fig.Children(8).CLim = [min(tmp_1(1), tmp_2(1)) max(tmp_1(2), tmp_2(2))];        
        
        if verbose
            prog_update(10, 11)
        end

        % Dist of rel err.
        sub_4 = subplot(3,10,28:30);
        hold on

        hist = histogram(double(rel_err.z), 10, 'FaceColor', rel_err.col, 'Normalization', 'probability');
        x = sub_4.XLim(1):(sub_4.XLim(2) - sub_4.XLim(1)) / 100:sub_4.XLim(2);
        y = pdf(rel_err.pdf, x);
        y = y / max(y) * (sub_4.YLim(2) * 0.9);
        plt_pdf = plot(x, y, 'Linewidth', 1.5, 'Color', rel_err.col_deepdark);
        patch([x fliplr(x)], [y zeros(1, length(x))], rel_err.col_light, 'FaceAlpha', 0.5, 'LineStyle', 'none')

        for i = 1:hist.NumBins
            txt = text((hist.BinEdges(i) + hist.BinEdges(i + 1)) / 2, sub_4.YLim(2) * 0.035 + hist.Values(i), num2str(hist.BinCounts(i)));
            txt.HorizontalAlignment = 'center';
        end

        hold off
        legend(plt_pdf, 'fitted dist. (scaled)')
        title('Distribution of relative error', 'FontWeight', 'bold')
        xlabel('log of relative error')
        ylabel('probability')
        ylim([0 sub_4.YLim(2) * 1.2])
        hist.Parent.YAxisLocation = 'right';

        if verbose
            prog_update(11, 11)
        end
    end
    
    if verbose
        elapsed = toc;

        % Report.
        fprintf(']\n\n%s\n', f_title('PROCESSING FINISHED'))
        fprintf('  @elapsed: %.02fms\n\n', elapsed * 1000)
    end
    
    % Turning on all warnings and restore original digit precision.
    warning('on', 'all')
    digits(digitOld)
end