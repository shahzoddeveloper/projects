#ab
land = {"norge":"oslo",
        "nederland":"amsterdam",
        "spania":"madrid"}

sprak = {"norge":"norsk",
        "nederland":"nederlandsk",
        "spania":"spansk"}

innbygger = {"norge":5391369,
            "nederland":17282163,
            "spania":46733038}

spm = input("Skriv inn et land: ").lower()
if spm in land:
    print("Hovedstaden til ",spm.capitalize() ," er: ",land[spm].capitalize(),". Språket til ", spm.capitalize(), "er ", sprak[spm],". Innbyyggerne til ",spm.capitalize(),"er ", innbygger[spm],".")
else:
    print("Landet finnes ikke i ordboken!")

#c
land = {"norge":"oslo",
        "nederland":"amsterdam",
        "spania":"madrid"}

sprak = {"oslo":"norsk",
        "nederland":"nederlandsk",
        "spania":"spansk"}

innbygger = {"norsk":5391369,
            "nederlandsk":17282163,
            "spansk":46733038}

spm = input("Skriv inn et land: ").lower()
if spm in land:
    print("Hovedstaden til ",spm.capitalize() ," er: ",land[spm].capitalize(),". Språket til ", spm.capitalize(), "er ", sprak[land[spm]],". Innbyyggerne til ",spm.capitalize(),"er ", innbygger[sprak[land[spm]]],".")
else:
    print("Landet finnes ikke i ordboken!")

#eksempel
# fakta = {"Norge": {
#             "hovedstad": "Oslo",
#             "spraak": "Norsk",
#             "innbyggere": 5391369},
#         "Nederland": {
#             "hovedstad": "Amsterdam",
#             "spraak": "Nederlandsk",
#             "innbyggere": 17282163},
#         "Spania": {
#             "hovedstad": "Madrid",
#             "spraak": "Spansk",
#             "innbyggere": 46733038},
#         }


# land = input("Gi navnet på et land: ")


# if land in fakta:
#     print("Hovedstaden til", land, "er", fakta[land]["hovedstad"])
#     print("I", land, "snakker folk", fakta[land]["spraak"])
#     print(land, "har", fakta[land]["innbyggere"],  "innbyggere")
# else:
#     print("Jeg kjenner ikke dette landet!")