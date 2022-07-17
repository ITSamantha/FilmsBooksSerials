import sqlite3
from sqlite3 import Error

PATH = "DataBase/projectDB"


class ControllerForDB(object):

    @staticmethod
    def create_connection(path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    @staticmethod
    def select_all_from_tables(table_name):
        connection = ControllerForDB.create_connection(PATH)
        cursor = connection.cursor()
        query = f"SELECT * FROM {table_name};"
        try:
            cursor.execute(query)
            res = cursor.fetchall()
            return res
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            if connection:
                connection.close()
                print("The SQLite connection is closed")


    #FILMS
    @staticmethod
    def insert_into_films(film_title,year,impression,isLike,date,picture = None):
        try:
            connection = ControllerForDB.create_connection(PATH)
            cursor = connection.cursor()
            query = f"""insert into films(film_title,film_year,film_impression,film_like,film_date,film_picture) 
                        values('{film_title}',{year},'{impression}',{isLike},'{date}',{'null' if picture is None else picture});"""
            cursor.execute(query)
            connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"DB error.{e}")
            return False



    #SERIALS
    @staticmethod
    def insert_into_serials(serial_title,year,impression,isLike,date):
        try:
            connection = ControllerForDB.create_connection(PATH)
            cursor = connection.cursor()
            query = f"""insert into serials(serial_title,serial_year,serial_impression,serial_like,serial_date) 
                    values('{serial_title}',{year},'{impression}',{isLike},'{date}')"""
            cursor.execute(query)
            connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"DB error.{e}")
            return False


    #BOOKS

    @staticmethod
    def insert_into_books(book_title,author,impression,isLike,date):
        try:
            connection = ControllerForDB.create_connection(PATH)
            cursor = connection.cursor()
            query = f"""insert into books(book_title, book_author, book_impression, book_like, book_date) 
                    values('{book_title}', '{author}', '{impression}', {bool(isLike)}, '{date}');"""
            cursor.execute(query)
            connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"DB error.{e}")
            return False

