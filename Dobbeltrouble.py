import random

roodtabel = ['-2','','','','','','','','','']
blauwetabel = ['','','','','','','','','','-2']
wittetabel = ['','','','','']

def rondetelling():
    ronde = 0
    ronde += 1
    print('ronde:', ronde)
    return ronde

def dobbelsteenrollen():
    wittedobbelsteennummers = [1,1,1,2,2,3]
    rooddobbelsteen = random.randint(1,6)
    blauwedobbelsteen = random.randint(1,6)
    wittedobbelsteen = random.choice(wittedobbelsteennummers)
    dobbelstenenlist = [rooddobbelsteen,blauwedobbelsteen,wittedobbelsteen]
    return rooddobbelsteen,blauwedobbelsteen,wittedobbelsteen,dobbelstenenlist

def dobbelsteenberekening(blauwedobbelsteen,rooddobbelsteen,wittedobbelsteen,dobbelstenenlist):
    a = blauwedobbelsteen + rooddobbelsteen + wittedobbelsteen
    b = blauwedobbelsteen + rooddobbelsteen - wittedobbelsteen
    c = blauwedobbelsteen + rooddobbelsteen
    d = max(dobbelstenenlist) - min(dobbelstenenlist)
    return a,b,c,d

def printdobbelstenen(rooddobbelsteen,blauwedobbelsteen,wittedobbelsteen,a,b,c,d):
    print('Rooddobbelsteen = ', rooddobbelsteen)
    print('Blauwdobbelsteen = ', blauwedobbelsteen)
    print('Wittedobbelsteen = ', wittedobbelsteen)
    print('------')
    print('A (Blauw + Rood + wit) = ', a)
    print('------')
    print('B (Blauw + rood - wit) = ', b)
    print('------')
    print('C (Blauw + rood) = ', c)
    print('------')
    print('D (HoogsteDobbelsteen - KleinsteDobbelsteen) = ', d)
    print('------')

def Dobbelsteenkeuzen():
    keuze = True
    Keuzedobbellist = ['A','a','B','b','C','c','D','d']
    while keuze == True:
        Keuzedobbelsteen = input('Welke dobbelsteen wilt u kiezen? (A/B/C/D): ')
        if Keuzedobbelsteen in Keuzedobbellist:
            break
        else:
            print('Sorry dat is geen optie...')
            keuze = True 
    return Keuzedobbelsteen

def vervolgkeuzekeus(Keuzedobbelsteen,a,b,c,d):
    if Keuzedobbelsteen in ['A','a']:
        print(f'Uw keuze was: {a} ')
    elif Keuzedobbelsteen == 'B' or Keuzedobbelsteen == 'b':
        print(f'Uw keuze was: {b}')
    elif Keuzedobbelsteen == 'C' or Keuzedobbelsteen == 'c':
        print(f'Uw keuze was: {c}')
    elif Keuzedobbelsteen == 'D' or Keuzedobbelsteen == 'd':
        print(f'Uw keuze was: {d}')

def KeuzeTabel(blauwedobbelsteen,rooddobbelsteen):
    if blauwedobbelsteen > rooddobbelsteen:
        Keuzetabel = 'Red'
    elif rooddobbelsteen > blauwedobbelsteen:
        Keuzetabel = 'Blue'
    elif blauwedobbelsteen == rooddobbelsteen:
        Keuzetabel = 'Beide'
        Tabelkiezen = input('Welke tabel wilt u kiezen? R/B ')
        if Tabelkiezen.upper() == 'R':
            Keuzetabel = 'Red'
        elif Tabelkiezen.upper() == 'B':
            Keuzetabel = 'Blue'
    return Keuzetabel

def printtabel(roodtabel,blauwetabel,wittetabel):
    print('Roodtabel: '), print(roodtabel)
    print('Blauwetabel: '), print(blauwetabel)
    print('-----------------------------------------------------------------')
    print('Wittetabel: '), print(wittetabel)
    print('-----------------------------------------------------------------')  
    return roodtabel,blauwetabel,wittetabel


def controleerdubbelcijfers(roodtabel,blauwetabel,wittetabel):
    for x in range(roodtabel):
        roodtabel.count(x)          #'list'.count() telt of er zelfde variant bevat. goed voor controle duplicates 



def Appendtabel(a,b,c,d,Keuzetabel,roodtabel,blauwetabel,Keuzedobbelsteen):
    positie = int(input('Welke positie moet de nummer? '))
    if Keuzetabel == 'Red':
        positie += 1
    else:
        positie -= 1
    if Keuzetabel == 'Red':
        if Keuzedobbelsteen == 'a':
            roodtabel[positie] = a
        elif Keuzedobbelsteen == 'b':
            roodtabel[positie] = b
        elif Keuzedobbelsteen == 'c':
            roodtabel[positie] = c
        elif Keuzedobbelsteen == 'd':
            roodtabel[positie] = d
    elif Keuzetabel == 'Blue':
        if Keuzedobbelsteen == 'a':
            blauwetabel[positie] = a
        elif Keuzedobbelsteen == 'b':
            blauwetabel[positie] = b
        elif Keuzedobbelsteen == 'c': 
            blauwetabel[positie] = c
        elif Keuzedobbelsteen == 'd':
            blauwetabel[positie] = d
    return roodtabel,blauwetabel


def appendwittetabel(wittedobbelsteen,wittetabel,Keuzedobbelsteen):
    positiewittetabel = 0
    if Keuzedobbelsteen == 'c' or Keuzedobbelsteen == 'C':
        wittetabel[positiewittetabel] = wittedobbelsteen
    elif Keuzedobbelsteen == 'd' or Keuzedobbelsteen == 'D':
        wittetabel[positiewittetabel] = wittedobbelsteen
    positiewittetabel += 1
    

def wittetabelcontrole(positiewittetabel):
    if positiewittetabel == 4:
        print('Game over, eindscore berekenen.')



def doubletrobbel(roodtabel,blauwetabel,wittetabel):
        ronde = rondetelling()
        rooddobbelsteen,blauwedobbelsteen,wittedobbelsteen,dobbellist = dobbelsteenrollen()
        a,b,c,d = dobbelsteenberekening(blauwedobbelsteen,rooddobbelsteen,wittedobbelsteen,dobbellist)
        printdobbel = printdobbelstenen(rooddobbelsteen,blauwedobbelsteen,wittedobbelsteen,a,b,c,d)
        Keuzetabel = KeuzeTabel(blauwedobbelsteen,rooddobbelsteen)
        print('De gekozen tabel(en) =', Keuzetabel)
        Keuzedobbelsteen = Dobbelsteenkeuzen()
        vervolgkeuzekeus(Keuzedobbelsteen,a,b,c,d)
        roodtabel,blauwetabel,wittetabel = printtabel(roodtabel,blauwetabel,wittetabel)
        roodtabel,blauwetabel = Appendtabel(a,b,c,d,Keuzetabel,roodtabel,blauwetabel,Keuzedobbelsteen)
        roodtabel,blauwetabel,wittetabel = printtabel(roodtabel,blauwetabel,wittetabel)

doubletrobbel(roodtabel,blauwetabel,wittetabel)
