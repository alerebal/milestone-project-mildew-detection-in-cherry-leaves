import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random


def leaves_visualizer_page_body():
    """ Functio to display the leaves visualizer page """
    st.write("### Leaves Visualizer")
    # Write the business requirement 1
    st.success(
        f"* The client is interested in conducting a study to visually differentiate a cherry leaf"
        f" that is healthy from one that contains powdery mildew.")
    
    # We are currently use the first version of the app
    version = 'v1'
    # Show average and variability of images
    if st.checkbox("Differences between average and variability images"):
      
        avg_var_healty = plt.imread(f"outputs/{version}/avg_var_healthy.png")
        avg_var_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")

        st.success(
        f"* We notice the average images show that the infected leaves have a color more white than the "
        f"healthy ones. Maybe they are qualities hard to appreciate when we are looking only to one leaf"
        f", without the posibility of compare with other one of different kind."
        f" The variability images show more lines in the surface of the powdery mildew infected leaves"
        f" than in the surface of the healthy ones, who have almost plane color. In this case it looks "
        f"not that hard to appreciate it when we are looking to only one leaf."
        )

        st.image(avg_var_healty, caption='Healty leaves - Avegare and Variability')
        st.image(avg_var_powdery_mildew, caption='Powdery Mildew infected leaves - Average and Variability')
        st.write("---")
    # Show the difference between average and variability images
    if st.checkbox("Differences between average haelthy and average infected leaves"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.success(
        f"* We can appreciate the same pattern here, where the healthy leaves have a "
        f"surface more clear, green, and the infected ones have more white color in "
        f"the surface. Difficult to appreciate when we cannot compare both different kind"
        f" of leaves."
        )

        st.image(diff_between_avgs, caption='Difference between average images')

    # Show the image montage
    if st.checkbox("Image Montage"): 
        st.write("* To refresh the montage, click on 'Create Montage' button")
        my_data_dir = 'inputs/datasets/cherry-leaves'
        labels = os.listdir(my_data_dir+ '/validation')
        label_to_display = st.selectbox(label="Select label", options=labels, index=0)
        if st.button("Create Montage"):      
            image_montage(dir_path= my_data_dir + '/validation',
                        label_to_display=label_to_display,
                        nrows=8, ncols=3, figsize=(10,25))
        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
    """ Function to create and display the image montage section """
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # subset the class you are interested to display
    if label_to_display in labels:

        # checks if your montage space is greater than subset size
        # how many images in that folder
        images_list = os.listdir(dir_path+'/'+ label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return
    

        # create list of axes indices based on nrows and ncols
        list_rows= range(0,nrows)
        list_cols= range(0,ncols)
        plot_idx = list(itertools.product(list_rows,list_cols))


        # create a Figure and display images
        fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
        for x in range(0,nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()
    
        st.pyplot(fig=fig)


    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")