import json
import csv
import os
import collections
import operator

def show_scores(path):
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) and not file.startswith('.') and file.endswith('.json')]
    for file in sorted(files):
        res = collections.defaultdict(list)
        print(os.path.join(path, file))
        with open(os.path.join(path, file), 'r') as f:
            parsed_json = json.loads(f.read())
            for d in parsed_json:
                for k in d:
                    res[k].append(d[k])
        for k in sorted(res.keys()):
            print(f'`{k}: min {min(res[k])}, max {max(res[k])}, avg {sum(res[k]) / len(res[k])}')

# show_scores('./json-files')

def passwd_csv_to_json(input_file, output_file):
    res = []
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        r = csv.reader(in_file, delimiter=":")
        for line in r:
            if len(line) < 7:
                continue
            if line[0].startswith('#'):
                continue
            res.append(tuple(line))
        print(res)
        json.dump(res, out_file)
    print('Done!')

# passwd_csv_to_json("passwd_example.txt", "passwd_csv_to_json.json")

passwd_names = {
    0: 'login',
    1: 'password',
    2: 'uid',
    3: 'guid',
    4: 'comment',
    5: 'home',
    6: 'shell'
}

def passwd_csv_to_json_dict(input_file, output_file, descriptions):
    res = []
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        r = csv.reader(in_file, delimiter=":")
        for line in r:
            if len(line) < 7:
                continue
            if line[0].startswith('#'):
                continue
            res.append({descriptions[i]: line[i] for i in range(len(line))})
        json.dump(res, out_file)
    print('Done!')

# passwd_csv_to_json_dict("passwd_example.txt", "passwd_csv_to_json_dict.json", passwd_names)

def create_directory_stats(path, output_file):
    res = []
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) and not file.startswith('.')]
    for file in files:
        stat = os.stat(os.path.join(path, file))
        res.append({'name': file, 'size': stat.st_size, 'last_modification': stat.st_mtime})
    with open(output_file, 'w') as f:
        json.dump(res, f)
    print('File created!')

def calc_directory_stats(input_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    print(sorted(data, key=operator.itemgetter('last_modification'), reverse=True)[0])
    print(sorted(data, key=operator.itemgetter('size'), reverse=True)[0])
    print(sorted(data, key=operator.itemgetter('size'), reverse=False)[0])

create_directory_stats('./test', 'stats.json')
calc_directory_stats('stats.json')
