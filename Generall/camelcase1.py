s = input("input:-")
temp = s.split(" ")

for i in temp[0:]:
  res = "".join(i.title())
  print(str(res))
  