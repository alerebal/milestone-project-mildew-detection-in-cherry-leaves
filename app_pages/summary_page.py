import streamlit as st
import matplotlib.pyplot as plt


def summary_page_body():
    """ Funtion to show the summary page """
    st.write("### Quick Project Summary")

    # General information and dataset
    st.success(
        f"**General Information**\n"
        f"* Many different fungal species cause powdery mildew, with each "
        f"species attacking a different plant or plant family. The widespread"
        f" disease affects many plant types, from annuals and vegetables to "
        f"ornamental shrubs.\n"
        f"* New shoots and buds develop distorted growth. Flowers and fruit are"
        f" normally spared the white mildew, but infected plants have low yields"
        f" and poor-quality fruits.\n"
        f"* Prevention and perseverance are essential in controlling powdery "
        f"mildew. \n"
        f"* The first sign of problems is usually white, powdery spots or patches"
        f" on the top side of leaves or on plant stems. The powdery surface "
        f"growth gradually spreads to cover the entire leaf, including the "
        f"undersides, until the plant looks like it's dusted with white powder."
        f" Infected leaves turn yellow and twisted.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 4208 thousand images taken from "
        f"different leaves, half infected and half healthy."
        )

    # Link to the README file
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/alerebal/milestone-project-mildew-detection-in-cherry-leaves).")
    
    # Project business requirements
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to "
        f"differentiate a cherry leaf"
        f" that is healthy from one that contains powdery mildew.\n"
        f"* 2 - The client is interested to predict if a cherry leaf is healthy"
        f" or contains powdery"
        f" mildew ")