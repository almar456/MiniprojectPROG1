from tkinter import *                                   # Tkinter importen om te gebruiken
from Ophalen import *                                   # het ophalen.py bestand importen
from Registreren import *                               # het Registreren.py bestand importen
from Stallen import stallen                             # het Stallen.py bestand importen
from info import *                                      # info.py importen voor de functies
from tkinter.messagebox import showinfo                 # showinfo importeren voor popups
from passlib.hash import pbkdf2_sha256                  # passlib importeren voor de decodering van wachtwoorden
from pushover import *                                  # pushover importen om gebruik te kunnen maken van de app


outfile = open('login_boolean.txt', 'w')                # login_boolean.txt maken en false erin schrijven
outfile.write('False')


def toon_start_frame():                                 # Functie om start_frame te laten zien
    start_frame.forget()
    fiets_stallen_frame.pack_forget()
    fiets_ophalen_frame.pack_forget()
    inloggen_frame.forget()
    geregistreerd_stallen_frame.forget()
    niet_geregistreerd_stallen_frame.forget()
    info_persoonlijk_frame.forget()
    info_algemeen_frame.forget()
    info_frame.pack_forget()
    button_info.grid(row=1, column=1, padx=20, pady=20)
    button_fiets_stallen.grid(row=2, column=1, padx=20, pady=20)
    button_fiets_ophalen.grid(row=3, column=1, padx=20, pady=20)
    start_frame.pack(fill="both",
                     expand=True)
    for x in range(0, 2):
        readfile = open('login_boolean.txt', 'r')
        lines = readfile.readlines()
        if 'True\n' in lines:                           # checken of er ingelogd is
            button_login_start.destroy()
        else:
            button_login_start.grid(row=4, column=1, padx=20, pady=20)


def toon_info_frame():                                  # Functie om info_frame te laten zien
    fiets_stallen_frame.pack_forget()
    fiets_ophalen_frame.pack_forget()
    inloggen_frame.forget()
    start_frame.forget()
    geregistreerd_stallen_frame.forget()
    niet_geregistreerd_stallen_frame.forget()
    info_persoonlijk_frame.forget()
    info_algemeen_frame.forget()
    info_frame.pack_forget()

    info_frame.pack(fill="both",
                    expand=True)
    button_info_algemeen.grid(row=1,
                              column=1,
                              padx=20,
                              pady=20)
    button_info_persoonlijk.grid(row=2,
                                 column=1,
                                 padx=20,
                                 pady=20)
    info_frame.grid_rowconfigure(0, weight=1)
    info_frame.grid_rowconfigure(3, weight=1)
    info_frame.grid_columnconfigure(0, weight=1)
    info_frame.grid_columnconfigure(2, weight=1)


def toon_fiets_stallen():                               # Functie om fiets_stallen_frame te laten zien
    fiets_stallen_frame.pack_forget()
    fiets_ophalen_frame.pack_forget()
    inloggen_frame.forget()
    start_frame.forget()
    geregistreerd_stallen_frame.forget()
    niet_geregistreerd_stallen_frame.forget()
    info_persoonlijk_frame.forget()
    info_algemeen_frame.forget()
    info_frame.pack_forget()
    readfile = open('login_boolean.txt', 'r')
    lines = readfile.readlines()
    fiets_stallen_frame.grid_rowconfigure(0, weight=1)
    fiets_stallen_frame.grid_rowconfigure(3, weight=1)
    fiets_stallen_frame.grid_columnconfigure(0, weight=1)
    fiets_stallen_frame.grid_columnconfigure(2, weight=1)
    fiets_stallen_frame.pack(fill="both", expand=True)
    if 'True\n' in lines:                               # checken of er ingelogd is
        button_geregistreerd_stallen.grid(row=1,
                                          column=1,
                                          padx=20,
                                          pady=20)
        button_niet_geregistreerd_stallen.forget()
    else:
        button_geregistreerd_stallen.grid(row=1,
                                          column=1,
                                          padx=20,
                                          pady=20)
        button_niet_geregistreerd_stallen.grid(row=2,
                                               column=1,
                                               padx=20,
                                               pady=20)


