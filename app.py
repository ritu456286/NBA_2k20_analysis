import streamlit as st
import pickle 
# import sklearn
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from PIL import Image

model = pickle.load(open('model.sav', 'rb'))

st.title('Player Salary Prediction')
st.sidebar.header('Input Player Data')
image = Image.open('bb_img.jpg')
st.image(image, 'Basketball') #Basketball is the caption of the image


#Function
def user_input():
    rating = st.sidebar.slider('Rating', 50, 100, value=50)
    jersey = st.sidebar.slider('Jersey', 0, 100, 0)
    team = st.sidebar.slider('Team', 0, 30, 0)
    position = st.sidebar.slider('Position', 0, 10, 0)
    country = st.sidebar.slider('Country', 0, 3, 0)
    draft_year = st.sidebar.slider('Draft Year', 2000, 2020, 2000)
    draft_round = st.sidebar.slider('Draft Round', 1,10, 0)
    draft_peak = st.sidebar.slider('Draft Peak', 1, 30, 0)


    user_input_data = {
        'rating': rating,
        'jersey':jersey,
        'team':team,
        'position':position,
        'country':country,
        'draft_year':draft_year,
        'draft_round':draft_round,
        'draft_peak':draft_peak
    }

    input_data = pd.DataFrame(user_input_data, index=[0])
    return input_data

# def plot_line():
#     m = model.coef_
#     b = model.intercept_



user_data_df = user_input()

st.header('Player Data Entered')
st.write(user_data_df)

salary = model.predict(user_data_df)
st.subheader('Player Salary Predicted: ')
st.subheader('$' + str(max(np.round(salary[0], 2), 0)))

