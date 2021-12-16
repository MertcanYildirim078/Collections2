import random
import string

# Maak een programma die een wachtwoord van 24 tekens genereerd.

# Het wachtwoord moet aan de volgende eisen voldoen:

# 2 tot 6 hoofdletters.
# Minimaal 8 kleine letters.
# 3 speciale tekens uit de volgende reeks: @ # $ % & _ ?.
# De speciale tekens mogen niet op de eerste of laatste positie staan en ook niet op een vaste plek.
# 4 tot 7 cijfers (0 t/m 9).
# Op de eerste 3 posities mag geen cijfer staan.
print('Welkom bij de password generator!')
specialetekens = ['@', '#', '$', '%', '&', '_', '?']
kleineletters = string.ascii_lowercase
hoofdletters = string.ascii_uppercase
nummers = [0,1,2,3,4,5,6,7,8,9]
while True:
    randomhoofdletter = random.randint(2,6)
    randomkleinletter = random.randint(8,14)
    randomnummer = random.randint(4,7)
    hoofdletterlist =[]
    kleinletterlist = []
    nummerlist = []
    speciallist = []

    totaalletters = randomhoofdletter + randomkleinletter + randomnummer + 3

    for h in range(randomhoofdletter):
        hoofdletter = random.choice(hoofdletters)
        hoofdletterlist.append(hoofdletter)

    for k in range(randomkleinletter):
        kleinletter = random.choice(kleineletters)
        kleinletterlist.append(kleinletter)

    for s in range(3):
        specialeteken = random.choice(specialetekens)
        speciallist.append(specialeteken)

    for n in range(randomnummer):
        nummer = random.choice(nummers)
        nummerlist.append(nummer)

    if totaalletters == 24:
        break

wachtwoord = hoofdletterlist + kleinletterlist + nummerlist + speciallist

random.shuffle(wachtwoord)
while True:
    if wachtwoord[0] in specialetekens or wachtwoord[-1] in specialetekens or wachtwoord[0:3] in nummers:
        print(wachtwoord)
        print('Requirements not met...')
        random.shuffle(wachtwoord)
    else:
        print('The Password:')
        print('--------------------------------------------------------------------------------------------------------')
        print(wachtwoord)
        print('--------------------------------------------------------------------------------------------------------')
        break






