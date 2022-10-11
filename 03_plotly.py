# import libraries

from turtle import width
import streamlit as st
import plotly.express as px
import pandas as pd

# import dataset

st.title("Combine plotly and streamlit to make a app")
df = px.data.gapminder()
st.write(df)

st.title("Only heads")
st.write(df.head())

st.title("Only columns")
st.write(df.columns)

# Summary Stats for EDA
st.write(df.describe())

# Data Management
year_option = df["year"].unique().tolist()
year = st.selectbox("Which year should we plot",year_option,0)
# df = df[df["year"]==year] # To show animation we should remove comment this

# Show Graph using plotly
fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent",hover_name="continent",
                log_x=True, size_max=55, range_x=[100,100000],range_y=[20,90],animation_frame="year",animation_group="country")
fig.update_layout(width=800,height=400)
st.write(fig)