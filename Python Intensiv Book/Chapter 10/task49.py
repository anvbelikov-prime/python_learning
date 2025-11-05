import time
import os

def generator_with_time(seq):
    time_start = time.perf_counter()
    time_new = time_start
    for e in seq:
        yield (e, round(time_new - time_start))
        time_start = time_new
        time_new = time.perf_counter()

def generator_with_time_v2(seq, min_timeout):
    time_new = None
    for e in seq:
        time_start = time.perf_counter()
        delta = time_start - (time_new or time_start)
        if min_timeout - round(delta) > 0:
            time.sleep(min_timeout - round(delta))
            time_new = time.perf_counter()
            yield (e, min_timeout)
        else:
            time_new = time.perf_counter()
            yield (e, round(delta))

# for c in generator_with_time_v2('abc', 1):
#     print(c)
#     time.sleep(3)

def format_time(time_in_seconds):
    return time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(time_in_seconds))

def file_usage_generator(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            stat = os.stat(os.path.join(path, file))
            yield (file, format_time(stat.st_atime), format_time(stat.st_mtime), format_time(stat.st_ctime))

# for file_stat in file_usage_generator('.'):
#     print(file_stat)

def filter_seq_generator(seq, func):
    return (e for e in seq if func(e))

for e in filter_seq_generator(range(0, 11), lambda x: x % 2 == 0):
    print(e)
