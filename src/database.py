import sqlite3
import pandas as pd

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database: {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_tables(conn):
    try:
        cursor = conn.cursor()

        # Create demand_forecasting table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS demand_forecasting (
                product_id TEXT,
                store_id TEXT,
                price REAL,
                competitor_prices REAL,
                discounts REAL,
                sales_volume INTEGER,
                customer_reviews TEXT,
                return_rate REAL,
                storage_cost REAL,
                elasticity_index REAL
            )
        ''')

        # Create inventory_monitoring table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory_monitoring (
                product_id TEXT,
                store_id TEXT,
                stock_levels INTEGER,
                supplier_lead_time INTEGER,
                stockout_frequency REAL,
                reorder_point INTEGER,
                expiry_date TEXT,
                warehouse_capacity INTEGER,
                order_fulfillment_time INTEGER
            )
        ''')

        # Create pricing_optimization table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pricing_optimization (
                product_id TEXT,
                store_id TEXT,
                price REAL,
                competitor_prices REAL,
                discounts REAL,
                sales_volume INTEGER,
                customer_reviews TEXT,
                return_rate REAL,
                storage_cost REAL,
                elasticity_index REAL
            )
        ''')

        conn.commit()
        print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def load_data_from_csv(conn, csv_file, table_name):
    try:
        data = pd.read_csv(csv_file)
        data.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Data loaded into {table_name} from {csv_file}.")
    except Exception as e:
        print(f"Error loading data from {csv_file} into {table_name}: {e}")