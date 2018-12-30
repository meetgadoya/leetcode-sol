def numIslands(grid):
    a=len(grid)
    b=len(grid[0])
    #print((a,b))
    c=0             #Count
    global v
    v=[[0]*b for i in range(a)]    #Visited
    #print(v)
    s=[]            #States
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            s.append((i,j))
    i=j=0
    #print(s)


    while(i<a):
        j=0
        while(j<b):
            if (int(grid[i][j])==1 and v[i][j]==0):
               
                helper(s,grid, c, i, j)
                #print(v)
                c=c+1
            j=j+1
        i=i+1

    #v[2][2]=1
    #print(v)
    return c


def helper(s,grid,c,i,j):
    global v
    if (i,j) in s:
        #print((i,j))
        if((int(grid[i][j])==1) and (v[i][j]==0)):
            #print(v,i,j)
            v[i][j]=1
            helper(s,grid,c,i+1,j)
            helper(s,grid, c, i-1 , j)
            helper(s,grid, c, i, j-1)
            helper(s,grid, c, i , j+1)


print(numIslands([["0","1","0"],["1","0","1"],["0","1","0"]]))