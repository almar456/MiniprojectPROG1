def registreren(wachtwoord: str, username: str, naam: str):
    import csv
    from random import randint

    # Genereer code d.m.v. randint
    code = randint(0, 10000000000)

    # Gegevens die de gebruiker invoert in een list
    gegevens = [code, wachtwoord, username, naam, False, '-']

    # Schrijven naar de CSV file d.m.v. van import csv
    with open('fietsen.csv', mode='a', newline="") as fietsen_file:
        writer = csv.writer(fietsen_file, delimiter=';')
        writer.writerow(gegevens)

registreren('lalala', 'xSketfchy0', 'AJ')