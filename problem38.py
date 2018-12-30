def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    l = ["1"]
    if (n == 1):
        return l[0]
    for i in range(1, n):
        l = self.helper(l)
    # print("K",k)
    return l[0]


def helper(self, l):
    b = l.pop()
    a = b[0]
    c = 0
    res = ""

    for j, ch in enumerate(b):

        if ch == a:
            # print("repeated")
            c += 1
        else:

            res = res + str(c) + a
            a = ch
            c = 1
            # print("Res",res)
            # if (j+1)==len(b):
    res = res + str(c) + ch
    # print("Res",res)
    l.append(res)
    # print("L=",l)
    # self.helper(n,l,i+1)
    return l
