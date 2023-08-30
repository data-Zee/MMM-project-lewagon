import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

st.sidebar.markdown("# 📈 Plots")

data=pd.read_csv('../raw_data/df.csv')

#Plots
st.subheader('Visualisations', divider='rainbow')

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
st.pyplot(fig2)

#THIRD PLOT
# Set the style for the plot (optional)
sns.set(style="whitegrid")
# Create the scatter plot using Seaborn
fig3=plt.figure(figsize=(10, 6))
sns.scatterplot(x='tt_costs', y='total_sales', data=data, label='TikTok', color='blue')
sns.scatterplot(x='fb_costs', y='total_sales', data=data, label='Facebook', color='green')
sns.scatterplot(x='google_costs', y='total_sales', data=data, label='Google', color='orange')
# Set plot title and labels
plt.title('Costs vs. Total Sales')
plt.xlabel('Costs')
plt.ylabel('Total Sales')
# Show legend
plt.legend()
# Show the plot
st.pyplot(fig3)
