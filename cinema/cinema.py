import funcs as fs

menu = [
    "Quitter",
    "Initialiser la salle",
    "Afficher la salle",
    "Réserver une place",
    "Annuler une réservation",
    "Vérifier une place",
    "Compter les places"
]

theater = []


def demander_entier(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Entrée invalide.")


def demander_place():
    row = input("Rangée (A-Z) : ").upper()
    seat = demander_entier("Numéro du siège : ")
    return row, seat


def initialiser_salle():
    while True:
        rows = demander_entier("Nombre de rangées (max 26) : ")

        if rows > 26:
            print("Maximum 26 rangées.")
            continue

        seats = demander_entier("Nombre de sièges : ")
        return fs.initialize_theater(rows, seats)


while True:
    fs.show_menu(menu)
    choix = input("Votre choix : ")

    # Quitter
    if choix == "0":
        print("Au revoir.")
        break

    
    elif choix == "1":
        if theater:
            rep = input("Écraser la salle actuelle ? (y/n) : ").lower()

            if rep != "y":
                continue

        theater = initialiser_salle()


    elif choix == "2":
        fs.show_theater(theater)


    elif choix == "3":
        try:
            row, seat = demander_place()

            if fs.check_availability(row, seat, theater):
                theater[ord(row) - 65][seat - 1] = "1"
                print("Place réservée.")
            else:
                print("Place déjà occupée.")

        except IndexError:
            print("Place inexistante.")


    elif choix == "4":
        try:
            row, seat = demander_place()

            if not fs.check_availability(row, seat, theater):
                theater[ord(row) - 65][seat - 1] = "0"
                print("Réservation annulée.")
            else:
                print("La place est déjà libre.")

        except IndexError:
            print("Place inexistante.")

    elif choix == "5":
        try:
            row, seat = demander_place()

            if fs.check_availability(row, seat, theater):
                print("Place libre.")
            else:
                print("Place occupée.")

        except IndexError:
            print("Place inexistante.")

    
    elif choix == "6":
        libres, occupees = fs.count_seats(theater)

        print(f"Places libres : {libres}")
        print(f"Places occupées : {occupees}")

    else:
        print("Choix invalide.")
