def para(curr,main,op,cl,maxp):
    if(len(curr)==2*maxp):
        main.append(curr)
    elif(op<maxp):
        para(curr+"{",main,op+1,cl,maxp)
    elif(cl<op):
        para(curr+"}",main,op,cl+1,maxp)

