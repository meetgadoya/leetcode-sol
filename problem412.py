def fizzBuzz(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    c = []
    for i in xrange(1, n + 1):
        if (i % 3 == 0 and i % 5 == 0):
            c.append("FizzBuzz")
        elif (i % 3 == 0):
            c.append("Fizz")
        elif (i % 5 == 0):
            c.append("Buzz")
        else:
            c.append(str(i))
    return c