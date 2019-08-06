# last 2 cases fails due to timeout
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        while len(tokens) > 1:
            for i, op in enumerate(tokens):
                if op == "+":
                    t = tokens.pop(i)
                    res = int(tokens[i - 2]) + int(tokens[i - 1])
                    a = tokens.pop(i - 1)
                    b = tokens.pop(i - 2)
                    tokens.insert(i - 2, str(res))
                    # print(tokens)
                    break

                elif op == "-":
                    t = tokens.pop(i)
                    res = int(tokens[i - 2]) - int(tokens[i - 1])
                    a = tokens.pop(i - 1)
                    b = tokens.pop(i - 2)
                    tokens.insert(i - 2, str(res))
                    # print(tokens)
                    break
                elif op == "*":
                    t = tokens.pop(i)
                    res = int(tokens[i - 2]) * int(tokens[i - 1])
                    a = tokens.pop(i - 1)
                    b = tokens.pop(i - 2)
                    tokens.insert(i - 2, str(res))
                    # print(tokens)
                    break
                elif op == "/":
                    t = tokens.pop(i)
                    res = float(tokens[i - 2]) / int(tokens[i - 1])
                    if res % 1 != 0 and res < 0:
                        res = int(res)
                    a = tokens.pop(i - 1)
                    b = tokens.pop(i - 2)
                    tokens.insert(i - 2, str(int(res)))
                    # print(tokens)
                    break
        return int(tokens[0])

# more optimized solution
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(float(l)/ int(r)))                    
        return stack.pop()
