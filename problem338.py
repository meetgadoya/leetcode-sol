def countBits(self, num):
    """
    :type num: int
    :rtype: List[int]
    """
    # s=[]
    '''
    for i in range(num+1):
        #a=[0]*31
        a=0
        while(i>0):
            k=0
            while(2**k<=i):
                k=k+1
            k-=1
            i-=2**k
            a+=1
        s.append(a)
    return s'''
    res = [0] * (num + 1)

    for i in xrange(1, num + 1):
        # print(i,i>>1,i&1)
        res[i] = res[i >> 1] + (i & 1)
    return res