#a
maaneder = ["januar","februar","mars", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "desember"]
#b
tall = int(input("Skriv inn et tall fra 1 til 12: "))

#c
if tall > 0 and tall < 13:
    print(tall, "=", maaneder[tall-1])
else:
    print("Skriv inn et riktig tall!")