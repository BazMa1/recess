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


# context manager for managing a database connection in python

import sqlite3

class DatabaseConnection:
#A context manager for managing a database connection
    def __init__(self, db_name):
        self.db_name =db_name
#Create a database connection.
        self.conn = connect_db(db_name)
    def __enter__(self):
#Return the database connection.
        return self.conn
    def __exit__(self, exc_type, exc_val, exc_tb):
#Close the database connection.
        close_db(self.conn)
        
#connect to databse
def connect_db():
    conn = sqlite3.connect("database.sqlite")
    return conn
def close_db(conn):
#Close the database connection
    conn.close()
    
    
print('===========Show a multithreading and multiprocessing that allows us to run the function for different amounts of time======')  
import time
import threading
import multiprocessing
def function(n):
    time.sleep(n)
    print(f"Function ran for {n} seconds")
def main():
# Create a thread pool with 4 threads
    threads = []
    for i in range(4):
        threads.append(threading.Thread(target=function, args=(i,)))
# Start all of the threads
    for thread in threads:
        thread.start()
# Wait for all of the threads to finish
    for thread in threads:
        thread.join()
def main_multiprocessing():
# Create a process pool with 1 process
    processes = []
    for i in range(1):
        processes.append(multiprocessing.Process(target=function, args=(i,)))
# Start all of the processes
    for process in processes:
        process.start()
# Wait for all of the processes to finish
    for process in processes:
        process.join()
if __name__ == "__main__":
    main()
    main_multiprocessing()