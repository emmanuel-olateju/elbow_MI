input_folder = 'gdf_files';   % <-- Replace with actual path
output_folder = 'mat_files'; % <-- Replace with actual path

% Create output folder if it doesn't exist
if ~exist(output_folder, 'dir')
    mkdir(output_folder);
end

% Get list of all .gdf files in the input folder
gdf_files = dir(fullfile(input_folder, '*.gdf'));

% Loop through each file and convert
for i = 1:length(gdf_files)
    input_file = fullfile(input_folder, gdf_files(i).name);
    [~, name, ~] = fileparts(gdf_files(i).name);
    output_file = fullfile(output_folder, [name '.mat']);

    if exist(output_file, 'file')
        fprintf('Skipping %s (already exists)\n', output_file);
        continue;
    end

    try
        [s, h] = sload(input_file); % Requires BIOSIG toolbox
        convert_gdf_to_mat(s, h, output_file);
    catch ME
        fprintf('Error converting %s: %s\n', gdf_files(i).name, ME.message);
    end
end

disp('Batch conversion complete.');
