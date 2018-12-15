def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    u = []

    if (len(digits) == 0):
        return u

    d = {'2': {'a', 'b', 'c'}, '3': {'d', 'e', 'f'}, '4': {'g', 'h', 'i'}, '5': {'j', 'k', 'l'}, '6': {'m', 'n', 'o'},
         '7': {'p', 'q', 'r', 's'}, '8': {'t', 'u', 'v'}, '9': {'w', 'x', 'y', 'z'}}
    s = list(d[digits[0]])
    # print(type(s))
    l = 1
    while (l < len(digits)):
        t = list(d[digits[l]])
        # u=list(s)

        for i in range(len(s)):
            for j in range(len(t)):
                u.append(s[i] + t[j])
        s = u.copy()
        u.clear()
        l += 1

    # s=s*"a"
    return s
