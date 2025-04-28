List = []

for _ in range(5):
    zahl = int(input("Was ist Zahl?: "))
    List.append(zahl)

List2 = []
for x in List:
    if (x%2) == 0:
        List2.append(x)

print(List2)