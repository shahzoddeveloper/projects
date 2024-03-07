#a
ordliste = ["I", "dag", "er", "jeg", "så", "lykkelig", "så", "lykkelig", "så", "lykkelig", "det", "hele", "endte", "dejligt", "jeg", "synger", "og", "er", "glad", "Ja", "alting", "endte", "lykkeligt", "så", "lykkeligt", "så", "lykkeligt", "i", "dag", "er", "jeg", "så", "lykkelig", "som", "dagen", "den", "er", "lang"]
print(len(ordliste))

#b
print(set(ordliste))

# antall = 0
# for x in range(len(ordliste)):
#     antall +=1
# print(antall)

# nyliste = []
# for x in ordliste:
#     if x not in nyliste:
#         nyliste.append(x)
# print(nyliste)

# gjentatt = 0
# for x in ordliste:
#     if "lykkelig" and "så" and "dag" in ordliste:
#         gjentatt += 1
# print(gjentatt)

#c
print(ordliste.count("lykkelig"))
print(ordliste.count("så"))
print(ordliste.count("dag"))

#d
ordbok ={}
ordbok["lykkelig"]=ordliste.count("lykkelig")
ordbok["så"]=ordliste.count("så")
ordbok["dag"]=ordliste.count("dag")
print(ordbok)


#e
print(list(ordbok))
print(set(ordbok))
