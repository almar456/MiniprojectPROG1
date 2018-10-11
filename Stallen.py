def stallen(nummer: str):
    import datetime                                                         # Imports

    bestand = 'fietsen.csv'                                                 # Informatie ophalen en in lijst zetten
    file = open(bestand, 'r').read()
    open(bestand).close()
    lijst = file.split('\n')
    for x in lijst:
        lijst[lijst.index(x)] = x.split(';')

    for x in lijst:                                                         # Check nummer
        if (str(nummer) == x[0]):
            index = lijst.index(x)
            break

    try:                                                                    # Checken of fiets al gestald is, zo niet
        if (lijst[index][4] == 'True'):                                     # dan de waarde 'gestald' naar True.
            print('De fiets is al gestald.')                                # En de tijd toevoegen.
        elif lijst[index][4] == 'False':
            lijst[index][4] = 'True'
            print('De fiets is gestald.')
    except:
        print('Incorrect nummer.')
    lijst[index][5] = datetime.datetime.today().strftime("%a %d %b %Y om %H:%M:%S")

    newFile = ''                                                            # eventuele verandering opslaan in csv
    for x in lijst:
        if x == ['']:
            break
        for y in x:
            if y != x[5]:
                newFile = newFile+y+';'
            else:
                newFile = newFile+y+'\n'
    open(bestand,'w').write(newFile)
    open(bestand).close()

stallen(1234567890)