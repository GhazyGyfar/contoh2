import streamlit as st
import pandas as pd

# ==========================
# 1. Load Data Unsur
# ==========================
# (Contoh sebagian, sisanya bisa di-extend)
data = [
    (1, 'H', 'Hidrogen', 1.008, 1.0, 1, 'Nonlogam'),
    (2, 'He', 'Helium', 4.0026, 18.0, 1, 'Gas mulia'),
    (3, 'Li', 'Litium', 6.94, 1.0, 2, 'Logam alkali'),
    (4, 'Be', 'Berilium', 9.0122, 2.0, 2, 'Logam alkali tanah'),
    (5, 'B', 'Boron', 10.81, 13.0, 2, 'Metaloid'),
    (6, 'C', 'Karbon', 12.011, 14.0, 2, 'Nonlogam'),
    (7, 'N', 'Nitrogen', 14.007, 15.0, 2, 'Nonlogam'),
    (8, 'O', 'Oksigen', 15.999, 16.0, 2, 'Nonlogam'),
    (9, 'F', 'Fluorin', 18.998, 17.0, 2, 'Halogen'),
    (10, 'Ne', 'Neon', 20.18, 18.0, 2, 'Gas mulia'),
    (11, 'Na', 'Natrium', 22.99, 1.0, 3, 'Logam alkali'),
    (12, 'Mg', 'Magnesium', 24.305, 2.0, 3, 'Logam alkali tanah'),
    (13, 'Al', 'Aluminium', 26.982, 13.0, 3, 'Logam pasca-transisi'),
    (14, 'Si', 'Silikon', 28.085, 14.0, 3, 'Metaloid'),
    (15, 'P', 'Fosfor', 30.974, 15.0, 3, 'Nonlogam'),
    (16, 'S', 'Sulfur', 32.06, 16.0, 3, 'Nonlogam'),
    (17, 'Cl', 'Klorin', 35.45, 17.0, 3, 'Halogen'),
    (18, 'Ar', 'Argon', 39.948, 18.0, 3, 'Gas mulia'),
    (19, 'K', 'Kalium', 39.098, 1.0, 4, 'Logam alkali'),
    (20, 'Ca', 'Kalsium', 40.078, 2.0, 4, 'Logam alkali tanah'),
    (21, 'Sc', 'Skandium', 44.956, 3.0, 4, 'Logam transisi'),
    (22, 'Ti', 'Titanium', 47.867, 4.0, 4, 'Logam transisi'),
    (23, 'V', 'Vanadium', 50.942, 5.0, 4, 'Logam transisi'),
    (24, 'Cr', 'Kromium', 51.996, 6.0, 4, 'Logam transisi'),
    (25, 'Mn', 'Mangan', 54.938, 7.0, 4, 'Logam transisi'),
    (26, 'Fe', 'Besi', 55.845, 8.0, 4, 'Logam transisi'),
    (27, 'Co', 'Kobalt', 58.933, 9.0, 4, 'Logam transisi'),
    (28, 'Ni', 'Nikel', 58.693, 10.0, 4, 'Logam transisi'),
    (29, 'Cu', 'Tembaga', 63.546, 11.0, 4, 'Logam transisi'),
    (30, 'Zn', 'Seng', 65.38, 12.0, 4, 'Logam transisi'),
    (31, 'Ga', 'Galium', 69.723, 13.0, 4, 'Logam pasca-transisi'),
    (32, 'Ge', 'Germanium', 72.63, 14.0, 4, 'Metaloid'),
    (33, 'As', 'Arsen', 74.922, 15.0, 4, 'Metaloid'),
    (34, 'Se', 'Selenium', 78.971, 16.0, 4, 'Nonlogam'),
    (35, 'Br', 'Bromin', 79.904, 17.0, 4, 'Halogen'),
    (36, 'Kr', 'Kripton', 83.798, 18.0, 4, 'Gas mulia'),
    (37, 'Rb', 'Rubidium', 85.468, 1.0, 5, 'Logam alkali'),
    (38, 'Sr', 'Stronsium', 87.62, 2.0, 5, 'Logam alkali tanah'),
    (39, 'Y', 'Yttrium', 88.906, 3.0, 5, 'Logam transisi'),
    (40, 'Zr', 'Zirkonium', 91.224, 4.0, 5, 'Logam transisi'),
    (41, 'Nb', 'Niobium', 92.906, 5.0, 5, 'Logam transisi'),
    (42, 'Mo', 'Molibdenum', 95.95, 6.0, 5, 'Logam transisi'),
    (43, 'Tc', 'Teknesium', 98.0, 7.0, 5, 'Logam transisi'),
    (44, 'Ru', 'Rutenium', 101.07, 8.0, 5, 'Logam transisi'),
    (45, 'Rh', 'Rodium', 102.91, 9.0, 5, 'Logam transisi'),
    (46, 'Pd', 'Palladium', 106.42, 10.0, 5, 'Logam transisi'),
    (47, 'Ag', 'Perak', 107.87, 11.0, 5, 'Logam transisi'),
    (48, 'Cd', 'Kadmium', 112.41, 12.0, 5, 'Logam transisi'),
    (49, 'In', 'Indium', 114.82, 13.0, 5, 'Logam pasca-transisi'),
    (50, 'Sn', 'Timah', 118.71, 14.0, 5, 'Logam pasca-transisi'),
    (51, 'Sb', 'Antimon', 121.76, 15.0, 5, 'Metaloid'),
    (52, 'Te', 'Telerium', 127.6, 16.0, 5, 'Metaloid'),
    (53, 'I', 'Iodin', 126.9, 17.0, 5, 'Halogen'),
    (54, 'Xe', 'Xenon', 131.29, 18.0, 5, 'Gas mulia'),
    (55, 'Cs', 'Sesium', 132.91, 1.0, 6, 'Logam alkali'),
    (56, 'Ba', 'Barium', 137.33, 2.0, 6, 'Logam alkali tanah'),
    (57, 'La', 'Lantanum', 138.91, 3.0, 6, 'Lantanida'),
    (58, 'Ce', 'Serium', 140.12, 0, 8, 'Lantanida'),
    (59, 'Pr', 'Praseodimium', 140.91, 0, 8, 'Lantanida'),
    (60, 'Nd', 'Neodimium', 144.24, 0, 8, 'Lantanida'),
    (61, 'Pm', 'Prometium', 145.0, 0, 8, 'Lantanida'),
    (62, 'Sm', 'Samarium', 150.36, 0, 8, 'Lantanida'),
    (63, 'Eu', 'Europium', 151.96, 0, 8, 'Lantanida'),
    (64, 'Gd', 'Gadolinium', 157.25, 0, 8, 'Lantanida'),
    (65, 'Tb', 'Terbium', 158.93, 0, 8, 'Lantanida'),
    (66, 'Dy', 'Disprosium', 162.5, 0, 8, 'Lantanida'),
    (67, 'Ho', 'Holmium', 164.93, 0, 8, 'Lantanida'),
    (68, 'Er', 'Erbium', 167.26, 0, 8, 'Lantanida'),
    (69, 'Tm', 'Tulium', 168.93, 0, 8, 'Lantanida'),
    (70, 'Yb', 'Iterbium', 173.05, 0, 8, 'Lantanida'),
    (71, 'Lu', 'Lutesium', 174.97, 3.0, 6, 'Lantanida'),
    (89, 'Ac', 'Aktinium', 227.0, 3.0, 7, 'Aktinida'),
    (90, 'Th', 'Torium', 232.04, 0, 9, 'Aktinida'),
    (91, 'Pa', 'Protaktinium', 231.04, 0, 9, 'Aktinida'),
    (92, 'U', 'Uranium', 238.03, 0, 9, 'Aktinida'),
    (93, 'Np', 'Neptunium', 237.0, 0, 9, 'Aktinida'),
    (94, 'Pu', 'Plutonium', 244.0, 0, 9, 'Aktinida'),
    (95, 'Am', 'Amerisium', 243.0, 0, 9, 'Aktinida'),
    (96, 'Cm', 'Kurium', 247.0, 0, 9, 'Aktinida'),
    (97, 'Bk', 'Berkelium', 247.0, 0, 9, 'Aktinida'),
    (98, 'Cf', 'Kalifornium', 251.0, 0, 9, 'Aktinida'),
    (100, 'Fm', 'Fermium', 257.0, 0, 9, 'Aktinida'),
    (101, 'Md', 'Mendelevium', 258.0, 0, 9, 'Aktinida'),
    (102, 'No', 'Nobelium', 259.0, 0, 9, 'Aktinida'),
    (103, 'Lr', 'Lawrensium', 266.0, 3.0, 7, 'Aktinida'),
    (104, 'Rf', 'Rutherfordium', 267.0, 4.0, 7, 'Logam transisi'),
    (105, 'Db', 'Dubnium', 268.0, 5.0, 7, 'Logam transisi'),
    (106, 'Sg', 'Seaborgium', 269.0, 6.0, 7, 'Logam transisi'),
    (107, 'Bh', 'Bohrium', 270.0, 7.0, 7, 'Logam transisi'),
    (108, 'Hs', 'Hassium', 277.0, 8.0, 7, 'Logam transisi'),
    (109, 'Mt', 'Meitnerium', 278.0, 9.0, 7, 'Logam transisi'),
    (110, 'Ds', 'Darmstadtium', 281.0, 10.0, 7, 'Logam transisi'),
    (111, 'Rg', 'Roentgenium', 282.0, 11.0, 7, 'Logam transisi'),
    (112, 'Cn', 'Copernicium', 285.0, 12.0, 7, 'Logam transisi'),
    (113, 'Nh', 'Nihonium', 286.0, 13.0, 7, 'Logam pasca-transisi'),
    (114, 'Fl', 'Flerovium', 289.0, 14.0, 7, 'Logam pasca-transisi'),
    (115, 'Mc', 'Moscovium', 290.0, 15.0, 7, 'Logam pasca-transisi'),
    (116, 'Lv', 'Livermorium', 293.0, 16.0, 7, 'Logam pasca-transisi'),
    (117, 'Ts', 'Tenesin', 294.0, 17.0, 7, 'Halogen'),
    (118, 'Og', 'Oganesson', 294.0, 18.0, 7, 'Gas mulia'),
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
for _, row in df.iterrows():
    try:
        p = int(row["Periode"]) - 1
        g = int(row["Golongan"]) - 1
        
        if 0 <= p < len(grid) and 0 <= g < len(grid[0]):
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
