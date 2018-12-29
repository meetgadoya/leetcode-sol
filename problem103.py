if not root:
    return []
head = root
level = [head]
ans = []
c = 1
while level:
    ans.append(node.val for node in level)
    temp = []

    c += 1
    while level:
        node = level.pop()
        if c % 2 == 0:
            temp.extend([node.right, node.left])
        else:
            temp.extend([node.left, node.right])

    level = [leaf for leaf in temp if leaf]

return ans