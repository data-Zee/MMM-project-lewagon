import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

#DATA
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fb_2023-08-24_AllTimeExcludingNL-Guido.csv")
fb_data=pd.read_csv(path)

st.subheader('Facebook Visualisations', divider='rainbow')
st.sidebar.markdown("# Facebook")
tab1, tab2 = st.tabs(["plot1", "plot2"])

#FIRST PLOT

# with tab1:
#    st.header("plot1")
#    st.pyplot(fig1)


#SECOND PLOT

# with tab2:
#    st.header("plot2")
#    st.pyplot(fig2)



# import numpy as np
# import plotly.figure_factory as ff

# # Add histogram data
# x1 = np.random.randn(200) - 2
# x2 = np.random.randn(200)
# x3 = np.random.randn(200) + 2

# # Group data together
# hist_data = [x1, x2, x3]

# group_labels = ['Group 1', 'Group 2', 'Group 3']

# # Create distplot with custom bin_size
# fig = ff.create_distplot(
#         hist_data, group_labels, bin_size=[.1, .25, .5])

# # Plot!
# st.plotly_chart(fig, use_container_width=True)


import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)
