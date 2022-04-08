import os
import numpy as np
import hipims_io as hp

dem_file, model_data, _ = hp.get_sample_data() # get sample data
case_folder = os.path.join(os.getcwd(), 'hipims_case') # define a case folder in the current directory
# create a single-gpu input object
obj_in = hp.InputHipims(dem_data=dem_file, num_of_sections=1, case_folder=case_folder)

# set a initial water depth of 0.5 m
obj_in.set_initial_condition('h0', 0.5)

# set boundary condition
bound_list = model_data['boundary_condition'] # with boundary information
obj_in.set_boundary_condition(bound_list, outline_boundary='fall')

# set rainfall mask and source
rain_source = model_data['rain_source']
obj_in.set_rainfall(rain_mask=0, rain_source=rain_source)

# set manning parameter
manning_array = np.zeros(obj_in.DEM.shape)+0.03 # create an array with the same shape of the DEM array
obj_in.set_grid_parameter(manning=manning_array)

# set monitor positions
gauges_pos = model_data['gauges_pos']
obj_in.set_gauges_position(gauges_pos)

# display model information
obj_in.domain_show() # show domain map
print(obj_in) # print model summary

# write all input files for HiPIMS to the case folder
obj_in.write_input_files()