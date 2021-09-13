def f(p):
    k=0
    if p>1:
        k+=10
        f(p-1)
    return k

p = 3
print(f(p))