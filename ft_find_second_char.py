def ft_len(str):
    length = 0
    for c in str:
        length += 1
    return length


def ft_find_second_char(char, str):
    char_count = 0
    length = ft_len(str)
    i = 0
    while char_count < 2 and i < length - 1:
        if str[i] == char:
            char_count += 1
        i += 1
    if char_count == 2:
        return i - 1
    if char_count == 1:
        return -1
    if char_count == 0:
        return -2
