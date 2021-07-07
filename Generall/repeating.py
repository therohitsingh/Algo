n = int(input("Enter the size of the array:-"))
arr = []
rep = []

for i in range(n):
    r = int(input("No."))
    arr.append(r)


for i in range(n):
    k = i+1
    for j in range(k,n):
        if arr[i] == arr[j]:
            rep.append(arr[i])
print(rep)            