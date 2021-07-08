def arrr(mat,n,x):
    if(n==0):
        return -1


    for i in range(n):
        for j in range(n):
            if mat[i][j]==x:
                print(i,j)

x= int(input())
r = int(input())
c = int(input())
mat = [[int(input()) for x in range(c)]for i in range(r)]
n = len(mat)
arrr(mat,x,n)