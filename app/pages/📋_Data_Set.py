import streamlit as st
import pandas as pd

st.sidebar.markdown("# 📋 Data Set")

#DataFrame
st.subheader('Data Set', divider='rainbow')
data=pd.read_csv('../raw_data/df.csv')
st.dataframe(data=data)
