import streamlit as st

st.set_page_config(page_title="Home - Prediksi Kolesterol", page_icon="🩺")

st.markdown("""
<div style='
    background: linear-gradient(90deg, #162447 60%, #21bf73 100%);
    color: #f8ede3;
    padding: 2.2rem 1rem 1.6rem 1rem;
    border-radius: 1.3rem;
    box-shadow: 0 4px 30px rgba(22,36,71,0.13);
    text-align: center;
    margin-bottom: 2.5rem;'>
    <h1 style='margin-bottom:0.5rem;font-size:2.6rem;'>🩺 Prediksi Kolesterol Non-Invasif</h1>
    <div style='font-size:1.18rem;font-weight:300;'>
    Selamat datang di aplikasi deteksi kolesterol dari gambar arteri tangan.<br>
    Silakan pilih menu di samping untuk mulai analisis.
    </div>
</div>
""", unsafe_allow_html=True)

st.info("Pilih **Deteksi Kolestrol** di sidebar untuk memulai analisis kolesterol Anda.")

st.markdown("<div style='text-align:center;'>Developed by <b>Ziyad</b></div>", unsafe_allow_html=True)
