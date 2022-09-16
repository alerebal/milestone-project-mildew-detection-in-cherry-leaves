import streamlit as st

# MultiPage class will generate a different Streamlit page to render in the app
class MultiPage:

    ['theme']
    base = 'dark'

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title = self.app_name,
            page_icon = "🍒"
            )

    def add_page(self, title, func) -> None:
        """Function to append different views to the pages list"""
        self.pages.append({"title": title, "function": func})


    def run(self):
        """Function to set the title and add a sidebar to the app"""
        st.title(self.app_name)
        page = st.sidebar.radio("Menu", self.pages, format_func= lambda page: page['title'])
        page['function']()