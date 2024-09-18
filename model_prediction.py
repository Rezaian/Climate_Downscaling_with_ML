# model_prediction.py

import xarray as xr
import numpy as np
from tensorflow.keras.models import load_model

def predict():
    # Load model
    model = load_model('models/downscaling_model.h5')

    # Load new low-resolution data
    ds_new_lr = xr.open_dataset('data/new_cmip6_iran_smoothed.nc')
    lr_data = ds_new_lr['tas'].values

    # Normalize data (use same mean and std from training)
    lr_mean = lr_data.mean()
    lr_std = lr_data.std()
    lr_data_norm = (lr_data - lr_mean) / lr_std

    # Reshape data
    lr_data_norm = lr_data_norm[..., np.newaxis]

    # Predict high-resolution data
    predicted_hr_data = model.predict(lr_data_norm)

    # Denormalize data
    predicted_hr_data = predicted_hr_data * lr_std + lr_mean

    # Create xarray Dataset
    predicted_hr_data = predicted_hr_data.squeeze()
    ds_predicted_hr = xr.Dataset(
        {'t2m': (('time', 'lat', 'lon'), predicted_hr_data)},
        coords={'time': ds_new_lr['time'],
                'lat': ds_new_lr['lat'],
                'lon': ds_new_lr['lon']})

    # Save predicted data
    ds_predicted_hr.to_netcdf('data/predicted_hr_data.nc')
    print("Prediction completed and saved.")

if __name__ == '__main__':
    predict()
