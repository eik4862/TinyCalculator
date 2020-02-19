function title = f_title(str, len)
% F_TITLE formats string as a title.
% 
% F_TITLE(STR, LEN) formats input string STR as title using placeholder
% character '-'. The length of title will be LEN. If the length of STR
% exceeds LEN, STR will be returned without any formatting.
% 
% Inputs:
%   STR - String for title.
%
% Optional inputs:
%   LEN - The length of title. (default = 56)
%
% Outputs:
%   TITLE - Formatted title string.

    % Argument validation.
    if nargin == 1
        len = 56;
    elseif nargin ~= 2
        error('Some arguments are missing. Terminate.')
    end
    
    if length(str) > len
        title = str;
    else
        lead_cnt = ceil((len - length(str) - 2) / 2);
        trail_cnt = len - length(str) - 2 - lead_cnt;
        title = sprintf('%s %s %s', repmat('-', [lead_cnt 1]), str, repmat('-', [trail_cnt 1]));
    end
end
