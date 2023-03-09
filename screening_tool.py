import pandas as pd
import streamlit as st
import pickle

from PrEP import prep
from TB import tb

st.set_page_config(layout="wide")


def screening_tools():
    col1, col2, col3 = st.columns(3)
    with col1:
        option = st.selectbox(
            'Choose screening tool',
            ('', 'TB', 'PrEP'))
    if option == "TB":
        tb(option)
    elif option == "PrEP":
        prep(option)


screening_tools()
