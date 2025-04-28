my_list = [1 ,12, 7, 3, 5]
new_list = []
for x in my_list:
    if x > my_list[((my_list.index(x))-1)]:
        new_list.append(x)

print(new_list)