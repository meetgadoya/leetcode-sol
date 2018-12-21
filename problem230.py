def kthSmallest(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    self.l = k
    self.res = None
    self.helper(root)
    return self.res


def helper(self, root):
    if root == None:
        return
    self.helper(root.left)
    self.l -= 1
    if self.l == 0:
        self.res = root.val
        return
    self.helper(root.right)
