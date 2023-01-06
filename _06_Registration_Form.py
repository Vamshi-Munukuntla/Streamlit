import streamlit as st

st.title('Registration Form')

first, last = st.columns(2)
first.text_input("First Name")
last.text_input('Last Name')

email, mobile = st.columns([2, 1])
email.text_input('Email')
mobile.text_input('Mobile Number')

user, pwd, pwd2 = st.columns(3)
user.text_input('Username')
pwd.text_input('Password', type='password')
pwd2.text_input('Retype your password', type='password')

check, blank, submit = st.columns(3)
check.checkbox('I Agree')
submit.button('Submit')

# Change Color Scheme



