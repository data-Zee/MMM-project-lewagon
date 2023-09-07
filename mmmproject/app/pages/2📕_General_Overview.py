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
path2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "df_avg.csv")
df_avg=pd.read_csv(path2)
path3 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "df_avg_cpc_cpm.csv")
df_avg_cpc_cpm=pd.read_csv(path3)
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


st.header('General Overview', divider='green')
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Monthly Sales/Spend/ROI","Media Buying","Impressions/Clicks vs Total Sales","Media Impressions/Clicks/Costs Corr To Sale","new","Average ROI vs Weekday"])

#FIRST PLOT
fig1_1 = make_subplots()
fig1_1.add_trace(go.Scatter(x=df.index,y=df['Total_Spend'],name='Total Spend',marker={'color':'#FF7F50'}))
fig1_1.add_trace(go.Scatter(x=df.index,y=df['total_sales'], name='Total Sales',marker={'color':'#008000'}))
# Set x-axis title
fig1_1.update_xaxes(title_text="Date")
# Set y-axes titles
fig1_1.update_yaxes(title_text="Amount ( € )")


fig1_2 = make_subplots()
fig1_2.add_trace(go.Scatter(x=df.index,y=df['ROI'], name='ROI',marker={'color':'#008000'}))
# Set x-axis title
fig1_2.update_xaxes(title_text="Date")
# Set y-axes titles
fig1_2.update_yaxes(title_text="ROI")
fig1_2.update_layout(xaxis_range=['2022-02-01','2023-08-24'])
fig1_2.update_layout(yaxis_range=[0,15])

with tab1:
    st.subheader("Monthly Sales/Spend")
    st.plotly_chart(fig1_1)
    st.subheader("Return On Investment")
    st.plotly_chart(fig1_2)
    st.markdown("""
    <div style="text-align: justify;">
    ✅ July (summer) seasonality is clearly visible.

    ✅ We improved ROI while increasing marketing spend which is a positive business result.
    </div>""",unsafe_allow_html=True)


#SECOND PLOT
fig2 = make_subplots(rows=1,cols=2)
fig2.add_trace(go.Scatter(x=df.index,y=df['Total_Spend_CPM'],marker={'color':'#008000'},showlegend=False),row=1,col=1)
fig2.update_xaxes(title_text="Date",row=1,col=1)
fig2.update_yaxes(title_text="Click Per Impression",row=1,col=1)
fig2.add_trace(go.Scatter(x=df.index,y=df['Total_Spend_CPC'],marker={'color':'#008000'},showlegend=False),row=1,col=2)
fig2.update_xaxes(title_text="Date",row=1,col=2)
fig2.update_yaxes(title_text="Cost Per Click",row=1,col=2)
with tab2:
    st.subheader("Media Buying")
    st.plotly_chart(fig2)
    st.markdown("""
    <div style="text-align: justify;">
    ✅ We can see that during season Click Per Impressions’ are increasing → competition is rising

    ✅ BUT! we can see that Cost Per Clicks in 2023 dropped during high season meaning we did a good job in terms of marketing strategy/activity.
    </div>""",unsafe_allow_html=True)


#THIRD PLOT
fig3 = make_subplots(rows=1,cols=2)
fig3.add_trace(go.Scatter(x=df['tt_impressions'],y=df['total_sales'],name='TikTok',mode='markers',marker={'color':'#FF7F50'}),row=1,col=1)
fig3.add_trace(go.Scatter(x=df['fb_impressions'],y=df['total_sales'], name='Facebook',mode='markers',marker={'color':'#069AF3'}),row=1,col=1)
fig3.add_trace(go.Scatter(x=df['google_impressions'],y=df['total_sales'],name='Google',mode='markers',marker={'color':'#008000'}),row=1,col=1)
# Set x-axis title
fig3.update_xaxes(title_text="Impressions",row=1,col=1)
# Set y-axes titles
fig3.update_yaxes(title_text="Total Sales",row=1,col=1)
fig3.add_trace(go.Scatter(x=df['tt_clicks'],y=df['total_sales'],name='TikTok',mode='markers',marker={'color':'#FF7F50'},showlegend=False),row=1,col=2)
fig3.add_trace(go.Scatter(x=df['fb_clicks'],y=df['total_sales'], name='Facebook',mode='markers',marker={'color':'#069AF3'},showlegend=False),row=1,col=2)
fig3.add_trace(go.Scatter(x=df['google_clicks'],y=df['total_sales'],name='Google',mode='markers',marker={'color':'#008000'},showlegend=False),row=1,col=2)
#fig2.update_layout(showlegend=False,row=1,col=2)
# Set x-axis title
fig3.update_xaxes(title_text="Clicks",row=1,col=2)
#FOR HAVING FRAME(in update_xaxes):mirror=True,showline=True, linecolor = 'lightgray'
# Set y-axes titles
fig3.update_yaxes(title_text="Total Sales",row=1,col=2)

fig3.update_traces(marker_size=6,marker_line=dict(width=1, color='black'))
with tab3:
    st.subheader("Impressions/Clicks vs Total Sales")
    st.plotly_chart(fig3)
    st.markdown("""
    <div style="text-align: justify;">
    ✅ We can see there is a positive correlation to the overall marketing spend and sales.

    ✅ Google is showing the strongest sales based on few impressions which makes sense as it is usually an important pull channel.

    ✅ When looking at the “Impressions to total sales” scatter plot, TikTok seems to show better sales results based on fewer impressions than Facebook → we know it is more a view platform or perhaps we had view objectives for the campaigns active compared to Facebook campaigns.

    ✅ Facebook needs higher amount of impressions (or has higher frequency) in order to get higher sales.

    ✅ For clicks TikTok is showing a difference when comparing Impressions with Clicks to sales. The clicks generated do not seem to result in direct sales.
    </div>""",unsafe_allow_html=True)


