# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# logic : runtime =  60ms beats 89%
class Solution(object):
    def __init__(self):
        self.lowest = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return root
        self.helper(root, p, q)
        return self.lowest

    def helper(self, node, p, q):

        is_node = False
        is_left = False
        is_right = False

        if node.val == p.val or node.val == q.val:
            is_node = True

        if node.left != None:
            is_left = self.helper(node.left, p, q)
            if self.lowest != None:
                return False

        if node.right != None:
            is_right = self.helper(node.right, p, q)
            if self.lowest != None:
                return False

        if is_node + is_left + is_right >= 2:
            self.lowest = node
            return

        return is_node or is_left or is_right

# logic : same logic and code but more optimized
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.lowest = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return root

        def helper(node):

            is_node = False
            is_left = False
            is_right = False

            if node.val == p.val or node.val == q.val:
                is_node = True

            if node.left != None:
                is_left = helper(node.left)
                if self.lowest != None:
                    return self.lowest
                    sys.exit()

            if node.right != None:
                is_right = helper(node.right)
                if self.lowest != None:
                    return self.lowest
                    sys.exit()

            if is_node + is_left + is_right >= 2:
                self.lowest = node
                return
            return is_node or is_left or is_right

        helper(root)
        return self.lowest

