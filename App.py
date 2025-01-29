# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:24:49 2025

@author: fortu
"""

import streamlit as st

st. title("streamlit is amazing!")
st.title("Streamlit is is awesome")

st.title("NEVER USE SPACES IN FUNCTIONS")

# My Plot of data

import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Title heading")

st.write("Hello, Streamlit!")

st.header("Sample Data")

data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})

# Display the data in the Streamlit app
st.write(data)

# Create a Plotly figure
fig = px.line(data, x="x", y="y", title="Simple Plotly Example")

# Display the plot in the Streamlit app
st.plotly_chart(fig)