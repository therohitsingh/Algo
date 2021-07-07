def getPairsCount(arr, n, sum):
 
     
 
  
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                print("Array elements are",arr[i],arr[j])
 
    return 0 
 
 

arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is",
      getPairsCount(arr, n, sum))