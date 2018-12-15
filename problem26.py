def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    l = 0
    n = len(nums)
    j = i + 1
    if (len(nums) == 0):
        return 0
    while (j < n):
        if (nums[j] <= nums[i]):
            j += 1
            continue
        nums[i + 1], nums[j] = nums[j], nums[i + 1]
        l = l + 1
        j += 1
        i += 1
    return l + 1
