# Face Skin Condition Classification Using Deep Learning

## Problem Background
`Kesehatan dan estetika kulit wajah merupakan perhatian utama bagi banyak individu, namun identifikasi masalah kulit seringkali bersifat subjektif dan memerlukan konsultasi ahli yang tidak selalu dapat diakses dengan cepat. Kondisi seperti jerawat, bercak hitam (darkspots), kerutan, dan kemerahan dapat muncul akibat berbagai faktor seperti pola hidup, paparan matahari, atau penuaan. Tanpa deteksi dini yang akurat, penanganan yang salah dapat memperburuk kondisi kulit. Saat ini, masyarakat cenderung melakukan diagnosa mandiri yang kurang akurat sebelum membeli produk perawatan. Oleh karena itu, diperlukan sebuah sistem berbasis kecerdasan buatan (Artificial Intelligence) yang mampu mengklasifikasikan kondisi kulit wajah secara otomatis melalui citra digital. Sistem ini diharapkan dapat memberikan deteksi awal yang objektif untuk membantu pengguna memahami kondisi kulit mereka secara lebih spesifik.`

Objective.`

## Project Output
`Output dari proyek ini adalah sebuah laporan analisis data lengkap dengan visualisasi, csv data yang sudah bersih, dan dashboard https://public.tableau.com/views/PenjualanSepatuAdidasTahun2021diAmerika/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link.`

## Data
`Dataset ini diambil dari link berikut: https://www.kaggle.com/datasets/davidmashishi/adidas-shoes-sales?resource=download Terdiri dari 12 kolom dan 9641 baris`

## Method
`Analisis ini menggunakan metode statistika deskriptif dan inferensial. Statistika deskriptif digunakan untuk melihat jumlah data numerik dengan menggunakan SUM dan groupby. Agregasi data dan visualisasi (grafik garis, batang, dan heatmap) digunakan untuk mengidentifikasi tren dan perbandingan jumlah atau rata-rata penjualan. Selain itu, uji hipotesis korelasi diterapkan untuk membuktikan signifikansi hubungan antara harga per unit dan total unit yang terjual, dan terakhir menggunakan heatmap sebagai acuan untuk melihat koefisien korelasi, dan menghasilkan yang terkuat adalah total sales sangat berkorelasi dengan total profit, yang artinya, semakin tinggi total penjualan, maka semakin tinggi juga profitnya. Dataload dan data cleaning juga dilakukan sebelum data diolah`

## Stacks
`Bahasa Pemrograman: Python

Library:

pandas dan numpy untuk manipulasi dan pengolahan data.

matplotlib dan seaborn untuk visualisasi data.

scipy untuk melakukan uji hipotesis (t-test).`

## Reference
`Link dataset (kaggle): https://www.kaggle.com/datasets/davidmashishi/adidas-shoes-sales?resource=download`

---



