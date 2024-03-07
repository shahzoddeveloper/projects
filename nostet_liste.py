o_liste = []
for x in range(5):
    o_liste.append("o")

stjerneliste = []
for x in range(5):
    stjerneliste.append("*")

rutenett = []
rutenett.append(o_liste)
rutenett.append(stjerneliste)
rutenett.append(o_liste)


print(rutenett[0])
print(rutenett[1])
print(rutenett[2])

for x in rutenett:
    print(x)