import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name")

# Using the slider
age = st.slider("Select your age: ", 0,100,25)
st.write(f"Your age is, {age}")

# Using the select box

# 1. Define the source array
options = ["Python","Java","C++","Javascript"]
choice = st.selectbox("Choose your favourite programming language : ", options)
st.write(f"You have selected : {choice}")

if name:
    st.write(f"Hello, {name}")

# Creating the dataframe
data = {
    "Name" : ["John","Jane","Jake","Jill"],
    "Age" : [28,24,35,40],
    "City" : ["New York", "Los Angeles","Chicago","Houston"]
}
df = pd.DataFrame(data)
# displaying the dataframe
st.write(df)

# converting the dataframe into csv
df.to_csv("sampledata.csv")

#Creating an upload file button
uploaded_file = st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)




