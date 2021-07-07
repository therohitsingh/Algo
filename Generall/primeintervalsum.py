start = int(input("start"))
end = int(input("end"))
a = [] 
for i in range(start,end):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        a.append(i)
print(sum(a))        
            
        
            
         
    