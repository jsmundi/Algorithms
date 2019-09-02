# Fibonacci Sequence


# Recursive
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def fibbottomup(n):

    fibarr = []

    for i in range(n):
        if i == 0:
            fibarr.insert(0, 0)
        elif i == 1:
            fibarr.insert(1, 1)
        else:
            fibarr.insert(i, fibarr[i - 1] + fibarr[i - 2])

    return fibarr[n-1]

if __name__ == '__main__':
    print("Answer {0}".format(fib(44)))
    #print((fibbottomup(44)))