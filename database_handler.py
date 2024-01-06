import sqlite3

class DatabaseHandler:
    def __init__(self, db_file='TaskManagementDB.db'):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, values=None):
        try:
            with self.connection:
                if values:
                    self.cursor.execute(query, values)
                else:
                    self.cursor.execute(query)
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def fetch_all(self, query, values=None):
        try:
            with self.connection:
                if values:
                    self.cursor.execute(query, values)
                else:
                    self.cursor.execute(query)
                return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
            return None

    def show_tables(self):
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        tables = self.fetch_all(query)
        if tables is not None:
            print("Tables in the database:")
            for table in tables:
                print(table[0])

    def close_connection(self):
        try:
            self.connection.close()
        except sqlite3.Error as e:
            print(f"Error closing connection: {e}")
