# Aplikasi Klasifikasi Spesies Penguin dengan Streamlit

[cite_start]Ini adalah proyek aplikasi web interaktif yang dibangun menggunakan Streamlit sebagai implementasi dari **Studi Kasus Praktikum Data Mining**. Aplikasi ini menerapkan model klasifikasi _machine learning_ untuk memprediksi spesies penguin (Adelie, Chinstrap, atau Gentoo) berdasarkan data pengukuran fisiknya.

## Tampilan Aplikasi

Berikut adalah tampilan dari aplikasi yang telah dibuat.

*(**Saran:** Ambil screenshot aplikasi Anda yang sedang berjalan, simpan di dalam folder proyek, dan ganti `screenshot.png` di bawah dengan nama file gambar Anda)*


## Fitur

* **Prediksi Interaktif**: Pengguna dapat memasukkan data fitur penguin melalui _slider_ dan mendapatkan prediksi spesies secara _real-time_.
* [cite_start]**Visualisasi Data**: Menampilkan grafik _scatter plot_ dan _histogram_ untuk membantu memahami hubungan dan distribusi data.
* [cite_start]**Tampilan Data**: Opsi untuk menampilkan tabel data mentah dari dataset yang digunakan.
* **Antarmuka Terstruktur**: Menggunakan navigasi tab untuk memisahkan halaman informasi dan halaman prediksi agar lebih rapi.
* [cite_start]**Informasi Performa Model**: Menampilkan akurasi model yang telah dilatih.

## Teknologi yang Digunakan

* **Python**: Bahasa pemrograman utama.
* [cite_start]**Streamlit**: _Framework_ untuk membangun dan _deploy_ aplikasi web.
* [cite_start]**Pandas**: Untuk manipulasi dan analisis data.
* [cite_start]**Scikit-learn**: Untuk membangun dan mengevaluasi model klasifikasi _Random Forest_.
* **Seaborn & Matplotlib**: Untuk membuat visualisasi data.

## Instalasi dan Setup

Untuk menjalankan proyek ini di lingkungan lokal, ikuti langkah-langkah berikut:

**1. Persiapan Awal**
   * [cite_start]Pastikan Anda sudah menginstal Python (versi 3.8 atau lebih baru).
   * Clone repositori ini atau unduh file proyek dalam bentuk ZIP.

**2. Buat Virtual Environment**
   [cite_start]Buka terminal di dalam folder proyek, lalu jalankan perintah berikut untuk membuat _virtual environment_:
   ```bash
   python -m venv .venv
   ```

**3. Aktifkan Virtual Environment**
   [cite_start]Aktifkan _environment_ yang baru dibuat sesuai dengan sistem operasi Anda:
   * **Windows (Command Prompt):**
     ```bash
     .venv\Scripts\activate.bat
     ```
   * **Windows (PowerShell):**
     ```bash
     .venv\Scripts\Activate.ps1
     ```
   * **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```

**4. Install Library yang Dibutuhkan**
   Setelah _environment_ aktif, install semua _library_ yang diperlukan dengan satu perintah. Buat file bernama `requirements.txt` dan isi dengan teks di bawah, lalu jalankan perintah `pip install -r requirements.txt`.

   *Isi file `requirements.txt`:*
   ```txt
   streamlit
   pandas
   scikit-learn
   seaborn
   matplotlib
   ```

   *Perintah untuk install:*
   ```bash
   pip install -r requirements.txt
   ```

## Cara Menjalankan Aplikasi

[cite_start]Setelah semua _library_ terinstal, jalankan aplikasi menggunakan perintah berikut di terminal:
```bash
streamlit run app.py
```
Aplikasi akan otomatis terbuka di _browser_ default Anda.

## Struktur Folder

Proyek ini memiliki struktur folder sebagai berikut untuk memastikan semua komponen berjalan dengan baik:
```
proyek-penguin/
├── images/
│   ├── adelie.jpg
│   ├── chinstrap.jpg
│   └── gentoo.jpg
├── .venv/
├── app.py
├── penguins.csv
├── requirements.txt
└── README.md
```

## Dataset

Proyek ini menggunakan dataset **Palmer Penguins**. Dataset ini berisi data observasi dari 344 penguin yang terdiri dari 3 spesies berbeda. Sumber data untuk proyek ini adalah file `penguins.csv` yang disimpan secara lokal.
