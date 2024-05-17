import streamlit as st

# Define the username and password
USERNAME = "admin"
PASSWORD = "password"

def login():
    st.title("Admin Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.success("Login successful!")
            return True
        else:
            st.error("Invalid username or password")
            return False