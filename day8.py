# Check is even or divisible by 5
# Write a function is_even_or_divisible_by_5 that takes an integer as input and return True if it is even or is divisible by 5 else False.
def is_even_or_divisible_by_5(x):
    return x % 5 == 0 or x % 2 == 0
print(is_even_or_divisible_by_5(40))