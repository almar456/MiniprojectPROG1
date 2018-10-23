from tkinter import *                                   # Tkinter importen om te gebruiken
from Ophalen import *                                   # het ophalen.py bestand importen
from Registreren import *                               # het Registreren.py bestand importen
from Stallen import stallen                                   # het Stallen.py bestand importen
from info import *
from tkinter.messagebox import showinfo
from passlib.hash import pbkdf2_sha256
from pushover import *


outfile = open('login_boolean.txt', 'w')
outfile.write('False')


def toon_start_frame():                                 # Functie om start_frame te laten zien
    fiets_stallen_frame.pack_forget()
    fiets_ophalen_frame.pack_forget()
    inloggen_frame.forget()
    start_frame.forget()
    geregistreerd_stallen_frame.forget()
    niet_geregistreerd_stallen_frame.forget()
    info_persoonlijk_frame.forget()
    info_algemeen_frame.forget()
    info_frame.pack_forget()
    start_frame.pack(fill="both",
                     expand=True)


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
    button_info_algemeen.pack(padx=20,
                              pady=20)
    button_info_persoonlijk.pack(padx=20,
                                 pady=20)


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

    fiets_stallen_frame.pack(fill="both",
                             expand=True)
    button_geregistreerd_stallen.pack(padx=20,
                                      pady=20)
    button_niet_geregistreerd_stallen.pack(padx=20,
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
    if 'True\n' in lines:
        button__login_fiets_ophalen.forget()
        button_fiets_ophalen_confirm.pack(pady=20, padx=20)
    else:
        button__login_fiets_ophalen.pack(padx=20, pady=20)

# sub frames laten zien


def toon_geregistreerd_stallen():
    fiets_stallen_frame.forget()
    geregistreerd_stallen_frame.pack(fill="both",
                                     expand=True)
    nummer.pack(padx=20, pady=20)
    button_stallen.pack(padx=20, pady=20)


def toon_niet_geregistreerd_stallen():
    fiets_stallen_frame.forget()
    niet_geregistreerd_stallen_frame.pack(fill="both",
                                          expand=True)
    readfile = open('login_boolean.txt', 'r')
    lines = readfile.readlines()
    if 'True\n' in lines:
        button_login_info.forget()
    else:
        naam_reg_entry.pack(padx=20, pady=20)
        gebruikersnaam_reg_entry.pack(padx=20, pady=20)
        wachtwoord_reg_entry.pack(padx=20, pady=20)
        user_key_entry.pack(padx=20, pady=20)
        button_registreer.pack(padx=20, pady=20)



def toon_info_algemeen():
    info_frame.forget()
    info_algemeen_frame.pack(fill="both",
                             expand=True)

var = 0

def toon_info_persoonlijk():
    global var
    info_frame.forget()
    info_persoonlijk_frame.pack(fill="both",
                                expand=True)
    readfile = open('login_boolean.txt', 'r')
    lines = readfile.readlines()
    if 'True\n' in lines:
            if var == 0:
                var = 1
                button_login_info.forget()
                readfile = open('login_boolean.txt', 'r')
                lines = readfile.readlines()
                list2 = [x.replace('\n', '') for x in lines]
                info_label = Label(master=info_persoonlijk_frame, text=persoonlijk(list2[1]))
                naam_label = Label(master=info_persoonlijk_frame, text='Dit account staat op de naam: ' + naam(list2[1]))
                fiets_nummer_label = Label(master=info_persoonlijk_frame, text='Uw fietsnummer is: ' + fietsnummer(list2[1]))
                info_label.pack_forget()
                naam_label.pack_forget()
                fiets_nummer_label.pack_forget()

                info_label.pack(padx=20, pady=20)
                naam_label.pack(padx=20, pady=20)
                fiets_nummer_label.pack(padx=20, pady=20)
    else:
        button_login_info.pack(padx=20, pady=20)


def login():
    info_persoonlijk_frame.forget()
    niet_geregistreerd_stallen_frame.forget()
    geregistreerd_stallen_frame.forget()
    fiets_ophalen_frame.forget()
    inloggen_frame.pack(fill="both", expand=True)
    gebruikersnaam_entry.pack(padx=20, pady=20)
    wachtwoord_entry.pack(padx=20, pady=20)
    button_confirm_login.pack(padx=20, pady=20)


def f_login():
        username = gebruikersnaam_entry.get()
        wachtwoord = wachtwoord_entry.get()
        global hash
        hash = pbkdf2_sha256.hash(wachtwoord)
        readfile = open('fietsen.csv', 'r').readlines()
        for lines in readfile:
            lijst = lines.split(';')
            if username == lijst[2] and (pbkdf2_sha256.verify(wachtwoord, hash) == True):
                outfile = open('login_boolean.txt', 'w')
                outfile.write('True\n'+username+'\n'+wachtwoord)
                toon_start_frame()
                break
        else:
            showinfo(title='popup', message='Uw ingevooerde combinatie is verkeerd!')

        # showinfo(title='popup', message='Uw ingevooerde combinatie is verkeerd!')


def if_loop():
    if stallen(nummer.get()) == 0:
        showinfo(title='popup', message='Uw fiets is gestald')
        toon_start_frame()
    elif stallen(nummer.get()) == 1:
        showinfo(title='popup', message='Het ingevoerde nummer is incorrect')
    else:
        showinfo(title='popup', message='Uw fiets is al gestald')
        toon_start_frame()


def registreer():
    if registreren(wachtwoord_reg_entry.get(), gebruikersnaam_reg_entry.get(), naam_reg_entry.get(), user_key_entry.get()) == 0:
        readfile = open('fietsen.csv', 'r').readlines()
        for lines in readfile:
            lijst = lines.split(';')
            if gebruikersnaam_reg_entry.get() == lijst[2]:
                message = 'Uw acount is geregistreerd, de code voor uw fiets is:' + lijst[0] + '\n onthoud deze code goed!'
                showinfo(title='popup', message=message)
                toon_start_frame()
    elif registreren(wachtwoord_reg_entry.get(), gebruikersnaam_reg_entry.get(), naam_reg_entry.get(), user_key_entry.get()) == 1:
        showinfo(title='popup', message='Uw wachtwoord voldoet niet aan de eisen!')
    elif registreren(wachtwoord_reg_entry.get(), gebruikersnaam_reg_entry.get(), naam_reg_entry.get(), user_key_entry.get()) == 2:
        showinfo(message='Sorry, deze gebruikersnaam is al bezet')

def info_ophalen():
    readfile = open('login_boolean.txt', 'r')
    lines = readfile.readlines()
    list2 = [x.replace('\n', '') for x in lines]
    print(list2[2])
    if ophalen(list2[1], list2[2]) == 0:
        username = list2[1]
        pushover_send(username)
        showinfo(title='popup', message='U kunt uw fiets nu pakken')
        # toon_start_frame()
    elif ophalen(list2[1], list2[2]) == 2:
        showinfo(title='popup', message='Uw fiets is momenteel niet gestald')
    elif ophalen(list2[1], list2[2]) == 1:
        print('verkeerd wachtwoord')
    else:
        print('wtf')

root = Tk()

menu = Menu(root)

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

info_algemeen_frame = Frame(master=root,
                            background='#f7d417')

info_persoonlijk_frame = Frame(master=root,
                               background='#f7d417')

inloggen_frame = Frame(master=root,
                       background="#f7d417")

registreren_frame = Frame(master=root,
                          background='#f7d417')

# buttons

button_info = Button(master=start_frame,                # Button_info defineren
                     text="Informatie",
                     command=toon_info_frame,
                     background="#00387b",
                     fg="white")
# button_info.config(height=150, width=300)
button_info.pack(padx=20, pady=20)

button_fiets_stallen = Button(master=start_frame,       # Button stallen defineren
                              text="Fiets stallen",
                              command=toon_fiets_stallen,
                              background="#00387b",
                              fg="white")
button_fiets_stallen.pack(padx=20, pady=20)

button_fiets_ophalen = Button(master=start_frame,       # Button ophalen defieneren
                              text="Fiets ophalen",
                              command=toon_fiets_ophalen,
                              background="#00387b",
                              fg="white")
button_fiets_ophalen.pack(padx=20, pady=20)

# sub buttons
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
                              text="Algemene informatie en voorwaarden",
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

# login buttons

button_login_info = Button(master=info_persoonlijk_frame,                   # om de button een functie mee tegeven:
                           text="Login",                                    # voeg command=functie toe
                           background="#00387b",                            # belangrijk: schrijf de functie zonder ()
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

# login velden
gebruikersnaam_entry = Entry(master=inloggen_frame)
wachtwoord_entry = Entry(master=inloggen_frame)
gebruikersnaam_ophalen_entry = Entry(master=fiets_ophalen_frame)
wachtwoord_ophalen_entry = Entry(master=fiets_ophalen_frame)
gebruikersnaam_reg_entry = Entry(master=niet_geregistreerd_stallen_frame)
gebruikersnaam_reg_entry.insert(END, 'Gebruikersnaam')
wachtwoord_reg_entry = Entry(master=niet_geregistreerd_stallen_frame)
wachtwoord_reg_entry.insert(END, 'Wachtwoord')
naam_reg_entry = Entry(master=niet_geregistreerd_stallen_frame)
naam_reg_entry.insert(END, 'Naam')
user_key_entry = Entry(master=niet_geregistreerd_stallen_frame)
nummer = Entry(master=geregistreerd_stallen_frame)


toon_start_frame()                                      # start_frame uitvoeren
root.mainloop()                                         # root mainloop uitvoeren

