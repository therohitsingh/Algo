
def countnsay(prev):
    count = 1 
    say = ""
    for i in range (len(prev)-1):
        curre = prev[i]
        nexte = prev[i+1]
        if curre == nexte:
            count+=1
        else:
            say += str(curre)+str(count)  
            count = 1  
    say+=str(prev[len(prev)-1])+str(count)  
    return say

prev = "wwwwaaadexxxxxx"
print(countnsay(prev))

