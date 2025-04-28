List = []

for _ in range(5):
    zahl = int(input("Was ist Zahl? : "))
    List.append(zahl)

gesamt = 0
for x in List:
    gesamt += x

print(gesamt)