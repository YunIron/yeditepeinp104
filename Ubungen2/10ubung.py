my_list = []

for _ in range(5):
    Gegenstand = int(input("Was ist das Gegenstand?: "))
    my_list.append(Gegenstand)

new_list = []

for i in my_list:
    if i < 0:
        new_list.append(i)

print(new_list)