function rgb = hex2rgb(hex, norm)
% HEX2RGB converts hex color code to rgb color code.
% 
% HEX2RGB(HEX, NORM) converts hexadecimal color code HEX to rgb color code.
% If NORM is true, then rgb color code will be normalized to range [0, 1]
% rathar than [0, 255].
% 
% Inputs:
%   HEX - Hex color code.
%
% Optional inputs:
%   NORM - Flag for normalization. (defult = true)
%
% Outputs:
%   RGB - Converted rgb color code.

    % Argument validation.
    if nargin == 1
        norm = true;
    elseif nargin ~= 2
        error('Some arguments are missing. Terminate.')
    end

    % Remove leading # char.
    if hex(1) == '#'
        hex = hex(2:end);
    end
    
    % Convert hex color code to rgb.
    if norm
        rgb = [hex2dec(hex(1:2)) hex2dec(hex(3:4)) hex2dec(hex(5:6))] / 255;
    else
        rgb = [hex2dec(hex(1:2)) hex2dec(hex(3:4)) hex2dec(hex(5:6))];
    end
end