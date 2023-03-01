import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction") #display a title in the webapp

    st.write("""### We need some information to predict the salary""") #three hashtages means h3

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    #create a select box
    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)

    #create a slider
    experience = st.slider("Years of Experience", 0, 50, 3)

    #add a button
    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:, 0])
        X[:, 1] = le_education.transform(X[:, 1])
        X = X.astype(float)

        #calculate the prediction
        salary = regressor.predict(X)
        #display the prediction
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")