import streamlit as st
import pandas as pd
import os
from mmmproject.app.streamlit_app import data

st.sidebar.markdown("# 📋 Data Set")

#DataFrame
st.subheader('Data Set', divider='rainbow')



st.dataframe(data=data)

if __name__ == "__main__":
    # print(os.path.join(os.path.dirname(os.path.abspath(__file__)), "df.py"))
    print(data)
