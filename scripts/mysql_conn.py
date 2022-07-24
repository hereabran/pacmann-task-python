import os
import mysql.connector
import pandas as pd

from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

db_host = str(os.environ.get("DB_HOST"))
db_user = str(os.environ.get("DB_USER"))
db_pass = str(os.environ.get("DB_PASS"))
db_name = str(os.environ.get("DB_NAME"))


class MysqlConn:
    """
    A class to create connection to MySQL Database and execute queries
    ...

    Attributes
    ----------
    host_name: str
    user: str
    user_pass: str
    db_name: str

    Methods
    -------
    __create_conn() -> None
    __create_database() -> None
    execute_query(query="") -> None
    read_query(query="") -> pd.DataFrame() 
    init_db() -> None
    """
    host_name: str = db_host
    user: str = db_user
    user_pass: str = db_pass
    db_name: str = db_name

    def __init__(self) -> None:
        try:
            self.conn = mysql.connector.connect(
                host=MysqlConn.host_name,
                user=MysqlConn.user,
                password=MysqlConn.user_pass,
                auth_plugin="mysql_native_password",
            )
        except Error as err:
            print(f"Error: {err}")

    def __create_conn(self):
        try:
            self.conn = mysql.connector.connect(
                host=MysqlConn.host_name,
                user=MysqlConn.user,
                passwd=MysqlConn.user_pass,
                auth_plugin="mysql_native_password",
                database=MysqlConn.db_name,
            )
            # print("MySQL database connection successfull")

        except Error as err:
            print(f"Error: {err}")

    def __create_database(self):
        conn = self.conn
        cursor = conn.cursor()
        try:
            query = f"""
            CREATE DATABASE IF NOT EXISTS {self.db_name}
            """
            cursor.execute(query)
            print("Database created successfully!")
        except Error as err:
            print(f"Error: {err}")

    def execute_query(self, query):
        self.__create_conn()
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            self.conn.commit()
            print("Query executed successfully!")
        except Error as err:
            print(f"Error: {err}")

    def read_query(self, query):
        self.__create_conn()
        cursor = self.conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        return pd.DataFrame(result, columns=columns)

    def init_db(self):
        self.__create_database()
        q_table = {
            "user": """CREATE TABLE IF NOT EXISTS user(
                        id_user INT(6) AUTO_INCREMENT PRIMARY KEY,
                        nama VARCHAR(50) NOT NULL,
                        tgl_lahir DATE NOT NULL,
                        pekerjaan VARCHAR(50),
                        alamat VARCHAR(50)
                    );""",
            "buku": """CREATE TABLE IF NOT EXISTS buku(
                        id_buku INT(6) AUTO_INCREMENT PRIMARY KEY,
                        nama_buku VARCHAR(50) NOT NULL,
                        kategori VARCHAR(50),
                        stock INT(10) NOT NULL
                    );""",
            "peminjaman": """CREATE TABLE IF NOT EXISTS peminjaman(
                        id_user INT(6),
                        id_buku INT(6),
                        nama_peminjam VARCHAR(50),
                        nama_buku VARCHAR(50),
                        tanggal_pinjam DATE NOT NULL,
                        tanggal_pengembalian DATE NOT NULL,
                        FOREIGN KEY (id_user) REFERENCES user(id_user),
                        FOREIGN KEY (id_buku) REFERENCES buku(id_buku)
                    );""",
        }
        for q in q_table.values():
            self.execute_query(q)
