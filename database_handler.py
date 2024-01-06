import sqlite3

class DatabaseHandler:
    def __init__(self, db_file='TaskManagementDB.db'):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, values=None):
        with self.connection:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)

    def fetch_all(self, query, values=None):
        with self.connection:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()

    def show_tables(self):
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        tables = self.fetch_all(query)
        print("Tables in the database:")
        for table in tables:
            print(table[0])