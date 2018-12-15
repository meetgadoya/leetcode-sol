def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    d = []
    # nums=[1,2,2]
    for i in nums:
        if i not in d:
            d.append(i)
            # print d
        else:
            # print i
            d.remove(i)
    # print d

    for i in d:
        return i