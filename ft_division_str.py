def ft_len(str):
    length = 0
    for c in str:
        length += 1
    return length


def ft_division_str(str):
    length = ft_len(str)
    str1 = str[:length // 2 + length % 2]
    str2 = str[length // 2 + length % 2:]
    return str2 + str1
