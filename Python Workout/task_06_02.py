def transpose_list(l):
    return [' '.join(e) for e in list(zip(*list(ll.split() for ll in l)))]

print(transpose_list(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']))
