import streamlit as st
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
# import altair as alt
import time

plt.style.use('fivethirtyeight')

data = {
    'num': [x for x in range(1, 11)],
    'square': [x**2 for x in range(1, 11)],
    'cubic': [x**3 for x in range(1, 11)]
}

rad = st.sidebar.radio('Navigation', ('Home', 'About us'))

if rad == 'Home':
    df = pd.DataFrame(data=data)
    col = st.sidebar.multiselect('Select a Column', df.columns)

    fig, ax = plt.subplots()
    ax.plot(df['num'], df[col])
    st.pyplot(fig)

if rad == 'About us':
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)

    st.balloons()

    st.write('Created by Vamshi')
    st.error('Error')
    st.success('Success')
    st.info('Information')
    st.exception(RuntimeError('This is an error'))
    st.warning('This is a Warning')
