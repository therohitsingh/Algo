def movehyphen(str):
    hyphen=""
    word = ""
    for i in str:
        if i == "-":
            hyphen+=i
        else:
            word+=i
    print(hyphen+word)

str = "Move-Hyphens-to-Front"
movehyphen(str)
