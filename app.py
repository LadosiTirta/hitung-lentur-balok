import streamlit as st

# Mengatur tampilan halaman
st.set_page_config(page_title="Ladosi Tirta - Pindah Alamat", page_icon="🚀")

# 1. Pesan Besar dan Jelas (Warna Biru)
st.info("### **APLIKASI TELAH DI TINGKATKAN MENJADI LEBIH LENGKAP**")

# 2. Teks dengan format khusus sebaris
st.markdown(
    'Silakan lanjut klik tombol <span style="color: #007bff; font-size: 1.2em; font-weight: bold;">LADOSI-TIRTA</span> sekarang untuk mengakses fitur terbaru.',
    unsafe_allow_html=True
)

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
        LADOSI-TIRTA
    </a>
    """, unsafe_allow_html=True)
