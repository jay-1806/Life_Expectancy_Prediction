import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model_path = "Life_Expectancy_Prediction.pkl"
with open(model_path, "rb") as model_file:
    rf_model = pickle.load(model_file)

# Function to predict life expectancy
def predict_life_expectancy(features):
    return rf_model.predict(features)

# Streamlit App
def main():
    st.title("Life Expectancy Prediction App")

    # User input for prediction
    year = st.number_input("Enter the year:", min_value=2000, max_value=2025, value=2020)
    status = st.radio("Select the country status:", ["Developed", "Developing"])
    population = st.number_input("Enter the population:", min_value=0, value=20835722)
    hepatitis_b = st.number_input("Enter hepatitis B coverage (%):", min_value=0, max_value=100, value=87)
    measles = st.number_input("Enter measles cases:", min_value=0, value=2500)
    alcohol = st.number_input("Enter alcohol consumption (liters):", min_value=0.0, value=7.0)
    bmi = st.number_input("Enter BMI:", min_value=0.0, value=28.0)
    polio = st.number_input("Enter polio coverage (%):", min_value=0, max_value=100, value=90)
    diphtheria = st.number_input("Enter diphtheria coverage (%):", min_value=0, max_value=100, value=88)
    hiv_aids = st.number_input("Enter HIV/AIDS prevalence (%):", min_value=0.0, value=2.0)
    gdp = st.number_input("Enter GDP per capita:", min_value=0, value=51386)

    # Convert status to binary (Developed=0, Developing=1)
    status_binary = 0 if status == "Developed" else 1

    # Create a DataFrame with user inputs
    user_inputs = pd.DataFrame({
        'year': [year],
        'status': [status_binary],
        'population': [population],
        'hepatitis_b': [hepatitis_b],
        'measles': [measles],
        'alcohol': [alcohol],
        'bmi': [bmi],
        'polio': [polio],
        'diphtheria': [diphtheria],
        'hiv/aids': [hiv_aids],
        'gdp': [gdp],
    })

    # Make a prediction
    prediction = predict_life_expectancy(user_inputs)

    # Display the prediction
    st.subheader("Predicted Life Expectancy:")
    st.write(prediction)

# Run the app
if __name__ == "__main__":
    main()
