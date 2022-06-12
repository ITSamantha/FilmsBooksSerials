import sqlite3
from sqlite3 import Error

PATH = "DataBase/projectDB"


class ControllerForDB(object):

    def create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    def select_all_from_tables(self, table_name):
        connection = ControllerForDB.create_connection(self, PATH)
        cursor = connection.cursor()
        query = f"select * from {table_name};"
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