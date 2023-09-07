import streamlit as st
import time
import requests
import datetime
import pandas as pd

#Prediction
st.header('Predict Your Clicks', divider='green')
facebook = st.number_input('Insert your budget for Facebook')
tiktok = st.number_input('Insert your budget for Tiktok')
google = st.number_input('Insert your budget for Google')
date = st.date_input("Insert your prefer date for prediction", datetime.date(2023, 9, 8))
st.write(f"""The current budget for Facebook is: {facebook},
         for Tiktok is: {tiktok}, for Google is: {google}, and date is: {date}""")

url='https://mmm-lewagon-iainnplz7a-ew.a.run.app/clickpredict'
params={'facebook':facebook,
        'google':google,
        'tiktok':tiktok,
        'date':date}

if st.button('prediction'):
    with st.spinner('Wait for it...'):
        time.sleep(1)
        response=requests.get(url,params).json()
        pred = response
    st.success(f"""PREDICTED CLICKS = {pred} !""")
    #coef=pd.DataFrame([co[0],co[1],co[2]],columns=('Google','Facebook','Tiktok'),index=['Coefficient'])
    #st.dataframe(coef)
