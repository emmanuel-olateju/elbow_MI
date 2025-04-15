function convert_gdf_to_mat(s, h, output_filename)
    data.signal = s;
    data.marker = h.EVENT.TYP;
    data.marker_ts = h.EVENT.POS;
    data.fs = h.SampleRate;
    data.ch_type = h.Label;
    save(output_filename, 'data', '-v7');
    disp(['MAT file created successfully: ', output_filename]);
end
