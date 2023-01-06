import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from plotly import graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np
st.set_option('deprecation.showPyplotGlobalUse', False)


data = pd.read_csv("data/Salary_Data.csv")
x = np.array(data['YearsExperience']).reshape(-1, 1)
lr = LinearRegression()
lr.fit(x, np.array(data['Salary']))

st.title('Salary Predictor')
nav = st.sidebar.radio("Navigation",['Home', 'Prediction', 'Contribute'])
if nav == 'Home':
    st.image("data//sal.jpg", use_column_width='always')
    if st.checkbox('Show Table'):
        st.table(data)

    graph = st.selectbox('What kind of Graph?',
                         ['Non-Interactive', 'Interactive'])

    val = st.slider('Filter data using years', 0, 15)
    data = data.loc[data['YearsExperience'] >= val]

    if graph == 'Non-Interactive':
        plt.scatter(data['YearsExperience'], data['Salary'])
        plt.ylim(0)
        plt.xlabel("Years of Experience")
        plt.ylabel('Salary')
        plt.tight_layout()
        st.pyplot()
    if graph == 'Interactive':
        layout = go.Layout(
            xaxis=dict(range=[0, 16]),
            yaxis=dict(range=[0, 210000])
        )
        fig = go.Figure(data=go.Scatter(
            x=data['YearsExperience'], y=data['Salary'],
            mode='markers'), layout=layout)
        st.plotly_chart(fig)

if nav == 'Prediction':
    st.header('Know your Salary')
    val = st.number_input('enter your experience', 0.00, 20.00, step=0.25)
    val = np.array(val).reshape(1, -1)
    predict = lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f'Your Predicted salary is {round(predict)}')

if nav == 'Contribute':
    st.header('Contribute to our dataset')
    ex = st.number_input('Enter your Experience', 0.0, 20.0, step=1.0)
    sal = st.number_input('Enter your Salary', 0.00, 1000000.00, step=1000.0)

    if st.button('Submit'):
        to_add = {'YearsExperience': [ex],
                  'Salary': [sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv('data/Salary_Data.csv', mode='a',
                      header=False, index=False)
        st.success("Submitted")


