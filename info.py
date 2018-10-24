def algemeen():
    file = open('fietsen.csv', 'r')
    aantalbezet = int(len(file.readlines()))
    aantalvrij = 1001 - aantalbezet
    aantalbezet = aantalbezet - 1
    open('fietsen.csv').close()
    return_waarde = 'Er zijn momenteel: ' + str(aantalvrij) + ' plekken vrij' + '\n Er zijn dus: ' + str(aantalbezet) + ' plekken bezet'
    return return_waarde


def persoonlijk(username):
    bestand = 'fietsen.csv'
    file = open(bestand, 'r').read()
    open(bestand).close()
    lijst = file.split('\n')
    for x in lijst:
        lijst[lijst.index(x)] = x.split(';')
    for gebruiker in lijst:
        if username in gebruiker:
            if gebruiker[7] == '-':
                return 'Uw fiets staat momenteel niet in de stalling'
            else:
                return_waarde = 'Uw fiets is gestald sinds: ' + gebruiker[7]
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
            return gebruiker[3]


def fietsnummer(username):
    bestand = 'fietsen.csv'
    file = open(bestand, 'r').read()
    open(bestand).close()
    lijst = file.split('\n')
    for x in lijst:
        lijst[lijst.index(x)] = x.split(';')
    for gebruiker in lijst:
        if username in gebruiker:
            return gebruiker[0]

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
                return return_waarde