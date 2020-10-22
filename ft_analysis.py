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
    ffw = ""
    all_two = ""
    chet = ""
    ne_chet = ""
    rev_str = ft_reverse_str(str)
    rev_chet = ""
    print(str[2])
    print(str[ft_len(str) - 2])
    for i in range(5):
        ffw += str[i]
    print(ffw)
    for i in range(ft_len(str) - 2):
        all_two += str[i]
    print(all_two)
    # print(str[:-2])
    for i in range(ft_len(str)):
        if i % 2 == 0:
            chet += str[i]
    print(chet)
    # print(str[::2])
    for i in range(ft_len(str)):
        if i % 2 == 1:
            ne_chet += str[i]
    print(ne_chet)
    # print(str[1::2])
    print(ft_reverse_str(str))
    # print(str[ft_len(str)::-1])
    for i in range(ft_len(rev_str)):
        if i % 2 == 0:
            rev_chet += rev_str[i]
    print(rev_chet)
    # print(rev_str[::2])
    print(ft_len(str))


ft_analysis("qwerty")