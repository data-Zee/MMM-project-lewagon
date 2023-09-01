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



st.sidebar.markdown("# 📈 Plots")
st.subheader('Visualisations', divider='rainbow')
tab1, tab2, tab3, tab4 = st.tabs(["Sales/Spend Data vs Time","Clicks/Impressions vs Total Sales","Cost Per Clicks / Impressions vs Total Sales","Average ROI vs Weekday"])

#FIRST PLOT
fig1 = make_subplots()
fig1.add_trace(go.Scatter(x=df.index,y=df['Total_Spend'],name='Total Spend'))
fig1.add_trace(go.Scatter(x=df.index,y=df['total_sales'], name='Total Sales'))
# Set x-axis title
fig1.update_xaxes(title_text="Date")
# Set y-axes titles
fig1.update_yaxes(title_text="Amount")
with tab1:
    st.header("Sales / Spend Data vs Time")
    st.plotly_chart(fig1)


#SECOND PLOT
fig2 = make_subplots(rows=1,cols=2,subplot_titles=("Subplot 1", "Subplot 2"))
fig2.add_trace(go.Scatter(x=df['tt_clicks'],y=df['total_sales'],name='TikTok',mode='markers',marker={'color':'red'}),row=1,col=1)
fig2.add_trace(go.Scatter(x=df['fb_clicks'],y=df['total_sales'], name='Facebook',mode='markers',marker={'color':'blue'}),row=1,col=1)
fig2.add_trace(go.Scatter(x=df['google_clicks'],y=df['total_sales'],name='Google',mode='markers',marker={'color':'green'}),row=1,col=1)
fig2.update_layout(showlegend=False)#,row=1,col=2)
# Set x-axis title
fig2.update_xaxes(title_text="Clicks",row=1,col=1)
#FOR HAVING FRAME(in update_xaxes):mirror=True,showline=True, linecolor = 'lightgray'
# Set y-axes titles
fig2.update_yaxes(title_text="Total Sales",row=1,col=1,mirror=True)
fig2.add_trace(go.Scatter(x=df['tt_impressions'],y=df['total_sales'],name='TikTok',mode='markers',marker={'color':'red'}),row=1,col=2)
fig2.add_trace(go.Scatter(x=df['fb_impressions'],y=df['total_sales'], name='Facebook',mode='markers',marker={'color':'blue'}),row=1,col=2)
fig2.add_trace(go.Scatter(x=df['google_impressions'],y=df['total_sales'],name='Google',mode='markers',marker={'color':'green'}),row=1,col=2)
# Set x-axis title
fig2.update_xaxes(title_text="Impressions",row=1,col=2)
# Set y-axes titles
fig2.update_yaxes(title_text="Total Sales",row=1,col=2)
fig2.update_traces(marker_size=6,marker_line=dict(width=1, color='black'))
with tab2:
    st.header("Clicks / Impressions vs Total Sales")
    st.plotly_chart(fig2)


#THIRD PLOT
fig3 = make_subplots(rows=1,cols=2)
fig3.add_trace(go.Scatter(x=df['tt_cpc'],y=df['total_sales'],name='TikTok',mode='markers',marker={'color':'red'}),row=1,col=1)
fig3.add_trace(go.Scatter(x=df['fb_cpc'],y=df['total_sales'], name='Facebook',mode='markers',marker={'color':'blue'}),row=1,col=1)
fig3.add_trace(go.Scatter(x=df['google_cpc'],y=df['total_sales'],name='Google',mode='markers',marker={'color':'green'}),row=1,col=1)
# Set x-axis title
fig3.update_xaxes(title_text="Cost Per Clicks",row=1,col=1)
# Set y-axes titles
fig3.update_yaxes(title_text="Total Sales",row=1,col=1)
fig3.add_trace(go.Scatter(x=df['tt_cpm'],y=df['total_sales'],name='TikTok',mode='markers',marker={'color':'red'}),row=1,col=2)
fig3.add_trace(go.Scatter(x=df['fb_cpm'],y=df['total_sales'], name='Facebook',mode='markers',marker={'color':'blue'}),row=1,col=2)
fig3.add_trace(go.Scatter(x=df['google_cpm'],y=df['total_sales'],name='Google',mode='markers',marker={'color':'green'}),row=1,col=2)
# Set x-axis title
fig3.update_xaxes(title_text="Clicks Per Impressions",row=1,col=2)
# Set y-axes titles
fig3.update_yaxes(title_text="Total Sales",row=1,col=2)
fig3.update_traces(marker_size=6,marker_line=dict(width=1, color='black',colorscale='Viridis'))
with tab3:
    st.header("Cost Per Clicks / Impressions vs Total Sales")
    st.plotly_chart(fig3)


#FORTH PLOT
x=df.groupby(df.index.dayofweek)["ROI"].mean()
fig4 = make_subplots()
fig4.update_layout(showlegend=False)
fig4.add_trace(go.Scatter(x=x.index,y=x,mode='lines'))
fig4.update_xaxes(title_text="Weekday")
fig4.update_yaxes(title_text="Average ROI")
#fig1.update_title(title_text="Impressions vs Costs")
with tab4:
    st.header("Average ROI vs Weekday")
    st.plotly_chart(fig4)
