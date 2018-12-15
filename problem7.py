def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    temp = abs(x)
    if (temp > math.pow(2, 31)):
        return 0
    sums = 0
    while temp > 0:
        y = temp % 10
        temp = temp / 10
        sums = (sums * 10) + y

    if (x < 0):
        sums = sums * (-1)
    if (abs(sums) > math.pow(2, 31)):
        return 0

    return sums