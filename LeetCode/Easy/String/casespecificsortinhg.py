def string(s):
    v1 = []
    v2 = []
    n = len(s)
    for i in range(n):
        if(s[i].islower()):
            v1.append(s[i])
        elif(s[i].isupper()):
            v2.append(s[i])
    v1 = sorted(v1)
    v2 = sorted(v2)
    i = 0
    j = 0
    for k in range(n):
        if(s[k].islower()):
            s[k]=v1[i]
            i+=1
        elif(s[k].isupper()):
            s[k]=v2[j]
            j+=1
    return "".join(s)
                        