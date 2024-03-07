def lag_interessegrupper(personer_interesse):
    interesse = {}
    mat = []
    film = []
    for x in personer_interesse:
        if personer_interesse[x] == "Mat":
            mat.append(x)
        elif personer_interesse[x] == "Film":
            film.append(x)
    interesse["Mat"] = mat
    interesse["Film"] = film
    print(interesse)
x = lag_interessegrupper({"Per":"Mat", "Palle":"Film", "Espen":"Mat"})

