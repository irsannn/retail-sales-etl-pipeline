import pandas as pd

def transform_data(df):
    """Membersihkan dan mentransformasi data."""
    print("Transforming data...")
    initial_rows = len(df)
    
    # 1. Hapus duplikat
    df = df.drop_duplicates()
    
    # 2. Bersihkan kolom sales & profit (hapus koma)
    df['sales'] = df['sales'].astype(str).str.replace(',', '', regex=False)
    df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
    
    df['profit'] = df['profit'].astype(str).str.replace(',', '', regex=False)
    df['profit'] = pd.to_numeric(df['profit'], errors='coerce')
    
    # 3. Konversi tipe data
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['discount'] = pd.to_numeric(df['discount'], errors='coerce')
    
    # 4. Konversi tanggal (dayfirst=True karena format DD/MM/YYYY)
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce', dayfirst=True)
    df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce', dayfirst=True)
    
    # 5. Hapus baris dengan tanggal atau sales invalid
    df = df.dropna(subset=['order_date', 'ship_date', 'sales', 'profit'])
    
    # 6. Feature engineering
    df['shipping_days'] = (df['ship_date'] - df['order_date']).dt.days
    df = df[df['shipping_days'] >= 0]
    
    # 7. Isi NULL
    df['category'] = df['category'].fillna('Unknown')
    df['segment'] = df['segment'].fillna('Unknown')
    
    # 8. Pilih kolom final
    df = df[[
        'order_id', 'order_date', 'ship_date', 'ship_mode',
        'customer_name', 'segment', 'country', 'market', 'region',
        'category', 'sub_category', 'product_name',
        'sales', 'quantity', 'discount', 'profit', 'shipping_days'
    ]]
    
    print(f"Data bersih: {len(df)} baris (dari {initial_rows} baris).")
    return df