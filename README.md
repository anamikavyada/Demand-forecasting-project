# Demand-forecasting-project

This project demonstrates how to forecast demand for retail products using time series analysis with the Prophet model. It aims to predict future demand to optimize inventory management, reduce stockouts, and improve customer satisfaction. The project involves data ingestion, data preprocessing, exploratory data analysis (EDA), and demand forecasting for top-selling SKUs. The goal is to provide businesses with insights on how to forecast and manage demand effectively.

## Why This Project?

This project aims to predict future demand for retail products to help optimize inventory management, prevent stockouts, and improve customer satisfaction. By leveraging time series forecasting techniques like Prophet, businesses can better plan for future demand, avoiding overstocking or understocking of products.

## Key Features

- **Ingests sales data from SQL Server**: Data is extracted from a SQL Server database using Python and loaded into a Pandas DataFrame.
- **Performs exploratory data analysis (EDA)**: The data is cleaned, aggregated, and visualized to understand sales trends and patterns.
- **Forecasts demand using Prophet**: The Prophet model is used to predict future demand for top-selling products, capturing both trend and seasonal components.

## Results

The demand forecasting analysis focused on the top-selling SKU 23343. Here are the insights gained:

- **Demand Trend**: The selected SKU exhibited a declining trend, indicating reduced sales over time.
- **Seasonality**: The sales showed clear seasonal patterns, with spikes in demand during specific months.
- **Forecasting**: The model predicted a stable decline in future demand, with some seasonal fluctuations.

These insights can help businesses plan better for future demand, adjust inventory levels, and forecast more accurately.

## Files in the Repository

- `demand_forecasting.py`: Main Python script for data preparation, analysis, and demand forecasting.
- `demand_forecasting.ipynb`: Jupyter notebook that replicates the steps in the Python script and provides interactive analysis and visualizations.
- `plots/`: Folder containing the saved forecast and components plots for analysis.
- `requirements.txt`: Lists all the dependencies required to run the project.

## Installation & Setup

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/demand-forecasting-project.git
   cd demand-forecasting-project


2.Install the required dependencies:

pip install -r requirements.txt

Usage
Option 1: Running the Python Script (.py)

To run the Python script for forecasting:

1.Ensure your SQL Server connection details are correct in the insertdata.py script.

2.Run the script:

3.The script will load the sales data, preprocess it, upload it to SQL Server.

Option 2: Using the Jupyter Notebook (.ipynb)

1. To install Jupyter in VS code .Go to extensions Write Jupyter and install it .

2. Open the demand_forecasting.ipynb notebook and run the cells interactively to explore the data, perform EDA, and forecast demand.

Contributions

Feel free to fork the repo, create a new branch, make improvements, and submit a pull request! Contributions are welcome.
=======
# Demand-forecasting-project
This project demonstrates how to forecast demand for products in a retail environment using time series analysis. The model uses Prophet to predict future demand for the top SKUs in the dataset. It ingests sales data, performs exploratory data analysis (EDA), and uses Prophet to forecast future demand with seasonality and trend components.
>>>>>>> 00c5783a63e547588f6c082711cf9f72b2aad37c
