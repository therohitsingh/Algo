def string(str,n):
    count0 = 0
    count1 = 0
    c = 0

    for i in range(n):
        if str[i] =="0":
            count0 += 1
        else: 
            count1 += 1
        if count0 == count1:
            c += 1
    if c == 0:
        return -1
    return c

str = "0100110101"
n = len(str)
print(string(str,n))