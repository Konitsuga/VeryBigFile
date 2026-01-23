def within_and_has_double_quotes(x):
    l = list(x)
    length = len(l)
    if ((l[0] == '"') and
        (l[-1] == '"')):
            for i in range(1,length-1):
                if l[i] == '"':
                    return True
    return False
print(within_and_has_double_quotes('lo"ve'))
# replace_middle_element_of_a_tuple_with_n_times_middle
def replace_middle_with_n_times_middle(y,n):
    l = list(y)
    length = len(l)
    middle = len(l)//2
    l2 = []
    for i in range(0, middle):
        l2 = l2 + [l[i]]
    for j in range(n):
        l2 = l2 + [l[middle]]
    for k in range((middle+1), length):
        l2 = l2 + [l[k]]
    return tuple(l2)
# Count_Positive_Integers_Ignoring_None
def Count_Positive_Integers_Ignoring_None(z):
    count = 0
    for i in z:
          if i != None:
            if i > 0:
                count += 1
    return count
# Matrix Walk
def matrix_shape(x, y):
    l = []
    length = len(x)
    if y == 'L':
        for i in range(length):
            l = l + [x[i][0]]
        for j in range(1, length):
            l = l + [x[length-1][j]]
    elif y == 'Z':
        for i in range(length):
            l = l + [x[0][i]]
        for j in range(length-1):
            l = l + [x[j+1][abs(j - length+2)]]
        for k in range(1, length):
            l = l + [x[length-1][k]]
    elif y == 'O':
        for i in range(length-1):
            l = l + [x[0][i]]
        for j in range(length):
            l = l + [x[j][length-1]]
        for k in range(length-1):
            l = l + [x[length-1][abs(length - k -2)]]
        for k2 in range(length-2):
            l = l + [x[abs(length - k2 -2)][0]]
    return l