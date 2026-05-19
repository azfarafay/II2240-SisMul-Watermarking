# Evaluasi Kinerja Watermarking (DCT) Terhadap Kompresi JPEG

Repositori ini berisi implementasi dan evaluasi algoritma **Discrete Cosine Transform (DCT) Additive Watermarking** pada citra digital. Proyek ini disusun untuk memenuhi Tugas Mata Kuliah Sistem Multimedia (II2240).

**Oleh:** Azfar Arafi Shofyan - 18224096  

---

## 📌 Deskripsi Proyek
Proyek ini mendemonstrasikan bagaimana sebuah *watermark* (berupa citra biner) disisipkan ke dalam sebuah foto wajah menggunakan transformasi domain frekuensi (DCT). Setelah disisipkan, gambar tersebut dikompresi menggunakan algoritma JPEG dengan berbagai nilai **Quality Factor (QF)** mulai dari 100 hingga 20. 

Tujuan utama dari proyek ini adalah untuk melakukan **Robustness Test** (Uji Ketahanan) guna melihat pada tingkat kompresi berapa *watermark* mulai rusak atau tidak dapat diekstrak kembali.

## 📁 Struktur Repositori
Repositori ini disusun secara modular dengan panduan struktur sebagai berikut:

```text
├── dctwatermark/          # Package utama modul watermarking
│   ├── __init__.py
│   ├── dct.py             # Logika transformasi DCT & IDCT
│   ├── embed.py           # Logika penyisipan & ekstraksi watermark
│   └── jpeg.py            # Simulasi kompresi JPEG
├── examples/
│   └── run_demo.py        # Skrip utama untuk menjalankan simulasi penuh
├── docs/                  # Laporan PDF dan dokumentasi
├── wajah.jpg              # Gambar host (foto wajah)
├── watermark.png          # Gambar watermark (logo/citra biner)
└── README.md