def toon_fiets_ophalen():                               # Functie om fiets_ophalen_frame te laten zien
    start_frame.pack_forget()
    fiets_stallen_frame.pack_forget()
    fiets_ophalen_frame.pack_forget()
    inloggen_frame.forget()
    start_frame.forget()
    geregistreerd_stallen_frame.forget()
    niet_geregistreerd_stallen_frame.forget()
    info_persoonlijk_frame.forget()
    info_algemeen_frame.forget()
    info_frame.pack_forget()
    fiets_ophalen_frame.pack(fill="both",
                             expand=True)
    readfile = open('login_boolean.txt', 'r')
    lines = readfile.readlines()
    fiets_ophalen_frame.grid_rowconfigure(0, weight=1)
    fiets_ophalen_frame.grid_rowconfigure(2, weight=1)
    fiets_ophalen_frame.grid_columnconfigure(0, weight=1)
    fiets_ophalen_frame.grid_columnconfigure(2, weight=1)
    if 'True\n' in lines:                                      # checken of er ingelogd is
        button__login_fiets_ophalen.destroy()
        button_registreer_login.pack_forget()
        button_fiets_ophalen_confirm.grid(row=1, column=1, pady=20, padx=20)
    else:
        button__login_fiets_ophalen.grid(row=1, column=1, padx=20, pady=20)
# sub frames


def toon_geregistreerd_stallen():                           # de frame van geregistreerd stallen laten zien
    fiets_stallen_frame.forget()
    geregistreerd_stallen_frame.pack(fill="both",
                                     expand=True)
    Label(master=geregistreerd_stallen_frame, text="Fietsnummer:  ", bg="#f7d417").grid(row=1, column=1)
    nummer.grid(row=1, column=2, padx=20, pady=20)
    button_stallen.grid(row=2, column=1, columnspan=2, padx=20, pady=20)
    geregistreerd_stallen_frame.grid_rowconfigure(0, weight=1)
    geregistreerd_stallen_frame.grid_rowconfigure(3, weight=1)
    geregistreerd_stallen_frame.grid_columnconfigure(0, weight=1)
    geregistreerd_stallen_frame.grid_columnconfigure(3, weight=1)


def toon_niet_geregistreerd_stallen():                          # frame van niet geregistreerd stallen laten zien
    fiets_stallen_frame.forget()
    niet_geregistreerd_stallen_frame.pack(fill="both",
                                          expand=True)
    readfile = open('login_boolean.txt', 'r')
    lines = readfile.readlines()
    if 'True\n' in lines:                                       # checken of er ingelogd is
        button_login_info.forget()
    else:                                                       # alle registratie velden laten zien
        inloggen_frame.forget()
        button_confirm_login.forget()
        gebruikersnaam_entry.forget()
        wachtwoord_entry.forget()
        button_registreer_login.forget()
        Label(master=niet_geregistreerd_stallen_frame,
              text="Naam:  ",
              bg="#f7d417").grid(row=1, column=1, padx=10, pady=20, sticky=E)
        naam_reg_entry.grid(row=1, column=2, padx=10, pady=20)
        Label(master=niet_geregistreerd_stallen_frame,
              text="Gebruikersnaam:  ",
              bg="#f7d417").grid(row=2, column=1, padx=10, pady=20, sticky=E)
        gebruikersnaam_reg_entry.grid(row=2, column=2, padx=10, pady=20)
        Label(master=niet_geregistreerd_stallen_frame,
              text="Wachtwoord:  ",
              bg="#f7d417").grid(row=3, column=1, padx=10, pady=20, sticky=E)
        wachtwoord_reg_entry.grid(row=3, column=2, padx=10, pady=20)
        Label(master=niet_geregistreerd_stallen_frame,
              text="Pushover key:  ",
              bg="#f7d417").grid(row=4, column=1, padx=10, pady=20, sticky=E)
        user_key_entry.grid(row=4, column=2, padx=10, pady=20)
        button_registreer.grid(row=5, columnspan=2, column=1, padx=20, pady=20)
        niet_geregistreerd_stallen_frame.grid_rowconfigure(0, weight=1)
        niet_geregistreerd_stallen_frame.grid_rowconfigure(6, weight=1)
        niet_geregistreerd_stallen_frame.grid_columnconfigure(0, weight=1)
        niet_geregistreerd_stallen_frame.grid_columnconfigure(3, weight=1)


def toon_info_algemeen():                                       # frame algemene informatie laten zien
    info_frame.forget()
    info_algemeen_frame.pack(fill="both", expand=True)
    aantal_vrij_label = Label(master=info_algemeen_frame, text=algemeen(), bg="#f7d417")
    aantal_vrij_label.grid(row=1, column=1, padx=20, pady=20)
    tekst = "Om een account te registreren zult u een pushover code opgeven\n Deze code verkrijgt u door de Pushover applicatie te downloaden en een account te registreren"
    pushover_label = Label(master=info_algemeen_frame, text=tekst, bg="#f7d417")
    pushover_label.grid(row=2, column=1, padx=20, pady=20)
    info_algemeen_frame.grid_rowconfigure(0, weight=1)
    info_algemeen_frame.grid_rowconfigure(3, weight=1)
    info_algemeen_frame.grid_columnconfigure(0, weight=1)
    info_algemeen_frame.grid_columnconfigure(2, weight=1)


