inter = int(input("input:-"))
exter = int(input("input:-"))
interw = []
exterw = []
if inter:
    for i in range(inter):
        interw.append(float(input("inter")))

if exter:
    for j in range(exter):
        exterw.append(float(input("exter:-")))

if inter == 0 and exter == 0:
    exit()

if inter and exter:
    print(sum(inter)*18+sum(exter)*12)