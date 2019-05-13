class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        l=preorder.pop(0)
        head=root
        while (len(preorder) > 0):
            node = preorder.pop(0)
            if(node>root.val):
                new=TreeNode(node)
                root.left=new
                root=new
            else:
                new = TreeNode(node)
                root.right = new
                root = new
            l=preorder.pop(0)


s=Solution()
print(s.bstFromPreorder([8,5,1,7,10,12]))

