def make_incrementor(n):
    return lambda x: x + n

def make_incrementor2(n):
    def tmp_fun(x):
        return x + n
    return tmp_fun

f = make_incrementor(42)
print(f(0))
print(f(1))

f2 = make_incrementor2(42)
print(f2(0))
print(f2(1))
