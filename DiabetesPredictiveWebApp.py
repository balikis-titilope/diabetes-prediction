# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 11:05:16 2025

@author: user
"""

import numpy as np
import pickle
import streamlit as st

#import the loaded model
loaded_model = pickle.load(open("C:/Users/user/OneDrive/Documents/Personal/ML Projects/Diabetes/Diabetes_trainedModel.sav", "rb"))

#creating a function
def diabetesPrediction(input_data):

    #changing input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    #reshaping the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if prediction[0] == 0:
        return "The person is not diabetic"
    else:
        return "The person is diabetic"


def main():
    #giving a title
    st.title("Diabetes Prediction Web App")
    
    #getting input from the user
    # Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age
    
    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure Value")
    SkinThickness = st.text_input("Skin thickness value/ Weight")
    Insulin = st.text_input("Insulin Level")
    BMI = st.text_input("BMI Value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    Age = st.text_input("Age of the user")
    
    #code for prediction
    diagnosis = ""
    
    #creating the button for prediction
    if st.button("Diabetes Test Result"):
        diagnosis = diabetesPrediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    st.success(diagnosis)


if __name__ ==  '__main__':
    main()
    
    
    
    
    
    
    
    
