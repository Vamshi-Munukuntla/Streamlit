import altair
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt


# data = pd.DataFrame(
#     np.random.randn(100, 3),
#     columns=['a', 'b', 'c']
# )
# st.line_chart(data)
# st.bar_chart(data)
# st.area_chart(data)

# fig, ax = plt.subplots()
# ax.scatter(data['a'], data['b'])
# plt.title('Scatter')
# plt.xlabel('a')
# plt.ylabel('b')
# st.pyplot(fig)
#
# chart = alt.Chart(data).mark_circle().encode(
#     x='a', y='b', tooltip=['a','b']
# )
# st.altair_chart(chart, use_container_width=True)
#
st.graphviz_chart("""
digraph{
victor -> campusx
campusx -> ineuron
ineuron -> victor
mrbright -> campusx}
""")

# Map

# df = pd.DataFrame({
#     'awesome cities': ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
#     'lat': [41, 44, 38, 39],
#     'lon': [-87, -93, -85, -95]}
# )
# st.map(df)

# Adding Media
st.image('data/sal.jpg')

st.audio('data/demo.wav')

st.video('https://www.youtube.com/watch?v=vAF-qM-VWiM&ab_channel=Storytellers')