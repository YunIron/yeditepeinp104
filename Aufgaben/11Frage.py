zahl = int(input("Welche Zahl wollen Sie? : "))

binaries=""

while (zahl//2) != 0:
    binaries += str(zahl % 2)
    #print("Binaries ====> "+ str(zahl % 2))
    #print("SSS " + binaries)
    zahl = zahl // 2
    #print("Zahl ====> " + str(zahl))

binaries.join(str(zahl))
binrev = ""
print(binrev.reversed(binaries))
print(str(zahl) + binaries[::-1])



