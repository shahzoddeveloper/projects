ord = input("Skriv inn et ord: ")
ord = ord.upper()
print(ord)
print(len(ord))
forste_tegn = ord[0]
print(forste_tegn)

tall = 0
for x in ord:
    if x == ord[1]:
        tall +=1
print(tall)
