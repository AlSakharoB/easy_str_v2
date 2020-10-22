def ft_len(str):
    length = 0
    for c in str:
        length += 1
    return length


def ft_remove_str(d, x):
    c = 0
    b = ''
    for i in d:
        if i in x:
            c += 1
        else:
            b += i
    if ft_len(d) == c:
        return False
    else:
        return b
    