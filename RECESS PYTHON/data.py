
print("=========context manager for file handling that automatically opens and closes file=====")
class Filemanager:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# create file
file_path = 'example.txt'
# Open the file in 'r' mode (read mode)
file = open(file_path, 'r')
mode = 'r'

# Using a context manager for file handling
with Filemanager(file_path, mode) as file:
    content = file.read()
    print(content)
print('=====================context manager for managing a database connection.=========================')


import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
db_name = 'example.db'
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Execute a CREATE TABLE query
create_table_query = '''
CREATE TABLE my_table (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);
'''# Using a context manager for database connection
with DatabaseConnection(db_name) as db:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM my_table")
    result = cursor.fetchall()
    for row in result:
        print(row)

