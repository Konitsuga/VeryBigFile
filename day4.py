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