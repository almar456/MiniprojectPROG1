def algemeen():
    file = open('fietsen.csv', 'r')
    aantalbezet = int(len(file.readlines()))
    aantalvrij = 1001 - aantalbezet
    aantalbezet = aantalbezet - 1                                       # Bereken hoeveel plekken er nog vrij zijn
    open('fietsen.csv').close()
    return_waarde = 'Er zijn momenteel: ' + str(aantalvrij) + ' plekken vrij' + '\n Er zijn dus: ' + str(aantalbezet) + ' plekken bezet'
    return return_waarde


def persoonlijk(username):
    bestand = 'fietsen.csv'
    file = open(bestand, 'r').read()
    open(bestand).close()
    lijst = file.split('\n')
    for x in lijst:
        lijst[lijst.index(x)] = x.split(';')                            # voor elk deel wordt de lijst split bij ";"
    for gebruiker in lijst:                                             # hier zoek die naar de de goeie lijst in de lijst
        if username in gebruiker:                                       
            if gebruiker[7] == '-':                                     # Het streepje geeft aan dat die niet in de stalling staat
                return 'Uw fiets staat momenteel niet in de stalling'
            else:
                return_waarde = 'Uw fiets is gestald sinds: ' + gebruiker[7]    # Als de naam overeenkomt wordt te tijd aangegeven vanaf hoelaat de fiets in de stalling staat
                return return_waarde


def naam(username):
    bestand = 'fietsen.csv'
    file = open(bestand, 'r').read()
    open(bestand).close()
    lijst = file.split('\n')
    for x in lijst:
        lijst[lijst.index(x)] = x.split(';')
    for gebruiker in lijst:
        if username in gebruiker:
            return gebruiker[3]                 # Hier wordt de naam van de user geprint


def fietsnummer(username):
    bestand = 'fietsen.csv'
    file = open(bestand, 'r').read()
    open(bestand).close()
    lijst = file.split('\n')
    for x in lijst:
        lijst[lijst.index(x)] = x.split(';')
    for gebruiker in lijst:
        if username in gebruiker:
            return gebruiker[0]                 # Hier wordt het fietsummer van de user geprint

def gemaakt(username):
    bestand = 'fietsen.csv'
    file = open(bestand, 'r').read()
    open(bestand).close()
    lijst = file.split('\n')
    for x in lijst:
        lijst[lijst.index(x)] = x.split(';')
    for gebruiker in lijst:
        if username in gebruiker:
            if gebruiker[4] != '-':
                return_waarde = 'Uw account bestaat sinds: ' + gebruiker[4]
                return return_waarde            # Hier wordt de datum van gemaakt geprint
