# streamlit is a python lib to create web apps for data projects - without needing HTML ,CSS or JavaScript
# It turns your python scripts into interactive web apps just by running a script.

import streamlit as st

st.title("Title Thala")
st.header("thala dhan pooleey")
st.subheader("subheader thala")
st.text("text thala")
st.markdown("## markdown thala")

# input widgets
name = st.text_input("Enter name if you are fan of thala")
age = st.slider("Enter age",0,100,20)
if name and age:
   st.write(f"Hello {name}, you are {age} years old and a true fan of thala!")

st.write("write thala")
st.code("code thala")

st.link_button("https://www.google.com","google thala")
st.button("button thala")
