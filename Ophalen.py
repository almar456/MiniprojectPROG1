def ophalen(username: str, wachtwoord: str):
    bestand = 'fietsen.csv'                                                     # Informatie ophalen en in lijst zetten
    file = open(bestand, 'r').read()
    open(bestand).close()
    lijst = file.split('\n')
    for x in lijst:
        lijst[lijst.index(x)] = x.split(';')

    for x in lijst:                                                             # Login gegevens checken
        if x == ['']:
            break
        if (x[1] == wachtwoord) and (x[2] == username):
            index = lijst.index(x)

    try:
        if lijst[index][4] == 'True':                                           # Kijken of de fiets al gestald is, zo ja
            lijst[index][4] = 'False'                                           # dan de waarde van 'gestald' naar False
            lijst[index][-1] = '-'
        elif lijst[index][4] == 'False':
            return 2
    except:
        return 1

    newFile = ''                                                                # eventuele verandering opslaan in csv
    for x in lijst:
        if x == ['']:
            break
        for y in x:
            if y != x[-1]:
                newFile = newFile + y + ';'
            else:
                newFile = newFile + y + '\n'
    open(bestand, 'w').write(newFile)
    open(bestand).close()
    return 0

ophalen('almar456', 'lmao420')