def getSum(n): 
 

    sumOdd = 0
    sumEven = 0
 
  
    while (n != 0) : 
 
        
        if (n % 2 == 0): 
            sumOdd += n % 10
 
         
        else: 
            sumEven += n % 10
 
        
        
 
       
        n //= 10
     
    print( "Sum odd = " , sumOdd ) 
    print("Sum even = " ,sumEven) 
 

if __name__ =="__main__": 
    n = int(input("Enter the input:-"))
    getSum(n) 
 