def fibonacci(n):      # q1
    if n <= 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(6))
