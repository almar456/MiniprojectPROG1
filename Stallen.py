def stallen(login: str, wachtwoord: str):

    bestand = 'fietsen.csv'                                                 # Informatie ophalen en in lijst zetten
    file = open(bestand, 'r').read()
    open(bestand).close()
    lijst = file.split('\n')
    for x in lijst:
        lijst[lijst.index(x)] = x.split(';')

    Correct = False                                                         # Check inloggegevens
    for x in lijst:
        if (login in x) and (wachtwoord in x):
            index = lijst.index(x)
            Correct = True
            break

    try:                                                                    # Checken of fiets al gestald is, zo niet
        if (lijst[index][3] == 'True'):                                     # dan de waarde 'gestald' naar True
            print('De fiets is al gestald.')
        elif lijst[index][3] == 'False':
            lijst[index][3] = 'True'
            print('De fiets is gestald.')
        print(lijst)
    except:
        print('Incorrecte inloggegevens')

    newFile = ''                                                            # eventuele verandering opslaan in csv
    for x in lijst:
        if x == ['']:
            break
        for y in x:
            if y != x[3]:
                newFile = newFile+y+';'
            else:
                newFile = newFile+y+'\n'
    print(newFile)
    open(bestand,'w').write(newFile)