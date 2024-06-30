import streamlit as st


def Account():
    st.header('Account page')

    login, logout, register = st.tabs(['Login', 'Logout', 'Register'])

    with login:
        st.subheader('Login')

    with logout:
        st.subheader('Logout')

    with register:
        st.subheader('Register')
