'''
A transaction is possibly invalid if:

    the amount exceeds $1000, or;
    if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.



Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.

Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]

Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
'''
#logic : bruteforce method but passes all test cahse
class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        res = []
        all_transaction = []

        for i, each in enumerate(transactions):
            all_transaction.append(each.split(','))

        n = len(all_transaction)
        check = [0 for i in all_transaction]
        for i, trans in enumerate(all_transaction):
            if int(trans[2]) > 1000:
                res.append(','.join(trans))

                check[i] = 1
                continue
            for j in range(i + 1, n):
                other_trans = all_transaction[j]
                if other_trans
                    if abs(int(trans[1]) - int(other_trans[1])) <= 60 and trans[0] == other_trans[0] and trans[3] != \
                            other_trans[3]:
                        res.append(','.join(trans))
                        res.append(','.join(other_trans))
                        break

        return res

#logic: sorting data by time and then by name
# runs in 88 sec, beats 83% of python code.

class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """

        t = [x.split(',') for x in transactions]
        t.sort(key=lambda x: (x[0], int(x[1])))
        # n = len(t)
        i = 0
        ret = set()
        while i < len(t):
            j = i + 1
            duplicate = False
            while j < len(t) and t[j][0] == t[i][0] and int(t[j][1]) - int(t[i][1]) <= 60:
                if t[j][3] != t[i][3]:
                    duplicate = True
                j += 1

            if duplicate:
                for k in range(i, j):
                    ret.add(','.join(t[k]))
            elif int(t[i][2]) > 1000:
                ret.add(','.join(t[i]))
            i += 1
        return ret

# logic: More better solution with runtime = 60 ms beats 92% soln
# uses technique to maintain dictionary with same name

class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """

        d = {}
        for trans in transactions:
            tran = trans.split(',')
            name = tran[0]

            if name in d:
                d[name].append((int(tran[1]), tran[3]))
            else:
                d[name] = [(int(tran[1]), tran[3])]

        ret = set()
        for trans in transactions:
            tran = trans.split(',')
            name = tran[0]

            if int(tran[2]) > 1000:
                ret.add(trans)
                continue

            for other_names in d[name]:
                if abs(other_names[0] - int(tran[1])) <= 60 and other_names[1] != tran[3]:
                    ret.add(trans)
                    break
        return ret
