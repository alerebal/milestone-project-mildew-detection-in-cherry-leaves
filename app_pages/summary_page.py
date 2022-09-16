import streamlit as st
import matplotlib.pyplot as plt


def summary_page_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Many different fungal species cause powdery mildew, with each species attacking"
        f" a different plant or plant family. The widespread disease affects many plant types,"
        f" from annuals and vegetables to ornamental shrubs.\n"
        f"* New shoots and buds develop distorted growth. Flowers and fruit are normally spared"
        f" the white mildew, but infected plants have low yields and poor-quality fruits.\n"
        f"* Prevention and perseverance are essential in controlling powdery mildew. \n"
        f"* The first sign of problems is usually white, powdery spots or patches on the top side"
        f" of leaves or on plant stems. The powdery surface growth gradually spreads to cover the"
        f" entire leaf, including the undersides, until the plant looks like it's dusted with white"
        f" powder. Infected leaves turn yellow and twisted.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 4208 thousand images taken from different leaves, half"
        f" infected and half healthy.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/alerebal/milestone-project-mildew-detection-in-cherry-leaves).")
    

    st.info(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf"
        f" that is healthy and that contains powdery mildew.\n"
        f"* 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery"
        f" mildew ")