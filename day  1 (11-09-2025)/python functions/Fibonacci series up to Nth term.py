def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def fibonacci_series(n):
    for i in range(n):
        print(fib(i), end=" ")

# Example usage
n = int(input("Enter N: "))
fibonacci_series(n)
