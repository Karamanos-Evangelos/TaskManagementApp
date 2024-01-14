import sqlite3
from queue import Queue

class DatabaseHandler:
    def __init__(self, db_file='TaskManagementDB.db', pool_size=5):
        self.db_file = db_file
        self.pool_size = pool_size
        self.connection_pool = Queue(maxsize=pool_size)
        self._initialize_pool()

    def _initialize_pool(self):
        for _ in range(self.pool_size):
            connection = sqlite3.connect(self.db_file)
            self.connection_pool.put(connection)

    def get_connection(self):
        return self.connection_pool.get()

    def release_connection(self, connection):
        self.connection_pool.put(connection)

    def execute_query(self, query, values=None):
        try:
            with self.get_connection() as connection:
                cursor = connection.cursor()
                if values:
                    cursor.execute(query, values)
                else:
                    cursor.executescript(query)

        except sqlite3.Error as e:
            print(f"Error executing statement: {e}")
        finally:
            self.release_connection(connection)

    def fetch_all(self, query, values=None):
        try:
            with self.get_connection() as connection:
                cursor = connection.cursor()
                if values:
                    cursor.execute(query, values)
                else:
                    cursor.execute(query)
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
            return None

    def initialize_tables(self):
        # Modify or add table creation queries as needed
        create_project_table_query = "CREATE TABLE IF NOT EXISTS Project (UniqueID TEXT PRIMARY KEY, Name TEXT, Description TEXT);"
        create_person_table_query = "CREATE TABLE IF NOT EXISTS Person (UniqueID TEXT PRIMARY KEY, Name TEXT, Company TEXT, Role TEXT);"
        create_task_table_query = "CREATE TABLE IF NOT EXISTS Task (UniqueID TEXT PRIMARY KEY, Name TEXT, Status TEXT, Assignee TEXT, Project TEXT, DateCreated TEXT, DateStarted TEXT, DateClosed TEXT, TimeTracked INTEGER, Priority TEXT, Description TEXT, Dependencies TEXT, CompletionPercentage INTEGER, FOREIGN KEY (Assignee) REFERENCES Person(UniqueID), FOREIGN KEY (Project) REFERENCES Project(UniqueID));"

        self.execute_query(create_project_table_query)
        self.execute_query(create_person_table_query)
        self.execute_query(create_task_table_query)

    def drop_tables(self):
        # Use with caution! This will drop all tables.
        drop_tables_query = "DROP TABLE IF EXISTS Project; DROP TABLE IF EXISTS Person; DROP TABLE IF EXISTS Task;"
        self.execute_query(drop_tables_query)

    def show_tables(self):
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        tables = self.fetch_all(query)
        if tables is not None:
            print("Tables in the database:")
            for table in tables:
                print(table[0])

    def close_connections(self):
        while not self.connection_pool.empty():
            connection = self.connection_pool.get()
            connection.close()
