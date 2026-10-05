# Retail Sales ETL Pipeline

Project latihan ETL pakai Python buat bersihin data penjualan retail. Datanya dari SuperStore Dataset, isinya 51.290 baris penjualan dari berbagai negara.

## Kenapa bikin ini?

Data mentahnya berantakan. Format tanggal campur aduk (`1/1/2011`, `13/01/2011`), ada nilai duplikat, dan beberapa kolom isinya kosong. Jadi aku bikin pipeline otomatis buat bersihin dan simpan ke database.

## Tools

- Python 3.10
- Pandas
- SQLAlchemy
- SQLite

## Alur

**Extract** - Baca CSV pakai Pandas.

**Transform** - Ini bagian paling ribet. Yang aku lakuin:
- Drop duplikat
- Ubah kolom `sales`, `profit`, `quantity`, `discount` dari string ke angka (ada yang pakai koma, jadi harus dibersihin dulu)
- Parse tanggal pakai `dayfirst=True` - ini penting banget
- Bikin kolom baru `shipping_days` (selisih tanggal kirim dan tanggal order)
- Isi kolom `category` dan `segment` yang kosong dengan "Unknown"

**Load** - Simpan ke SQLite, tabel `sales`.

## Hasil

Data mentah: 51.290 baris
Data bersih: 51.290 baris (gak ada yang dibuang, alhamdulillah)

## Temuan yang menarik

Awalnya aku bingung kenapa 61% data dianggap invalid. Ternyata karena `pd.to_datetime` default-nya baca format MM/DD/YYYY, sedangkan dataset ini pakai DD/MM/YYYY. Setelah aku tambahin `dayfirst=True`, semua tanggal ke-parse dengan benar.

Pelajaran: baca dokumentasi library itu penting. 

## cara menjalankan project ini
```bash
git clone https://github.com/USERNAME/retail-sales-etl-pipeline.git
cd retail-sales-etl-pipeline
python -m venv venv
venv\Scripts\activate  # windows
pip install -r requirements.txt
cd scripts
python main.py

## struktur folder

retail-sales-etl-pipeline/
├── data/               # dataset & database
├── scripts/            # kode ETL
├── sql/                # schema
├── screenshots/        # bukti hasil query
└── README.md
