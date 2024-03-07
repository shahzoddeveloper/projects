def heie(tabellplass_ordbok):
    for key in tabellplass_ordbok:
        if key == "Brann":
            if tabellplass_ordbok[key] <= 3:
                return f"Brann"
        elif tabellplass_ordbok[key] == 1:
            return key
 
lag = heie({"Rosenborg":4, "Odd":1, "Molde":3, "Brann":2})
print(lag)
lag = heie({"Rosenborg":2, "Odd":1, "Molde":3, "Brann":4})
print(lag)