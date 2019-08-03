 
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # print(n)
        if not n:
            return 1
        if n == 1:
            return x
        if n < 0:
            # print("1st if")
            return 1 / self.myPow(x, -n)
        if n % 2:
            # print("2nd if")
            return x * self.myPow(x, n-1)
        # print("hey")
        return self.myPow(x*x, n/2)
