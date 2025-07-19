# file: tabel_periodik.py

import streamlit as st
import pandas as pd

# Data unsur kimia (hanya sebagian, bisa ditambah sesuai kebutuhan)
unsur = [
    {"Nomor": 1, "Simbol": "H",  "Nama": "Hidrogen",    "Massa Atom": 1.008, "Golongan": 1, "Periode": 1},
    {"Nomor": 2, "Simbol": "He", "Nama": "Helium",      "Massa Atom": 4.0026, "Golongan": 18, "Periode": 1},
    {"Nomor": 3, "Simbol": "Li", "Nama": "Litium",      "Massa Atom": 6.94, "Golongan": 1, "Periode": 2},
    {"Nomor": 4, "Simbol": "Be", "Nama": "Berilium",    "Massa Atom": 9.0122, "Golongan": 2, "Periode": 2},
    {"Nomor": 5, "Simbol": "B",  "Nama": "Boron",       "Massa Atom": 10.81, "Golongan": 13, "Periode": 2},
    {"Nomor": 6, "Simbol": "C",  "Nama": "Karbon",      "Massa Atom": 12.01, "Golongan": 14, "Periode": 2},
    {"Nomor": 7, "Simbol": "N",  "Nama": "Nitrogen",    "Massa Atom": 14.007, "Golongan": 15, "Periode": 2},
    {"Nomor": 8, "Simbol": "O",  "Nama": "Oksigen",     "Massa Atom": 15.999, "Golongan": 16, "Periode": 2},
    {"Nomor": 9, "Simbol": "F",  "Nama": "Fluorin",     "Massa Atom": 18.998, "Golongan": 17, "Periode": 2},
    {"Nomor": 10, "Simbol": "Ne", "Nama": "Neon",       "Massa Atom": 20.180, "Golongan": 18, "Periode": 2},
    # Tambahkan data lainnya sampai 118 unsur jika diperlukan
]

# Konversi ke DataFrame
df_unsur = pd.DataFrame(unsur)

# Judul
st.title("🧪 Tabel Periodik Unsur Kimia")

# Filter berdasarkan golongan dan periode
golongan = st.sidebar.selectbox("Pilih Golongan", sorted(df_unsur["Golongan"].unique()))
periode = st.sidebar.selectbox("Pilih Periode", sorted(df_unsur["Periode"].unique()))

# Filter DataFrame
df_filter = df_unsur[(df_unsur["Golongan"] == golongan) & (df_unsur["Periode"] == periode)]

# Tampilkan Data
st.subheader(f"Unsur dengan Golongan {golongan} dan Periode {periode}")
st.dataframe(df_filter)

# Cari berdasarkan simbol
cari_simbol = st.text_input("Cari Unsur berdasarkan Simbol", "")
if cari_simbol:
    hasil = df_unsur[df_unsur["Simbol"].str.upper() == cari_simbol.upper()]
    if not hasil.empty:
        st.success("Unsur ditemukan!")
        st.table(hasil)
    else:
        st.error("Unsur tidak ditemukan.")
