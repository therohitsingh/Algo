def LargeSmallSum(a):
    n = len(a)
    eve = []
    odd = []
    for i in range(len(a)):
        if i%2==0:
            eve.append(a[i])
        else:
            odd.append(a[i]) 
    eve = sorted(eve)
    odd = sorted(odd)
    print(eve[-2]+odd[-2])

a = [3,2,1,7,5,4]   
LargeSmallSum(a)   
    
                      



