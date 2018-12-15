def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """

    def generate(p, left, right, parens=[]):
        if left:
            # print("In left",left, right)
            generate(p + '(', left - 1, right)
        if right > left:
            # print(left,right)
            generate(p + ')', left, right - 1)
        if not right:    parens += p,
        return parens

    return generate('', n, n)

