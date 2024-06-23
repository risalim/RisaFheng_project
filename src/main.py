import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("NLP Service")


with st.form("form") :
  urls = st.text_area(label="Enter URLs")
  scrape_button = st.form_submit_button("Scrape")
  if scrape_button and urls != "" :

    urls = urls.split("\n")

    
    for url in urls :
      page = requests.get(URL)
      soup = BeautifulSoup(page.content, "html.parser")
      st.write("soup", soup)
