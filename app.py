import streamlit as st

# 1. Judul Halaman
st.set_page_config(page_title="Ladosi Tirta - Redirect", page_icon="🚀")

# 2. Pesan Warning Warna Biru (st.info) dengan format tebal
st.info("### **APLIKASI TELAH PINDAH KE ALAMAT BARU YANG LEBIH LENGKAP**")

# 3. Tombol Redirect Langsung
if st.button("Lanjut ke Ladosi Tirta Sekarang"):
    # Kode HTML di bawah ini akan otomatis membuka link di tab yang sama saat tombol diklik
    st.markdown('<meta http-equiv="refresh" content="0;URL=\'https://ladositirta.streamlit.app\'" />', unsafe_allow_html=True)
    st.write("Sedang mengarahkan Anda...")
