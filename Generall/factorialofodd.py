def factor(n):
    if(n%2!=0):
        fact = 1
        while(n > 1): 
            fact *= n 
            n -= 1
        return fact 
        
    else:
        print("Even")
        
        
        
        
#Drivercode

n = int(input("input"))
print(factor(n))
