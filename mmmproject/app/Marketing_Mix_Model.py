import streamlit as st
import pandas as pd
import os


st.title("Marketing Mix Model")
st.sidebar.markdown("# Dashboard")


if __name__ == "__main__":
    print(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "setup.py"))
