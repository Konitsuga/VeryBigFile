# Convert date from mm-dd-yy to yy-dd-mm
def date_format(x):
    l2 = []
    l = list(x)
    for i in range(6, 8, 1):
        l2 = l2 + [l[i]]
    l2 = l2 + ['-']
    for j in range(3, 5, 1):
        l2 = l2 + [l[j]]
    l2 = l2 + ['-']
    for k in range(0, 2, 1):
        l2 = l2 + [l[k]]
    return ''.join(l2)
