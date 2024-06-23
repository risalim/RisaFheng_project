import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("NLP Service")
urls = st.text_area(label="Enter URLs")

for url in urls :
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  st.write("soup", soup)
