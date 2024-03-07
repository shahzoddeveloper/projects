passasjerer = 0

nye = int(input("Stasjon 1: Hvor mange passasjerer er det? "))

if passasjerer + nye >= 30:
    print("Bussen er fullt!", passasjerer + nye - 30, "passasjerer må gå fots!")
    passasjerer = 30
else:
    passasjerer = passasjerer + nye
    print(nye, "passasjerer om bord")

nye = int(input("Stasjon 2: Hvor mange passasjerer er det? "))

if passasjerer + nye >= 30:
    print("Bussen er fullt!", passasjerer + nye - 30, "passasjerer må gå fots!")
    passasjerer = 30
else:
    passasjerer = passasjerer + nye
    print(nye, "passasjerer om bord")

nye = int(input("Stasjon 3: Hvor mange passasjerer er det? "))

if passasjerer + nye >= 30:
    print("Bussen er fullt!", passasjerer + nye - 30, "passasjerer må gå fots!")
    passasjerer = 30
else:
    passasjerer = passasjerer + nye
    print(nye, "passasjerer om bord")

print("Bussen er fremme med: ", passasjerer, "passasjerer.")