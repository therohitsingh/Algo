def anagram(st,sc):
    n = len(st)
    n1 = len(sc)
    count = 0
    if (n!=n1):
        return 0
    else:
        for i in st:
            if i in sc:
                count+=1
        if count == n:
            print("its anagram")
        else:
            print("not anagram")    

st = "geeksforgeeks"
sc = "forgeeksgeeks"
anagram(st,sc)


