def checkpassword(str,n):

    if n<4:
        return 0
    else:
        if(str[0].isdigit()):
            return 0
        else:
            for i in str:
                if(i.isupper()):
                    isupper = True
                if(i.islower()):
                    islower = True
                if(i.isdigit()):
                    isdigit = True
                if(i!=" " or "/"):
                    ispace = True
            if (isdigit and islower and isupper and ispace):
                return 1
            else:
                return 0                            

str = "Ac012"
n = len(str)
print(checkpassword(str,n))
