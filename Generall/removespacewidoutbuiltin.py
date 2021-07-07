s = input("")
a = s.split()
for i in a[1:]:
    if i == " ":
        a.pop(i)
    print(''.join(a))    