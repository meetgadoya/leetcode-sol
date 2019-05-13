def partition(s):
    k = [s]
    res=[]
    c=0
    while c<2:
        k=helper(k)
        res.append(k)
        print("In main L",k)
        #res.insert(-1,L)
        print("RES",res)
        c+=1
        # for l in L:
        #     if len(l)>1:
        #         c=0

    print("2nd Time")

    print("In main",res )

def helper(L):
    temp = []
    while L:
        n = L.pop(0)

        #print(L)
        if len(n) < 2:
            temp.extend(n)
        elif len(n) == 2:
            temp.extend(n[0])
            temp.extend(n[1])
            #print("len==2", temp)
        else:
            i = 0
            while i < len(n):
                flag = 0
                for j in range(len(n) - 1, i - 1, -1):
                    #print(i, j)
                    # if(n[i]!=n[j]):
                    #     flag=1
                    #     break
                    if (n[i] == n[j]):
                        # print(i,j)

                        for k in range(i + 1, j):
                            if (n[k] != n[j - k]):
                                flag = 1
                                break
                        if (flag == 1):
                            break
                        else:
                            #print("Hey", i, j, n[i:j + 1])
                            temp.extend([n[i:j + 1]])
                            #print("Temp", temp)
                            i = j
                            break
                i += 1
    L = temp
    print("Final L", L)
    return L


print(partition("aab"))