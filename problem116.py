"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# logic: Runtime : 44 ms beats 98.17%
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        # logic: code to find the Level order of the tree
        head = root

        queue = [root]
        res = []
        while queue:
            temp = []
            for node in queue:
                if node.left != None:
                    temp.append(node.left)
                if node.right != None:
                    temp.append(node.right)
            res.append(queue)
            queue = temp

        for level in res:
            if len(level) == 1:
                level[0].next = None
                continue
            for i in range(0, len(level) - 1):
                level[i].next = level[i + 1]
            level[-1].next = None

        return head

#logic: combining both parts into one
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        queue = [root]
        root.next = None
        while queue:
            temp = []
            for node in queue:
                if node.left != None:
                    temp.append(node.left)
                if node.right != None:
                    temp.append(node.right)

            if temp:
                for i in range(0, len(temp) - 1):
                    temp[i].next = temp[i + 1]
                temp[-1].next = None

            queue = temp

        return root


