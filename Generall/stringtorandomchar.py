s = input("Enter the input:-")
v = ("a","e","i","o","u")
count1 = 0
count2 = 0
for i in s:
    for j in range(0,len(v)):
        if(i == v[j]):
            count1 = count1 + 1 
            break
count2 = len(s)-count1        
print(count1)
print(count2)           