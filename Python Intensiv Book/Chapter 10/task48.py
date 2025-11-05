import os

def all_files_reader(path):
    file_count = 0
    for dir_tuple in os.walk(path):
        for file in dir_tuple[2]:
            if file.startswith('.'):
                continue
            try:
                f = open(os.path.join(dir_tuple[0], file), 'r')
            except:
                continue
            file_count += 1
            line_count = 0
            for line in f:
                line_count += 1
                yield (file, file_count, line_count, line.strip())
            f.close()

def all_files_reader_v2(path):
    file_count = 0
    for dir_tuple in os.walk(path):
        for file in dir_tuple[2]:
            if file.startswith('.'):
                continue
            try:
                f = open(os.path.join(dir_tuple[0], file), 'r')
            except:
                continue
            file_count += 1
            line_count = 0
            for line in f:
                line_count += 1
                if line_count == file_count:
                    yield (file, file_count, line_count, line.strip())
            f.close()

def all_files_reader_v3(path, s):
    file_count = 0
    for dir_tuple in os.walk(path):
        for file in dir_tuple[2]:
            if file.startswith('.'):
                continue
            try:
                f = open(os.path.join(dir_tuple[0], file), 'r')
            except:
                continue
            file_count += 1
            line_count = 0
            for line in f:
                line_count += 1
                if s in line.strip():
                    yield (file, file_count, line_count, line.strip())
            f.close()

for line in all_files_reader_v3('.', 'def'):
    print(line)
