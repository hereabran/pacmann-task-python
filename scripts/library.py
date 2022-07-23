from datetime import datetime, timedelta
from scripts.mysql_conn import MysqlConn


class Library(MysqlConn):
    """
    A class to to manage Library and call MySQL connection to execute the right query
    ...

    Attributes
    ----------
    book_stocks: dict

    Methods
    -------
    new_user() -> None
    list_user() -> None
    new_book() -> None
    stock_book() -> None
    list_book() -> None
    find_book(sep_dot="") -> None
    peminjaman(sep_dot="") -> None
    list_peminjaman() -> None
    pengembalian(sep_dot="") -> None
    """
    def __init__(self) -> None:
        self.book_stocks = dict()

    def new_user(self):
        try:
            nama = input("Masukkan nama user: ")
            tgl_lahir = input("Masukkan tanggal lahir (YYYY-MM-DD): ")
            pekerjaan = input("Pekerjaan: ")
            alamat = input("Masukkan Alamat: ")
            query = f"""
            INSERT INTO user (nama, tgl_lahir, pekerjaan, alamat) 
            VALUES("{nama}", "{tgl_lahir}", "{pekerjaan}", "{alamat}");
            """
            self.db_conn().execute_query(query)
        except ValueError as e:
            print("Error: ", e)

    def list_user(self):
        query = "SELECT * FROM user"
        try:
            users = self.db_conn().read_query(query)
            print(users)
        except Exception as e:
            print("Error: ", e)

    def new_book(self):
        try:
            kode_buku = input("Masukkan kode buku: ")
            nama_buku = input("Masukkan nama buku: ")
            kategori = input("Masukkan kategori buku: ")
            stock = input("Stok buku: ")
            query = f"""
            INSERT INTO buku (id_buku, nama_buku, kategori, stock) 
            VALUES("{kode_buku}", "{nama_buku}", "{kategori}", "{stock}");
            """
            self.db_conn().execute_query(query)
        except ValueError as e:
            print("Error: ", e)

    def stock_book(self):
        try:
            query = "SELECT id_buku, stock FROM buku"
            bs = self.db_conn().read_query(query)
            self.book_stocks = bs.to_dict(orient="records")
        except Exception as e:
            print("Error: ", e)

    def list_book(self):
        query = "SELECT * FROM buku"
        try:
            books = self.db_conn().read_query(query)
            print(books)
        except Exception as e:
            print("Error: ", e)

    def find_book(self, sep_dot):
        try:
            string = input("Masukkan nama buku yang anda cari: ")
            query = f"SELECT * FROM buku WHERE nama_buku LIKE '%{string}%'"
            books = self.db_conn().read_query(query)
            print(sep_dot, "\n", books)
        except ValueError as e:
            print("Error: ", e)

    def peminjaman(self, sep_dot):
        try:
            self.stock_book()
            f_date = "%Y-%m-%d"
            id_user = int(input("Masukkan id peminjam: "))
            id_buku = int(input("Masukkan id buku: "))
            stock = [
                data["stock"] for data in self.book_stocks if data["id_buku"] == id_buku
            ][0]
            if stock == 0:
                print(f"Stock buku {id} untuk dipinjamkan: {stock}")
                id_buku = int(input("Masukkan id buku: "))
                stock = [
                    data["stock"]
                    for data in self.book_stocks
                    if data["id_buku"] == id_buku
                ][0]
            nama = input("Masukkan nama peminjam: ")
            buku = input("Masukkan nama buku: ")
            today = datetime.strptime(datetime.today().strftime(f_date), f_date)
            tanggal_pinjam = today.strftime(f_date)
            tanggal_pengembalian = (today + timedelta(days=3)).strftime(f_date)
            queries = {
                "insert": f"""INSERT INTO peminjaman (id_user, id_buku, nama_peminjam, nama_buku, tanggal_pinjam, tanggal_pengembalian) 
                    VALUES("{id_user}", "{id_buku}", "{nama}", "{buku}", "{tanggal_pinjam}", "{tanggal_pengembalian}");""",
                "update": f"UPDATE buku SET stock={(stock - 1) if stock > 0 else 0} WHERE id_buku={id_buku};",
            }
            for q in queries.values():
                self.db_conn().execute_query(q)
            print(sep_dot, "\n", f"Buku dipinjamkan ke: {nama}\n", sep_dot)
        except Exception as e:
            print("Error: ", e)

    def list_peminjaman(self):
        query = "SELECT * FROM peminjaman"
        try:
            peminjamans = self.db_conn().read_query(query)
            print(peminjamans)
        except Exception as e:
            print("Error: ", e)

    def pengembalian(self, sep_dot):
        try:
            self.stock_book()
            id_user = int(input("Masukkan id peminjam: "))
            id_buku = int(input("Masukkan id buku: "))
            stock = [
                data["stock"] for data in self.book_stocks if data["id_buku"] == id_buku
            ][0]
            queries = {
                "delete": f"DELETE FROM peminjaman WHERE id_user={id_user} AND id_buku={id_buku}",
                "update": f"UPDATE buku SET stock={stock + 1} WHERE id_buku={id_buku};",
            }
            for q in queries.values():
                self.db_conn().execute_query(q)
            print(sep_dot, f"\nBuku telah dikembalikan\n", sep_dot)
        except Exception as e:
            print("Error: ", e)
