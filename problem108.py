def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if not nums:
        return
    l = len(nums) // 2
    m = nums[l]
    root = TreeNode(m)

    root.left = self.sortedArrayToBST(nums[:l])
    root.right = self.sortedArrayToBST(nums[l + 1:])

    return root