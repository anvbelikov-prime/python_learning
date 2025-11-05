import os

def get_unique_extensions():
    return {file.split('.')[-1] for file in os.listdir()}

print(get_unique_extensions())
