# Face Skin Condition Classification Using Deep Learning

## Problem Background
Kesehatan dan estetika kulit wajah merupakan perhatian utama bagi banyak individu, namun identifikasi masalah kulit seringkali bersifat subjektif dan memerlukan konsultasi ahli yang tidak selalu dapat diakses dengan cepat. Kondisi seperti jerawat, bercak hitam (darkspots), kerutan, dan kemerahan dapat muncul akibat berbagai faktor seperti pola hidup, paparan matahari, atau penuaan. Tanpa deteksi dini yang akurat, penanganan yang salah dapat memperburuk kondisi kulit. Saat ini, masyarakat cenderung melakukan diagnosa mandiri yang kurang akurat sebelum membeli produk perawatan. Oleh karena itu, diperlukan sebuah sistem berbasis kecerdasan buatan (Artificial Intelligence) yang mampu mengklasifikasikan kondisi kulit wajah secara otomatis melalui citra digital. Sistem ini diharapkan dapat memberikan deteksi awal yang objektif untuk membantu pengguna memahami kondisi kulit mereka secara lebih spesifik.

## Project Objective
Proyek ini bertujuan untuk membangun model klasifikasi berbasis Deep Learning yang mampu mengidentifikasi 5 kondisi kulit wajah, yaitu: Darkspot, Jerawatan, Kemerahan, Kerutan, dan Normal. Model dikembangkan untuk memberikan hasil prediksi yang cepat dan akurat berdasarkan input gambar wajah. Dengan adanya sistem ini, diharapkan pengguna dapat melakukan pemantauan kondisi kulit secara mandiri, yang selanjutnya dapat digunakan sebagai referensi awal dalam memilih produk perawatan kulit yang tepat atau memutuskan kapan harus melakukan konsultasi medis profesional.

## Dataset Information
Dataset ini diambil dari link berikut: (https://www.kaggle.com/datasets/harishnivasagam/multi-class-skin-condition-image-dataset-msc-6?utm_source)

## Tech Stacks
Proyek ini dibangun menggunakan **Python** sebagai bahasa utama, dengan dukungan ekosistem library berikut:

| No | Library | Fungsi |
| :--- | :--- | :--- |
| 1 | **OS** | Akses direktori, path dataset, dan manajemen file |
| 2 | **Random** | PShuffle / sampling data secara acak |
| 3 | **Warnings** | Menonaktifkan warning agar output notebook lebih bersih |
| 4 | **Pandas** | Pengolahan data tabular/metadata (jika diperlukan untuk analisis) |
| 5 | **NumPy** | Operasi numerik dan manipulasi array |
| 6 | **Matplotlib** | Visualisasi (grafik training, evaluasi, dsb.) |
| 7 | **TensorFlow** | Framework utama deep learning |
| 8 | **Keras** | Training & inferensi model (Sequential/Model, layers, callbacks, optimizer) |
| 9 | **ImageDataGenerator** | Pipeline input gambar + augmentasi & preprocessing |
| 10 | **MobileNetV2** | Transfer learning backbone untuk ekstraksi fitur |
| 11 | **PIL** | Load untuk manipulasi gambar dasar |
| 12 | **Scikit-learn** | Evaluasi model (classification report, confusion matrix, display) |
| 13 | **Streamlit** | Pembuatan antarmuka aplikasi (Deployment) |

**Tools Pendukung:**
* **VSCode**: Digunakan sebagai *Integrated Development Environment* (IDE) utama untuk penulisan, pengujian, dan pengelolaan kode program.
* **Hugging Face**: Digunakan sebagai platform untuk penyimpanan, publikasi, dan *deployment* model machine learning.

## Project Output
https://huggingface.co/spaces/goetzel11/graded_chll7






