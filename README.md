# Regional Climate Downscaling for Iran

This repository contains code for downscaling CMIP6 climate model data to high-resolution data over Iran using deep learning techniques.

## Project Overview

- **Objective:** Enhance the spatial resolution of climate data for Iran.
- **Data Sources:**
  - **Low-resolution input:** CMIP6 climate model data.
  - **High-resolution target:** ERA5-Land data.

## Installation

Clone the repository and install the required packages using Conda:

```bash
git clone https://github.com/yourusername/climate-downscaling-iran.git
cd climate-downscaling-iran
conda env create -f environment.yml
conda activate climate_downscaling
Usage

Run the scripts in the following order:

    data_acquisition.py - Download and prepare data.
    data_preprocessing.py - Preprocess and align data.
    model_training.py - Train the downscaling model.
    model_prediction.py - Apply the model to new data.
    analysis_visualization.py - Analyze and visualize results.

##License

##Specify your project's license here.

#### 2. `environment.yml`

Define your Conda environment with all necessary packages.

```yaml
name: climate_downscaling
channels:
  - conda-forge
dependencies:
  - python=3.9
  - numpy
  - scipy
  - xarray
  - zarr
  - matplotlib
  - cartopy
  - regionmask
  - xesmf
  - pip
  - pip:
    - cdsapi
    - climetlab
    - cfgrib
    - tensorflow-macos
    - tensorflow-metal
Note: Adjust packages based on your requirements and hardware.