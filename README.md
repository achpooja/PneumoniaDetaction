# Pneumonia Detection

This repository contains code for a Pneumonia Detection system using a Convolutional Neural Network (CNN) built with Keras and deployed as a web application using Streamlit.

## Files

- `main.py`:Implements the web application using Streamlit for uploading chest X-ray images and performing pneumonia detection.
- `model.py`:Contains the code to train the CNN model using the VGG16 architecture and TensorFlow/Keras. 

## Usage

1. **Training the Model**:
   - To train the model:
     - Ensure the dataset is arranged in the specified directory structure.
     - Run the `model.py` script using the following command:
       ```
       python model.py
       ```
     - The trained model will be saved as `pneumoniaDetect.h5` in the current directory.

2. **Running the Web Application**:
   - To run the web application:
     - Execute the `main.py` script using the following command:
       ```
       streamlit run main.py
       ```
     - The application will start, and you can access it in your web browser by navigating to the provided URL.
     - Upload a chest X-ray image to detect pneumonia.

## Deployement

This project is deployed and accessible online. You can access the deployed application [here](https://pneumonia-detaction.streamlit.app/).

## Requirements

- Python 3.x
- TensorFlow
- Keras
- Streamlit
     
## Acknowledgments

- The model architecture is based on the VGG16 pre-trained model.
- Deployed using Streamlit and (Github).
