def bordsetting(introverte, ekstroverte):
    ny_liste = []
    for x in range(len(introverte)):
        ny_liste.append(introverte[x])
        ny_liste.append(ekstroverte[x])
    print(ny_liste)

s = bordsetting(["Per","Palle","Espen"], ["Putti", "Plutti", "Pott"])

