# Check is even or divisible by 5
# Write a function is_even_or_divisible_by_5 
# that takes an integer as input and return True if it is even or is divisible by 5 else False.
def is_even_or_divisible_by_5(x):
    return x % 5 == 0 or x % 2 == 0

'''
Deinterleave Even and Odd Indices in String
Write a function deinterleave that takes a string s as input 
and returns a new string where
the characters at even indices are placed 
before the characters at odd indices.
'''
def deinterleave(x):
    l = list(x)
    z = []
    for i in range(0, len(l), 2):
        z.append(l[i])
    for j in range(1, len(l), 2):
        z.append(l[j])
    return ''.join(z)
print(deinterleave('01345'))