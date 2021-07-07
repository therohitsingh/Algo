s = input("Enter the string:-")


print("before removing duplicate",s)
print("after removing duplicate",set(s))


t = ""
for i in s:

    if(i in t):
        pass
    else:
        t = t+i

    print(t)     