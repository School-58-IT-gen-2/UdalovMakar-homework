def factorial(n):
    for i in range(1, n):
        n *= i
    return n
def going(n):
    return round(1 / factorial(n) * sum([factorial(i) for i in range(1, n + 1)]), 6)