def spoer_is():
    kule = 30
    spoor = int(input("En kule koster 30NOK. Hvor mange kuler vil du ha? "))
    totalt = spoor * kule
    print("Isen koster: ", totalt,"NOK.")

def spoer_pizza():
    pizza = input("Hva har du lyst på pizzaen (ost/ingenting):")
    pizza_ost = 80
    pizza_ingenting = 100
    if pizza == "ost" or pizza == "Ost":
        print("Du har bestilt en pizza med ost og koster", pizza_ost, "kr.")
    elif pizza == "ingenting" or pizza == "Ingenting":
        print("Du har bestilt en pizza og koster", pizza_ingenting, "kr.")
    else:
        print("Finnes ikke på menyen!")

def spoer_spise():
    valg = input("Hva har dere lyst å spise? (pizza/is): ")
    if valg == "is" or valg == "Is":
        spoer_is()
    elif valg == "pizza" or valg == "Pizza":
        spoer_pizza()
    else:
        print("Vi selger ikke dette.")

spoer_spise()
