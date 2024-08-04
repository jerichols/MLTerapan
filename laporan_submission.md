# Laporan Proyek Machine Learning - Jericho Luthfi Syahli

## Domain Proyek

### Pengenalan dan Konteks

Saham adalah salah satu instrumen investasi yang memungkinkan individu dan institusi untuk memiliki bagian kepemilikan dalam perusahaan. Memahami harga saham penting karena membantu investor dalam pengambilan keputusan investasi yang lebih baik. Proyek ini bertujuan untuk memprediksi harga saham berdasarkan data historis, memberikan insight mengenai kapan waktu yang tepat untuk membeli atau menjual saham.

### Masalah yang Dihadapi

Investor sering menghadapi tantangan dalam memprediksi pergerakan harga saham yang fluktuatif. Ketidakpastian ini dapat menyebabkan keputusan investasi yang kurang optimal. Dengan memprediksi harga saham secara lebih akurat, investor dapat mengurangi risiko dan memaksimalkan keuntungan.

### Tujuan Proyek

Tujuan proyek ini adalah membangun model Machine Learning yang dapat memprediksi harga saham dengan akurat. Model ini akan membantu investor dalam membuat keputusan investasi yang lebih informed. Proyek ini juga bertujuan untuk mengidentifikasi fitur-fitur yang paling berpengaruh terhadap harga saham.

### Manfaat Proyek

Manfaat dari proyek ini meliputi:
- Memberikan alat yang dapat digunakan oleh investor untuk memprediksi harga saham dengan lebih akurat.
- Mengidentifikasi faktor-faktor kunci yang mempengaruhi harga saham, sehingga membantu dalam strategi investasi.
- Meningkatkan pemahaman tentang dinamika harga saham berdasarkan data historis.

## Business Understanding

### Problem Statements

- Bagaimana cara memprediksi harga saham menggunakan data historis?
- Apa faktor-faktor yang paling mempengaruhi harga saham?

### Goals

- Membangun model prediksi harga saham menggunakan algoritma Machine Learning.
- Mengidentifikasi fitur-fitur penting yang mempengaruhi harga saham.

### Solution Statements

- Menggunakan dua algoritma Machine Learning, yaitu Random Forest dan XGBoost, dengan manual paramater tuning untuk menentukan model yang paling efektif.
- Mengevaluasi performa model dengan metrik Mean Squared Error (MSE) untuk memilih model terbaik.

## Data Understanding

