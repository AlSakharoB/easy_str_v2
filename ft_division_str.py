def ft_len(str):
    length = 0
    for c in str:
        length += 1
    return length


def ft_division_str(str):
    length = ft_len(str)
    print(str[:length // 2 + length % 2])
    print(str[length // 2 + length % 2:])
