def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    s=0
    start=prices[0]
    i=0
    while(i<len(prices)):
        k=i
        start=0
        end=0
        while(i>0 and (prices[i]>prices[i-1])):
            i=i+1
            if(i>=len(prices)):
                i=k
                break
        start=prices[i]
        j=i+1
        l=j
        print(j)
        while(j<len(prices) and prices[j]>prices[j-1]):
            end=prices[j]
            j=j+1
            if(j>=len(prices)):
                j=j-1
                break
        if(end>start):
            s+=end-start
            print("S=",s)
            print("Start,End=", start, end)

        i=j
        print("Final",i,j)
    return s
print(maxProfit([5,4,3,2,1]))