Dataset yang digunakan adalah data historis harga saham yang dapat diunduh dari [Data](https://finance.yahoo.com/quote/BBRI.JK/history/). Dataset ini mencakup variabel-variabel berikut:
- **Open**: Harga pembukaan saham pada hari tertentu.
- **High**: Harga tertinggi saham pada hari tertentu.
- **Low**: Harga terendah saham pada hari tertentu.
- **Adj Close**: Harga penutupan yang disesuaikan untuk dividen dan pemecahan saham.
- **Volume**: Jumlah saham yang diperdagangkan pada hari tertentu.
- **Close**: Harga penutupan saham pada hari tertentu (target yang diprediksi).

Fitur Adj CLose didrop dikarenakan nilai ini baru bisa didapatkan jika market telah ditutup dan merupakan penyesuaian nilai "close" itu sendiri. 

### Informasi Data
- **Ukuran Data Frame**: (5134, 6) sebelum diclean, (4799, 6) setelah diclean
- **Kondisi Data**: Data memiliki Outlier, berjumlah 35
- **Statistik Deskriptif**:
  
  ![gambar](https://github.com/user-attachments/assets/3ed826fc-1cef-4fe1-bef3-358e2cebdba7)

## Data Preparation

### Tahapan Data Preparation

- **Checking Outlier**: Outlier diidentifikasi dan dihapus untuk memastikan kualitas data yang baik.
- **Split Data**: Data dibagi menjadi set pelatihan (80%) dan set pengujian (20%).
- **Feature Scaling**: Menggunakan MinMaxScaler untuk menskalakan fitur ke rentang [0, 1]. Scaling diterapkan terlebih dahulu pada data training, kemudian data testing discaling.

## Modeling

### Random Forest Regressor
Random Forest adalah algoritma ensemble yang menggabungkan beberapa pohon keputusan untuk meningkatkan akurasi prediksi dan mengurangi overfitting. 
- Cara Kerjanya: Random Forest membuat beberapa pohon keputusan selama pelatihan dan menghasilkan rata-rata prediksi dari pohon-pohon individual untuk tugas regresi. Ini mengurangi overfitting dengan merata-ratakan banyak pohon.
- Kelebihan: Menangani dataset besar dengan baik, mengurangi overfitting, dan memberikan pentingnya fitur.
- Kekurangan: Dapat memerlukan sumber daya komputasi yang besar, dan model bisa menjadi besar dan kompleks.

#### Paramater
Parameter ini didapat dengan mencoba berbagai parameter secara manual. 
- **n_estimators**: 200 - Jumlah pohon keputusan dalam hutan.
    - Alasan: Semakin banyak pohon dalam Random Forest, semakin baik kemampuannya dalam menggeneralisasi data dan mengurangi overfitting. Dengan 200 pohon, model dapat  memanfaatkan lebih banyak keputusan individu untuk membuat prediksi yang lebih akurat dan stabil. 
- **max_depth**: 8 - Kedalaman maksimum dari setiap pohon keputusan.
    - Alasan : Nilai 8 dipilih dikarenakan  kompromi yang baik untuk menyeimbangkan kemampuan model dalam menangkap pola data tanpa menjadi terlalu rumit.
- **random_state**: 55 - Nilai acak untuk memastikan hasil yang konsisten.
    - Alasan: Menggunakan random_state memastikan bahwa hasil pelatihan model dapat direproduksi. 
- **n_jobs**: -1 - Menggunakan semua CPU yang tersedia untuk mempercepat proses pelatihan.
    - Alasan: Mengatur n_jobs ke -1 memungkinkan model untuk memanfaatkan semua core CPU yang tersedia, yang mempercepat pelatihan model secara signifikan agar berjalan secara paralel

### XGBoost
XGBoost adalah algoritma boosting yang mengoptimalkan model dengan memperbaiki kesalahan dari model-model sebelumnya.

- Cara Kerjanya: XGBoost membangun ansambel pohon secara berurutan, di mana setiap pohon memperbaiki kesalahan dari pohon sebelumnya. Ini menggunakan boosting gradien untuk mengoptimalkan kinerja model.
- Kelebihan: Performa dan akurasi tinggi, menangani nilai yang hilang, dan memiliki regularisasi bawaan.
- Kekurangan: Dapat kompleks untuk disetel, dan mungkin memerlukan waktu pelatihan yang lebih lama.

#### Parameter
Parameter ini didapat dengan mencoba berbagai parameter secara manual. 
- **learning_rate**: 0.08 - Kecepatan pembelajaran untuk model.
    - Alasan : Learning rate 0.08 dipilih setelah mencoba berbagai learning rate.Learning rate yang terlalu tinggi bisa menyebabkan model tidak stabil dan overfitting, sementara learning rate yang terlalu rendah mungkin memerlukan lebih banyak iterasi untuk mencapai hasil yang optimal
- **n_estimators**: 200 - Jumlah iterasi boosting.
    - Alasan : Dengan nilai 200, model memiliki keseimbangan antara menangkap pola data dan menjaga performa yang stabil.
- **max_depth**: 4 - Kedalaman maksimum pohon keputusan.
    - Alasan : Nilai 4 memastikan model tidak terlalu kompleks tetapi cukup kuat untuk menangkap hubungan yang ada dalam data.
- **random_state**: 55 - Nilai acak untuk konsistensi hasil.
    - Alasan : Menggunakan random_state memastikan bahwa hasil pelatihan model dapat direproduksi. 

## Evaluation

### Metrik Evaluasi

- **Mean Squared Error (MSE)**: Metrik evaluasi yang digunakan untuk mengukur performa model. MSE mengukur rata-rata dari kuadrat selisih antara nilai yang diprediksi dan nilai aktual. MSE yang lebih kecil menunjukkan model yang lebih baik.

  Rumus:
  
   ![gambar](https://github.com/user-attachments/assets/32b75d48-db96-400e-8147-a804e6017167)

    - yi​ adalah nilai aktual dari data ke-i.
    - y^​i​ adalah nilai prediksi dari model untuk data ke-i.
    - n adalah jumlah total data.

Interpretasi MSE

- Ukuran Kesalahan Rata-Rata: MSE memberikan ukuran dari rata-rata kesalahan kuadrat model. Nilai MSE yang lebih rendah menunjukkan bahwa model memiliki kesalahan yang lebih kecil dalam prediksi, dan dengan demikian, performa model lebih baik.
- Skala Kesalahan: Karena MSE melibatkan kuadrat dari selisih antara nilai aktual dan prediksi, MSE lebih sensitif terhadap outlier dibandingkan dengan beberapa metrik lain seperti Mean Absolute Error (MAE). Kesalahan besar akan memberikan kontribusi yang lebih besar pada MSE dibandingkan kesalahan kecil.
- Unit Pengukuran: MSE memiliki unit yang sama dengan kuadrat dari unit data asli. Misalnya, jika data asli adalah harga dalam dolar, maka MSE akan memiliki unit dolar kuadrat. Ini berarti interpretasi langsung dari nilai MSE mungkin tidak selalu intuitif karena tidak berada dalam skala yang sama dengan data asli.
- Perbandingan Model: MSE dapat digunakan untuk membandingkan performa beberapa model regresi. Model dengan MSE lebih rendah dianggap lebih baik karena menunjukkan bahwa prediksi model lebih mendekati nilai aktual.

### Hasil Evaluasi
![gambar](https://github.com/user-attachments/assets/409cc116-0570-484f-886d-c61f7b55cb4b)

#### Analisis Hasil
- Random Forest:
    - Train MSE: 0.188381
   -  Test MSE: 0.366601
  
Random Forest menunjukkan performa yang lebih baik pada data pelatihan dibandingkan data uji, tetapi perbedaan antara Train MSE dan Test MSE menunjukkan adanya overfitting. Model ini mungkin terlalu cocok dengan data pelatihan dan tidak generalisasi dengan baik ke data uji.

  - Feature Importance
    
    Skor kepentingan fitur  menunjukkan seberapa besar kontribusi masing-masing fitur terhadap prediksi model :
    ![gambar](https://github.com/user-attachments/assets/c946e4cc-9f24-4721-87ef-66016ce42853)
    - Low (0.656859): Fitur ini memiliki skor kepentingan tertinggi, yang berarti memiliki pengaruh terbesar terhadap prediksi harga saham oleh model.
    - High (0.221128): Fitur ini juga cukup penting, tetapi tidak sebesar Low.
    - Open (0.111589): Fitur ini berkontribusi moderat terhadap prediksi.
    - Adj Close (0.010415): Fitur ini memiliki pengaruh yang relatif kecil terhadap prediksi.
    - Volume (0.000009): Fitur ini hampir tidak berpengaruh terhadap prediksi.

- Boosting:
      - Train MSE: 0.261435
      - Test MSE: 0.449671
Boosting juga menunjukkan performa yang lebih baik pada data pelatihan dibandingkan data uji, tetapi perbedaan antara Train MSE dan Test MSE lebih besar daripada Random Forest. Ini menunjukkan bahwa Boosting mungkin mengalami overfitting lebih parah dibandingkan Random Forest.

  - Feature Importance
    
    ![gambar](https://github.com/user-attachments/assets/2c6f7bcc-e940-407a-bd42-9bc360044860)
    
      - Low (0.675950): Fitur ini juga merupakan fitur paling penting menurut model XGBoost, hampir sama dengan Random Forest.
      - High (0.213537): Fitur ini juga penting, dengan kontribusi yang mirip dengan Random Forest.
      - Open (0.089589): Fitur ini memiliki pengaruh lebih kecil dibandingkan dengan Low dan High.
      - Adj Close (0.020904): Fitur ini memiliki sedikit pengaruh pada model.
      - Volume (0.000020): Sama seperti di Random Forest, fitur ini hampir tidak berpengaruh.

#### Kesimpulan
Berdasarkan hasil MSE, Random Forest tampaknya lebih baik dibandingkan Boosting karena MSE-nya pada data uji (0.366601) lebih rendah dibandingkan Boosting (0.449671). Ini menunjukkan bahwa Random Forest mungkin lebih baik dalam generalisasi ke data baru. Meskipun kedua model menunjukkan tanda-tanda overfitting, Random Forest memiliki kinerja yang lebih stabil di data uji dibandingkan Boosting.

### Dampak Evaluasi terhadap Business Understanding

- **Problem Statement**: Model Random Forest berhasil menjawab permasalahan dengan memberikan prediksi harga saham yang lebih akurat dibandingkan model XGBoost.
- **Goals**:
    - Tujuan proyek untuk membangun model prediksi yang efektif tercapai dengan memilih Random Forest sebagai model terbaik.
    - 2 Fitur yang memiliki kontribusi besar dalam harga saham adalah Low dan High. 
- **Solution Statement**: Solusi yang diterapkan memberikan dampak positif dengan meningkatkan akurasi prediksi harga saham dan memenuhi kebutuhan investor untuk keputusan investasi yang lebih informed.
