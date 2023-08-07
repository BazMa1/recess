#context manager for file handling that automatically opens and closes file
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
print('==============================================')