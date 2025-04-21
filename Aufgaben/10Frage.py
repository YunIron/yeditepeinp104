x = input("Geben Sie Bitte irgendetwases Wort ein? : ")

buchstaben = "aeiıoöüu"

i = 0
for a in x:
    for b in buchstaben:
        if a == b:
            i+=1

print(i)
