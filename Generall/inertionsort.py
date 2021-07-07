def insertionsort(a):
    for i in range(1,len(a)):
        key = a[i] 

        j = i-1  
        while j>=0 and key < a[j]:
            a[j+1]=a[j]
            j = j-1
        a[j+1]=key    
if __name__ == "__main__":
    a = []
    n = int(input("Enter the number of elements in array:-"))
    for i in range(0,n):
        m = int(input("Enter the elements:-"))
        a.append(m)
    insertionsort(a)    
    print("Sorted array is :-")
    for i in range(len(a)):
        print(a[i])  
            