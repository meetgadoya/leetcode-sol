# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        self.x_address = ""
        # to find address of x
        def find_helper_x(root, x):
            if self.x_address == "":
                if root.val == x:
                    self.x_address = root
                    return
                if root.left:
                    find_helper_x(root.left,x)
                if root.right:
                    find_helper_x(root.right,x)
                               
        def helper_y(y,num, x):
            if y is None:
                return num
            if y.left and y.left.val != x:
                num = helper_y(y.left, num + 1, x)
            if  y.right and y.right.val != x:
                num = helper_y(y.right, num + 1,x)
            return num
        
        find_helper_x(root,x)

        no_of_nodes_x_left = 0
        no_of_nodes_x_right = 0
        no_of_nodes_x_parent = 0
        if self.x_address.left:
            no_of_nodes_x_left = helper_y(self.x_address.left,1, x)
            if no_of_nodes_x_left > n/2:
                return True
        if self.x_address.right:
            no_of_nodes_x_right = helper_y(self.x_address.right,1, x)
            if no_of_nodes_x_right > n/2:
                return True

        no_of_nodes_x_parent = n - (no_of_nodes_x_left + no_of_nodes_x_right) -1
        if no_of_nodes_x_parent > n/2:
            return True
        
        
        return False
            
 #######################################################################################################################################
 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        c = [0, 0]
        def count(node):
            if not node: return 0
            l, r = count(node.left), count(node.right)
            if node.val == x:
                c[0], c[1] = l, r
            return l + r + 1
        
        return count(root) / 2 < max(max(c), n - sum(c) - 1)
