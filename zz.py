def fib(n):
    if n == 0 or n == 1:
        return n
    fib_0 = 0
    fib_1 = 1
    for _ in range(n - 1):
        fib = fib_0 + fib_1
        fib_0 = fib_1
        fib_1 = fib
    return fib_1

print(fib(3))