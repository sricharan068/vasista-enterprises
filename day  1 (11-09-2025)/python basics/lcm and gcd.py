def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm_and_gcd(a, b):
    gcd_val = gcd(a, b)
    lcm_val = abs(a * b) // gcd_val if a and b else 0
    return [lcm_val, gcd_val]

# Example usage
a, b = 12, 18
print(lcm_and_gcd(a, b))  # Output: [36, 6]