#FORTH PLOT
df_corr1=df[['orders', 'total_sales',
       'fb_impressions',  'google_impressions', 'tt_impressions', 'Total_Spend', 'ROI']].corr()
labels1=['Orders', 'Total_sales','Facebook_impressions',  'Google_impressions', 'Tiktok_impressions', 'Total_Spend', 'ROI']
fig4_1=go.Figure(data=go.Heatmap(z=df_corr1, colorscale='greens',x=labels1,y=labels1))
fig4_1.layout.height = 600
fig4_1.layout.width = 600

df_corr2=df[['orders', 'total_sales',
             'fb_clicks',  'google_clicks', 'tt_clicks', 'Total_Spend', 'ROI']].corr()
labels2=['Orders', 'Total_sales',
             'Facebook_clicks',  'Google_clicks', 'Tiktok_clicks', 'Total_Spend', 'ROI']
fig4_2=go.Figure(data=go.Heatmap(z=df_corr2, colorscale='oranges',x=labels2,y=labels2))
fig4_2.layout.height = 600
fig4_2.layout.width = 600

df_corr3=df[['orders', 'total_sales',
             'fb_costs',  'google_costs', 'tt_costs', 'Total_Spend', 'ROI']].corr()
labels3=['Orders', 'Total_sales',
             'Facebook_costs',  'Google_costs', 'Tiktok_costs', 'Total_Spend', 'ROI']
fig4_3=go.Figure(data=go.Heatmap(z=df_corr3, colorscale='blues',x=labels3,y=labels3))

fig4_3.layout.height = 600
fig4_3.layout.width = 600
with tab4:
    st.subheader('Social Media Impressions Corr To Sale')
    st.plotly_chart(fig4_1)
    st.subheader("Social Media Clicks Corr To Sale")
    st.plotly_chart(fig4_2)
    st.subheader("Social Media Costs Corr To Sale")
    st.plotly_chart(fig4_3)
    st.markdown("""
    <div style="text-align: justify;">
    ✅ We can see that there is indeed a correlation between facebook impressions with orders and total sales (revenue).

    ✅ When looking at the clicks correlation data, Google clicks correlate with orders and total sales which we could already see in the scatter plots.

    ✅ But also the total (marketing) spend is correlated to orders and total sales.

    ✅ TikTok clicks is showing the least correlation to orders and sales which we also already noticed in the scatter plots.

    ✅ Lastly we see that Facebook costs in particular is effecting the ROI which may tells us we should watch out with spending too much on Facebook. Trying to find a better sweet spot. Of course this makes sense as it is the highest spending channel.
    </div>""",unsafe_allow_html=True)

# ##FIFTH PLOT
# fig5 = make_subplots(rows=1,cols=2)
# fig5.add_trace(go.Bar(x=df_avg,y=df['% Clicks'], name=, marker={'color':'#008000'},orientation='v'),row=1,col=1)
# fig5.add_trace(go.Bar(x=df_avg,marker={'color':'#008000'},orientation='v'),row=1,col=1)
# fig5.add_trace(go.Bar(x=df_avg,marker={'color':'#008000'},orientation='v'),row=1,col=1)
# fig3.update_xaxes(title_text="Amount",row=1,col=1)
# fig3.update_yaxes(title_text="Percentage Value",row=1,col=1)
# fig5.add_trace(go.Bar(x=df_avg_cpc_cpm,marker={'color':'#069AF3'}, orientation='v'),row=1,col=2)
# fig5.add_trace(go.Bar(x=df_avg,marker={'color':'#008000'},orientation='v'),row=1,col=2)
# fig5.add_trace(go.Bar(x=df_avg,marker={'color':'#008000'},orientation='v'),row=1,col=2)
# fig3.update_xaxes(title_text="Company",row=1,col=2)
# fig3.update_yaxes(title_text="Average Value",row=1,col=2)
# with tab5:
#     st.subheader("Percentage From Total/Average CPC & CPM")
#     st.plotly_chart(fig5)
# #fig.update_layout(barmode='group')


#SIXTH PLOT
x=df.groupby(df.index.dayofweek)["ROI"].mean()
fig6 = make_subplots()
fig6.update_layout(showlegend=False)
fig6.add_trace(go.Scatter(x=x.index.map({0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}),y=x,mode='lines',marker={'color':'#008000'}))
fig6.update_xaxes(title_text="Weekday")
fig6.update_yaxes(title_text="Average ROI")
with tab6:
    st.subheader("Average ROI vs Weekday")
    st.plotly_chart(fig6)
    st.markdown("""
    <div style="text-align: justify;">
    ✅ The graphs clearly reveal that our average return on investment (ROI) is at its lowest on Fridays and Saturdays, suggesting these days witness the weakest sales performance throughout the week.

    ✅ To address this, we should delve into the underlying reasons behind this trend and consider tailored marketing strategies to potentially boost sales during these weekend days.
    </div>""",unsafe_allow_html=True)