def toon_info_persoonlijk():                                    # frame persoonlijke informatie laten zien
    info_frame.forget()
    info_persoonlijk_frame.pack(fill="both",
                                expand=True)
    readfile = open('login_boolean.txt', 'r')
    lines = readfile.readlines()
    readfile.close()
    if 'True\n' in lines:                                       # checken of er ingelogd is
        button_login_info.destroy()
        readfile = open('login_boolean.txt', 'r')
        lines = readfile.readlines()
        list2 = [x.replace('\n', '') for x in lines]
        info_label = Label(master=info_persoonlijk_frame,
                           text=persoonlijk(list2[1]),
                           bg="#f7d417").forget()
        info_label = Label(master=info_persoonlijk_frame,
                           text=persoonlijk(list2[1]),
                           bg="#f7d417")
        naam_label = Label(master=info_persoonlijk_frame,
                           text='Dit account staat op de naam: ' + naam(list2[1]),
                           bg="#f7d417")
        fiets_nummer_label = Label(master=info_persoonlijk_frame,
                                   text='Uw fietsnummer is: ' + fietsnummer(list2[1]),
                                   bg="#f7d417")
        account_aangemaakt_label = Label(master=info_persoonlijk_frame,
                                         text=gemaakt(list2[1]), bg="#f7d417")
        info_label.forget()
        naam_label.forget()
        fiets_nummer_label.forget()
        account_aangemaakt_label.forget()
        info_label.grid(row=1, column=1, padx=20, pady=20)
        naam_label.grid(row=2, column=1, padx=20, pady=20)
        fiets_nummer_label.grid(row=3, column=1, padx=20, pady=20)
        account_aangemaakt_label.grid(row=4, column=1, padx=20, pady=20)
        info_persoonlijk_frame.grid_rowconfigure(0, weight=1)
        info_persoonlijk_frame.grid_rowconfigure(5, weight=1)
        info_persoonlijk_frame.grid_columnconfigure(0, weight=1)
        info_persoonlijk_frame.grid_columnconfigure(2, weight=1)
    else:

        info_persoonlijk_frame.grid_rowconfigure(0, weight=1)
        info_persoonlijk_frame.grid_rowconfigure(2, weight=1)
        info_persoonlijk_frame.grid_columnconfigure(0, weight=1)
        info_persoonlijk_frame.grid_columnconfigure(2, weight=1)
        button_login_info.grid(row=1, column=1, padx=20, pady=20)


def login():                                                   # de functie om het inlog scherm te laten zien
    info_persoonlijk_frame.forget()
    niet_geregistreerd_stallen_frame.forget()
    geregistreerd_stallen_frame.forget()
    fiets_ophalen_frame.forget()
    start_frame.forget()
    button_fiets_ophalen.forget()
    button_fiets_stallen.forget()
    button_info.forget()
    button_login_start.forget()
    inloggen_frame.pack(fill="both", expand=True)
    Label(master=inloggen_frame, text="Gebruikersnaam:  ", bg="#f7d417").grid(row=1, column=1, pady=20, sticky=E)
    gebruikersnaam_entry.grid(row=1, column=2, pady=20)
    Label(master=inloggen_frame, text="Wachtwoord:  ", bg="#f7d417").grid(row=2, column=1, pady=20, sticky=E)
    wachtwoord_entry.grid(row=2, column=2, pady=20)
    button_confirm_login.grid(row=3, column=2, padx=20, pady=20)
    button_registreer_login.grid(row=3, column=1, padx=20, pady=20)
    inloggen_frame.grid_rowconfigure(0, weight=1)
    inloggen_frame.grid_rowconfigure(4, weight=1)
    inloggen_frame.grid_columnconfigure(0, weight=1)
    inloggen_frame.grid_columnconfigure(3, weight=1)


