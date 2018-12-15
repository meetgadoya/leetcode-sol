def numJewelsInStones(self, J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    c = 0
    for s in S:
        if s in J:
            c += 1
    return c
