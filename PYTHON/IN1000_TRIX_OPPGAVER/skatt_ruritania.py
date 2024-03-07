inntekt = float(input("Hva er inntekten din: "))

if inntekt < 10000.0: #mindre enn
    skatt = inntekt * 0.1
    print("Du skal betale:",skatt,"kr.")
else:
    grense = 10000.0
    grense_minst = grense * 0.1
    rest = inntekt - grense
    rest_skatt = rest * 0.3
    summ = rest_skatt + grense_minst
    print("Du skal betale:",summ,"kr skatt.")
