import streamlit as st
import pandas as pd
import plotly.express as px
from login import login

def sales_dashboard():
    # Check if the user is logged in
    if not st.session_state.is_logged_in:
        if not login():
            return

    st.title(":bar_chart: Sales Dashboard")

    # Load the dataset
    df = pd.read_excel("pre.xlsx")

    # Convert 'Year', 'Month', and 'Day' columns to datetime format
    df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])

    # Sidebar for date selection
    selected_day = st.sidebar.selectbox("Select Day", sorted(df['Day'].unique()))
    selected_month = st.sidebar.selectbox("Select Month", sorted(df['Month'].unique()))
    selected_year = st.sidebar.selectbox("Select Year", sorted(df['Year'].unique()))

    # Filter data based on selected year, month, and day
    filtered_data = df[(df['Year'] == selected_year) & (df['Month'] == selected_month) & (df['Day'] == selected_day)]
    
    # Calculate total sales revenue and number of rows (transactions) in the dataset
    total_revenue = df['Total'].sum()
    total_transactions = len(df)  # Count the number of rows in the DataFrame

    # Sidebar for additional options
    option = st.sidebar.selectbox("Select Option", ["Select Time Series", 
                                                    "Pie Chart for Sales by Quantity and Data",
                                                    "Pie Chart for Sales by Revenue and Data", 
                                                    "Overall Sales by Revenue",
                                                    "Overall Sales by Quantity"])

    # Display the selected option
    if option == "Select Time Series":
        # Display time series
        st.header("Time Series")
        fig_time_series = px.line(df, x='Date', y='Total', title='Sales Trends Over Time', hover_name='Item Name')
        st.plotly_chart(fig_time_series)
    elif option == "Pie Chart for Sales by Quantity and Data":
        # Pie chart for sales by quantity
        st.header("Pie Chart for Sales by Quantity and Data")
        top_selling_qty = filtered_data.groupby('Item Name')['Qty'].sum().nlargest(5).reset_index()
        fig_pie_qty = px.pie(top_selling_qty, values='Qty', names='Item Name', title='Top 5 Sales by Quantity')
        st.plotly_chart(fig_pie_qty)
    elif option == "Pie Chart for Sales by Revenue and Data":
        # Pie chart for sales by revenue
        st.header("Pie Chart for Sales by Revenue and Data")
        top_selling_revenue = filtered_data.groupby('Item Name')['Total'].sum().nlargest(5).reset_index()
        fig_pie_revenue = px.pie(top_selling_revenue, values='Total', names='Item Name', title='Top 5 Sales by Revenue')
        st.plotly_chart(fig_pie_revenue)
    elif option == "Overall Sales by Revenue":
        # Overall sales by revenue
        st.header("Overall Sales by Revenue")
        overall_sales_revenue = df.groupby('Item Name')['Total'].sum().nlargest(5).reset_index()
        st.write(overall_sales_revenue)
        fig_overall_revenue = px.pie(overall_sales_revenue, values='Total', names='Item Name', title='Overall Top 5 Sales by Revenue')
        st.plotly_chart(fig_overall_revenue)
    elif option == "Overall Sales by Quantity":
        # Overall sales by quantity
        st.header("Overall Sales by Quantity")
        overall_sales_quantity = df.groupby('Item Name')['Qty'].sum().nlargest(5).reset_index()
        st.write(overall_sales_quantity)
        fig_overall_quantity = px.pie(overall_sales_quantity, values='Qty', names='Item Name', title='Overall Top 5 Sales by Quantity')
        st.plotly_chart(fig_overall_quantity)

    # Sales Overview in the sidebar
    st.sidebar.header("Sales Overview")
    st.sidebar.subheader(f"Total Revenue: ₹{total_revenue:,.0f}")
    st.sidebar.subheader(f"Total Transactions: {total_transactions:,}")  # Display the total number of rows

