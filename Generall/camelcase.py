s = (input("Enter the input:-"))
temp = s.split(" ")

res = "".join(i.title() for i in temp[0:])
print(str(res))