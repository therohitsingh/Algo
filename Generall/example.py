n = int(input("input:-"))
k = int(input("rotate:-")) 
a = []
for i in range(n):
    r = int(input("input:-"))
    a.append(r) 


for i in range(k):
    a.append(a[-1])
    a.pop()
print(a)   

  
