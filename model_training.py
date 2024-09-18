# model_training.py

import xarray as xr
import numpy as np
from tensorflow.keras.layers import Input, Conv2D, UpSampling2D
from tensorflow.keras.models import Model
from sklearn.model_selection import train_test_split

def create_sr_model():
    inputs = Input(shape=(None, None, 1))
    x = Conv2D(64, (9, 9), activation='relu', padding='same')(inputs)
    x = UpSampling2D(size=(2, 2))(x)
    x = Conv2D(32, (1, 1), activation='relu', padding='same')(x)
    x = Conv2D(1, (5, 5), activation='linear', padding='same')(x)
    model = Model(inputs, x)
    return model

def train_model():
    # Load preprocessed data
    ds_lr = xr.open_dataset('data/cmip6_iran_smoothed.nc')
    ds_hr = xr.open_dataset('data/era5_land_iran_202001.nc')

    # Select variable (e.g., temperature)
    lr_data = ds_lr['tas'].values
    hr_data = ds_hr['t2m'].values

    # Normalize data
    lr_mean = lr_data.mean()
    lr_std = lr_data.std()
    lr_data = (lr_data - lr_mean) / lr_std

    hr_mean = hr_data.mean()
    hr_std = hr_data.std()
    hr_data = (hr_data - hr_mean) / hr_std

    # Reshape data
    lr_data = lr_data[..., np.newaxis]
    hr_data = hr_data[..., np.newaxis]

    # Split data
    lr_train, lr_val, hr_train, hr_val = train_test_split(
        lr_data, hr_data, test_size=0.2, random_state=42)

    # Create and train model
    model = create_sr_model()
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(lr_train, hr_train, validation_data=(lr_val, hr_val),
              epochs=10, batch_size=16)

    # Save model
    model.save('models/downscaling_model.h5')
    print("Model trained and saved.")

if __name__ == '__main__':
    train_model()
