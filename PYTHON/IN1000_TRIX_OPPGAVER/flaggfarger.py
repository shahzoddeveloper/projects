flaggOrdbok = {"norge" : ["rødt", "hvitt", "blått"], 
            "sverige" : ["blått", "gult"],
            "danmark" : ["rødt", "hvitt"],
            "finland" : ["hvitt", "blått"],
            "japan" : ["rødt", "hvitt"],
            "gabon" : ["grønt", "gult", "blått"],
            "storbritannia" : ["rødt", "blått", "hvitt"],
            "chile" : ["blått", "hvitt", "rødt"]}
# Oppgave 1
print(flaggOrdbok)


# Oppgave 2
flaggOrdbok["usa"] = ["blått", "rødt", "hvitt"]


# Oppgave 3
def flaggFargeProsedyre3():
    land = input("Skriv inn navnet til et land: ")
    land = land.lower() # .lower() gjør om til små bokstaver. 

    if land in flaggOrdbok:
        print(flaggOrdbok[land])
    else:
        print("Landet", land, "er ikke registrert i ordboken.")

# Oppgave 4
def flaggFargeProsedyre4():
    land = input("Skriv inn navnet til et land: ")
    land = land.lower() # .lower() gjør om til små bokstaver. 

    if land in flaggOrdbok:
        farge = input("Skriv inn et farge: ")
        farge = farge.lower() 

        if farge in flaggOrdbok[land]:
            print(farge, "forekommer i flaggen av", land)
        else:
            print(farge, "forekommer ikke i flaggen av", land)
    else:
        print("Landet", land, "er ikke registrert i ordboken.")

flaggFargeProsedyre3()
flaggFargeProsedyre4()