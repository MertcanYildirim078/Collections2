import random

roodtabel = ['Rode Tabel:','-2','','','','','','','','','']
blauwetabel = ['Blauwe Tabel:','','','','','','','','','','-2']
wittetabel = ['Witte Tabel:','','','','','']

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
    if Keuzedobbelsteen == 'A' or 'a':
        print(f'Uw keuze was: {a} ')
    elif Keuzedobbelsteen == 'B' or 'b':
        print(f'Uw keuze was: {b}')
    elif Keuzedobbelsteen == 'C' or 'c':
        print(f'Uw keuze was: {c}')
    elif Keuzedobbelsteen == 'D' or 'd':
        print(f'Uw keuze was: {d}')

def KeuzeTabel(blauwedobbelsteen,rooddobbelsteen):
    if blauwedobbelsteen > rooddobbelsteen:
        Keuzetabel = 'Red'
    elif rooddobbelsteen > blauwedobbelsteen:
        Keuzetabel = 'Blue'
    elif blauwedobbelsteen == rooddobbelsteen:
        Keuzetabel = 'Beide'
    return Keuzetabel

def Appendtabel(a,b,c,d,Keuzetabel,roodtabel,blauwetabel,Dobbelsteenvragen):
    if Keuzetabel == 'Red':
        roodtabel.append(Dobbelsteenvragen)



def doubletrobbel():
    rooddobbelsteen,blauwedobbelsteen,wittedobbelsteen,dobbellist = dobbelsteenrollen()
    a,b,c,d = dobbelsteenberekening(blauwedobbelsteen,rooddobbelsteen,wittedobbelsteen,dobbellist)
    printdobbel = printdobbelstenen(rooddobbelsteen,blauwedobbelsteen,wittedobbelsteen,a,b,c,d)
    Keuzetabel = KeuzeTabel(blauwedobbelsteen,rooddobbelsteen)
    print('De gekozen tabel(en) =', Keuzetabel)
    print(roodtabel)
    print(blauwetabel)
    print('-----------------------------------------------------------------')
    print(wittetabel)
    print('-----------------------------------------------------------------')
    Dobbelsteenvragen = Dobbelsteenkeuzen()
    vervolgkeuzekeus(Dobbelsteenvragen,a,b,c,d)

doubletrobbel()