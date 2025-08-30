from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pypyodbc
import pandas as pd

# ✅ Use raw strings or escape the backslashes
SERVER_NAME = r'IBM-5SDQPM3\MSSQLSERVER01'
DATABASE_NAME = 'D2C_SupplyChain'
TABLE_NAME = 'Orders'

# ✅ Again, use raw string or double-backslashes for file paths
excel_file_path = r'C:\Users\0044Y7744\Downloads\onlineretail\OnlineRetailNew.xlsx'  # make sure it has .xlsx
# ✅ Create connection string properly
connection_string = f"""
    DRIVER={{SQL Server}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trusted_Connection=yes;
"""
connection_url = URL.create('mssql+pyodbc', query={'odbc_connect': connection_string})
engine = create_engine(connection_url, module=pypyodbc)

# ✅ Read all sheets in the Excel file
excel_file = pd.read_excel(excel_file_path, sheet_name=None)

# ✅ Loop through and write to SQL
for sheet_name, df_data in excel_file.items():
    print(f'Loading worksheet {sheet_name}...')
    df_data.to_sql(TABLE_NAME, engine, if_exists='append', index=False)