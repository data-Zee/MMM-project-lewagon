import streamlit as st
import time
import datetime 
import requests 

st.sidebar.markdown("# 🧮 Prediction")


#Prediction
st.subheader('Predict Your Sales', divider='rainbow')
facebook = st.number_input('Insert your budget for Facebook')
tiktok = st.number_input('Insert your budget for Tiktok')
google = st.number_input('Insert your budget for Google')
date=st.date_input('Instert your current date', datetime.date(2019, 7, 6)
st.write(f"""The current budget for Facebook is: {facebook},
         for Tiktok is: {tiktok}, and for Google is: {google}""")

params= {'facebook':facebook,
        'tiktok':tiktok,
        'google':google,
        'date':date}

if st.button('prediction'):
    with st.spinner('Wait for it...'):
         url='https://mmm-project-lewagon-iainnplz7a-ew.a.run.app/salepredict'
         result=requests.get(url, params=params).json ()
    st.success(f" Here is your  prediction of sales: {result['predicted_sale']}")
         
