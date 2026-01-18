import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input
import pandas as pd
from PIL import Image
import tensorflow as tf

@st.cache_resource
def load_my_model():
    # Pastikan file .keras berada di folder yang sama dengan app.py
    # Jika di dalam folder 'model', gunakan './model/Skin_Project.keras'
    return load_model('./model/Skin_Project.keras')

Skin_Project = load_my_model()

# Pastikan label ini urutannya sama dengan folder saat training
labels = ['Darkspot', 'Jerawatan', 'Kemerahan', 'Kerutan', 'Normal']

def run():
    st.title("Aplikasi Klasifikasi Kondisi Kulit Wajah")
    st.write("Unggah foto wajah untuk mendeteksi kondisi kulit.")

    uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img_display = Image.open(uploaded_file)
        st.image(img_display, caption='Gambar yang diunggah', use_container_width=True)
        
        if st.button('Mulai Prediksi'):
            with st.spinner('Sedang memproses...'):
                # 1. Preprocessing Gambar
                img = img_display.resize((224, 224)) 
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                
                # Preprocessing khusus MobileNetV2
                img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

                # 2. Prediksi
                predictions = Skin_Project.predict(img_array)
                
                # Mengonversi output menjadi probabilitas menggunakan Softmax
                score = tf.nn.softmax(predictions[0]) 
                
                # Mengambil indeks kelas dengan nilai tertinggi
                class_idx = np.argmax(score)
                # Menghitung persentase keyakinan
                conf_score = np.max(score) * 100

                # 3. Tampilkan Hasil
                st.subheader(f"Hasil Prediksi: {labels[class_idx]}")
                st.info(f"Tingkat Keyakinan (Confidence): {conf_score:.2f}%")
                
                # Menampilkan grafik probabilitas untuk semua kelas
                chart_data = pd.DataFrame(score, index=labels, columns=['Probabilitas'])
                st.bar_chart(chart_data)

if __name__ == '__main__':
    run()