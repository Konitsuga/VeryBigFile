def natural_numbers(n):
    if n == 1:
        return 1
    return n, natural_numbers(n-1)
print(natural_numbers(67))

def factorial(n): # recursion for factorial
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)
