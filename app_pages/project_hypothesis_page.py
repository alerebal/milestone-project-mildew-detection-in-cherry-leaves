import streamlit as st
import matplotlib.pyplot as plt


def project_hypothesis_page_body():
    """ Function to show the hypothesis page """
    
    st.write("### Project Hypothesis and Validation")
    
    st.success(
        f"* The first sign of problems is usually white, powdery spots or "
        f"patches on the top side of  leaves or on plant stems."
        f" The powdery surface growth gradually spreads to cover the entire"
        f" leaf, including the undersides, until the plant looks like it's "
        f"dusted with white powder.\n"
        f"We believe that these types of characteristics should be sufficient"
        f" to differentiate a leaf infected with powdery mildew from a healthy"
        f" leaf.\n"
    )

    st.success(
        f"* An Image Montage of powdery mildew infected leaves shows the signs"
        f" commented above, the difference between both kind of leaves is "
        f"pretty clear.\n"
        f"This difference is not than clear in the average and variability "
        f"images, where is complicated appreciate the difference between both "
        f"kind of leaves. The surfice of infected leaves is more white, but"
        f" complicated to appreciate without compare both leaves."
    )