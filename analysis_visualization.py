# analysis_visualization.py

import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np

def visualize_results():
    # Load predicted and actual high-resolution data
    ds_predicted = xr.open_dataset('data/predicted_hr_data.nc')
    ds_actual = xr.open_dataset('data/era5_land_iran_202001.nc')

    # Select a time step
    time_step = 0

    # Plot predicted data
    plt.figure(figsize=(10, 5))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ds_predicted['t2m'].isel(time=time_step).plot(
        ax=ax, transform=ccrs.PlateCarree(), cmap='coolwarm')
    ax.coastlines()
    ax.set_title('Downscaled 2m Temperature')
    plt.show()

    # Plot difference
    difference = ds_predicted['t2m'] - ds_actual['t2m']

    plt.figure(figsize=(10, 5))
    ax = plt.axes(projection=ccrs.PlateCarree())
    difference.isel(time=time_step).plot(
        ax=ax, transform=ccrs.PlateCarree(), cmap='bwr', vmin=-5, vmax=5)
    ax.coastlines()
    ax.set_title('Difference between Downscaled and ERA5-Land Data')
    plt.show()

    # Compute RMSE
    predicted = ds_predicted['t2m'].values.flatten()
    actual = ds_actual['t2m'].values.flatten()
    rmse = np.sqrt(np.mean((predicted - actual) ** 2))
    print(f'RMSE: {rmse:.2f} K')

if __name__ == '__main__':
    visualize_results()
