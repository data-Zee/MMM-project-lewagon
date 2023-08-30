import streamlit as st
import time

st.sidebar.markdown("# 🧮 Prediction")


#Prediction
st.subheader('Predict Your Sales', divider='rainbow')
facebook = st.number_input('Insert your budget for Facebook')
tiktok = st.number_input('Insert your budget for Tiktok')
google = st.number_input('Insert your budget for Google')
st.write(f"""The current budget for Facebook is: {facebook},
         for Tiktok is: {tiktok}, and for Google is: {google}""")


if st.button('prediction'):
    with st.spinner('Wait for it...'):
        time.sleep(5)
    st.success('Done!')
