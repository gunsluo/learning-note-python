
def test():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
            else:
                print(n, 'not equals', x, '*', n//x)
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')

test()

