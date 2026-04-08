import sqlite3

def create_connection(db_file):
    """ Create a database connection with the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print('SQLite database version:', sqlite3.sqlite_version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    create_connection('example.db')

