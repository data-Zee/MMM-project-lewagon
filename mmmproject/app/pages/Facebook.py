import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

#DATA
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "df.csv")
data=pd.read_csv(path)

st.subheader('Facebook Visualisations', divider='rainbow')
st.sidebar.markdown("# Facebook")
tab1, tab2 = st.tabs(["plot1", "plot2"])

#FIRST PLOT
# Set the style for the plot (optional)
sns.set(style="whitegrid")
# Create the scatter plot using Seaborn
fig1=plt.figure(figsize=(10, 6))
sns.scatterplot(x='tt_clicks', y='total_sales', data=data, label='TikTok', color='blue')
sns.scatterplot(x='fb_clicks', y='total_sales', data=data, label='Facebook', color='green')
sns.scatterplot(x='google_clicks', y='total_sales', data=data, label='Google', color='orange')
# Set plot title and labels
plt.title('Clicks vs. Total Sales')
plt.xlabel('Clicks')
plt.ylabel('Total Sales')
# Show legend
plt.legend()
# Show the plot
with tab1:
   st.header("plot1")
   st.pyplot(fig1)


#SECOND PLOT
# Set the style for the plot (optional)
sns.set(style="whitegrid")
# Create the scatter plot using Seaborn
fig2=plt.figure(figsize=(10, 6))
sns.scatterplot(x='tt_impressions', y='total_sales', data=data, label='TikTok', color='blue')
sns.scatterplot(x='fb_impressions', y='total_sales', data=data, label='Facebook', color='green')
sns.scatterplot(x='google_impressions', y='total_sales', data=data, label='Google', color='orange')
# Set plot title and labels
plt.title('Impressions vs. Total Sales')
plt.xlabel('Impressions')
plt.ylabel('Total Sales')
# Show legend
plt.legend()
# Show the plot
with tab2:
   st.header("plot2")
   st.pyplot(fig2)
