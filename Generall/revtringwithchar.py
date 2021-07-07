def string(s):
    arr = s.split(".")
    r = ""
    for i in arr[::-1]:
        r+=i
    print("".join(r))    

s = input("input:-")
string(s)