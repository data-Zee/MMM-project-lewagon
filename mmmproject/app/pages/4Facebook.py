import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots


#DATA
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "df_NAN.csv")
df=pd.read_csv(path)
channels_spend = ["tt_costs", "fb_costs", "google_costs"]
df["Total_Spend"] = df[channels_spend].sum(axis=1)
df.drop(columns=['Unnamed: 0'], inplace=True, axis=1)
df['ROI']= df['total_sales']/df["Total_Spend"]
df['fb_cpc']=df['fb_costs']/df['fb_clicks']
df['tt_cpc']=df['tt_costs']/df['tt_clicks']
df['google_cpc']=df['google_costs']/df['google_clicks']
df['fb_cpm']=(df['fb_costs']/df['fb_impressions'])*1000
df['tt_cpm']=(df['tt_costs']/df['tt_impressions'])*1000
df['google_cpm']=(df['google_costs']/df['google_impressions'])*1000
channels_spend_CPC = ["tt_cpc", "fb_cpc", "google_cpc"]
df["Total_Spend_CPC"] = df[channels_spend_CPC].sum(axis=1)
channels_spend_CPM = ["tt_cpm", "fb_cpm", "google_cpm"]
df["Total_Spend_CPM"] = df[channels_spend_CPM].sum(axis=1)
# Convert 'Day' column to datetime type
df['Day'] = pd.to_datetime(df['Day'])
# Set 'Day' column as index
df.set_index('Day', inplace=True)
# Check if the index is a DatetimeIndex
print(df.index)
# Resample data by month and aggregate using sum (you can use other aggregation functions)
df_monthly = df.resample('M').sum()



st.subheader('Facebook Visualisations', divider='green')
st.sidebar.markdown("# Facebook")
tab1, tab2 = st.tabs(["Impressions / Clicks vs Costs","Monthly Impressions, Clicks, and Costs"])


#FIRST PLOT
fig1 = make_subplots(rows=1,cols=2)
fig1.update_layout(showlegend=False)
fig1.add_trace(go.Scatter(x=df["fb_impressions"],y=df["fb_cpm"],mode='markers',marker={'color':'#FF7F50'}),row=1,col=1)
fig1.update_xaxes(title_text="Impressions",row=1,col=1)
fig1.update_yaxes(title_text="Clicks per Impressions",row=1,col=1)
#fig1.update_title(title_text="Impressions vs Costs",row=1,col=1)
fig1.add_trace(go.Scatter(x=df["fb_clicks"],y=df["fb_cpc"],mode='markers',marker={'color':'#008000'}),row=1,col=2)
fig1.update_xaxes(title_text="Clicks",row=1,col=2)
fig1.update_yaxes(title_text="Cost Per Clicks",row=1,col=2)
#fig1.update_layout(title="Clicks vs Costs",row=1,col=2)
fig1.update_traces(marker_size=6,marker_line=dict(width=1, color='black'))
with tab1:
    st.header("Facebook Impressions / Clicks vs Costs")
    st.plotly_chart(fig1)


#SECOND PLOT
# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig2.add_trace(go.Scatter(x=df_monthly.index,y=df_monthly['fb_clicks'],name='Clicks',marker={'color':'#069AF3'}), secondary_y=False)
fig2.add_trace(go.Scatter(x=df_monthly.index,y=df_monthly['fb_impressions'], name='Impressions',marker={'color':'#008000'}), secondary_y=True)
fig2.add_trace(go.Scatter(x=df_monthly.index,y=df_monthly['fb_costs'],name='Costs',marker={'color':'#FF7F50'}), secondary_y=False)
# Set x-axis title
fig2.update_xaxes(title_text="Date")
# Set y-axes titles
fig2.update_yaxes(title_text="Costs / Clicks", secondary_y=False)
fig2.update_yaxes(title_text="Impressions", secondary_y=True)
with tab2:
    st.header("Facebook Monthly Impressions, Clicks, and Costs")
    st.plotly_chart(fig2)
