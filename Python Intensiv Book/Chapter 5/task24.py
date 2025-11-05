from collections import defaultdict

def revert_files(input_file, output_file):
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        for line in in_file:
            out_file.write(line[::-1].replace('\n', '') + '\n')

# revert_files("source.txt", "reverted.txt")

def encrypt_file(input_file, output_file):
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        for line in in_file:
            out_file.write(' '.join([str(ord(w)) for w in line[:-1]]) + '\n')

def decrypt_file(input_file, output_file):
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        for line in in_file:
            out_file.write(''.join([chr(int(c)) for c in line[:-1].split()]) + '\n')

# encrypt_file('source.txt', 'encrypted.txt')
# decrypt_file('encrypted.txt', 'source_new.txt')

def split_letters(input_file, vowel_output_file, consonant_output_file):
    with open(input_file, 'r') as in_file, open(vowel_output_file, 'w') as vowel_file, open(consonant_output_file, 'w') as consonant_file:
        for line in in_file:
            vowel_file.write(''.join([w for w in line[:-1] if w.isalpha() and w.lower() in 'aeiou']) + '\n')
            consonant_file.write(''.join([w for w in line[:-1] if w.isalpha() and w.lower() not in 'aeiou']) + '\n')

# split_letters("letters.txt", "vowels.txt", "consonants.txt")

def create_shell_usage(input_file, output_file):
    res = defaultdict(list)
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        for line in in_file:
            line = line.strip().split(':')
            if len(line) < 7:
                continue
            if line[0].startswith('#'):
                continue
            res[line[-1]].append(line[0])
        for k, v in res.items():
            out_file.write(f'{k}: {", ".join(v)}\n')

create_shell_usage("passwd_example.txt", "shell_usage.txt")
