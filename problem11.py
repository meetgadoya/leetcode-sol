def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    s = 0

    maxo = 0
    e = len(height) - 1
    while (s < e):

        if (height[s] >= height[e]):
            maxo = max(((e - s) * height[e]), maxo)
            e -= 1
        else:
            maxo = max(((e - s) * height[s]), maxo)
            s += 1

    return maxo