def f_login():                            # de functie om het ingevoerde wachtwoord en gbrnaam te checken
        username = gebruikersnaam_entry.get()
        wachtwoord = wachtwoord_entry.get()
        hash = pbkdf2_sha256.hash(wachtwoord)
        readfile = open('fietsen.csv', 'r').readlines()
        for lines in readfile:
            lijst = lines.split(';')
            if username == lijst[2] and (pbkdf2_sha256.verify(wachtwoord, hash) == True):
                outfile = open('login_boolean.txt', 'w')
                outfile.write('True\n'+username+'\n'+wachtwoord)
                showinfo(title='popup', message='U bent ingelogd')
                outfile.close()
                button_login_start.forget()
                start_frame.forget()
                toon_start_frame()
                break
        else:
            showinfo(title='popup', message='Uw ingevooerde combinatie is verkeerd!')


def if_loop():                                                          # alle return waardes van stallen() afgaan
    if stallen(nummer.get()) == 0:
        showinfo(title='popup', message='Uw fiets is gestald')
        toon_start_frame()
    elif stallen(nummer.get()) == 1:
        showinfo(title='popup', message='Het ingevoerde nummer is incorrect')
    elif stallen(nummer.get()) == 3:
        showinfo(title='popup', message='De fietsen stalling staat vol, sorry')
    else:
        showinfo(title='popup', message='Uw fiets is al gestald')
        toon_start_frame()


def registreer():                                           # alle return waardes van registeren() afgaan
    if registreren(wachtwoord_reg_entry.get(), gebruikersnaam_reg_entry.get(), naam_reg_entry.get(), user_key_entry.get()) == 0:
        readfile = open('fietsen.csv', 'r').readlines()
        for lines in readfile:
            lijst = lines.split(';')
            if gebruikersnaam_reg_entry.get() == lijst[2]:
                message = 'Uw acount is geregistreerd en uw fiets is gestald, de code voor uw fiets is:' + lijst[0] + '\n onthoud deze code goed!'
                showinfo(title='popup', message=message)
                toon_start_frame()
    elif registreren(wachtwoord_reg_entry.get(), gebruikersnaam_reg_entry.get(), naam_reg_entry.get(), user_key_entry.get()) == 1:
        showinfo(title='popup', message='Uw wachtwoord voldoet niet aan de eisen!')
    elif registreren(wachtwoord_reg_entry.get(), gebruikersnaam_reg_entry.get(), naam_reg_entry.get(), user_key_entry.get()) == 2:
        showinfo(message='Sorry, deze gebruikersnaam is al bezet')


def info_ophalen():                                             # alle return waardes van ophalen() afgaan
    readfile = open('login_boolean.txt', 'r')
    lines = readfile.readlines()
    list2 = [x.replace('\n', '') for x in lines]
    if ophalen(list2[1], list2[2]) == 0:
        username = list2[1]
        pushover_send(username)
        showinfo(title='popup', message='U kunt uw fiets nu pakken')
        toon_start_frame()
    elif ophalen(list2[1], list2[2]) == 2:
        showinfo(title='popup', message='Uw fiets is momenteel niet gestald')
        toon_start_frame()
    elif ophalen(list2[1], list2[2]) == 1:
        print('verkeerd wachtwoord')


root = Tk()

menu = Menu(root)                       # menu maken
menu.add_command(label='Home', command=toon_start_frame)
menu.add_command(label='Informatie', command=toon_info_frame)
menu.add_command(label='Fiets stallen', command=toon_fiets_stallen)
menu.add_command(label='Fiets ophalen', command=toon_fiets_ophalen)

root.config(menu=menu)

start_frame = Frame(master=root,
                    background='#f7d417')                        # start_frame maken en packen
start_frame.pack(fill="both",
                 expand=True)

info_frame = Frame(master=root,
                   background='#f7d417')                         # info_frame maken en packen

fiets_stallen_frame = Frame(master=root,
                            background='#f7d417')                # fiets_stallen_frame maken en packen

fiets_ophalen_frame = Frame(master=root,
                            background='#f7d417')                # fiets_ophalen_frame maken en packen

# sub frames

geregistreerd_stallen_frame = Frame(master=root,
                                    background='#f7d417')     # geregistreerd_stallen_frame maken en packen

niet_geregistreerd_stallen_frame = Frame(master=root,
                                         background='#f7d417')

info_algemeen_frame = Frame(master=root,                       # algemeen frame maken
                            background='#f7d417')

info_persoonlijk_frame = Frame(master=root,                     # info persoonlijk frame maken
                               background='#f7d417')

inloggen_frame = Frame(master=root,                             # inloggen frame maken
                       background="#f7d417")

registreren_frame = Frame(master=root,                          # registreren frame maken
                          background='#f7d417')

# buttons
start_frame.grid_rowconfigure(0, weight=1)
start_frame.grid_rowconfigure(5, weight=1)
start_frame.grid_columnconfigure(0, weight=1)
start_frame.grid_columnconfigure(2, weight=1)


