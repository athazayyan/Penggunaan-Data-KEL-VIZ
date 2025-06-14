import streamlit as st
import pandas as pd
import os

# Set page title
st.title("Penjelasan Data untuk Visualisasi Kawasan Ekosistem Leuser")

# Introduction
st.write("""
Data yang digunakan dalam dashboard visualisasi Kawasan Ekosistem Leuser berasal dari dua sumber utama:
1. **Data Tutupan Hutan & Kehilangan Tutupan Hutan Aceh 2018 - 2024**: Berisi informasi tentang tutupan hutan dan kehilangan tutupan hutan di wilayah Aceh, digunakan untuk analisis prediksi kehilangan hutan.
2. **Data Putusan Perdagangan Satwa Liar di Aceh 2020-2024**: Berisi data terkait putusan hukum perdagangan satwa liar, memberikan konteks tentang aktivitas ilegal yang memengaruhi ekosistem.
Berikut adalah isi dari masing-masing file Excel, dengan data dari setiap sheet ditampilkan dalam tabel.
""")

# Function to load and display Excel sheets
def display_excel_sheets(file_path, file_title):
    try:
        # Load Excel file
        xl = pd.ExcelFile(file_path)
        st.header(file_title)
        # Iterate through each sheet
        for sheet_name in xl.sheet_names:
            st.subheader(f"Sheet: {sheet_name}")
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            st.dataframe(df)
            st.write(f"**Deskripsi**: Data pada sheet '{sheet_name}' berisi informasi terkait {file_title.lower()}. Kolom-kolom mencakup {', '.join(df.columns)}.")
    except FileNotFoundError:
        st.error(f"File {file_path} tidak ditemukan. Pastikan file berada di direktori yang sama dengan aplikasi.")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memuat {file_path}: {str(e)}")

# File paths
forest_file = "Data Tutupan Hutan & Kehilangan Tutupan Hutan Aceh 2018 - 2024.xlsx"
wildlife_file = "Data Putusan Perdagangan Satwa Liar di Aceh 2020-2024.xlsx"

# Display data from both Excel files
display_excel_sheets(forest_file, "Data Tutupan Hutan & Kehilangan Tutupan Hutan Aceh 2018 - 2024")
display_excel_sheets(wildlife_file, "Data Putusan Perdagangan Satwa Liar di Aceh 2020-2024")