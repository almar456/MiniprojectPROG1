def registreren(wachtwoord: str, username: str, naam: str, user_code: str):
    import csv
    import re
    from datetime import datetime
    from passlib.hash import pbkdf2_sha256
    from random import randint

    # Genereer code d.m.v. randint

    code = randint(1000, 9999)

    registeredDate = datetime.now().strftime("%x %X")


    # Gegevens die de gebruiker invoert in een list

    hash = pbkdf2_sha256.hash(wachtwoord)

    gegevens = [code, hash, username, naam, registeredDate, True, user_code, '-']

    # Valideer het wachtwoord

    global valid

    valid = 0
    readfile = open('fietsen.csv', 'r').read()

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
        elif username in readfile:
            valid = -2
            break
        else:
            valid = 0
            # Schrijven naar de CSV file d.m.v. van import csv
            with open('fietsen.csv', mode='a', newline="") as fietsen_file:
                writer = csv.writer(fietsen_file, delimiter=';')
                writer.writerow(gegevens)
                print("Succesfully registered.")
                print("The code to stall your bike is: " + str(code))
                return 0
    if valid == -1:
        return 1
        print("Password doesn't meet the requirements.")
    if valid == -2:
        return 2
