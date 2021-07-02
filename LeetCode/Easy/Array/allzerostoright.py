a = [0,0,1,2,3,5]
b = []
count=0
for i in range(0,len(a)):
    if(a[i]==0):
        count = count+1
        b.append(a[i])


a.remove(0)
print(a)        
        


     