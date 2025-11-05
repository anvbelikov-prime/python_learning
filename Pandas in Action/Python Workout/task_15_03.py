import collections

def count_word_letters(file_path):
    stats = collections.defaultdict(int)
    with open(file_path, 'r') as f:
        for line in f:
            for word in line.strip().split():
                stats[len(word)] += 1
    keys_sorted = sorted(stats.keys())
    for k in keys_sorted:
        print(f'{k}-length words: {stats[k]} ones.')

count_word_letters('test.txt')
