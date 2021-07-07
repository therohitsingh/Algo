def digitfreq(n,d):
    n = str(n)
    d = str(d)
    count = 0
    for i in n:
        if i == d:
            count+=1
    return count        



n = 994543234
d = 4
print(digitfreq(n,d))