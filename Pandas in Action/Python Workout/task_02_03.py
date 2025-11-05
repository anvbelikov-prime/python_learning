def strings_stat(*args):
    lengths = [len(s) for s in args]
    return (min(lengths), max(lengths), sum(lengths)/len(lengths))

print(strings_stat('a', 'aa', 'aaa'))
