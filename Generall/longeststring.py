 s = input("Enter the string:-")
 m = -1
 for i in s:
     if len(i) > m:
         m = len(i)
         res = i

print(res)