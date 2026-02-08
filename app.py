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
    input_data_reshaped = input_data_as_numpy_array.reshape()

    prediction = loaded_model.predict(input_data_reshaped)
    
    if prediction[0] == 0:
        return 'The person does not have heart disease'
    else:
        return 'The person has heart disease'
    
def main():

    # giving a title
    st.title('Heart Disease Prediction Web App')

    # getting the input data from the user
    age = st.number_input('Enter your age', min_value=0, max_value=120, step=1)
    
    sex = st.selectbox('Male / Female', ['Male','Female'])
    sex = 1 if sex =='Male' else 0
    
    cp = st.selectbox('Select chest pain category', [0,1,2,3])
    
    trestbps = st.number_input('Blood pressure at rest', min_value=0)
    
    chol = st.number_input('Cholesterol level', min_value=0)

    fbs = st.selectbox('Above 120 mg/dl (Yes/No)', ['Yes','No'])
    fbs = 1 if fbs == 'Yes' else 0

    restecg = st.selectbox('ECG test result', [0,1,2])

    thalach = st.number_input('Highest heart rate achieved', min_value=0)

    exang = st.selectbox('Chest pain during exercise (Yes/No)', ['Yes','No'])
    exang = 1 if exang == 'Yes' else 0

    oldpeak = st.number_input('Exercise-induced ST depression', min_value=0.0, step=0.1)

    slope = st.selectbox('ST segment slope', [0,1,2])

    ca = st.number_input('Number of major blood vessels', min_value=0, max_value=4, step=1)
    
    thal = st.selectbox('lood disorder type', [1,2,3])

    # Prediction button
    if st.button('Heart Disease Result'):
        input_data = [
            age, sex, cp, trestbps, chol, fbs,
            restecg, thalach, exang, oldpeak,
            slope, ca, thal
        ]
        result = heart_disease_prediction(input_data)
        st.success(result)
    
if __name__ == '__main__':
    main()

