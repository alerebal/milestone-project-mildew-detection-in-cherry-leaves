import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_probabilities
                                                    )

def mildew_detector_body():
    """ Function to display the mildew detection page """
    # Business requirement 2
    st.success(
        f"The client is interested in predicting if a cherry leaf is healthy "
        f"or contains powdery mildew."
        )
    # The user must be able to donwload some images to test the application 
    # if the don't have any other image to do it, so the link
    # to the dataset is shown to them.
    st.write(
        f"* Download a set of haelthy and powdery mildew infected leaves for live "
        f"prediction [here](https://www.kaggle.com/codeinstitute/cherry-leaves)"
        )

    st.write("---")
    # The file uploader is shown with three extensions allowed, png, jpg and jpeg.
    images_buffer = st.file_uploader('Upload leaves images samples. You may select more than one.',
                                        type=['png','jpg','jpeg'],accept_multiple_files=True)
    # if the user load at least one image, we can analyze the image in real time and show them 
    # the report and allow download it using the function imported from data_managment
    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Leaf image Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(img_pil)

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = df_report.append({"Name":image.name, 'Result': pred_class },
                                        ignore_index=True)
        
        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)


