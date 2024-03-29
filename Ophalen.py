def ophalen(username: str, wachtwoord: str):
    from passlib.hash import pbkdf2_sha256
    bestand = 'fietsen.csv'                                                     # Informatie ophalen en in lijst zetten
    file = open(bestand, 'r').read()
    open(bestand).close()
    lijst = file.split('\n')
    hash = pbkdf2_sha256.hash(wachtwoord)
    for x in lijst:
        lijst[lijst.index(x)] = x.split(';')

    for x in lijst:                                                             # Login gegevens checken
        if x == ['']:
            break
        if (pbkdf2_sha256.verify(wachtwoord, hash) == True) and (x[2] == username):
            index = lijst.index(x)

    try:
        if lijst[index][5] == 'True':                                           # Kijken of de fiets al gestald is, zo ja
            lijst[index][5] = 'False'                                           # dan de waarde van 'gestald' naar False
            lijst[index][-1] = '-'
        elif lijst[index][5] == 'False':
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
