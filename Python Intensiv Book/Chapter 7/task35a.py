import string
import json
import collections

def gematria_create_letter_dict():
    return {w: i for i, w in enumerate(string.ascii_lowercase, 1)}

# print(gematria_create_letter_dict())

def create_config_dict(file_path):
    with open(file_path, 'r') as f:
        return {line.strip().split('=')[0]: line.strip().split('=')[1] for line in f}
    
# print(create_config_dict('config.txt'))

# def safe_int(i):
#     try:
#         return int(i)
#     except:
#         return None

def create_config_dict_v2(file_path):
    with open(file_path, 'r') as f:
        return {line.strip().split('=')[0]: int(line.strip().split('=')[1]) for line in f if line.strip().split('=')[1].isdigit()}

# print(create_config_dict_v2('config.txt'))

def create_cities_dict(file_path):
    with open(file_path, 'r') as f:
        cities = json.load(f)
    return {(city['city'], city['state']): int(city['population']) for city in cities}

print(len(create_cities_dict('cities.json')))
