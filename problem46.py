def permute(nums):
    res = []
    dfs(nums, [], res)
    return res


def dfs(nums, path, res):
    if not nums:
        res.append(path)
        #print("res",res)
        # return # backtracking
    for i in range(len(nums)):
        print(nums[:i],nums[i + 1:],path+[nums[i]],res)
        dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

print(permute([1,2,3]))