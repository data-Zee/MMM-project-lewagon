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



st.header('Facebook Visualisations', divider='green')
tab1, tab2,tab3 = st.tabs(["Impressions / Clicks vs Costs","Costs vs Impressions/Clicks","Monthly Impressions, Clicks, and Costs"])


#FIRST PLOT
fig1 = make_subplots(rows=1,cols=2)
fig1.update_layout(showlegend=False)
fig1.add_trace(go.Scatter(x=df["fb_impressions"],y=df["fb_cpm"],mode='markers',marker={'color':'#FF7F50'}),row=1,col=1)
fig1.update_xaxes(title_text="Impressions",row=1,col=1)
fig1.update_yaxes(title_text="Cost Impressions",row=1,col=1)
#fig1.update_title(title_text="Impressions vs Costs",row=1,col=1)
fig1.add_trace(go.Scatter(x=df["fb_clicks"],y=df["fb_cpc"],mode='markers',marker={'color':'#008000'}),row=1,col=2)
fig1.update_xaxes(title_text="Clicks",row=1,col=2)
fig1.update_yaxes(title_text="Cost Per Click",row=1,col=2)
#fig1.update_layout(title="Clicks vs Costs",row=1,col=2)
fig1.update_traces(marker_size=6,marker_line=dict(width=1, color='black'))
with tab1:
    st.subheader("Impressions/Clicks vs Costs")
    st.plotly_chart(fig1)
    st.markdown("""
    <div style="text-align: justify;">
    ✅ The Facebook impressions and clicks plot reflects the effectiveness of our marketing efforts on the platform.

    ✅ The cost per 1000 impressions and clicks serves as an indicator of user interest in our marketing content.

    ✅ Notably, fewer clicks on our advertisements lead to higher costs per click and impressions on Facebook, underlining the importance of user engagement.

    ✅ Conversely, increased clicks and impressions result in more cost-effective advertising. It's important to consider that other factors also impact pricing, but this data highlights the need for potential ad improvements or changes.

    ✅ **Keep in mind that**, in addition to user engagement, various other factors can influence the cost per click and cost per impression.
    </div>""",unsafe_allow_html=True)

#SECOND PLOT
fig2 = make_subplots(rows=1,cols=2)
fig2.update_layout(showlegend=False)
fig2.add_trace(go.Scatter(x=df["fb_impressions"],y=df["fb_costs"],mode='markers',marker={'color':'#FF7F50'}),row=1,col=1)
fig2.update_xaxes(title_text="Impressions",row=1,col=1)
fig2.update_yaxes(title_text="Costs",row=1,col=1)
fig2.add_trace(go.Scatter(x=df["fb_clicks"],y=df["fb_costs"],mode='markers',marker={'color':'#008000'}),row=1,col=2)
fig2.update_xaxes(title_text="Clicks",row=1,col=2)
fig2.update_yaxes(title_text="Costs",row=1,col=2)
fig2.update_traces(marker_size=6,marker_line=dict(width=1, color='black'))
with tab2:
    st.subheader("Costs vs Impressions/Clicks")
    st.plotly_chart(fig2)
    st.markdown("""
    <div style="text-align: justify;">
    ✅ The plots reveal a strong correlation between marketing costs on the Facebook platform and the volume of clicks and impressions received by the advertised products.

    ✅ There is compelling evidence that increased spending is directly linked to higher impressions and clicks for the products.

    ✅ This data underscores the significance of the marketing budget in influencing user engagement and product visibility on the Facebook platform.
    </div>""",unsafe_allow_html=True)

#THIRD PLOT
# Create figure with secondary y-axis
fig3 = make_subplots(specs=[[{"secondary_y": True}]])
fig3.add_trace(go.Scatter(x=df_monthly.index,y=df_monthly['fb_clicks'],name='Clicks',marker={'color':'#069AF3'}), secondary_y=False)
fig3.add_trace(go.Scatter(x=df_monthly.index,y=df_monthly['fb_impressions'], name='Impressions',marker={'color':'#008000'}), secondary_y=True)
fig3.add_trace(go.Scatter(x=df_monthly.index,y=df_monthly['fb_costs'],name='Costs',marker={'color':'#FF7F50'}), secondary_y=False)
fig3.update_xaxes(title_text="Date")
fig3.update_yaxes(title_text="Costs / Clicks", secondary_y=False)
fig3.update_yaxes(title_text="Impressions", secondary_y=True)
with tab3:
    st.subheader("Monthly Impressions, Clicks, and Costs")
    st.plotly_chart(fig3)
    st.markdown("""
    <div style="text-align: justify;">
    ✅ Visualizes Facebook platform metrics: Clicks, impressions, and costs.

    ✅ Highlights trends: Marketing spend dips before January and July, along with clicks and impressions.

    ✅ Shows spikes: Increased spending and engagement after the new year and in the summer.

    ✅ Provides a clear snapshot of campaign performance over time.
    </div>""",unsafe_allow_html=True)
