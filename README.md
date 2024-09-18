# Climate_Downscaling_with_ML: Machine Learning-Based Regional Climate Downscaling for Iran

---

### Project Overview

This project aims to downscale low-resolution climate model data to high-resolution climate data using machine learning techniques, specifically focusing on the region of Iran. Due to the hardware limitations of a MacBook M1 Air, this project currently targets Iran, but the approach can be applied to larger regions or globally in the future.

Global climate models (GCMs), like CMIP6, often provide climate projections at coarse resolutions (about 100-250 km), which limits their usability for local or regional analysis. Downscaling is a technique that increases the spatial resolution of climate data, making it more suitable for localized applications. Traditional downscaling methods, such as regional climate models (RCMs), can be computationally expensive. This project uses machine learning to achieve similar results in a more computationally efficient manner.

The project uses convolutional neural networks (CNNs) to predict high-resolution climate data (downscaled to ~9 km resolution) based on low-resolution inputs from global climate models. The target high-resolution data is sourced from ERA5-Land reanalysis, which provides climate data over Iran at a finer spatial scale.

---

### Motivation

Accurate, high-resolution climate data is critical for assessing the impacts of climate change at regional levels. While global climate models offer valuable information, their coarse resolution makes it difficult to provide detailed insights for local decision-making. Downscaling offers a solution by converting this low-resolution data into higher resolution, more localized projections.

Machine learning, especially deep learning, has shown great potential for this task. It offers the possibility to learn complex spatial relationships from data without needing the computational resources required by traditional dynamical downscaling models. This project aims to explore how well a CNN can handle downscaling tasks for the region of Iran, and provide a scalable framework for future work in other regions.

---

### Key Components

1. **Low-Resolution Input Data**  
   - Climate data from CMIP6 models, interpolated and smoothed to simulate coarse resolution.
  
2. **High-Resolution Target Data**  
   - ERA5-Land reanalysis data with approximately 9 km resolution, used as the high-resolution reference for training.

3. **Machine Learning Model**  
   - A convolutional neural network (CNN) is used to perform the downscaling. This model learns from paired low-resolution and high-resolution data.

4. **Regional Focus**  
   - Currently, the model is trained and tested using data from Iran due to hardware limitations. The project’s methodology is designed to be scalable to larger regions or even global data in future iterations.

5. **Climate Variable**  
   - The primary variable being downscaled in this project is the 2-meter air temperature. Other variables, such as precipitation or wind speed, could be added in the future.

---

### Methodology

This project applies machine learning techniques to downscale climate data, using the following process:

#### 1. Data Acquisition

- **ERA5-Land Data:** Downloaded using the Copernicus Climate Data Store (CDS) API. ERA5-Land provides high-resolution data over the region of Iran, which is used as the ground truth in model training.
- **CMIP6 Data:** Sourced from the Earth System Grid Federation (ESGF), low-resolution climate data is extracted from global climate models and used as input for the downscaling process.

#### 2. Data Preprocessing

- **Regridding:** The CMIP6 data is regridded to match the resolution and grid of the ERA5-Land data using bilinear interpolation. This ensures compatibility between the low-resolution input and high-resolution target data.
- **Smoothing:** Gaussian smoothing is applied to the high-resolution ERA5 data to simulate the coarse resolution of global climate models.

#### 3. Model Training

- **Convolutional Neural Network (CNN):** A CNN model is trained to predict high-resolution outputs (ERA5-Land) based on low-resolution inputs (smoothed CMIP6). The model learns the mapping between these two datasets and improves the spatial resolution of the input.
- **Data Normalization:** Input and output data are normalized during training to help the model converge more effectively.

#### 4. Prediction

- After training, the model is used to generate high-resolution predictions from new low-resolution input data. This allows for the creation of high-resolution climate projections, which are valuable for local climate analysis.

#### 5. Post-Processing and Validation

- The model's predictions are compared with actual high-resolution data to assess accuracy. Metrics such as Root Mean Square Error (RMSE) are used to measure the performance of the downscaling process.
- Visual comparisons between predicted and actual data are produced to highlight areas where the model performs well and where improvements can be made.

---

### Repository Structure

The project is organized as follows:

```
Climate_Downscaling_with_ML/
├── README.md               # Project documentation
├── environment.yml         # Conda environment configuration
├── data_acquisition.py     # Script to download ERA5-Land data for Iran
├── data_preprocessing.py   # Preprocess and align CMIP6 and ERA5 data
├── model_training.py       # Script for training the downscaling model
├── model_prediction.py     # Script to generate predictions using the trained model
├── analysis_visualization.py # Script for analyzing and visualizing results
├── .gitignore              # Exclude data and environment files from git
```

---

### Installation Instructions

To run this project on your local machine, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Rezaian/Climate_Downscaling_with_ML.git
   cd Climate_Downscaling_with_ML
   ```

2. **Set up the Conda environment:**

   Install the required Python packages using Conda:

   ```bash
   conda env create -f environment.yml
   conda activate climate_downscaling
   ```

   This will create an environment with all the necessary dependencies, including data handling (`xarray`, `cdsapi`, `xesmf`), machine learning (`tensorflow`), and visualization tools (`matplotlib`, `cartopy`).

---

### Usage

#### 1. Data Acquisition

To download the high-resolution ERA5-Land data for Iran:

```bash
python data_acquisition.py
```

This script will use the CDS API to retrieve 2-meter temperature and surface pressure data for the region of Iran. Make sure your CDS API key is correctly configured.

#### 2. Data Preprocessing

Once the data is downloaded, you can preprocess it by running:

```bash
python data_preprocessing.py
```

This script aligns the low-resolution CMIP6 data with the high-resolution ERA5 grid and applies Gaussian smoothing to create the low-resolution inputs.

#### 3. Model Training

To train the convolutional neural network (CNN) using the preprocessed data:

```bash
python model_training.py
```

This script will train the model using the paired low-resolution and high-resolution data, and the trained model will be saved for future use.

#### 4. Prediction

To use the trained model on new low-resolution data:

```bash
python model_prediction.py
```

The script will generate high-resolution predictions based on the low-resolution input.

#### 5. Analysis and Visualization

To visualize the model's performance and compare its predictions to actual high-resolution data:

```bash
python analysis_visualization.py
```

This script generates visual comparisons and computes error metrics such as RMSE.

---

### Future Directions

Currently, this project is focused on downscaling for Iran due to hardware constraints. In the future, the project could be extended to other regions or even globally as follows:

- **Expanding the Model:** Apply the model to other climate variables such as precipitation or wind speed.
- **Global Downscaling:** With more computational resources, this methodology could be applied to global datasets, generating high-resolution climate projections across larger regions.
- **Advanced Architectures:** Implement more complex models such as GANs (Generative Adversarial Networks) to improve the performance and accuracy of the downscaling process.

---

### License

This project is released under MIT.
---

### Contributions

Contributions are welcome to enhance the scalability, accuracy, and performance of this project. Feel free to submit issues or pull requests on GitHub.

For any questions or suggestions, please contact Reza Rezaian at Rezaian@ut.ac.ir
