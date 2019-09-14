'''
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.



Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.

Example 2:

Input: n = 100
Output: 682289015

'''

import math
class Solution(object):
    def numPrimeArrangements(self, l):
        """
        :type n: int
        :rtype: int
        """
        if l <= 2:
            return 1

        def permute(no, r):
            p = (math.factorial(no) / math.factorial(no - r))
            return p % (1000000000 + 7)

        def countPrimes(n):

            if n <= 2:
                return 0
            m = n + 1
            composite = [False for i in range(m)]
            composite[0] = True
            composite[1] = True
            for i in range(2, int(n ** 0.5) + 1):
                if composite[i] == False:
                    composite[i * i: m: i] = [True] * len(composite[i * i: m: i])
            return (m - sum(composite))

        no_of_primes = countPrimes(l)
        no_of_comp = l - no_of_primes
        ans = permute(no_of_primes, no_of_primes) * permute(no_of_comp, no_of_comp)
        ans = ans % (1000000000 + 7)
        return ans
