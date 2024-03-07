passasjerer = 0


inp = input("Stasjon 1! Hvor mange går på bussen?\n> ")
nye = int(inp)

if passasjerer + nye >= 30:
    print("Bussen er full.", passasjerer + nye - 30, "må gå til fots")
    passasjerer = 30
else:
    passasjerer += nye
    print(nye, "personer gaar ombord i bussen")


inp = input("Stasjon 2! Hvor mange gaar paa bussen?\n> ")
nye = int(inp)

if passasjerer + nye >= 30:
    print("Bussen er full.", passasjerer + nye - 30, "maa gaa til fots")
    passasjerer = 30
else:
    passasjerer += nye
    print(nye, "personer gaar ombord i bussen")


inp = input("Stasjon 3! Hvor mange gaar på bussen?\n> ")
nye = int(inp)

if passasjerer + nye >= 30:
    print("Bussen er full.", passasjerer + nye - 30, "maa gaa til fots")
    passasjerer = 30
else:
    passasjerer += nye
    print(nye, "personer gaar ombord i bussen")


print("Bussen er fremme med", passasjerer, "personer ombord")