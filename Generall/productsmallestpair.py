sum = int(input())
n = int(input("Enter the size of the array:-"))
arr = []
for i in range(0,n):
    r = int(input("Enter the elements:-"))
    arr.append(r)

if n<2:
    print("-1")
    

for i in range(0,n):
    if arr[i]+arr[i+1]<sum:
        print(arr[i]*arr[i+1])
        break
    else:
        print("0")
        

