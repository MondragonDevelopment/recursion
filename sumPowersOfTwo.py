def sumPowersOfTwo(n):
    if n == 1:
        return 2
    elif n > 1:
        before = sumPowersOfTwo(n - 1)
        return 2**n + before


print(sumPowersOfTwo(5))
