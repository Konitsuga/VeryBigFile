'''
Check If a number divides two other numbers
Write a function is_both_divisible_by that takes
three integers a, b and c as input and checks if
a and b are divisible by c. Assume that c number is non-zero.
'''
def is_both_divisible_by(x, y, z):
    return x % z == 0 and y % z == 0
print(is_both_divisible_by(12, 13, 4))