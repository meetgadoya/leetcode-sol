def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    s1 = []
    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            s1.append(ch)

        elif (ch == ')' or ch == '}' or ch == ']') and len(s1) > 0:
            if ch == '}' and (s1.pop() != '{'):
                return False
            elif ch == ']' and (s1.pop() != '['):
                return False
            elif ch == ')' and (s1.pop() != '('):
                return False
        else:
            return False

    if (len(s1) > 0):
        return False
    return True
