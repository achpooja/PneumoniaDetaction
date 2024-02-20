import streamlit as st
import warnings
import tensorflow as tf
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import numpy as np
from keras.preprocessing import image
from PIL import ImageEnhance
import platform

if platform.system() == 'Windows':
    from win32com.client import Dispatch



warnings.filterwarnings('ignore')


def speak(str1):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)


def main():
    st.title("Pneumonia Detection App")
    st.write("Upload a chest X-ray image to detect pneumonia.")


    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.subheader("Uploaded Image")
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        st.write("Image uploaded successfully!")

        # Button to Detect
        if st.button("Detect Pneumonia"):
         model = load_model('pneumonia.h5')
         img = image.load_img(uploaded_file, target_size=(224, 224))
         x = image.img_to_array(img)
         x = np.expand_dims(x, axis=0)
         img_data = preprocess_input(x)
         classes = model.predict(img_data)

         if classes[0][0] > 0.5:
                st.success("Result: No Pneumonia Detected")
                speak("No Pneumonia Detected")

         else:
                st.error("Result: Pneumonia Detected")
                speak("Pneumonia Detected")



if __name__ == '__main__':
    main()