# Streamlit is a application view of our work.

import streamlit as st
import seaborn as sns

st.header("Hellow my name is asjad") # heading
st.text("Hellow my name is asjad")  # small font

df = sns.load_dataset("iris")
st.write(df.head(10))  # all dataset loaded
st.write(df[["species","sepal_length","petal_length"]].head(10)) # only two columns

st.bar_chart(df["sepal_length"])
st.line_chart(df["sepal_length"])