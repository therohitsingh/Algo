def prime(s,e):
    for i in range(s,e+1):
        if s>1:
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                print(i)


    
s = int(input("Enter the no:-"))
e = int(input("Enter the no:-"))
prime(s,e)