def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = [1] * len(nums)

    p = 1
    for i in range(len(nums)):
        res[i] *= p
        p *= nums[i]
    print(res)
    p = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= p
        p *= nums[i]

    return res
