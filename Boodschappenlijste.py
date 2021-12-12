process = True
boodschappenlijst = {}
while process:
    Productvraag = input('Wat voor product wilt u toevoegen aan de boodschappenlijstje? ')
    if Productvraag in boodschappenlijst:
        boodschappenlijst[Productvraag.lower()] += 1
    else:
        boodschappenlijst[Productvraag.lower()] = 1
    Doorgaan = input('Wilt u verder gaan? J/N ')
    if Doorgaan.lower() == 'j':
        process = True
    elif Doorgaan.lower() == 'n':
        print(boodschappenlijst)
        process = False

