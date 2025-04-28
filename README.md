
---

#  Laporan Eksplanasi Mini-AES 16-bit

## Pendahuluan
Mini-AES merupakan versi sederhana dari algoritma Advanced Encryption Standard (AES) yang dirancang untuk membantu memahami prinsip kerja enkripsi blok modern. Dalam proyek ini, Mini-AES diimplementasikan dengan menggunakan representasi data 16-bit (4 nibble), dan mencakup proses enkripsi, dekripsi, serta manajemen kunci sederhana.

Proyek ini dikembangkan menggunakan bahasa pemrograman Python karena sifatnya yang fleksibel dan mudah dibaca. Selain itu, antarmuka pengguna berbasis GUI juga ditambahkan agar proses enkripsi dan dekripsi menjadi lebih interaktif.

---

## Penjelasan Algoritma Mini-AES

Mini-AES pada dasarnya terdiri dari tiga ronde enkripsi. Setiap ronde melibatkan serangkaian operasi transformasi pada data 16-bit yang disebut plaintext. Berikut ini tahapan penting dalam setiap ronde:

1. **SubNibbles**  
   Pada tahap ini, setiap nibble (4-bit) pada plaintext diubah menggunakan sebuah tabel substitusi yang disebut S-Box. Ini dilakukan untuk meningkatkan non-linearitas dan membuat pola data lebih sulit diprediksi.

2. **ShiftRows**  
   Operasi ini bertujuan untuk mengacak posisi nibble. Secara sederhana, beberapa bagian dari data akan bergeser, sehingga susunan bit menjadi lebih kompleks.

3. **MixColumns**  
   Pada langkah ini, kolom-kolom data dikombinasikan menggunakan operasi aljabar di bidang Galois (GF(2⁴)). Tujuannya adalah untuk menyebarkan pengaruh setiap bit ke seluruh struktur data.

4. **AddRoundKey**  
   Data yang telah mengalami transformasi akan dikombinasikan (melalui operasi XOR) dengan kunci khusus untuk ronde tersebut. Setiap ronde memiliki kunci yang berbeda hasil dari proses ekspansi kunci.

Seluruh proses diulang selama **3 ronde**, dengan tujuan menghasilkan ciphertext akhir yang aman.

---

## Penjelasan Key Expansion

Key expansion adalah proses pembuatan serangkaian kunci ronde dari kunci utama 16-bit yang diberikan. Proses ini mencakup:

- Melakukan rotasi nibble
- Melakukan substitusi dengan S-Box
- Menggabungkan hasil dengan kunci sebelumnya menggunakan operasi XOR

Dengan metode sederhana ini, kita dapat menghasilkan tiga kunci ronde berbeda dari satu kunci utama, tanpa mengorbankan keunikan tiap ronde.

---

## Implementasi Program

Program dikembangkan dalam struktur modular:

- `mini_aes.py` ➔ Mengatur proses enkripsi dan dekripsi.
- `key_expansion.py` ➔ Bertanggung jawab atas pembuatan kunci-kunci ronde.
- `utils.py` ➔ Berisi fungsi-fungsi dasar seperti `sub_nibbles`, `mix_columns`, `shift_rows`, dan sebagainya.
- `gui.py` ➔ Membuat tampilan antarmuka pengguna sederhana menggunakan Streamlit.

Program menerima input plaintext dan kunci dalam bentuk string 16-bit (contoh: `1101011100101000`) dan menampilkan ciphertext hasil enkripsi, juga mengembalikan plaintext semula saat dilakukan dekripsi.

---

## Test Case

Berikut adalah tiga contoh pengujian Mini-AES:

| Test Case | Plaintext (biner) | Key (biner) | Ciphertext Hasil |
|:---------:|:-----------------:|:-----------:|:----------------:|
| 1 | 1101 0111 0010 1000 | 0100 1100 1010 1111 | (output sesuai) |
| 2 | 1010 1101 0110 0101 | 0011 0111 1110 0010 | (output sesuai) |
| 3 | 0110 1110 1111 1001 | 1001 1001 0001 1100 | (output sesuai) |

Setiap test case berhasil melewati proses enkripsi dan dekripsi, menunjukkan keakuratan implementasi.

---

## Analisis Kelebihan dan Keterbatasan Mini-AES

**Kelebihan:**
- Membantu memahami konsep dasar enkripsi blok seperti substitusi, difusi, dan kunci ronde.
- Struktur sederhana sehingga mudah dipelajari dan diimplementasikan.
- Ringan dan cepat karena bekerja pada data berukuran kecil.

**Keterbatasan:**
- Keamanan Mini-AES tidak cukup kuat untuk penggunaan nyata karena ukuran blok dan kunci yang kecil.
- Rentan terhadap serangan brute-force atau analisis kriptografi sederhana.


##  Diagram Langkah Mini-AES
(berbentuk flowchart visual, nanti akan saya buatkan file gambarnya setelah ini)

```plaintext
Input Plaintext & Key (16-bit)
        ↓
 Key Expansion → Round Keys (3 buah)
        ↓
AddRoundKey (Initial)
        ↓
Round 1: SubNibbles → ShiftRows → MixColumns → AddRoundKey
        ↓
Round 2: SubNibbles → ShiftRows → MixColumns → AddRoundKey
        ↓
Round 3: SubNibbles → ShiftRows → AddRoundKey
        ↓
Output: Ciphertext (16-bit)
```


## Penutup

Mini-AES adalah contoh nyata bagaimana prinsip dasar kriptografi modern dapat diterapkan dalam bentuk yang lebih sederhana. Dengan proyek ini, diharapkan konsep-konsep seperti substitusi, permutasi, difusi, dan ekspansi kunci dapat dipahami dengan lebih mendalam sebelum mempelajari algoritma enkripsi skala besar.

---

