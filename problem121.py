def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0
    mini = prices[0]
    ans = 0
    for x in prices:
        temp = x - mini
        if (x < mini):
            mini = x
        if (temp) > ans:
            ans = temp

    return ans