button_info = Button(master=start_frame,                # Button_info defineren
                     text="Informatie",
                     command=toon_info_frame,
                     background="#00387b",
                     fg="white")
button_info.grid(row=1, column=1, padx=20, pady=20)

button_fiets_stallen = Button(master=start_frame,       # Button stallen defineren
                              text="Fiets stallen",
                              command=toon_fiets_stallen,
                              background="#00387b",
                              fg="white")
button_fiets_stallen.grid(row=1, column=1, padx=20, pady=20)

button_fiets_ophalen = Button(master=start_frame,       # Button ophalen defineren
                              text="Fiets ophalen",
                              command=toon_fiets_ophalen,
                              background="#00387b",
                              fg="white")
button_fiets_ophalen.grid(row=1, column=1, padx=20, pady=20)

button_login_start = Button(master=start_frame,         # button login defineren
                            text="Inloggen",
                            command=login,
                            background="#00387b",
                            fg="white")
button_login_start.grid(row=1, column=1, padx=20, pady=20)
# sub buttons maken
button_fiets_ophalen_confirm = Button(master=fiets_ophalen_frame,
                                      text="Weet u zeker dat u uw fiets wilt ophalen?",
                                      command=info_ophalen,
                                      background="#00387b",
                                      fg="white")
button_geregistreerd_stallen = Button(master=fiets_stallen_frame,
                                      text="Klik hier als uw fiets al geregistreerd is",
                                      command=toon_geregistreerd_stallen,
                                      background="#00387b",
                                      fg="white")

button_niet_geregistreerd_stallen = Button(master=fiets_stallen_frame,
                                           text="Klik hier als uw fiets nog niet geregistreerd is",
                                           command=toon_niet_geregistreerd_stallen,
                                           background="#00387b",
                                           fg="white")

button_info_algemeen = Button(master=info_frame,
                              text="Algemene informatie",
                              command=toon_info_algemeen,
                              background="#00387b",
                              fg="white")

button_info_persoonlijk = Button(master=info_frame,
                                 text="Mijn gegevens",
                                 command=toon_info_persoonlijk,
                                 background="#00387b",
                                 fg="white")

button_stallen = Button(master=geregistreerd_stallen_frame,
                        text="Stal uw fiets",
                        command=if_loop,
                        background="#00387b",
                        fg="white")

# verschillende login knopen maken voor de verschillende frames

button_login_info = Button(master=info_persoonlijk_frame,
                           text="Login",
                           background="#00387b",
                           fg="white",
                           command=login)
button_login_fiets_geregistreerd = Button(master=geregistreerd_stallen_frame,
                                          text="Login",
                                          background="#00387b",
                                          fg="white",
                                          command=login)
button_login_fiets_niet_geregistreerd = Button(master=niet_geregistreerd_stallen_frame,
                                               text="Login",
                                               background="#00387b",
                                               fg="white",
                                               command=login)
button__login_fiets_ophalen = Button(master=fiets_ophalen_frame,
                                     text="Login",
                                     background="#00387b",
                                     fg="white",
                                     command=login)

button_confirm_login = Button(master=inloggen_frame,
                              text="Login",
                              background="#00387b",
                              fg="white",
                              command=f_login)

button_registreer = Button(master=niet_geregistreerd_stallen_frame,
                           text="Registreer",
                           background="#00387b",
                           fg="white",
                           command=registreer)

button_registreer_login = Button(master=inloggen_frame,
                                 text="Registreer",
                                 background="#00387b",
                                 fg="white",
                                 command=toon_niet_geregistreerd_stallen)


# login en registreer velden maken
gebruikersnaam_entry = Entry(master=inloggen_frame)
wachtwoord_entry = Entry(master=inloggen_frame)
gebruikersnaam_ophalen_entry = Entry(master=fiets_ophalen_frame)
wachtwoord_ophalen_entry = Entry(master=fiets_ophalen_frame)
gebruikersnaam_reg_entry = Entry(master=niet_geregistreerd_stallen_frame)
wachtwoord_reg_entry = Entry(master=niet_geregistreerd_stallen_frame)
naam_reg_entry = Entry(master=niet_geregistreerd_stallen_frame)
user_key_entry = Entry(master=niet_geregistreerd_stallen_frame)
nummer = Entry(master=geregistreerd_stallen_frame)


toon_start_frame()                                      # start_frame uitvoeren
root.mainloop()                                         # root mainloop uitvoeren
