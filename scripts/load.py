import pandas as pd
from sqlalchemy import create_engine

def load_data(df, db_path):
    """Memuat data ke database SQL."""
    print("Loading data to SQL...")
    engine = create_engine(f'sqlite:///{db_path}')
    df.to_sql('sales', con=engine, if_exists='replace', index=False)
    print(f"Data berhasil dimuat ke tabel 'sales'.")