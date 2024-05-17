import streamlit as st
from login import login
from sales import sales_dashboard
from inventory_code import inventory_dashboard
def main():

    # Set page configuration
    st.set_page_config(page_title="Main Page", page_icon=":rocket:")

    # Initialize is_logged_in in session state
    if 'is_logged_in' not in st.session_state:
        st.session_state.is_logged_in = False

    if not st.session_state.is_logged_in:
        if login():
            st.session_state.is_logged_in = True
            # Clear login elements from the display
            st.empty()
    else:
        tab_selected = st.sidebar.radio("Select Dashboard", ("Sales Dashboard", "Inventory Dashboard"))

        if tab_selected == "Sales Dashboard":
            sales_dashboard()

        elif tab_selected == "Inventory Dashboard":
            inventory_dashboard()

if __name__ == "__main__":
    main()  
