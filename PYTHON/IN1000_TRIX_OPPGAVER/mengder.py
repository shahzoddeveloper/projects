#a
frukt = {"banan", "eple", "banan", "appelsin", "Banan", "banan"}
print(frukt)

#b
navn = set(['Anna', 'Ola', 'Inger'])

if 'anna' in navn:
    print("Anna er i mengde")
else:
    print("Anna er ikke i mengde")

#c
mengde_a = set([1, 2, 3, 2, 3])
mengde_b = {1, 2, 3}

print(mengde_a == mengde_b)


#d
dyr = {'Dromedar', 'Dromedar', 'Sjiraff', 'Kakadue'}

dyr.remove('Dromedar')
dyr.add('Katt')

print(dyr)

#e
bokstav = set("abcdefg")

print(bokstav)
