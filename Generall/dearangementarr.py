n = int(input("Enter the input:-"))
a = []
k = int(input("rotation:-"))
for i in range(0,n):
    a.append(int(input("input:-")))
for j in range(0,k):
    
    a.insert(-1,a[1])
    a.pop()
print(a)

   