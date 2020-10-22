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


def ft_analysis(str):
    rev_str = ft_reverse_str(str)
    print(str[2])
    print(str[ft_len(str) - 2])
    print(str[:5])
    print(str[:ft_len(str) - 2])
    print(str[::2])
    print(str[1::2])
    print(ft_reverse_str(str))
    print(rev_str[::2])
    print(ft_len(str))
