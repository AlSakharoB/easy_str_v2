def ft_len(str):
    length = 0
    for c in str:
        length += 1
    return length


def ft_change_place_word(str):
    length = ft_len(str)
    index_s = 0
    f_word = ""
    s_word = ""
    for i in range(length):
        if str[i] == " ":
            index_s = i
    f_word = str[:index_s]
    s_word = str[index_s + 1:]
    return s_word + str[index_s] + f_word
