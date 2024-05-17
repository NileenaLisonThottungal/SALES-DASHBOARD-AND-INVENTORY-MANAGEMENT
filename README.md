# Sales and Inventory Management Dashboard
This project is a Sales and Inventory Management Dashboard developed using Streamlit and Python. The application provides an intuitive interface for visualizing sales data, managing inventory, and performing various analyses.

## Features

### Sales Dashboard
- **Time Series Visualization**: Displays sales data over the past two years.
- **Transactions Overview**: Shows the total number of transactions, quantity sold, and revenue generated.
- **Top Selling Products**: Visualizes the top 5 selling products by revenue and quantity using pie charts.
- **Filtering Options**: Allows filtering of sales data by day, date, and month.

### Inventory Dashboard
- **ABC Analysis**: Classifies inventory into categories (A, B, and C) based on their importance.
- **Product Search**: Includes a search bar for selecting and viewing specific products.
- **Top Products Bar Chart**: Displays the top 10 selling products by revenue and quantity.

### Authentication
- **Login Function**: Ensures secure access to the dashboard with a unique username and password for the admin.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/sales-inventory-dashboard.git
   cd sales-inventory-dashboard
   ```

2. **Install required packages**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```sh
   streamlit run main.py
   ```

## Project Structure

```
sales-inventory-dashboard/
│
├── data/
│   ├── sales_data.xlsx
│   ├── inventory_data.xlsx
│
├── src/
│   ├── main.py
│   ├── sales.py
│   ├── inventory.py
│   ├── auth.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

- **data/**: Contains the raw sales and inventory data files.
- **src/**: Contains the main application file and modules for sales, inventory, and authentication functionalities.
- **README.md**: Provides information about the project.
- **requirements.txt**: Lists the Python packages required for the project.
- **.gitignore**: Specifies files and directories to be ignored by Git.

## Usage

### Sales Function
- Visualizes a time series graph for the past two years of sales data.
- Shows total transactions, quantities sold, and revenue.
- Displays the top 5 products by revenue and quantity using pie charts.
- Allows filtering based on selected day, date, and month.

### Inventory Function
- Performs ABC analysis to classify inventory items.
- Provides a search bar to find specific products.
- Generates a bar chart of the top 10 products by revenue and quantity.

### Login Function
- Ensures that only authorized users (admin) can access the dashboard.
- Requires a unique username and password for authentication.

## Data Preprocessing
- The raw dataset is preprocessed to add several attributes for analysis.
- Data cleaning and transformation steps are applied to ensure the accuracy and reliability of the visualizations and analyses.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries or issues, please contact [nileenalison@gmail.com].

---
