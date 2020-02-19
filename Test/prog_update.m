function prog_update(curr, tot)
% PROG_UPDATE renders progress bar to stdout.
% 
% PROG_UPDATE(CURR, TOT) updates previously rendered progress bar to
% progress bar where current progess stastus is CURR / TOT.
% 
% Inputs:
%   CURR - Current progress status.
%   TOT  - Total amout of work.

    % Argument validation.
    if nargin ~= 2
        error('Some arguments are missing. Terminate.')
    end
    
    if curr > tot
        error('current status must be less than or equal to total amout of work. Terminate.')
    end

    prev = ceil(sym(curr - 1) / sym(tot) * sym(25));
    next = ceil(sym(curr) / sym(tot) * sym(25));
    fprintf('\b\b\b\b\b\b\b%s%06.2f%%', repmat('=', [1, next - prev]), sym(curr) / sym(tot) * sym(100))
end