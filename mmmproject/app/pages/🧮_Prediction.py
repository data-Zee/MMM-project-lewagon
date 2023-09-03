import streamlit as st
import time
import requests
import datetime

st.sidebar.markdown("# 🧮 Prediction")


#Prediction
st.subheader('Predict Your Sales', divider='rainbow')
facebook = st.number_input('Insert your budget for Facebook')
tiktok = st.number_input('Insert your budget for Tiktok')
google = st.number_input('Insert your budget for Google')
date = st.date_input("Insert your prefer date for prediction", datetime.date(2019, 7, 6))
st.write(f"""The current budget for Facebook is: {facebook},
         for Tiktok is: {tiktok}, for Google is: {google}, and date is: {date}""")

url='https://mmm-project-lewagon-iainnplz7a-ew.a.run.app/salepredict'
params={'facebook':facebook,
        'google':google,
        'tiktok':tiktok,
        'date':date}

if st.button('prediction'):
    with st.spinner('Wait for it...'):
        time.sleep(1)
        response=requests.get(url,params).json()
        pred = response['predicted_sale']
    st.success(f'PREDICTED SALE = {pred} !')
