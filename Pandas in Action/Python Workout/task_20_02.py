import os

def get_files_size():
    res = {}
    for file in [file for file in os.listdir() if os.path.isfile(file)]:
        res[file] = os.stat(file).st_size
    return res 

print(get_files_size())
