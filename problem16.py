def threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    mini = 999999
    nums.sort()
    a = 0
    b = 0
    c = 0
    N, result = len(nums), []
    for i in range(N):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        s, e = i + 1, N - 1
        while s < e:
            if nums[i] + nums[s] + nums[e] == target:
                return target
            else:
                if (abs(target - (nums[i] + nums[s] + nums[e])) < abs(mini)):
                    mini = abs(target - (nums[i] + nums[s] + nums[e]))
                    a = nums[i]
                    b = nums[s]
                    c = nums[e]
                if ((nums[i] + nums[s] + nums[e]) < target):
                    s += 1
                    while s < e and nums[s] == nums[s - 1]:
                        s += 1
                else:
                    e -= 1
                    while s < e and nums[e] == nums[e + 1]:
                        e -= 1

    return (a + b + c)
