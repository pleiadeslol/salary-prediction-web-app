import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

#create a sidebar
page = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))

#show predict or explore page
if page == "Predict":
    show_predict_page()
else: 
    show_explore_page()
