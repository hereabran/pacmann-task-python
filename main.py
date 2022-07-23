import sys

from scripts.mysql_conn import MysqlConn
from scripts.menu import Menu


def __main():
    sep_dot = "...................................................."

    if "init" in sys.argv:
        MysqlConn.db_conn(init=True)
    else:
        m = Menu.main_menu()
        if m.select == 1:
            print(sep_dot)
            m.new_user()
            print(sep_dot)
            __main()
        if m.select == 2:
            print(sep_dot)
            m.new_book()
            print(sep_dot)
            __main()
        if m.select == 3:
            print(sep_dot)
            m.peminjaman(sep_dot)
            print(sep_dot)
            __main()
        if m.select == 4:
            print(sep_dot)
            m.list_book()
            print(sep_dot)
            __main()
        if m.select == 5:
            print(sep_dot)
            m.list_user()
            print(sep_dot)
            __main()
        if m.select == 6:
            print(sep_dot)
            m.list_peminjaman()
            print(sep_dot)
            __main()
        if m.select == 7:
            print(sep_dot)
            m.find_book(sep_dot)
            print(sep_dot)
            __main()
        if m.select == 8:
            print(sep_dot)
            m.pengembalian(sep_dot)
            print(sep_dot)
            __main()
        if m.select == 9:
            print(sep_dot, "\n", "Sampai Jumpa")
            sys.exit(1)


if __name__ == "__main__":
    __main()
