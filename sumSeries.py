def sumSeries(n):
    if n == 1:
        return 1
    elif n > 1:
        before = sumSeries(n - 1)
        return n + before


print(sumSeries(18))
