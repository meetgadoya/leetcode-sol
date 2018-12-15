def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sums = 0
    i = 0
    while i < (len(s) - 1):
        if s[i] == 'I':
            if s[i + 1] == 'V':
                sums += 4
                i = i + 1
            elif s[i + 1] == 'X':
                sums += 9
                i = i + 1
            else:
                sums += 1
        elif s[i] == 'X':
            if s[i + 1] == 'L':
                sums += 40
                i = i + 1
            elif s[i + 1] == 'C':
                sums += 90
                i = i + 1
            else:
                sums += 10
        elif s[i] == 'C':
            if s[i + 1] == 'D':
                sums += 400
                i = i + 1
            elif s[i + 1] == 'M':
                sums += 900
                i = i + 1
            else:
                sums += 100
        else:
            sums += dic[s[i]]
        i += 1
    if (i <= (len(s) - 1)):
        sums += dic[s[i]]
    return sums