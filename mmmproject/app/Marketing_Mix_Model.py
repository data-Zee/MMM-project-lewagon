import streamlit as st
import pandas as pd
import os


title = '<p style="font-family:sans-serif; color:Green; font-size: 48px;">Marketing Mix Model</p>'
st.markdown(title, unsafe_allow_html=True)
st.markdown("""
<div style="text-align: justify;"><p style="font-family:sans-serif; font-size: 18px;">
Welcome to our website, where we delve into the realm of marketing data analysis. Our project aims to empower you to predict sales trends based on factors such as seasonality and marketing budget allocation across popular platforms like Google, Facebook, and TikTok.

<p style="font-family:sans-serif; font-size: 18px;">
Within this platform, you'll discover an insightful exploration of data trends in marketing.Beyond that, our predictive model enables you to estimate total sales for this specific product, offering valuable insights for optimizing marketing strategies. We've designed this interface with user-friendliness in mind, making it accessible for anyone looking to gain a deeper understanding of marketing dynamics and make data-driven decisionsr!

</div></p>""",unsafe_allow_html=True)
# new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">New image</p>'
# st.markdown(new_title, unsafe_allow_html=True)

if __name__ == "__main__":
    print(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "setup.py"))
