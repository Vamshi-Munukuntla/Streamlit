import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import altair as alt

st.title('WIDGETS')

if st.button("Price of Ambition"):
    st.write('Pay that price.')

name = st.text_input("Name")
st.write(name)

address = st.text_area('Enter your address')
st.write(address)

# Date and Time Input
st.date_input('Enter a date')
st.time_input('Enter time')

# Checkbox
if st.checkbox('You accept the terms and conditions'):
    st.write('The app is initialized')

# Radio and Select box
st.radio('colors', ['Red', 'Blue', 'Green'], index=2)
st.selectbox('colors', ['Red', 'Blue', 'Green'], index=2)

# Multiselect
ms = st.multiselect('colors', ('Red', 'Green', 'Yellow'))
st.write(ms)

# Slider
st.slider('Age', min_value=25, max_value=30, value=27, step=2)

# number_input
st.number_input('numbers', min_value=25.0,
                max_value=100.0, value=27.0, step=2.0)

# File Upload
st.file_uploader("Upload a file")



