def wordcount(file_path):
    res = {}
    chars_cnt = 0
    words_cnt = 0
    lines_cnt = 0
    uniqs = set()
    with open(file_path, 'r') as f:
        for line in f:
            lines_cnt += 1
            chars_cnt += len(line)
            for word in line.replace('\n', '').split():
                words_cnt += 1
                uniqs.add(word)
    res['chars_cnt'] = chars_cnt
    res['words_cnt'] = words_cnt
    res['lines_cnt'] = lines_cnt
    res['uniqs_cnt'] = len(uniqs)
    return res

print(wordcount('wcfile.txt'))
