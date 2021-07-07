def matoi(string):

    res = 0 

    for i in range(len(string)):
        res = res*10 + (ord(string[i])-ord('0'))
    return res

string = "89789"
print (matoi(string)  )      

