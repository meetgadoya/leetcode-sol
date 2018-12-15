def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    s = str(x)
    if s[::-1] == s:
        return True
    return False