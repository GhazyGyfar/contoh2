import streamlit as st
import pandas as pd

# ==========================
# 1. Load Data Unsur
# ==========================
# (Contoh sebagian, sisanya bisa di-extend)
data = [
    (1, "H", "Hidrogen", 1.008, 1, 1, "Nonlogam"),
    (2, "He", "Helium", 4.0026, 18, 1, "Gas mulia"),
    (3, "Li", "Litium", 6.94, 1, 2, "Logam alkali"),
    (4, "Be", "Berilium", 9.0122, 2, 2, "Logam alkali tanah"),
    (5, "B", "Boron", 10.81, 13, 2, "Metaloid"),
    (6, "C", "Karbon", 12.011, 14, 2, "Nonlogam"),
    (7, "N", "Nitrogen", 14.007, 15, 2, "Nonlogam"),
    (8, "O", "Oksigen", 15.999, 16, 2, "Nonlogam"),
    (9, "F", "Fluorin", 18.998, 17, 2, "Halogen"),
    (10, "Ne", "Neon", 20.180, 18, 2, "Gas mulia"),
    (11, "Na", "Natrium", 22.990, 1, 3, "Logam alkali"),
    (12, "Mg", "Magnesium", 24.305, 2, 3, "Logam alkali tanah"),
    (13, "Al", "Aluminium", 26.982, 13, 3, "Logam pasca-transisi"),
    (14, "Si", "Silikon", 28.085, 14, 3, "Metaloid"),
    (15, "P", "Fosfor", 30.974, 15, 3, "Nonlogam"),
    (16, "S", "Sulfur", 32.06, 16, 3, "Nonlogam"),
    (17, "Cl", "Klorin", 35.45, 17, 3, "Halogen"),
    (18, "Ar", "Argon", 39.948, 18, 3, "Gas mulia"),
    # Tambahkan hingga ke-118
]

df = pd.DataFrame(data, columns=["Nomor", "Simbol", "Nama", "Massa", "Golongan", "Periode", "Kategori"])

# ==========================
# 2. Warna berdasarkan jenis unsur
# ==========================
warna_kategori = {
    "Logam alkali": "#FFB6C1",
    "Logam alkali tanah": "#FFA07A",
    "Logam transisi": "#FFD700",
    "Logam pasca-transisi": "#DAA520",
    "Metaloid": "#98FB98",
    "Nonlogam": "#87CEEB",
    "Halogen": "#7FFFD4",
    "Gas mulia": "#DDA0DD",
    "Lantanida": "#F5DEB3",
    "Aktinida": "#E9967A"
}

# ==========================
# 3. Tampilan Grid Tabel
# ==========================
st.set_page_config(layout="wide")
st.title("🧪 Tabel Periodik Unsur Kimia")

# Buat grid 7x18
grid = [["" for _ in range(18)] for _ in range(7)]

# Masukkan ke dalam grid
for _, row in df.iterrows():
    p, g = int(row["Periode"]) - 1, int(row["Golongan"]) - 1
    grid[p][g] = row

# Inisialisasi klik
unsur_diklik = None

# Tampilkan tabel
for baris in grid:
    kolom = st.columns(18)
    for i in range(18):
        if isinstance(baris[i], pd.Series):
            u = baris[i]
            warna = warna_kategori.get(u["Kategori"], "#CCCCCC")
            with kolom[i]:
                if st.button(f"{u['Simbol']}\n({int(u['Nomor'])})", key=f"{u['Nomor']}", help=u["Nama"]):
                    unsur_diklik = u
                st.markdown(f"<div style='height:5px; background-color:{warna}'></div>", unsafe_allow_html=True)
        else:
            kolom[i].empty()

# ==========================
# 4. Detail Unsur Klik
# ==========================
if unsur_diklik is not None:
    st.markdown("---")
    st.subheader(f"🧾 Detail Unsur: {unsur_diklik['Nama']} ({unsur_diklik['Simbol']})")
    st.write(f"**Nomor Atom:** {unsur_diklik['Nomor']}")
    st.write(f"**Massa Atom:** {unsur_diklik['Massa']} uma")
    st.write(f"**Golongan:** {unsur_diklik['Golongan']}")
    st.write(f"**Periode:** {unsur_diklik['Periode']}")
    st.write(f"**Kategori:** {unsur_diklik['Kategori']}")
