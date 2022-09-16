import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.summary_page import summary_page_body
from app_pages.project_hypothesis_page import project_hypothesis_page_body
from app_pages.leaves_visualizer_page import leaves_visualizer_page_body


app = MultiPage(app_name= "Powdery Mildew Detector")

app.add_page('Quick Project Summary', summary_page_body)
app.add_page('Leaves Visualizer', leaves_visualizer_page_body)
app.add_page('Project Hyphosis', project_hypothesis_page_body)


app.run()