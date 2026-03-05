# AES-Algorithm-ISD-First-Task-
Laman ini dibuat untuk penjelasan program AES, dibuat dengan menggunakan Python sebagai dasar language.

HOW TO MAKE AES WORK/ENCRYPTION PHASE
1. Menggunakan python, gunakan dan buat fungsi s-box untuk matriks awal
2. Pada fase awal, initial RoundKey, plaintext akan dikonversi menjadi round key pertama lewat bitwise XOR
3. Round Loop/SubBytes: Substitusi non-linear yang diturunkan dari inversi multiplikatif dalam Galois Field (operasi inti diffusion dan confusion pada AES)
4. ShiftRows: Tiap kolom terenkripsi, akan mengalami pergeseran bit melingkar ke kiri pada tiap matriks
5. MixColumns: Lalu dilakukan operasi percampuran linear yang memanipulasi matriks dengan polinomial atas
6. AddRoundKey: Kode matriks akan diubah kembali dengan logika XOR dengan roundkey dari iterasi akhir
7. Dan di output terakhir, output yang dihasilkan untuk generate key AES hanyalah SubBytes, ShiftRows. dan AddRoundKey.

untuk decrypt, lakukan metode inversion pada SubBytes, ShiftRows, MixColumns, dan AddRoundKey dengan logika bitwise XOR

Cara menjalankan:
Masuk ke program bernama AES.py (abaikan .gitignore), lalu run dan coba ketikkan beberapa karakter dan tunggu begitu outputnya keluar. 

Harsya Javier Mahijja
24051204047
TI B 2024
TUGAS 1 KEAMANAN DATA DAN INFORMASI
