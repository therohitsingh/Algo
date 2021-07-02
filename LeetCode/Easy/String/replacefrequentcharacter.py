ASCII_SIZE = 256
def freqchar(tom,x):

    count = [0]*ASCII_SIZE
    maxm = -1
    c = ""
    
    for i in tom:
        count[ord(i)]+=1
    for i in tom:
        maxm = max(maxm,count[ord(i)])
        m = i
    print(tom.replace(m,x))    


tom = "bbadbbababb"
x = str(input("char:"))
freqchar(tom,x)