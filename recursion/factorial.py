# Compute the factorial of some num n
def factorial(n):
    base_cases = (0, 1, 2)
    if n in base_cases:
        return n
    else:
        return n * factorial(n - 1)

print(factorial(3)) # should be 6
print(factorial(5)) # should be 120?
