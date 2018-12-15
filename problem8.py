def myAtoi(self, str):
    """
    :type str: str
    :rtype: int
    """
    s = 0
    flag = 1
    j = 0
    for i, ch in enumerate(str):
        if (ch == ' ') and (j == 0):
            continue
        if (ch == '-') and (j == 0):
            flag = -1
            j = 1
            continue
        elif (ch == '+') and (j == 0):
            j = 1
            continue

        if ord(ch) >= 48 and ord(ch) <= 57:
            j = 1
            s = s * 10 + int(ch)

        else:
            break
    s = flag * s
    if (s > (2 ** 31) - 1):
        return ((2 ** 31) - 1)
    elif s < (-(2 ** 31)):
        return (-2 ** 31)
    else:
        return (s)
