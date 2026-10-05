import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, 'data', 'SuperStoreOrders.csv')

df = pd.read_csv(file_path, encoding='latin-1')

print("Total baris:", len(df))
print("Duplikat:", df.duplicated().sum())
print("Order date invalid:", pd.to_datetime(df['order_date'], errors='coerce').isna().sum())
print("Ship date invalid:", pd.to_datetime(df['ship_date'], errors='coerce').isna().sum())
print("Sales NULL:", df['sales'].isna().sum())
print("Profit NULL:", df['profit'].isna().sum())
print("Quantity NULL:", df['quantity'].isna().sum())
print("Discount NULL:", df['discount'].isna().sum())
