# data_acquisition.py

import cdsapi

def download_era5_land():
    c = cdsapi.Client()

    iran_bbox = [44.0, 25.0, 63.0, 40.0]  # [west, south, east, north]

    c.retrieve(
        'reanalysis-era5-land',
        {
            'variable': ['2m_temperature', 'surface_pressure'],
            'year': '2020',
            'month': '01',
            'day': [f'{day:02d}' for day in range(1, 32)],
            'time': [f'{hour:02d}:00' for hour in range(0, 24)],
            'area': [iran_bbox[3], iran_bbox[0], iran_bbox[1], iran_bbox[2]],
            'format': 'netcdf',
        },
        'data/era5_land_iran_202001.nc')

if __name__ == '__main__':
    download_era5_land()
    print("ERA5-Land data downloaded successfully.")
