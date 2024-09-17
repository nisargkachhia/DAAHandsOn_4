def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# Example call for fib(5)
print(fib(5))

def fib(n):
    print(f"Calling fib({n})")
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = fib(n-1) + fib(n-2)
    print(f"fib({n}) = {result}")
    return result

# Example call for fib(5)
fib(5)
