# very bruteforce solution but O(N)
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        lis = []
        num = ""
        for ch in s:
            if ch == '+' or ch == '-' or ch == '*' or ch =='/':
                
                lis.append(int(num))
                lis.append(ch)
                num = ""
            else:
                num = num + ch
        lis.append(int(num))
        
        lis1 = []
        for i,op in enumerate(lis):
            if  i == 0:
                lis1.append(op)
                continue
            elif i+1 >= len(lis):
                if lis[i-1]!= '*' and lis[i-1]!= '/':
                    lis1.append(op)
                break
            else:
                if op == '*':
                    first = lis1.pop()
                    res = first * lis[i+1]
                    lis1.append(res)
                elif op == '/':
                    first = lis1.pop()
                    res = int(first/lis[i+1])
                    lis1.append(res)
                elif op == '+':
                    lis1.append(op)
                elif op == '-':
                    lis1.append(op)
                elif lis[i-1]== '*' or lis[i-1]=="/":
                    continue
                else:
                    lis1.append(op)
        if len(lis1)==1:
            return lis1[0]
    
        lis2 = []
        for i,op in enumerate(lis1):
            if i ==0:
                lis2.append(op)
                continue
            if op == '+':
                first = lis2.pop()
                lis2.append(first + lis1[i+1])
                    
            elif op == '-':
                first = lis2.pop()
                lis2.append(first - lis1[i+1])
            
    
        return lis2.pop()
   
 ###########################################################################################################################3
 # opitmized and faster one
 class Solution(object):
    def calculate(self, s):
        s += '+0'
        stack, num, preOp = [], "", "+"
        for i in range(len(s)):
            if s[i].isdigit(): num = num + s[i]
            elif not s[i].isspace():
                if   preOp == "-":  stack.append(-int(num))
                elif preOp == "+":  stack.append(int(num))
                elif preOp == "*":  stack.append(int(stack.pop()) * int(num))
                else:               stack.append(int(float(stack.pop()) / int(num)))
                preOp, num = s[i], ""
        return sum(stack)
