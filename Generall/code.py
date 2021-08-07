a = []
N = int(input())
for i in range(N):
    a.append(int(input()))
K = int(input())

for i in range(K):
    a.insert(-1,a[i])
    a.pop()
print(a)
     