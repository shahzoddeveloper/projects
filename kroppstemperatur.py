temp = float(input("Hva er kroppstemperaturen din?: "))
if temp >= 36.5 and temp <= 37.5:
    print("Normal temperatur!")
elif temp <= 36.4:
    print("For lavt temperatur.")
else:
    print("For høyt temperatur.")
