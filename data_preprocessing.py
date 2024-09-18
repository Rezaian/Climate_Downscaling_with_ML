# data_preprocessing.py

import xarray as xr
import xesmf as xe
from scipy.ndimage import gaussian_filter

def preprocess_cmip6():
    # Load CMIP6 data
    ds_cmip6 = xr.open_dataset('data/cmip6_global.nc')

    # Subset to Iran
    iran_bbox = [44.0, 25.0, 63.0, 40.0]
    ds_cmip6_iran = ds_cmip6.sel(
        lon=slice(iran_bbox[0], iran_bbox[2]),
        lat=slice(iran_bbox[1], iran_bbox[3]))

    # Load ERA5-Land data for target grid
    ds_era5 = xr.open_dataset('data/era5_land_iran_202001.nc')

    # Regrid CMIP6 data to ERA5-Land grid
    regridder = xe.Regridder(ds_cmip6_iran, ds_era5, 'bilinear')
    ds_cmip6_regridded = regridder(ds_cmip6_iran)

    # Apply Gaussian smoothing
    sigma = 2
    smoothed_data = ds_cmip6_regridded.copy()
    for var in ds_cmip6_regridded.data_vars:
        data = ds_cmip6_regridded[var].values
        smoothed = gaussian_filter(data, sigma=sigma)
        smoothed_data[var].values = smoothed

    # Save preprocessed data
    smoothed_data.to_netcdf('data/cmip6_iran_smoothed.nc')
    print("CMIP6 data preprocessed and saved.")

if __name__ == '__main__':
    preprocess_cmip6()
