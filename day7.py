# Checks whether a given number is an even two-digit number. 
def is_even_two_digit_number(x):
    l = list(str(x))
    if l[0] == '-':
        if len(l) == 3:
            if int(l[2]) % 2 == 0:
                return True
    elif l[0] != '-':
        if len(l) == 2:
            if int(l[1]) % 2 == 0:
                return True
    return False