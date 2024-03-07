pris = 50
tekst = input("Skriv inn alder: ")
alder = int(tekst)

if alder < 12 or alder > 67:
    print("Du må betale", pris*0.5, "kr")
else:
    print("Du må betale", pris, "kr")

print("ha en fin dag!")