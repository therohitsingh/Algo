a = []
b = []
c = []
n = int(input())
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if(a[i]%10==0):
        b.append(a[i])
    else:
        c.append(a[i])
print(c+b)                