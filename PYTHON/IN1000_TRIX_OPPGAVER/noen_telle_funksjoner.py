#a
num1 = 99
def noen_telle(num1):
    num1 = num1 *2
    return num1

#b
tekst = input("Skriv et ord: ")
tall = int(input("Skriv et tall: "))
def streng_tall(tekst, tall):
    if len(tekst) > tall:
        return True
    else:
        return False

#c
def antallSifre(heltall):
    return len(str(heltall))
#eller
def antallSifre(heltall):
    teller = 0
    for tegn in str(heltall):
        teller += 1
    return teller
