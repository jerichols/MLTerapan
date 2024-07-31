# Laporan Proyek Machine Learning - Nama Anda

## Domain Proyek

Super App merupakan sebuah perusahaan yang bergerak di bidang bisnis atau industri retail.
 
Di dalam bisnis retail, diskon merupakan salah satu strategi untuk menjaga loyalitas customer dalam bertransaksi atau bahkan untuk meningkatkan penjualan.
 
Masalah yang timbul dari strategi ini ialah diskon yang kurang efektif dalam meningkatkan penjualan. Dampaknya ialah dapat merusak margin keuntungan. Selain itu diskon yang terlalu tinggi dapat merusak nilai brand, sementara diskon yang terlalu rendah mungkin tidak cukup menarik bagi pelanggan.
 

**Rubrik/Kriteria Tambahan (Opsional)**:
- Masalah tersebut harus diselesaikan agar pemberian diskon dapat efektif, kita perlu menentukan tingkat diskon yang optimal dengan membentuk cluster-cluster transaksi. Clustering diperlukan untuk mengidentifikasi pola dan karakteristik transaksi berdasarkan fitur-fitur yang relevan, sehingga kita dapat menyesuaikan strategi diskon yang lebih tepat sasaran.

## Business Understanding

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Pemberian diskon kurang efektif dan relevan
- Diskon yang tinggi dapat mengurangi keuntungan per transaksi

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Mengidentifikasi pola transaksi agar pemberian diskon relevan
- Mengidentifikasi pemberian diskon pada setiap transaksi


    ### Solution statements
    - K-Means Clustering untuk mengelompokkan data transaksi sesuai dengan karakteristiknya.

## Data Understanding
Dataset terdiri dari empat bagian utama: lokasi, produk, transaksi, dan pengguna. Dataset lokasi mencakup nama dan kode unik untuk provinsi, kabupaten, dan kecamatan. Dataset produk berisi ID dan nama setiap produk yang dijual. Dataset transaksi mencatat setiap transaksi dengan detail seperti ID transaksi, ID pengguna, ID produk, jumlah uang yang dibelanjakan, jumlah diskon, dan tanggal transaksi. Dataset pengguna mencakup informasi pengguna seperti ID, nama lengkap, jenis kelamin, total uang yang dihabiskan, pengembalian uang, saldo dompet, tanggal bergabung, dan tanggal lahir.

### Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- lokasi : lokasi tempat store
- produk : produk yang dijual
- transaksi : catatan transaksi penjualan
- pengguna : pengguna yang melakukan transaksi

**Rubrik/Kriteria Tambahan (Opsional)**:
- Teknik Exploratory Data Analysis dilakukan serta proses visualisasi pada setiap EDA.

## Data Preparation
- Formatting Data
- Handling Missing Values
- Cleaning Noisy Data
- Concatenate Data

Proses Data Preparation dilakukan agar data dapat diproses dengan baik dan data tersebut digunakan di langkah selanjutnya. 

## Modeling
Pada tahap modeling data, Saya menggunakan K-Means Clustering untuk mengelompokkan data transaksi sesuai dengan karakteristiknya. Berdasarkan Jurnal Penelitian yang saya baca, algoritma ini telah terbukti efektif untuk mengelompokkan data dalam berbagai konteks, termasuk dalam bisnis retail, segmentasi pelanggan, dan analisis transaksi


**Rubrik/Kriteria Tambahan (Opsional)**: 
- K-Means Clustering:
    Kelebihan:
        Mudah dipahami dan diimplementasikan.
        Efisien dalam hal waktu komputasi dengan data besar.
        Memiliki kemampuan untuk menangani data yang cukup besar dan kompleks.
    Kekurangan:
        Memerlukan penentuan jumlah cluster yang optimal (k) yang tidak selalu mudah.
        Sensitif terhadap outlier yang dapat mempengaruhi hasil clustering.
        Asumsi bentuk cluster bulat dapat menyebabkan masalah jika cluster memiliki bentuk yang berbeda.
- Dari elbow method, terlihat bahwa jumlah cluster optimal adalah 2 cluster, yang juga didukung oleh nilai dari Silhouette Score dan Davies-Bouldin Index nya.
Silhouette Score digunakan untuk engukur seberapa dekat setiap titik data dalam sebuah cluster dengan titik data lain dalam cluster yang sama dibandingkan dengan cluster lainnya. Semakin tinggi nilainya menunjukkan clustering yang lebih baik.
DBI (Davies-Bouldin Index) digunakan untuk mengukur kekompakan dan pemisahan antara cluster, di mana nilai yang lebih rendah menunjukkan clustering yang lebih baik.


## Evaluation
Silhouette Score:
- Mengukur seberapa baik setiap titik data dikelompokkan dengan titik data lain dalam cluster yang sama dibandingkan dengan cluster lainnya. Nilai yang lebih tinggi menunjukkan bahwa cluster lebih baik terpisah dan lebih homogen.

Davies-Bouldin Index (DBI):
- Mengukur kekompakan dan pemisahan antara cluster. Nilai yang lebih rendah menunjukkan bahwa cluster lebih baik terpisah satu sama lain dan lebih homogen di dalam cluster.

KPI Cluster Analysis:
- Membandingkan berbagai indikator kinerja antara cluster, seperti jumlah order, pendapatan, anggaran diskon, frekuensi pemesanan, dan average order value untuk memberikan wawasan tentang efektivitas diskon dan karakteristik masing-masing cluster.

Burn Rate Percentage:
- Persentase diskon dari total pembelian, yang membantu menilai seberapa besar diskon diberikan dalam transaksi.

Z-Score dari Burn Rate:
- Menilai seberapa jauh Burn Rate suatu transaksi menyimpang dari rata-rata, memberikan indikasi seberapa efektif diskon dalam transaksi.


