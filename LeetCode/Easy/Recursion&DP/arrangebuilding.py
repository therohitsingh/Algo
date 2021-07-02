n = 3
ob = 1
os = 1
for i in range(2,n+1):
    nb = os
    ns = ob + os

    ob = nb
    os = ns
total = ob+os
total = total*total
print(total)
        