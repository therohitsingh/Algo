def replacechar(tom,x,y):
    for i in tom:
        if i == x:
            tom.replace(y,x)
        if i ==y:
            tom.replace(x,y)
    print(tom)            
    

tom = "apples"     
x = "a"
y = "p"   
replacechar(tom,x,y)    