if " "==digit: return []

    kmaps = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    ret = ['']
    for c in digit:
        tmp=[]
        for y in ret:
            for x in kmaps[c]:
                ret.append(x+y)
        ret = tmp
         
    return ret            