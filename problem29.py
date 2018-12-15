def divide(self, dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    if abs(divisor) > abs(dividend):
        return 0
    elif abs(divisor) == 1:
        q = abs(dividend)
    else:
        q = 0
        r = 1
        d = abs(dividend)
        c = abs(divisor)
        while (d >= c):
            d -= c
            q += r
            r += r
            c += c
            if (d < c):
                r = 1
                c = abs(divisor)
    if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
        q = q
    else:
        q = q * -1
    return min(max(-2147483648, q), 2147483647)
