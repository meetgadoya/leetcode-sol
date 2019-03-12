# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        head = root
        while (root != None):
            pre = root
            # print(root.val)
            if val > root.val:
                root = root.right
            else:
                root = root.left

        root = TreeNode(val)
        if (val > pre.val):
            pre.right = root
        else:
            pre.left = root
        return head
