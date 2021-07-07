def sortarr(a,n):
    a = []
    n = len(a)

    count0 = 0
    count1 = 0
    count2 = 0

    for i in range(n):
        if a[i]==0:
            count0+=1
        elif a[i]==1:
            count1+=1
        elif a[i]==2:
            count2+=1        
    i = 0

    while(count0>0):
        a[i] = 0
        i+=1
        count0-=1
    while(count1>0):
        a[i]=1
        i+=1
        count1-=1            
    while(count2>0):
        a[i]=2
        i+=1
        count2-=1    

def printarr(a,n):
    for i in range(n):
        print(a[i])        

if __name__ == "__main__":
    a = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    n = len(a)

    sortarr(a,n)        