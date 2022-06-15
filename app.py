import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title = 'Insurance Premium Prediction App', page_icon = '🏥', layout = 'wide')

st.markdown("<h1 style='text-align: center; color: white;'>Health Insurance Premium Prediction App</h1>", unsafe_allow_html=True)

st.write('---')

name = st.text_input('Enter your name:')

st.subheader(f'Hi {name}')

st.markdown(f'''The Insurance Premium Prediction App can used to predict an estimate of medical expenses that can incur 
    based on their attributes and health conditions. This can assist a person in concentrating on the health side of their life 
    rather than the ineffective part. Insurance policies are being charged based on the person's age and medical conditions.
    To use the app, the user has to select the relevant options below to generate results. The generated results are predicted by the model
    which is already trained with the data of past insurance holders with their medical conditions. After entering the information,
    the app generates an estimate of the medical expenses that the user will incur.''')

# inputs
sex = st.selectbox("What is your gender?", ('male', 'female'))

age = st.slider("What is your age?", min_value=18, max_value=64)

bmi = st.slider("What is your BMI?", min_value=16.0, max_value=53.1, help='BMI stands for Body Mass Index. You can calculate your by using, BMI = weight/height^2')

children = st.selectbox("How many children do you have?", ('0', '1', '2', '3', '4', '5'))

smoker = st.selectbox("Do you have smoking tendencies?", ('yes', 'no'))

region = st.selectbox("What region do you belong?", ('northwest', 'northeast', 'southwest', 'southeast'))

# col names and created df for inputs
cols = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']

data = pd.DataFrame([[age, sex, bmi, children, smoker, region]], columns = cols)


def predict_premium(df):
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    prediction = model.predict(df)
    print(prediction)
    return prediction


if(st.button('Predict')):
    result = ''
    result = predict_premium(data)
    st.write('---')
    st.success('Your Estimated Medical Expenses Bill is {} USD'.format(np.around(*result, decimals=2)))
    st.write('---')
# remove main menu and footer note of streamlit
hide_menu_style = '''
       <style>
       #MainMenu {visibility: hidden;}
       footer{visibility: hidden;}
       </style>
        '''
st.markdown(hide_menu_style, unsafe_allow_html=True)