#------------ Create classes, attributes, methods etc
# Connect to database
# Implement functionality
# Implement GUI
# Database path: "C:\\Users\\Developer\\Desktop\\TaskManagementApp\\Database\\TaskManagementDB\\TaskManagementDB"

#Imports
import sqlite3


def initialize_database():
    # Create connection
    connection = sqlite3.connect('TaskManagementDB.db')

    # Initialize tables if they don't exist
    with connection:
        cursor = connection.cursor()

    """
    # Create Table Project
    cursor.execute("CREATE TABLE Project (UniqueID TEXT PRIMARY KEY,Name TEXT,Description TEXT);")

    # Create Table Person
    cursor.execute("CREATE TABLE Person (UniqueID TEXT PRIMARY KEY,Name TEXT,Company TEXT,Role TEXT);")

    # Create Table Task
    cursor.execute("CREATE TABLE Task (UniqueID TEXT PRIMARY KEY,Name TEXT,Status TEXT,Assignee TEXT,Project TEXT,DateCreated TEXT,DateStarted TEXT,DateClosed TEXT,TimeTracked INTEGER,Priority TEXT,Description TEXT,Dependencies TEXT,CompletionPercentage INTEGER,FOREIGN KEY (Assignee) REFERENCES Person(UniqueID),FOREIGN KEY (Project) REFERENCES Project(UniqueID));")
    """

    return connection

# Initialize the database connection
db_connection = initialize_database()


def show_tables(db_connection):
    with db_connection:
        cursor = db_connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("Tables in the database:")
        for table in tables:
            print(table[0])

# Assuming db_connection is your SQLite database connection
show_tables(db_connection)
