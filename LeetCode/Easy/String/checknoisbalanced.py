def balanced(s):
    n = len(s)
    l = 0
    r = 0
    if s==s[::-1]:
        print("balanced")
    else:
        for i in range(0,int(n/2)):
            l = l+int(s[i])    
            r = r+int(s[len(s)-1-i])
        if (l==r):
            print("Balanced")
        else:
            print("Not Balanced")
s = "12328" 
balanced(s)                   


