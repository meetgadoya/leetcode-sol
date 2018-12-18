def subsets( nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res=[[]]
    dfs(nums,[],res)
    return res

def dfs(nums,path,res):
    if (path not in res):
        res.append(path)

    for i in range(len(nums)):
        dfs(nums[i+1:],path+[nums[i]],res)
print(subsets([1,2,3,4]))