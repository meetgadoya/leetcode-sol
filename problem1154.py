class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year = date[0:4]
        leap_check = date[2:4]

        month = date[5:7]
        day = date[8:]

        d = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        days = 0
        for i in range(1, int(month)):
            days += d[i]

        days += int(day)
        if int(month) >= 3 and (int(year) % 400 == 0 or (int(year) % 4 == 0 and int(year) % 100 != 0)):
            days += 1

        return days


'''
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Example 2:

Input: date = "2019-02-10"
Output: 41

Example 3:

Input: date = "2003-03-01"
Output: 60

Example 4:

Input: date = "2004-03-01"
Output: 61
'''