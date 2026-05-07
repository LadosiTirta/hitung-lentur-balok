import streamlit as st

# Mengatur tampilan halaman
st.set_page_config(page_title="Ladosi Tirta - Pindah Alamat", page_icon="🚀")

# 1. Pesan Besar dan Jelas (Warna Biru)
st.info("### **APLIKASI TELAH PINDAH KE ALAMAT BARU YANG LEBIH LENGKAP**")

# 2. Teks biasa
st.write("Silakan lanjut ke platform utama Ladosi Tirta sekarang untuk mengakses fitur terbaru.")

# 3. Link Tombol (Membuka di Tab Baru)
st.markdown("""
    <a href="https://ladositirta.streamlit.app" target="_blank" style="
        display: block;
        background-color: #007bff;
        color: white;
        padding: 14px 24px;
        text-decoration: none;
        border-radius: 8px;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        width: 100%;
        box-sizing: border-box;
        ">
        Klik Di Sini Untuk Pindah
    </a>
    """, unsafe_allow_html=True)
