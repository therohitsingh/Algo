def getstair(n):
    if n<=1:
        return n
    return getstair(n-1)+getstair(n-2)
        