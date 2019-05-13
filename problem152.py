def maxProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    r = nums[0]
    maxi = r
    mini = r
    for x in xrange(1, len(nums)):
        if (nums[x] < 0):
            maxi, mini = mini, maxi

        maxi = max(nums[x], maxi * nums[x])
        mini = min(nums[x], mini * nums[x])
        r = max(r, maxi)
        print(maxi, mini)
    return r