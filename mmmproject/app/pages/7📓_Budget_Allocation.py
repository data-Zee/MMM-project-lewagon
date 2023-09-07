import streamlit as st
import time
import requests
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import datetime


#Prediction
st.header('Best Fit for Your Advertisements Budget', divider='green')
budget = st.number_input('Insert your budget for advertising')
date = st.date_input("Insert your prefer date for prediction", datetime.date(2023, 9, 8))
st.write(f"""The current budget for advertising is: {round(budget,2)}, and date is: {date}""")

url='https://mmm-lewagon-iainnplz7a-ew.a.run.app/budgetdivider'
params={'TOTAL_DAILY_BUDGET':budget,
        'Date':date}

if st.button('Best Fit'):
    with st.spinner('Wait for it...'):
        time.sleep(1)
        response=requests.get(url,params).json()
        st.success(f" Google Budget= {round(response['Google Budget'],2)}!")
        st.success(f" Facebook Budget= {round(response['Facebook Budget'],2)} !")
        st.success(f" Tiktok Budget= {round(response['Tiktok Budget'],2)} !")
        st.success(f" Total Clicks= {round(response['Total_clicks'],2)} !")
        labels = ['Google', 'Facebook', 'Tiktok']
        values = [round(response['Google Budget'],2), round(response['Facebook Budget'],2), round(response['Tiktok Budget'],2)]
        colors=['#008000','#069AF3','#FF7F50']

        fig = go.Figure(data=[go.Pie(labels=labels, values=values#, hole=.3
                                    )])
        fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=20,
                        marker=dict(colors=colors, line=dict(color='#000000', width=2)))
        st.plotly_chart(fig)
