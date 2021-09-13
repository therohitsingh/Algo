def zero(a):
    n = len(a)
    sum = 0
    s = set()
    for i in range(n):
        sum +=a[i]

        if sum == 0 and sum in s:
            return 1
        s.add(sum)
    return 0    








a = [-2,2]
print(zero(a))