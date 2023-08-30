import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

#DATA
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "df.csv")
data=pd.read_csv(path)

st.subheader('Tiktok Visualisations', divider='rainbow')
st.sidebar.markdown("# Tiktok")
tab1, tab2 = st.tabs(["plot1", "plot2"])
