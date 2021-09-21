n1 = int(input())
a = []
for i in range(n1):
    a.append(input())
n2 = int(input())
b = []
for j in range(n2):
    b.append(input())

h = [str(i) for i in a]
res = int("".join(h))
g = [str(i) for i in b]
res1 = int("".join(g))
c = res1 - res
c = str(c)
for i in c:
    print(i)