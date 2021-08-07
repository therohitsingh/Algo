s = input()
n = len(s)
count = 0
for i in range(0,n):
    for j in range(i+1,n):
        if (s[i]==s[j]):
            count+=1
if (count>0):
    print("No")
else:
    print("yes")