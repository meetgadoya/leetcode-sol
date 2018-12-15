def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    h = root
    if h:
        return (max(1 + self.maxDepth(h.left), 1 + self.maxDepth(h.right)))
    else:
        return 0