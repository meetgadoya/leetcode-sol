def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    print(n)
    s = n
    l = []
    while True:
        num = s
        s = 0
        while num > 0:
            a = num % 10
            # print(a)
            s += a * a
            num = num // 10
        if s == 1:
            return True
        elif s in l:
            return False
        else:
            l.append(s)