def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    a = [0] * 31
    while (x > 0):
        k = 0
        while (2 ** k <= x):
            k = k + 1
        k -= 1
        x -= 2 ** k
        a[k] = 1

    b = [0] * 31
    while (y > 0):
        l = 0
        while (2 ** l <= y):
            l = l + 1
        l -= 1
        y -= 2 ** l
        b[l] = 1
    print(b)
    c = 0
    for i in range(31):
        if (a[i] != b[i]):
            c += 1
    return c