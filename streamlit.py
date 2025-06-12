import streamlit as st

# Judul aplikasi
st.title("Aplikasi Streamlit Sederhana")

# Input dari pengguna
nama = st.text_input("Masukkan nama Anda:")

# Tombol submit
if st.button("Kirim"):
    st.success(f"Halo, {nama}! Selamat datang di Streamlit.")
