import os
from extract import extract_data
from transform import transform_data
from load import load_data

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA = os.path.join(BASE_DIR, 'data', 'SuperStoreOrders.csv')
DB_PATH = os.path.join(BASE_DIR, 'data', 'clean_sales.db')

def run_pipeline():
    print(" Memulai ETL Pipeline...")
    df_raw = extract_data(RAW_DATA)
    df_clean = transform_data(df_raw)
    load_data(df_clean, DB_PATH)
    print(" Pipeline selesai!")

if __name__ == "__main__":
    run_pipeline()