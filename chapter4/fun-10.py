pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

def tmp_func(pair):
    return pair[1]
pairs.sort(key=tmp_func)
print(pairs)
