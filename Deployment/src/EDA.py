def run():  
    import streamlit as st
    import os
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from PIL import Image, ImageOps

    st.title("Skin Condition Analysis (Facial Skin Classification)")
    st.subheader("Exploratory Data Analysis (EDA)")

    st.write(
        """
        Halaman ini menampilkan Exploratory Data Analysis (EDA) untuk dataset klasifikasi kondisi kulit wajah.
        Data ini digunakan untuk melatih model Deep Learning berbasis MobileNetV2.
        """
    )



    # 1. DISTRIBUSI DATA

    st.write("## 1. Profiling & Distribusi Data")
    st.image('./image/dist.png')

    st.info(
        "Berdasarkan laporan, dataset memiliki distribusi yang seimbang dengan total "
        "sekitar 4.996 gambar di Training Set."
    )


    # 2. ANALISIS DIMENSI (EDA TEKNIS)

    st.write("## 2. Variasi Dimensi Gambar")
    st.image('./image/dim.png')

    st.warning(
        "Catatan Penting: Terdapat perbedaan resolusi signifikan (contoh: Kemerahan 720x480 vs Normal 149x121). "
        "Proses resizing ke 224x224 dilakukan untuk menstandarisasi input model MobileNetV2."
    )


    # 3. VISUALISASI SAMPEL GAMBAR

    st.write("## 3. Galeri Visual Tiap Kondisi Kulit")
    st.image('./image/vis.png')

    # 4. HASIL EVALUASI MODEL (DARI LAPORAN)

    st.write("## 4. Ringkasan Performa Model")
    
    # Data dari classification_report di file P2G7 copy.pdf
    report_data = {
        'Kategori': ['Darkspot', 'Jerawatan', 'Kemerahan', 'Kerutan', 'Normal'],
        'Precision': [0.00, 0.66, 0.74, 0.76, 0.86],
        'Recall': [0.00, 0.79, 0.89, 0.89, 0.80],
        'F1-Score': [0.00, 0.72, 0.81, 0.82, 0.83]
    }
    df_report = pd.DataFrame(report_data)
    st.dataframe(df_report)
    
    st.error(
        "Analisis Performa: Model memiliki akurasi keseluruhan 76%. Namun, kelas 'Darkspot' "
        "memiliki nilai 0 karena kegagalan model dalam mengenali fitur tersebut secara spesifik."
    )


    # 5. PENJELASAN KARAKTERISTIK TIAP KELAS (TAMBAHAN BARU)
    st.write("## 5. Karakteristik Tiap Kondisi Kulit")
    st.write("Berikut adalah penjelasan mendalam mengenai ciri-ciri visual dari setiap kelas dalam dataset:")

    with st.expander("Klik untuk melihat penjelasan tiap kategori"):
        st.markdown("""
        1. *Darkspot (Bercak Hitam)*
           - *Ciri Visual:* Area pada kulit yang berwarna lebih gelap (cokelat hingga hitam) dibandingkan kulit di sekitarnya.
           - *Penyebab:* Hiperpigmentasi akibat bekas jerawat, paparan sinar matahari (sunspots), atau faktor penuaan.
           - *Tantangan Model:* Teksturnya seringkali sangat halus dan samar, sehingga model kesulitan membedakannya dari bayangan atau kulit normal.

        2. *Jerawatan (Acne)*
           - *Ciri Visual:* Munculnya benjolan (papula), bintik merah, atau pori-pori tersumbat yang seringkali meradang.
           - *Tekstur:* Memiliki bentuk 3D (menonjol) dan seringkali memiliki gradasi warna merah yang kuat di area tengah atau pinggir.

        3. *Kemerahan (Redness/Rash)*
           - *Ciri Visual:* Perubahan warna kulit menjadi rona merah yang tersebar (tidak selalu berupa bintik tunggal).
           - *Kondisi:* Seringkali berkaitan dengan iritasi, rosacea, atau kulit sensitif. Dalam dataset, kelas ini memiliki variasi resolusi yang cukup tinggi.

        4. *Kerutan (Wrinkles)*
           - *Ciri Visual:* Adanya garis-garis halus, lipatan, atau kerutan pada permukaan kulit wajah.
           - *Area Umum:* Biasanya terlihat jelas di sekitar mata (crow's feet), dahi, dan garis senyum.
           - *Fitur Model:* Model mengenali pola garis berkelanjutan sebagai fitur utama kelas ini.

        5. *Normal*
           - *Ciri Visual:* Kulit yang sehat dengan warna yang merata, pori-pori kecil, dan tidak ada gangguan warna atau tekstur yang signifikan.
           - *Baseline:* Berfungsi sebagai data pembanding utama (ground truth) untuk kulit yang tidak memerlukan perawatan khusus medis/kosmetik saat ini.
        """)


# MAIN

if __name__ == "__main__":
    run()