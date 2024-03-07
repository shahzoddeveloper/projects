def gyldig_rgb():
    liste = []
    tall = input("Skriv inn tre separate tall: ")
    tall = tall.strip().split()
    liste.extend(tall)
    print(liste)

    if len(liste) == 3:
        print("Alt er i orden!")
    else:
        print("Du må skrive tre separate tall!")
        return
    
    for x in liste:
        try:
            if 0 <= int(x) <= 255:
                print("Du har skrevet riktig!")
            else:
                print("Tallene du har skrevet inn er utenfor grensene!")
        except ValueError:
            print(f"{x} er ikke et heltall.")

gyldig_rgb()