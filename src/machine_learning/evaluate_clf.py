import streamlit as st
from src.data_management import load_pkl_file

def load_test_evaluation(version):
    """ Funtion to load the evaluation file """
    return load_pkl_file(f'outputs/{version}/trainings/train-3/evaluation.pkl')