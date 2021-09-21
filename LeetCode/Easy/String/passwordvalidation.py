import string 

def pun(a):
    j=[]
    for i in a:
        if i in string.punctuation:
            j.append(i)
    return(len(j))

def SimplePassword(str): 
    b='password'
    c=[i.isupper() for i in str]  # Capital letter
    n=c.count(True)
    d=[i.isdigit() for i in str] # Number
    m=d.count(True)
    p=pun(str)
    j=str.find(b)
    l=len(str)
    if ((n>=1)&(m>=1)&(p==1)&(j==-1)&(7<l<31)):
        a='true'
    else:
        a='false'
    # code goes here 
    return a
    
# keep this function call here  
print(SimplePassword(input()))