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

# def Count_Positive_Integers_Ignoring_None(x):
     