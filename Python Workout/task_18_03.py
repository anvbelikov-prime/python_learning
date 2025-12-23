import collections

def get_vowel_stats(file_path):
    vowels = set('aeiou')
    stats = collections.defaultdict(int)
    with open(file_path, 'r') as f:
        for line in f:
            for c in line.strip().lower():
                if c in vowels:
                    stats[c] += 1
    return stats

print(get_vowel_stats('linux-etc-passwd.txt'))
