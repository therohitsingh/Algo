def string(s):
    a = 0
    n = len(s)
    for i in range(n):
        if(s[i+1]=="A"):
            a = int(s[i-1])&int(s[i+1])
        elif(s[i+1]=="B"):
            a = int(s[i-1])|int(s[i+1])
        elif(s[i+1]=="C"):
            a = int(s[i-1])^int(s[i+1])
        else:
            break    
    return a    
s = "0C1A1B1C1C1B0A0"
print(string(s))