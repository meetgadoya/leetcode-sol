def findDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    t = nums[0]
    h = nums[0]
    while True:
        t = nums[t]
        h = nums[nums[h]]
        if h == t:
            break
    p1 = nums[0]
    p2 = t
    while p1 != p2:
        p1 = nums[p1]
        p2 = nums[p2]
    return p1s