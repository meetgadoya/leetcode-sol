def divide(dividend, divisor):
    if abs(divisor) > abs(dividend):
        return 0
    elif abs(divisor) == 1:
        q = abs(dividend)
    else:
        q = 0
        r = 1
        d = abs(dividend)
        c=abs(divisor)
        while (d >=c):
            d -= c
            q+=r
            r += r
            c+=c
            if(d<c):
                r=1
                c=abs(divisor)
    if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
        q = q
    else:
        q = q * -1
    if q > (2 ** 31) - 1:
        return (2 ** 31) - 1
    elif q < (-2 ** 31):
        return (-2 ** 31)
    else:
        return q


'''def divide(dividend, divisor):
    if abs(divisor) > abs(dividend):
        return 0
    elif abs(divisor) == 1:
        q = abs(dividend)
    else:
        q = 0
        r = 0
        d = abs(dividend)

        while (d >= abs(divisor)):
            d -= abs(divisor)
            q += 1
    if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
        q = q
    else:
        q = q * -1
    if q > (2 ** 31) - 1:
        return (2 ** 31) - 1
    elif q < (-2 ** 31):
        return (-2 ** 31)
    else:
        return q
'''
print(divide(2147483647,2))