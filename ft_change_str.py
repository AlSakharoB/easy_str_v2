def ft_len(str):
    length = 0
    for c in str:
        length += 1
    return length


def ft_change_str(str1, str2, str3):
    a = ''
    ind = 0
    if str3.find(str1) == -1:
        return False
    else:
        while str3.find(str1) != -1:
            ind = str3.find(str1)
            a = a + str3[:ind] + str2
            str3 = str3[ind + ft_len(str1):]
    return a + str3
