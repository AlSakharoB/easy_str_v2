def ft_len(str):
    length = 0
    for c in str:
        length += 1
    return length


def ft_count_words(str):
    wordcount = 0
    length = ft_len(str)
    f = False
    count = 0
    for i in range(length):
        if f == False and str[i] != " ":
            f = True
            count += 1
        if str[i] == " ":
            f = False
    return count

