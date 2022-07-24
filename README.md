### Tujuan Pengerjaan
>Untuk memenuhi Tugas 4 Python Programming Pacmann non-degree program BI Batch 9

## Deskripsi Tasks
#### 1. `main.py` dan Class Menu
- Membuat folder dengan nama `scripts` untuk menyimpan class yang dibutuhkan program.
- Membuat file [scripts/menu.py](scripts/menu.py) dan membuat `Class Menu` untuk menampilkan Command-line Interactive Menu.
- `Class Menu` juga berfungsi sebagai `Child Class` untuk berinteraksi dengan fungsi library.
- `main.py` berfungsi sebagai control flow.
#### 2. `Class MysqlConn` dan `Classmethod db_conn(cls, init: bool)`
- membuat file [scripts/mysql_conn.py](scripts/mysql_conn.py) untuk menampung fungsi-fungsi yang berhubungan dengan Database Connection & Queries.
- saat inisialisasi instance magic method `__init__(self)` akan di-call dan akan membuat koneksi ke Database, jika konksi gagal akan di print error.
- method `init_db(self)` berfungsi untuk inisialisasi DB seperti Create Database dan Create Tables if not exist.
- method `execute_query(self, query)` saat di-call akan mengeksekusi query yang tidak me return data seperti query `CREATE TABLE`, `UPDATE table SET`, `INSERT INTO` dan query lainnya yang tidak me return data.
- method `read_query(self, query)` saat di-call akan mengeksekusi query `SELECT` dan mereturn data dalam bentuk `pandas.DataFrame`.
#### 3. `Class Library`
- Class yang di buat khusus untuk manajemen library dan gerbang untuk eksekusi query MySQL untuk melakukan tugas yang spesifik.
- membuat file [scripts/library.py](scripts/library.py) untuk menampung class beseta method yang dibutuhkan.
- method `new_user(self)` dan `list_user(self)` berfungsi untuk me-manage user seperti membuat user baru dan menampilkan semua user yang terdata di Database.
- method `new_book(self)` berfungsi untuk membuat buku baru didalam LMS, method `list_book(self)` berfungsi untuk menampilkan daftar buku yang terdata di Database dan method `find_book(self)` berfungsi untuk mencari buku yang terdata di Database dengan memasukkan keyword.
- method `stock_book(self)` berfungsi untuk mensinkronisasi stock buku yang ada di Database dengan instance property `self.book_stock` yang nantinya dijadikan sebagai referensi nilai awal.
- method `peminjaman(self)` berfungsi untuk me-manage alur peminjaman buku dari mulai menginputkan data peminjam ke table peminjaman hingga mengupdate stock buku.
- method `list_peminjaman(self)` berfungsi untuk menampilkan daftar peminjam dan tanggal deadline pengembaliannya.
- method `pengembalian(self)` berfungsi untuk mengupdate stock buku ke stock awal sebelum di pinjam dan menghapus peminjam di daftar peminjaman buku.

## How to run the program
#### Prerequisites:
##### create .env file from .example.env
```bash
cp .example.env .env
```
##### Populate the value inside `.env` for local DB Connection
##### Install dependencies
```bash
pip install -r requirements.txt
```
#### Run the program:
#### 1. Initial Database (Create Database and Tables)
```bash
python main.py init
```
#### 2. Run `main.py`
```bash
python main.py
```

## Hasil Test Case
#### 1. Pendaftaran User
  - **Menginputkan Data**
  * ![input data](img/1-sel-1.png)
  - **Menampilkan Data User Setelah Insert**
  * ![input data](img/2-sel-5.png)
#### 2. Pendaftaran Buku
  - **Menginputkan Buku**
  * ![input data](img/3-sel-2.png)
  - **Menampilkan Daftar Buku**
  * ![input data](img/4-sel-4.png)
  - **Mencari nama buku dengan keyword**
  * ![input data](img/5-sel-7.png)
#### 3. Peminjaman
  - **Menginputkan Data Peminjaman dan Menampilkan Data Buku Setelah Dilakukan Peminjaman (Stock Berkurang)**
  * ![input data](img/6-sel-3.png)
  - **Menampilkan Data Peminjaman**
  * ![input data](img/7-sel-6.png)
#### 4. Pengembalian
  - **Menginputkan Data Pengembalian**
  * ![input data](img/8-sel-8.png)
  - **Menampilkan Data Buku Setelah Pengembalian (Stock terupdate) dan Menampilkan Data Peminjaman Setelah Pengembalian (Data di Peminjaman Terhapus)**
  * ![input data](img/9-sel-4.png)
#### 5. Exit
  * ![input data](img/10-sel-9.png)

### Saran Perbaikan
> masih banyak potensi error dan bug dari user input sehingga prinsip polymorphism tidak terpenuhi, selanjutnya bisa dibuat banyak kondisi dan exception agar menghindari kesalahan input dan kesalahan program.
