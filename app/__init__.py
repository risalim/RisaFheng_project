import os
import streamlit as st
import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError

def get_http_status(url) :
    try :
        r = requests.get(url)
        r.raise_for_status()
    except (ConnectionError, Timeout):
        st.sidebar.error("Error")
    except HTTPError :
        st.sidebar.error("HTTPError")
    else :
        st.sidebar.info("Endpoint is ok")
