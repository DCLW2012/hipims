{
    "grid_attr": {
        "area": "[4351200.0, 'm^2']",
        "shape": "(269, 269)",
        "cellsize": "[10.0, 'm']",
        "num_cells": 43512,
        "extent": {
            "left": 0.0,
            "right": 2690.0,
            "bottom": 0.0,
            "top": 2690.0
        }
    },
    "model_attr": {
        "case_folder": "E:\\opengithub\\hipims\\hipims\\demo\\hipims_case",
        "birthday": "2022-04-08 17:21",
        "num_GPU": 1,
        "run_time": "[[0, 3600, 3600, 3600], 's']",
        "num_gauges": 2
    },
    "initial_attr": {
        "h0": 0.5,
        "hU0x": 0,
        "hU0y": 0
    },
    "boundary_attr": {
        "num_boundary": 3,
        "boundary_details": "['0. (outline) fall, h and hU fixed as zero, number of cells: 788', '1. open, hU given, number of cells: 2', '2. open, h given, number of cells: 46']"
    },
    "rain_attr": {
        "num_source": 1,
        "max": "[100.0, 'mm/h']",
        "sum": "[52.5, 'mm']",
        "average": "[52.5, 'mm/h']",
        "spatial_res": "[2086.0, 'm']",
        "temporal_res": "[1800.0, 's']"
    },
    "params_attr": {
        "manning": "[[0.03], '[100.0]%']",
        "sewer_sink": 0,
        "cumulative_depth": 0,
        "hydraulic_conductivity": 0,
        "capillary_head": 0,
        "water_content_diff": 0
    }
}