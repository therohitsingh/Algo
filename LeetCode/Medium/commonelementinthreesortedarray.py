a1 = [1, 5, 5]
a2 = [3, 4, 5, 5, 10]
a3 = [5, 5, 10, 20]

n1 = len(a1)
n2 = len(a2)
n3 = len(a3)

mn = min(n1,n2,n3)

for i in range(mn):
    if a1[i] in a2 and a3:
        print(a1[i])

        