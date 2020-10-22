def ft_len(str):
    length = 0
    for c in str:
        length += 1
    return length


def ft_reverse_str(str):
    res = ""
    for i in range(ft_len(str) - 1, -1, -1):
        res += str[i]
    return res


def ft_char_count(char, str):
    count = 0
    for i in range(ft_len(str)):
        if str[i] == char:
            count += 1
    return count


def ft_find_char(char, str):
    count = ft_char_count(char, str)
    count1 = 0
    count2 = 0
    length = ft_len(str)
    rev_str = ft_reverse_str(str)
    i1 = 0
    j1 = 0
    i = 0
    j = 0
    while count2 < 1 and i < length - 1:
        if str[i] == char:
            i1 = i
            count2 += 1
        i += 1
    while count1 < 1 and j < length - 1:
        if rev_str[j] == char:
            j1 = j
            count1 += 1
        j += 1
    l_char = length - j1 - 1
    if count >= 2:
        return i1, l_char
    if count == 1:
        return i1
    if count == 0:
        return False
