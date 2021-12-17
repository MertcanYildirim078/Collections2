# Schrijf een python programma voor het genereren van Kerstlootjes

# Vraag namen op van deelnemers
# Controleer telkens of een ingevoerde naam wel uniek is
# Als er meer dan 2 namen zijn opgegeven kunnen er lootjes worden getrokken
# Maak lootjes voor alle namen
# Trek voor alle namen willekeurig (random) een lootje
# Iedereen heeft dus één uniek lootje
# Niemand mag het lootje van zichzelf hebben getrokken
# Print een lijst met namen en bijbehorende lootjes

import random

Lijstdeelnemers = []
Lijstlootjes = []
while True:
    hoeveelheiddeelnemers = int(input('Hoeveel deelnemers zijn er? '))
    if hoeveelheiddeelnemers <=2:
        print('Sorry er moet minimaal 2 deelnemers zijn')
    elif hoeveelheiddeelnemers >2:
        break

d = 1
while len(Lijstdeelnemers) != hoeveelheiddeelnemers:
    deelnemers = input(f'Wat is uw naam van de deelnemer {d}? ')
    if deelnemers.lower() in Lijstdeelnemers:
        print('Die naam bestaat al, sorry!')
    else:
        Lijstdeelnemers.append(deelnemers.lower())
        d += 1
aantal = len(Lijstdeelnemers)
aantal = aantal - 1

Lijstlootjes += Lijstdeelnemers
random.shuffle(Lijstdeelnemers)

while aantal > 0:
    if Lijstlootjes[aantal] == Lijstdeelnemers[aantal]:
        random.shuffle(Lijstdeelnemers)
        aantal = len(Lijstdeelnemers)
        aantal = aantal -1
    else:
        aantal = aantal - 1

print('De deelnemers: ')
print(Lijstdeelnemers) 
print('De lootjes op volgorde van de namen: ')
print(Lijstlootjes)
