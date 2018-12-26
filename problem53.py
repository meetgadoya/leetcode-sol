for i in range(1, len(nums)):
    if nums[i-1] > 0:
        nums[i] += nums[i-1]
print(nums)
return max(nums)