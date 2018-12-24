def __init__(self, nestedList):
    """
    Initialize your data structure here.
    :type nestedList: List[NestedInteger]
    """
    # print(nestedList)
    self.stack = nestedList[::-1]

    # print self.stack.pop().getInteger()


def next(self):
    """
    :rtype: int
    """
    return self.stack.pop().getInteger()


def hasNext(self):
    """
    :rtype: bool
    """
    while self.stack:
        top = self.stack[-1]
        print(top)
        if top.isInteger():
            return True
        self.stack = self.stack[:-1] + top.getList()[::-1]
    return False