#pip install -U streamlit
#pip install -U plotly

#streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title('Predicting if message is Spam or not')

message = st.text_input('Enter a message')

if st.button('Predict'):
    prediction = model.predict([message])

    print(prediction)

    if prediction[0]=='spam':
        st.warning('This message is Spam')
    
    else:
        st.success("This message is legit message")

st.balloons()