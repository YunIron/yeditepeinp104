note = ()
for _ in range(3):
    Note = int(input("Was haben Sie als Note bekommen?: "))
    note = note + (Note,)

Durchschnitt = 0
for x in note:
    Durchschnitt += note
Durchschnitt = Durchschnitt/3

print(Durchschnitt)