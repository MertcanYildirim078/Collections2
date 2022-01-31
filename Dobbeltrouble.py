import random
listscore = []
roodtabel = [-2,0,0,0,0,0,0,0,0,0]
blauwetabel = [0,0,0,0,0,0,0,0,0,-2]
wittetabel = [0,0,0,0,0]

def waarschuwing():
    print('Waarschuwing! Tweeddezelfde getallen in een tabel proberen en de -2 overscheiden zal de spel beindigen!')

ronde = 1

def rondetelling(ronde):
    print('ronde:', ronde)
    ronde += 1
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
    return Keuzetabel

def printtabel(roodtabel,blauwetabel,wittetabel):
    print('Roodtabel: '), print(roodtabel)
    print('Blauwetabel: '), print(blauwetabel)
    print('-----------------------------------------------------------------')
    print('Wittetabel: '), print(wittetabel)
    print('-----------------------------------------------------------------')  
    return roodtabel,blauwetabel,wittetabel

#'list'.count() telt of er zelfde variant bevat. goed voor controle duplicates 

def positievragen(Keuzetabel):
    positie = int(input('Welke positie moet de nummer? '))
    if Keuzetabel == 'Blue':
        positie -= 1
    return positie

def controlepositie(positie,Keuzetabel):
    if Keuzetabel == 'Red':
        while positie <= 0 or positie >= 10:
                print('Sorry die positie gaat uit de bepaalde grens...')
                positie = int(input('Welke positie moet de nummer? '))
                if Keuzetabel == 'Blue':
                    positie -= 1
    elif Keuzetabel == 'Blue':
        while positie <0 or positie >= 9:
                print('Sorry die positie gaat uit de bepaalde grens...')
                positie = int(input('Welke positie moet de nummer? '))
                if Keuzetabel == 'Blue':
                    positie -= 1
    return positie

def controleerdubbelcijfers(Keuzetabel,Keuzedobbelsteen,roodtabel,blauwetabel,a,b,c,d):
    Dubbelcijfers = ''
    if Keuzetabel == 'Red':
        if Keuzedobbelsteen in ['a','A']:
            if a in roodtabel:
                Dubbelcijfers = 'Dubbel'
        elif Keuzedobbelsteen in ['b','B']:
            if b in roodtabel:
                Dubbelcijfers = 'Dubbel'
        elif Keuzedobbelsteen in ['c','C']:
            if c in roodtabel:
                Dubbelcijfers = 'Dubbel'
        elif Keuzedobbelsteen in ['d','D']:
            if d in roodtabel:
                Dubbelcijfers = 'Dubbel'
    elif Keuzetabel == 'Blue':
        if Keuzedobbelsteen in ['a','A']:
            if a in blauwetabel:
                Dubbelcijfers = 'Dubbel'
        elif Keuzedobbelsteen in ['b','B']:
            if b in blauwetabel:
                Dubbelcijfers = 'Dubbel'
        elif Keuzedobbelsteen in ['c','C']:
            if c in blauwetabel:
                Dubbelcijfers = 'Dubbel'
        elif Keuzedobbelsteen in ['d','D']:
            if d in blauwetabel:
                Dubbelcijfers = 'Dubbel'
    else:
        Dubbelcijfers = 'Goed'
    return Dubbelcijfers


def Appendtabel(a,b,c,d,Keuzetabel,roodtabel,blauwetabel,Keuzedobbelsteen,positie):
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
    return roodtabel,blauwetabel,positie

positiewittetabel = 0
def appendwittetabel(wittedobbelsteen,wittetabel,Keuzedobbelsteen,positiewittetabel):
    if Keuzedobbelsteen == 'c' or Keuzedobbelsteen == 'C':
        wittetabel[positiewittetabel] = wittedobbelsteen
        positiewittetabel += 1
        return positiewittetabel
    elif Keuzedobbelsteen == 'd' or Keuzedobbelsteen == 'D':
        wittetabel[positiewittetabel] = wittedobbelsteen
        positiewittetabel += 1
        return positiewittetabel

def wittetabelcontrole(positiewittetabel):
    if positiewittetabel == 5:
        Wittetabelcontrole = 'vol'
    else:
        Wittetabelcontrole = ''
    return Wittetabelcontrole
    
def Eindscoreberekenen1(roodtabel,blauwetabel,wittetabel):
    for i in range(10):
        calculate = roodtabel[i] * blauwetabel[i]
        listscore.append(calculate)
        i += 1
    subtotaal1 = sum(listscore) #sum() = alle cijfers in lijst samen opgeteld
    return subtotaal1

def nullenberekenen():
    roodnullentabel = roodtabel.count(0)
    blauwenullentabel = blauwetabel.count(0)
    totaalnullen = roodnullentabel + blauwenullentabel
    return blauwenullentabel,roodnullentabel,totaalnullen

def wittetabeloptellen():
    wittetabelopgeteld = sum(wittetabel)
    return wittetabelopgeteld

def Eindscoreberekenen2(wittetabelopgeteld,totaalnullen):
    subtotaal2 = totaalnullen * wittetabelopgeteld
    return subtotaal2

def eindscore(subtotaal1,subtotaal2):
    Eindscore = subtotaal1 - subtotaal2
    return Eindscore

def printeindscore(Eindscore):
    print('Uw eindscore:', Eindscore)    

def mintweecontrole():
    if -2 in roodtabel and -2 in blauwetabel:
        Mintwee = 'goed'
    else:
        Mintwee = 'overscheden'
    return Mintwee

