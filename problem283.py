def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 0
    while (i < len(nums) and j < len(nums)):
        while (nums[i] != 0):
            if (i >= len(nums) - 1):
                return
            i += 1

        j = i + 1
        # print(nums,i,j)
        # while(i<len(nums) and j<len(nums)):
        while (j < len(nums)):
            if (nums[j] == 0):
                j = j + 1
                continue
            else:
                break
        if (j < len(nums)):
            # print(i,j)
            nums[i], nums[j] = nums[j], nums[i]
            # print(nums,i,j)
        else:
            # print("Hey")
            return 