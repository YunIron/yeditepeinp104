x = input("Geben Sie Bitte irgendetwases Wort ein? : ")
menge = int(input("Welche Zahl wollen Sie? : "))
buchstab = input("Welche Buchstabe wollen Sie nutzen? : ")

print(f"{x[:menge-1]}{buchstab}{x[menge:]}")
