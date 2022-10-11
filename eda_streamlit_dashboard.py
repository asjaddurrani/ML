import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from pandas_profiling import ProfileReport, profile_report
from streamlit_pandas_profiling import st_profile_report

# Title of webapp

st.markdown('''
# **Exploratory Data Analysis Web Application**
This app is developed by Muhammad Asjad
''')

# How to upload a file from pc

with st.sidebar.header("upload your dataset(.csv)"):
    uploaded_file = st.sidebar.file_uploader("upload your file", type = ["csv"])
    # df = sns.load_dataset("titanic")
    st.sidebar.markdown("[Example CSV file](https://www.kaggle.com/louise2001/quantum-physics-articles-on-arxiv-1994-to-2009)")

# Profiling report for pandas

if uploaded_file is not None:
    @st.cache   #  # function to save data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header("**Input DF**")
    st.write(df)
    st.write("---")
    st.header("**Profiling report with pandas**")
    st_profile_report(pr)
else:
    st.info("Awaiting for csv file")
    if st.button("Press to use example data"):
        @st.cache  # function to save data
        def load_data():
            a=pd.DataFrame(np.random.rand(100,5),
                        columns=["age","banana","cat","Deutschland","Ear"])
            return a

        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header("**Input DF**")
        st.write(df)
        st.write("---")
        st.header("**Profiling report with pandas**")
        st_profile_report(pr)