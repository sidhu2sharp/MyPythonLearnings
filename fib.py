def fib(n):
    return n if n in [0, 1] else fib(n - 2) + fib(n - 1)

print (fib(9))