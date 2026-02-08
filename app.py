import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('heart_model.sav', 'rb'))

# creating a function for prediction
def heart_disease_prediction(input_data):

    # changing the input-data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshaped()

    prediction = loaded_model.predict(input_data_reshaped)
    
    if prediction[0] == 0:
        return 'The person does not have heart disease'
    else:
        return 'The person has heart disease'
    
def main():

    # giving a title
    st.title('Heart Disease Prediction Web App')

    # getting the input data from the user
    age = st.text_input('Enter your age')
    sex = st.text_input('Male / Female')
    cp = st.text_input('Select chest pain category')
    trestbps = st.text_input('Blood pressure at rest')
    chol = st.text_input('Cholesterol level')
    fbs = st.text_input('Above 120 mg/dl (Yes/No)')
    restecg = st.text_input('ECG test result')
    thalach = st.text_input('Highest heart rate achieved')
    exang = st.text_input('Chest pain during exercise (Yes/No)')
    oldpeak = st.text_input('Exercise-induced ST depression')
    slope = st.text_input('ST segment slope')
    ca = st.text_input('Number of major blood vessels')
    thal = st.text_input('lood disorder type')

    # code for Prediction
    pridiction = ''

    # creating button for prediction
    if st.button('Heart Disease Result'):
        if "" in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]:
            st.error("Please fill in all fields with numeric values.")
        else:
            # run prediction
            prediction = heart_disease_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
            st.success(prediction)

if __name__ == '__main__':
    main()