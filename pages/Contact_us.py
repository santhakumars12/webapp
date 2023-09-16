import streamlit as st

st.write("Contact Me")

with st.form():
    st.text_input("Your Email Address")
    st.text_area("Write your message")
    st.form_submit_button("submit")