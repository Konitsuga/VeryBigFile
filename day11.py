# >>>is_rotation('abcde','cdeab')
# True
# >>>is_rotation('hello','ehllo')
# False
# >>>is_rotation('hello','helol')
# False

def is_rotation(x, y):
    c = x * len(x)
    for i in range(len(c)):
        if c[i:i+len(x)] == y:
                return True
    return False
print(is_rotation('laughing', 'ughingla'))

# Took help of AI
def is_rotation(x, y):
     if len(x) != len(y):
        return False
     else:
        return x in (y + y)
print(is_rotation('laugh', 'ughla'))