def Stopspel():
    while True:
        stop = input('Wilt u de spel beindigen? J/N (Bijvoorbeeld door perongeluk een foute positie te geven)')
        if stop.upper() == 'J' or stop.upper() == 'N':
            break
        else:
             print('Dat is geen geldige optie!')
    return stop
    
def doubletrobbel(roodtabel,blauwetabel,wittetabel):
    waarschuwing()
    ronde = 1
    while True:
        ronde = rondetelling(ronde)
        rooddobbelsteen,blauwedobbelsteen,wittedobbelsteen,dobbellist = dobbelsteenrollen()
        a,b,c,d = dobbelsteenberekening(blauwedobbelsteen,rooddobbelsteen,wittedobbelsteen,dobbellist)
        printdobbel = printdobbelstenen(rooddobbelsteen,blauwedobbelsteen,wittedobbelsteen,a,b,c,d)
        Keuzetabel = KeuzeTabel(blauwedobbelsteen,rooddobbelsteen)
        print('De gekozen tabel(en) =', Keuzetabel)
        Keuzedobbelsteen = Dobbelsteenkeuzen()
        vervolgkeuzekeus(Keuzedobbelsteen,a,b,c,d)
        roodtabel,blauwetabel,wittetabel = printtabel(roodtabel,blauwetabel,wittetabel)
        positie = positievragen(Keuzetabel)
        positie = controlepositie(positie,Keuzetabel)
        Dubbelcijfers = controleerdubbelcijfers(Keuzetabel,Keuzedobbelsteen,roodtabel,blauwetabel,a,b,c,d)
        roodtabel,blauwetabel,positie = Appendtabel(a,b,c,d,Keuzetabel,roodtabel,blauwetabel,Keuzedobbelsteen,positie)
        Mintwee = mintweecontrole()
        Positiewittetabel = appendwittetabel(wittedobbelsteen,wittetabel,Keuzedobbelsteen,positiewittetabel)
        Wittetabelcontrole = wittetabelcontrole(positiewittetabel)
        roodtabel,blauwetabel,wittetabel = printtabel(roodtabel,blauwetabel,wittetabel)
        stop = Stopspel()
        if stop.upper() == 'J':
            print('Game over, eindscore berekenen...')
            subtotaal1 = Eindscoreberekenen1(roodtabel,blauwetabel,wittetabel)
            print('Subtotaal 1:', subtotaal1)
            blauwenullentabel,roodnullentabel,totaalnullen = nullenberekenen()
            wittetabelopgeteld = wittetabeloptellen()
            subtotaal2 = Eindscoreberekenen2(wittetabelopgeteld,totaalnullen)
            print('Subtotaal 2:', subtotaal2)
            Eindscore = eindscore(subtotaal1,subtotaal2)
            roodtabel,blauwetabel,wittetabel = printtabel(roodtabel,blauwetabel,wittetabel)
            printeindscore(Eindscore)
            return False
        elif Wittetabelcontrole == 'vol':
            print('Wittetabel zit vol. Game over, eindscore berekenen...')
            subtotaal1 = Eindscoreberekenen1(roodtabel,blauwetabel,wittetabel)
            print('Subtotaal 1:', subtotaal1)
            blauwenullentabel,roodnullentabel,totaalnullen = nullenberekenen()
            wittetabelopgeteld = wittetabeloptellen()
            subtotaal2 = Eindscoreberekenen2(wittetabelopgeteld,totaalnullen)
            print('Subtotaal 2:', subtotaal2)
            Eindscore = eindscore(subtotaal1,subtotaal2)
            roodtabel,blauwetabel,wittetabel = printtabel(roodtabel,blauwetabel,wittetabel)
            printeindscore(Eindscore)
            return False
        elif Dubbelcijfers == 'Dubbel':
            print('Dezelfde cijfer bestaat al en kan niet meer toegevoegd worden. Game over, eindscore berekenen...')
            subtotaal1 = Eindscoreberekenen1(roodtabel,blauwetabel,wittetabel)
            print('Subtotaal 1:', subtotaal1)
            blauwenullentabel,roodnullentabel,totaalnullen = nullenberekenen()
            wittetabelopgeteld = wittetabeloptellen()
            subtotaal2 = Eindscoreberekenen2(wittetabelopgeteld,totaalnullen)
            print('Subtotaal 2:', subtotaal2)
            Eindscore = eindscore(subtotaal1,subtotaal2)
            roodtabel,blauwetabel,wittetabel = printtabel(roodtabel,blauwetabel,wittetabel)
            printeindscore(Eindscore)
            return False
        elif Mintwee == 'overscheden':
            print('De -2 in de tabellen is overscheden. Game over, eindscore berekenen...')
            subtotaal1 = Eindscoreberekenen1(roodtabel,blauwetabel,wittetabel)
            print('Subtotaal 1:', subtotaal1)
            blauwenullentabel,roodnullentabel,totaalnullen = nullenberekenen()
            wittetabelopgeteld = wittetabeloptellen()
            subtotaal2 = Eindscoreberekenen2(wittetabelopgeteld,totaalnullen)
            print('Subtotaal 2:', subtotaal2)
            Eindscore = eindscore(subtotaal1,subtotaal2)
            roodtabel,blauwetabel,wittetabel = printtabel(roodtabel,blauwetabel,wittetabel)
            printeindscore(Eindscore)
            return False

doubletrobbel(roodtabel,blauwetabel,wittetabel)
