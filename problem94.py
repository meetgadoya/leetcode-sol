def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    h = root
    if h:
        stack = [root]
    else:
        return []
    c = []
    visited = []
    while len(stack) > 0:
        while h.left and (h.left not in visited):
            h = h.left
            stack.append(h)
            visited.append(h)

        h = stack.pop()
        c.append(h.val)
        print(c)
        if h.right and (h.right not in visited):
            h = h.right
            stack.append(h)
            visited.append(h)
        # print(stack)

    return c