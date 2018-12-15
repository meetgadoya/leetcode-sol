def fourSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    mini = 999999
    nums.sort()
    a = 0
    b = 0
    c = 0
    d = 0
    N, result = len(nums), []
    i = 0
    while (i < N - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            i += 1
            continue
        j = i + 1
        while (j < N - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                j += 1
                continue
            s = j + 1
            e = N - 1
            while s < e:
                if (nums[i] + nums[j] + nums[s] + nums[e]) == target:
                    result.append([nums[i], nums[j], nums[s], nums[e]])
                if (nums[i] + nums[j] + nums[s] + nums[e]) < target:
                    s += 1
                    while s < e and nums[s] == nums[s - 1]:
                        s += 1
                else:
                    e -= 1
                    while s < e and nums[e] == nums[e + 1]:
                        e -= 1
            j += 1
        i += 1
    return result
