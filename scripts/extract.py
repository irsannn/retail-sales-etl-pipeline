import pandas as pd

def extract_data(file_path):
    """Membaca data mentah dari CSV."""
    print("Extracting data...")
    df = pd.read_csv(file_path, encoding='latin-1')
    print(f"Berhasil membaca {len(df)} baris data.")
    print(f"Kolom: {list(df.columns)}")
    return df