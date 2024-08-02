# Laporan Proyek Machine Learning - Jericho Luthfi Syahli

## Domain Proyek

Proyek ini bertujuan untuk memprediksi harga salah satu saham berdasarkan data historis saham tersebut. Hal ini dapat bermanfaat sebagai salah satu insight dalam memprediksi kapan waktu yang tepat untuk membeli saham.
  

## Business Understanding

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Bagaimana cara memprediksi harga saham menggunakan data historis?
- Apa faktor-faktor yang paling mempengaruhi harga saham?
  
### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Menggunakan algoritma Random Forest untuk membangun model prediksi harga saham.
- Mengidentifikasi fitur-fitur penting dari data yang mempengaruhi harga saham.

    ### Solution statements
    - Saya menggunakan 2 Algoritma dengan hyperparameter tuning. 2 Algoritma tersebut adalah Random Forest dan XGBoost untuk melihat mana yang paling cocok.
    - Mengevaluasi performa model dengan metrik MSE.

## Data Understanding
Dataset yang digunakan adalah data historis harga saham yang mencakup beberapa variabel penting. Data ini dapat diunduh dari [Data](https://finance.yahoo.com/quote/BBRI.JK/history/). Berikut adalah variabel yang ada dalam dataset:

- Open: Harga pembukaan saham pada hari tertentu.
- High: Harga tertinggi saham pada hari tertentu.
- Low: Harga terendah saham pada hari tertentu.
- Adj Close: Harga penutupan yang disesuaikan untuk dividen dan pemecahan saham.
- Volume: Jumlah saham yang diperdagangkan pada hari tertentu.
- Close: Harga penutupan saham pada hari tertentu (target yang diprediksi).

Beberapa teknik dilakukan untuk memahami data salah satunya adalah Correlation untuk melihat relationship yang dimiliki tiap kolom. 

## Data Preparation
Proses data preparation meliputi:
- Checking Outlier : Melihat dan membersihkan outlier yang ada. Pembersihan dilakukan dengan menghapus outlier.
- Split Data: Membagi data menjadi set pelatihan dan pengujian. Dilakukan pembagian 80:20 untuk training dan testing data.
- Feature Scaling: Menggunakan MinMaxScaler untuk menskalakan fitur sehingga berada dalam rentang [0, 1]. Scaling dilakukan terlebih dahulu untuk data training. Lalu saat model akan dievaluasi data testing baru discaling.
  
## Modeling
Model Random Forest Regressor.
    Parameter:
        n_estimators: 200
        max_depth: 8
        random_state: 55
        n_jobs: -1

Model XGBoost
   Parameter:
        learning_rate = 0.08
        n_estimators = 200
        max_depth = 4
        random_state: 55
        
Setelah mengevaluasi kedua model, yaitu Random Forest dan XGBoost, model Random Forest menunjukkan performa yang lebih baik dalam hal MSE. Berdasarkan hasil ini, Random Forest dipilih sebagai model terbaik untuk memprediksi harga saham karena memiliki performa lebih baik dalam memprediksi harga saham. Dan juga memiliki nilai MSE yang lebih kecil dibanding dengan XGBoost.

## Evaluation
Evaluasi dilakukan dengan menggunakan:
    Mean Squared Error (MSE)

Setelah itu dilakukan plotting untuk perbandingan prediction vs actual keseluruhan data.

