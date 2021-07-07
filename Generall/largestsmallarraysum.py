length = int(input())
arr = []

for i in range(length):
    r = int(input())
    arr.append(r)
    

even = []
odd = []
for i in range(length):
    if i%2 == 0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
even = sorted(even)
odd = sorted(odd) 
print("This is eve",even[-2])
print("This is odd",odd[-2])
sum = even[-2]+odd[-2]
print(sum)