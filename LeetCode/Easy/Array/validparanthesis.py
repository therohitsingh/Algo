def isBalanced(s):
    restart=True
    while restart:
        if '{}' in s:
            s=s.replace('{}','')
        elif '()' in s:
            s=s.replace('()','')
        elif '[]' in s:
            s=s.replace('[]','')
        else:
            restart=False
    return 'true' if len(s)==0 else 'false'

s = input()
print(isBalanced(s))

            
