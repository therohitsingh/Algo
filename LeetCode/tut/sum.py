n1 = int(input())
a = []
for i in range(n1):
    a.append(input())
n2 = int(input())
b = []
for j in range(n2):
    b.append(input())

a = "".join(a)
b = "".join(b)
c = int(b)-int(a)
c = str(c)
for i in c:
    print(i)