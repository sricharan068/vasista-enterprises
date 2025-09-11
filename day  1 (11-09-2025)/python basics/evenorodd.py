def check_even_odd(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
x = int(input("Enter a positive integer: "))
print(check_even_odd(x))
