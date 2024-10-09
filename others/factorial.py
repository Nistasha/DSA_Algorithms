def factorial(num):
    # Check if num is a non-negative integer
    if not isinstance(num, int) or num < 0:
        return None

    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# Example usage
print(factorial(5))       # Output: 120
print(factorial("5"))     # Output: None
print(factorial(1.2))     # Output: None
print(factorial(-3))      # Output: None
print(factorial(0))       # Output: 1
