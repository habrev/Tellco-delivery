import streamlit as st
import pandas as pd
import plotly.express as px

st.title("User Overview Analysis")

# Sample data
data = pd.DataFrame({
    "Region": ["North", "South", "East", "West"],
    "Users": [1000, 1500, 1200, 800]
})

# Visualization
fig = px.bar(data, x="Region", y="Users", title="Total Users by Region")
st.plotly_chart(fig)
