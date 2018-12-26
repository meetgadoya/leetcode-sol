class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.s={}
        self.s = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        l1 = len(self.s)
        self.s.add(val)
        l2 = len(self.s)
        if (l2 > l1):
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        l1 = len(self.s)
        if val in self.s:
            self.s.remove(val)
            return True
        # if(l2<l1):
        #     return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        a = random.sample((list(self.s)), 1)
        return a.pop()

##################################      2nd Method      #####################################3333
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        # self.s=set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            self.d[val] = val
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        # l1=len(self.s)
        if val in self.d:
            del self.d[val]
            return True
        # if(l2<l1):
        #     return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        a = self.d[random.choice(list(self.d))]
        return a

