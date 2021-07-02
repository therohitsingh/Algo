def backtrack(ans,op,cl,maxp,curr):
    if len(curr)==2*maxp:
        ans.append(curr)
    if (op<maxp):
        backtrack(ans,op+1,cl,maxp,curr+'(')
    if (cl<op):
        backtrack(ans,op,cl+1,maxp,curr+')')
ans = []
op = 0
cl = 0
curr = ' '
backtrack(ans,op,cl,maxp,curr)
print(ans)            