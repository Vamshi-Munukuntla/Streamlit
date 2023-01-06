import streamlit as st
import pandas as pd
import numpy as np
import time

a = [1, 2, 3, 4, 5, 6, 7, 8]
n = np.array(a)
nd = n.reshape((2, 4))
d = {
    'name': ['vamshi'],
    'age': [25],
    'city': ['warangal']
}

data = pd.read_csv('Salary_Data.csv')

# Displaying dataframe in streamlit
# st.dataframe(nd)
# st.dataframe(d)
# st.dataframe(data, width=1000, height=1000)
# st.table(data)
# st.json(d)
# st.write(data)


@st.cache
def ret_time(ab):
    time.sleep(2)
    return time.time()


if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))


