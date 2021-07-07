n = int(input("n:-"))
a = []
b = []
count0 = 0
count1 = 0
e = 0
d = 1
for i in range(n):
    r = int(input("no.:-"))
    a.append(r)

 for i in range(len(a)):
    if a[i]==0:
        count0+=1 
    elif a[i]==1:
        count1+=1 


while(e<count0):
    b.append(e)
    count0-=1
while(e<count1):
    b.append(d)
    count1-=1    

    
print(b)