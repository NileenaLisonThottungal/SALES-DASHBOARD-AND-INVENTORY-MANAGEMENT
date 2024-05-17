import streamlit as st
import pandas as pd
import plotly.express as px
from login import login

def inventory_dashboard():
    # Initialize is_logged_in in session state
    if 'is_logged_in' not in st.session_state:
        st.session_state.is_logged_in = False

    # Check if the user is logged in
    if not st.session_state.is_logged_in:
        if not login():
            return

    # Load the categorized items dataset
    df = pd.read_excel("categorize_item.xlsx")

    # Title
    st.markdown("<h1 class='title'>Inventory Dashboard</h1>", unsafe_allow_html=True)

    # Sidebar for selecting features
    st.sidebar.header("Select Features")
    selected_feature = st.sidebar.radio("Feature:", ("Categorized Items", "ABC Analysis", "ABC Pie Chart", "Top 10 Selling Products Brand-wise"))

    # Calculate ABC categories
    total_quantity = df['Qty'].sum()
    df['CumulativePercentage'] = (df['Qty'].cumsum() / total_quantity) * 100
    df['ABC_Category'] = pd.cut(df['CumulativePercentage'], bins=[-float('inf'), 20, 50, float('inf')],
                                 labels=['A', 'B', 'C'], include_lowest=True)

    if selected_feature == "Categorized Items":
        # Search and Filter Functionality
        search_term = st.text_input("Search for a product:")
        selected_category = st.selectbox("Filter by category:", sorted(df["Category"].unique()))

        # Apply search and filter
        filtered_df = df[(df["Item Name"].str.contains(search_term, case=False)) & (df["Category"] == selected_category)]

        st.subheader("Categorized Items")
        st.dataframe(filtered_df)

    elif selected_feature == "ABC Analysis":
        st.subheader("ABC Analysis Results")
        st.write("ABC Analysis Results:")
        st.dataframe(df[['Item Name', 'Qty', 'CumulativePercentage', 'ABC_Category']])

    elif selected_feature == "ABC Pie Chart":
        fig_pie = px.pie(df, values='Qty', names='ABC_Category', title='ABC Analysis Pie Chart',
                         color='ABC_Category', color_discrete_map={'A': '#FF5733', 'B': '#F4D03F', 'C': '#4CAF50'})
        st.plotly_chart(fig_pie)

    elif selected_feature == "Top 10 Selling Products Brand-wise":
        sub_option = st.sidebar.radio("Select Sub-Option", ["A", "B", "C"])

        if sub_option in ["A", "B", "C"]:
            # Filter data for the selected ABC category
            df_category = df[df['ABC_Category'] == sub_option]
            # Get top 10 selling products
            top_10_products = df_category.groupby('Item Name')['Qty'].sum().nlargest(10).reset_index()
            # Create bar chart
            fig = px.bar(top_10_products, x='Qty', y='Item Name', orientation='h', title=f'Top 10 Selling Products in Category {sub_option}',
                         labels={'Qty': 'Quantity', 'Item Name': 'Product Name'}, color='Qty')
            st.plotly_chart(fig)
