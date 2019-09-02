# Factorial of a given Integer


# Non Recursive
def fact(n):
    j = n
    i = 1
    while j > 1:
        i = i * j
        j = j - 1
    return i


# Recursive
def recfact(n):
    if n <= 1:
        return 1
    else:
        return n * recfact(n - 1)


if __name__ == "__main__":
    print(fact(5))
    print(recfact(5))
