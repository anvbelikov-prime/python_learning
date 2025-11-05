import string

def ubbi_dubbi(word):
    res = []
    for w in word:
        if w in 'aeiou':
            res.append('ub' + w)
        else:
            res.append(w)
    return ''.join(res)

def ubbi_dubbi_v2(word):
    res = []
    for n, w in enumerate(word):
        if w.lower() in 'aeiou':
            if n == 0 and w.isupper():
                res.append('Ub' + w.lower())
            else:
                res.append('ub' + w)
        else:
            res.append(w)
    return ''.join(res)

# print(ubbi_dubbi_v2('soap'))
# print(ubbi_dubbi_v2('Milk'))
# print(ubbi_dubbi_v2('program'))
# print(ubbi_dubbi_v2('Python'))

input_text = 'This is a very large science pages containing some very important and very difficult results. Authored by NameOne, BigNameTwo, NameThree and with some help of SmallNameFour...'

names = ['NameOne', 'BigNameTwo', 'NameThree', 'SmallNameFour']

def erase_names(text, names):
    res = []
    for word in text.split():
        res_tmp = []
        ending = []
        for w in word:
            if w.isalpha():
                res_tmp.append(w)
            else:
                ending.append(w)
        res_tmp = ''.join(res_tmp)
        ending = ''.join(ending)
        if res_tmp not in names:
            res.append(res_tmp + ending)
        else:
            res.append('_' * len(res_tmp) + ending)
    return ' '.join(res)

# print(erase_names(input_text, names))

def url_encoding(url_path):
    res = []
    for w in url_path:
        if w in (string.ascii_letters + string.digits):
        # if w.isalpha() or w.isdigit():
            res.append(w)
        else:
            res.append(hex(ord(w)).replace('0x', '%'))
    return ''.join(res)

print(url_encoding('https://abc empty/text/_oops'))
