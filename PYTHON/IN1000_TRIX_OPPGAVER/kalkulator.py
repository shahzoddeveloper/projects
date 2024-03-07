def kalkulator():
    tall1 = float(input("Første tall: "))
    operasjon = input("Operasjon: ")
    tall2 = float(input("Andre tall: "))

    if operasjon == "+":
        print(tall1, "+", tall2, "=", tall1 + tall2)
    elif operasjon == "-":
        print(tall1, "-", tall2, "=", tall1 - tall2)
    elif operasjon == "*":
        print(tall1, "*", tall2, "=", tall1 * tall2)
    elif operasjon == "/":
        print(tall1, "/", tall2, "=", tall1 / tall2)
    else: # b
        print("advarsel: operasjon", operasjon, "eksisterer ikke")

kalkulator()
