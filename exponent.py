def exponent(a, n):
    # Base Case
    if n < 0:
        denominator = exponent(a, -n)
        return 1 / denominator
    if n == 0:
        return 1
    elif n % 2 == 1:
        half = exponent(a, n//2)
        return half * half * a
    elif n % 2 == 0:
        half = exponent(a, n // 2)
        return half * half


print(exponent(2, -7))
