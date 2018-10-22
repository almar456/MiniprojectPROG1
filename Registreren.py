def registreren(wachtwoord: str, username: str, naam: str):
    import csv
    import re
    from datetime import datetime
    from passlib.hash import pbkdf2_sha256
    from random import choice

    # Genereer code d.m.v. randint

    list = []

    bestand = 'fietsen.csv'  # Informatie ophalen en in lijst zetten
    file = open(bestand, 'r').read()
    open(bestand).close()
    lijst = file.split('\n')

    for x in lijst:
        lijst[lijst.index(x)] = x.split(';')

    for x in lijst:
        list.append(x[0])

    code = choice([i for i in range(1000, 9999) if i not in list])

    registeredDate = datetime.now().strftime("%x %X")


    # Gegevens die de gebruiker invoert in een list

    hash = pbkdf2_sha256.hash(wachtwoord)

    gegevens = [code, hash, username, naam, registeredDate, False, '-']

    # Valideer het wachtwoord

    usernames = []

    bestand = 'fietsen.csv'  # Informatie ophalen en in lijst zetten
    file = open(bestand, 'r').read()
    open(bestand).close()
    lijst = file.split('\n')

    for x in lijst:
        lijst[lijst.index(x)] = x.split(';')

    lijst.pop()

    for x in lijst:
        usernames.append(x[2])

    try:
        if username in usernames:
            print("Try again! This user already exists.")
            return 2
    except:
        print("Wrong!")

    global valid

    valid = 0

    while True:
        if (len(wachtwoord) < 6):
            valid = -1
            break
        elif not re.search("[a-z]", wachtwoord):
            valid = -1
            break
        elif not re.search("[0-9]", wachtwoord):
            valid = -1
            break
        else:
            valid = 0
            # Schrijven naar de CSV file d.m.v. van import csv
            with open('fietsen.csv', mode='a', newline="") as fietsen_file:
                writer = csv.writer(fietsen_file, delimiter=';')
                writer.writerow(gegevens)
                print("Succesfully registered.")
                print("The code to stall your bike is: " + str(code))

                uniqueCode = code

                return uniqueCode
    if valid == -1:
        print("Password doesn't meet the requirements.")
        return 1


print(
    registreren('1234', 'yayayeee', 'AJ')
)

