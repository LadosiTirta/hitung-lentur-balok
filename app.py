import streamlit as st

# Mengatur tampilan halaman
st.set_page_config(page_title="Ladosi Tirta - Pindah Alamat", page_icon="🚀")

# 1. Pesan Besar dan Jelas (Warna Biru)
st.info("### **APLIKASI TELAH PINDAH KE ALAMAT BARU YANG LEBIH LENGKAP**")

st.write("Silakan klik tombol di bawah untuk mengakses fitur terbaru di platform utama kami.")

# 2. Tombol Redirect yang Aman (Buka di Tab Baru agar tidak Loop)
st.markdown("""
    <a href="https://ladositirta.streamlit.app" target="_self">
        <button style="
            background-color: #007bff;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 18px;
            font-weight: bold;
            width: 100%;
            ">
            Lanjut ke Ladosi Tirta Sekarang
        </button>
    </a>
    """, unsafe_allow_html=True)

# Tambahan pesan kecil jika tombol tidak berfungsi
st.caption("Jika tombol tidak berfungsi, [klik di sini](https://ladositirta.streamlit.app)")
