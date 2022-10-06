print('\n\n\nWelkom bij de Random Vragen Quiz 2022')

thislist = [":)", ":("]

def goodscoremessage() :
 print("Gefeliciteerd met je score!")
 print(thislist[0])

def badscoremessage() :
 print("Je score had beter kunnen zijn!")
 print(thislist[1])


antwoord=input('Ben je klaar om de Quiz te spelen? (ja/nee) :')
punten=0
aantal_vragen=10
 
if antwoord.lower()=='ja':

    print('\n\nMooi. Dan gaat de Random Vragen Quiz beginnen!!\nBeantwoord de vragen.\n\n')

    antwoord=input('Vraag 1: Wat is voornaam van de persoon die Python gemaakt heeft? ')
    if antwoord.lower()=='guido' or antwoord.lower()=='guido':
        punten += 1
        print('goed!')
    else:
        print('fout!')
 
    antwoord=input('Vraag 2: Is Python vernoemd naar een slang? ')
    if antwoord.lower()=='nee':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 3: In welk land ligt Rome ? ')
    if antwoord.lower()=='spanje':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 4 : Wat ontstaat wanneer suiker wordt verhit ? ')
    if antwoord.lower()=='karamel':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 5 : Wat is meestal de hoogste en de laagste kaart in een kaartspel ? ')
    if antwoord.lower()=='aas':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 6 : Naar welke Romeinse god is zaterdag vernoemd ? ')
    if antwoord.lower()=='saturnus':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 7 : Welke kleur heeft zuurstofarm bloed ? ')
    if antwoord.lower()=='blauw':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 8 : Wat is het tegenovergestelde van analoog ? ')
    if antwoord.lower()=='digitaal':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 9 : Van welke stof in het zwembadwater kun je rode ogen krijgen ? ')
    if antwoord.lower()=='chloor':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 10 : In welk lichaamsdeel zit de meniscus ? ')
    if antwoord.lower()=='knie':
        punten += 1
        print('goed')
    else:
        print('fout')                                       

    print('\n\nBedankt voor het spelen van de Quiz, je hebt '+str(punten)+' van de '+str(aantal_vragen)+' vragen juist beantwoord!')
    cijfer = round(float(10/aantal_vragen*punten), 1)
    print('Je cijfer voor project komt daarmee op een voorlopige '+str(cijfer)+'.')
    if punten >= 6: goodscoremessage()
    else:           badscoremessage()

elif antwoord.lower()=='nee':
    print('De Quiz gaat niet beginnen, want ik begrijp dat je er nog niet klaar voor bent.\nJammer joh!')
else:
    print('Dit antwoord ken ik niet!')
