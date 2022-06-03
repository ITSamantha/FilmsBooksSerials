import psycopg2 as bd


class ControllerForDB(object):
    # Constants
    DB_NAME = 'FilmsBooksSerials'
    DB_USER = 'postgres'
    DB_PASSWORD = '01dr10kv'
    DB_HOST = 'localhost'

    def ConnectToDB(self, db_name=DB_NAME, db_user=DB_USER,db_pass=DB_PASSWORD,db_host=DB_HOST):

        connection = bd.connect(dbname=db_name,
                                user=db_user,
                                password=db_pass,
                                host=db_host
                                )
        self.cursor = connection.cursor()

    def example(self):
        self.cursor.execute("SELECT * FROM books")
        rec = tuple(self.cursor.fetchall())
        self.cursor.close()
        return rec

