import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

# Make Containers
header = st.container()
data_sets = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Titanic ki app")
    st.text("In this project we will work on a titanic dataset")

with data_sets:
    st.header("ship is floating")
    st.text("We will work with titanic dataset")

    # Load dataset
    df = sns.load_dataset("titanic") 

    # Drop nan values
    df = df.dropna()

    # show dataset   
    st.write(df.head(10)) 

    # Bar Plot 
    st.subheader("Bar plot according to sex")   
    st.bar_chart(df["sex"].value_counts())

    # Other plots
    st.subheader("Bar plot according to class")
    st.bar_chart(df["class"].value_counts())

    # Random sample
    st.bar_chart(df["age"].sample(10))



with features:
    st.header("There are our app features")
    st.text("We will add many features")
    st.markdown("**Feature 1:** We are using markdown")
    st.markdown("**Feature 2:** We are using markdown")

with model_training:
    st.header("ship walon ka kiya bana")
    st.text("we will set our parameters")

    # Making columns
    input,display = st.columns(2)

    # Selection points
    max_depth = input.slider("How many people do you know", min_value=10,max_value=100,value=20,step=5)

    # n_estimator
    n_estimators = input.selectbox("How many tree should be their in a RF",options = [50,100,200,300,"No_Limit"])

    # Select feature
    input.write(df.columns)

    # input feature from user
    input_feature = input.text_input("which feature we should use")

    # Machine Learning Model
    model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

    if n_estimators == "No_Limit" :
        model = RandomForestRegressor(max_depth=max_depth)
    else:
        model = RandomForestRegressor(max_depth=max_depth,n_estimators=n_estimators)

    # Define X and y
    X = df[[input_feature]]
    y = df[["fare"]]

    # fit our model
    model.fit(X,y)
    pred = model.predict(y)

    # Display metrices
    display.subheader("Mean absolute error of the model is: ")
    display.write(mean_absolute_error(y,pred))

    display.subheader("Mean squared error of the model is: ")
    display.write(mean_squared_error(y,pred))

    display.subheader("R squared score of the model is: ")
    display.write(r2_score(y,pred))

