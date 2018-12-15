def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    s = ""

    j = 1000000
    for i in range(len(strs)):
        k = len(strs[i])
        if (k < j):
            j = k
    k = 0
    if len(strs) == 0:
        return ""
    while (k < j):
        flag = 0
        for i in range(len(strs)):
            if strs[0][k] != strs[i][k]:
                flag = 1
                return s

        s = s + strs[0][k]
        k += 1
    return s
