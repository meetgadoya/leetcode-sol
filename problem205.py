'''
Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

'''

# My bruteforce solution. passes all test case.
# logic: runtime = 1084ms
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        ans = 0
        composite = [False for i in range(n)]

        for i in range(2, n):
            if composite[i] == False:
                ans += 1
                j = i
                while j < n:
                    composite[j] = True
                    j += i
        return ans

########################################################################################################################
#logic : runtime = 416 ms
# similar approach to above one but in a smarter way.
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return 0
        ans = 0
        composite = [False for i in range(n)]
        composite[0] = True
        composite[1] = True
        for i in range(2, int(n ** 0.5) + 1):
            if composite[i] == False:
                composite[i * i: n: i] = [True] * len(composite[i * i: n: i])
        return (n - sum(composite))