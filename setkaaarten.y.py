
import random
Setkaarten = []
nummers= ['Aas',2,3,4,5,6,7,8,9,10,'Boer', 'Vrouw', 'Heer']
typen= ['Klaveren', 'Schoppen', 'Ruiten', 'Harten']
deck = []

for type in typen:
    for nummer in nummers:
        kaarten = {type:nummer}
        deck.append(kaarten)

for j in range(2):
    deck.append('joker')

random.shuffle(deck)
for x in range(6):
    print(deck.pop(0))
 
print("---")
print(deck)

