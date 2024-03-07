#a
liste = [6, -4, 7, -2, 8, -3, 9, -11]

#b
minst = liste[0]
for x in liste:
    if x < minst:
        minst = x
print(minst)

#c
stoerst = liste[0]
for x in liste:
    if x > stoerst:
        stoerst = x
print(stoerst)
