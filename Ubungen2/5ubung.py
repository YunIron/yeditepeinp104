my_list = [5, 2, -5, 10, 23, -21,78,1,-876]
biggest_int = 0

for x in my_list:
    for b in my_list:
        if x > b:
            biggest_int = x
        else:
            break

print(biggest_int)
