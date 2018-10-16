def registreren(wachtwoord: str, username: str, naam: str):
    import csv
    import re
    from random import randint

    # Genereer code d.m.v. randint

    code = randint(0, 10000000000)

    # Gegevens die de gebruiker invoert in een list

    gegevens = [code, wachtwoord, username, naam, False, '-']

    # Valideer het wachtwoord

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
                return print("The code to stall your bike is: " + str(code))
    if valid == -1:
        return print("Password doesn't meet the requirements.")


registreren('abcdef1234', 'AJSijpenhof1337', 'AJ')
