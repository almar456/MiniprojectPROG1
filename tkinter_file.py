from tkinter import *                                   # Tkinter importen om te gebruiken


def toon_start_frame():                                 # Functie om start_frame te laten zien
    fiets_stallen_frame.pack_forget()
    fiets_ophalen_frame.pack_forget()
    info_frame.pack_forget()
    start_frame.pack(fill="both",
                     expand=True)


def toon_info_frame():                                  # Functie om info_frame te laten zien
    start_frame.pack_forget()
    info_algemeen_frame.pack_forget()
    info_persoonlijk_frame.pack_forget()
    info_frame.pack(fill="both",
                    expand=True)
    button_info_algemeen.pack(padx=20,
                              pady=20)
    button_info_persoonlijk.pack(padx=20,
                                 pady=20)
    button_ga_terug_info.pack(padx=20, pady=20)


def toon_fiets_stallen():                               # Functie om fiets_stallen_frame te laten zien
    start_frame.pack_forget()
    geregistreerd_stallen_frame.pack_forget()
    niet_geregistreerd_stallen_frame.pack_forget()
    fiets_stallen_frame.pack(fill="both",
                             expand=True)
    button_geregistreerd_stallen.pack(padx=20,
                                      pady=20)
    button_niet_geregistreerd_stallen.pack(padx=20,
                                           pady=20)
    button_ga_terug_stallen.pack(padx=20, pady=20)


def toon_fiets_ophalen():                               # Functie om fiets_ophalen_frame te laten zien
    start_frame.pack_forget()
    fiets_ophalen_frame.pack(fill="both",
                             expand=True)
    button_ga_terug_ophalen.pack(padx=20, pady=20)

# sub frames laten zien


def toon_geregistreerd_stallen():
    fiets_stallen_frame.forget()
    geregistreerd_stallen_frame.pack(fill="both",
                                     expand=True)
    button_ga_terug_stallen_geregistreerd.pack(padx=20, pady=20)


def toon_niet_geregistreerd_stallen():
    fiets_stallen_frame.forget()
    niet_geregistreerd_stallen_frame.pack(fill="both",
                                          expand=True)
    button_ga_terug_stallen_niet_geregistreerd.pack(padx=20, pady=20)


def toon_info_algemeen():
    info_frame.forget()
    info_algemeen_frame.pack(fill="both",
                             expand=True)
    button_ga_terug_info_algemeen.pack(padx=20, pady=20)


def toon_info_persoonlijk():
    info_frame.forget()
    info_persoonlijk_frame.pack(fill="both",
                                expand=True)
    button_ga_terug_info_persoonlijk.pack(padx=20, pady=20)


root = Tk()


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

# buttons

button_info = Button(master=start_frame,                # Button_info defineren
                     text="Informatie",
                     command=toon_info_frame,
                     background="#00387b",
                     fg="white")
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

# ga terug buttons

button_ga_terug_info = Button(master=info_frame,
                              text="Ga terug",
                              command=toon_start_frame,
                              background="#00387b",
                              fg="white")

button_ga_terug_info_algemeen = Button(master=info_algemeen_frame,
                                       text="Ga terug",
                                       command=toon_info_frame,
                                       background="#00387b",
                                       fg="white")

button_ga_terug_info_persoonlijk = Button(master=info_persoonlijk_frame,
                                          text="Ga terug",
                                          command=toon_info_frame,
                                          background="#00387b",
                                          fg="white")

button_ga_terug_stallen = Button(master=fiets_stallen_frame,
                                 text="Ga terug",
                                 command=toon_start_frame,
                                 background="#00387b",
                                 fg="white")

button_ga_terug_ophalen = Button(master=fiets_ophalen_frame,
                                 text="Ga terug",
                                 command=toon_start_frame,
                                 background="#00387b",
                                 fg="white")

button_ga_terug_stallen_geregistreerd = Button(master=geregistreerd_stallen_frame,
                                               text="Ga terug",
                                               command=toon_fiets_stallen,
                                               background="#00387b",
                                               fg="white")

button_ga_terug_stallen_niet_geregistreerd = Button(master=niet_geregistreerd_stallen_frame,
                                                    text="Ga terug",
                                                    command=toon_fiets_stallen,
                                                    background="#00387b",
                                                    fg="white")


toon_start_frame()                                      # start_frame uitvoeren
root.mainloop()                                         # root mainloop uitvoeren
