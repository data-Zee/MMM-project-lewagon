import streamlit as st
import requests
import pandas as pd

st.title("Marketing Mix Model")

st.subheader('This is DataFrame', divider='rainbow')
data=pd.read_csv('../raw_data/df.csv')

st.dataframe(data=data)


st.subheader('Some Visualisations', divider='rainbow')
st.line_chart(data=None)
st.caption('This a line chart')





st.subheader('Predict Your Sales', divider='rainbow')
facebook = st.number_input('Insert your budget for Facebook')
tiktok = st.number_input('Insert your budget for Tiktok')
google = st.number_input('Insert your budget for Google')
st.write(f"""The current budget for Facebook is: {facebook},
         for Tiktak is: {tiktok}, and for Google is: {google}""")

st.button('prediction')
