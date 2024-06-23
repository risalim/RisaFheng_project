import streamlit as st
from streamlit_option_menu import option_menu
from app import app

st.set_page_config(
    page_title="Web Scrapper",
    layout="wide"
)

def main() :
    with st.sidebar :
        pages = {
            "Web Scrapper": app
        }

if __name__ == "__main__" :
    main()
