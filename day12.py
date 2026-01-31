'''
Given a list with numbers from 1 to n (inclusive) except one number in 
the range, write a function to find the missing number.
Assume that only one number from the range will be missing in the given list.
'''
def missing_digit_in_list(x):
    a = max(x)
    b = min(x)
    for i in range(b, a + 1):
        if i not in x:
            return i
print(missing_digit_in_list([1, 4, 2, 4, 6, 5, 6]))