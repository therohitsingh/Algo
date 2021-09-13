a = [2, 3, 5, 8]
b = [10, 12, 14, 16, 18, 20]

c = sorted(a+b)
n = len(c)
if n%2!=0:
    l = 0
    h = len(c)-1
    mid = l+h//2
    print(c[mid])
else:
    l = 0
    h = len(c)-1
    mid = l+h//2
    print((c[mid]+c[mid+1])//2)
   
