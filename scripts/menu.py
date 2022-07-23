from scripts.library import Library


class Menu(Library):
    """
    A class to interact with library through Terminal UI menu
    ...

    Attributes
    ----------
    select: int

    Methods
    -------
    main_menu() -> Class
    """
    def __init__(self) -> None:
        super().__init__()
        self.select = int()

    @classmethod
    def main_menu(cls):
        menu = cls()
        text_menu = """
        ............LIBRARY MANAGEMENT............
        1. Pendaftaran User Baru
        2. Pendaftaran Buku Baru
        3. Peminjaman 
        4. Tampilkan Daftar Buku
        5. Tampilkan Daftar User
        6. Tampilkan Daftar Peminjaman
        7. Cari Buku
        8. Pengembalian
        9. Exit
        """
        print(text_menu)
        try:
            select = int(input("Masukkan Nomor Tugas: "))
            if select not in range(1, 10):
                print("Masukan nomor yang tertera pada menu!")
                menu.main_menu()

            menu.select = select
        except ValueError:
            print("Selain angka tidak diperkenankan!")
            menu.main_menu()

        return menu
