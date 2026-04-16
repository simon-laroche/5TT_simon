menu_liste = ["quitter le menu", "afficher le catalogue", "enregistrez un noouveau client", "ajouter un article au panier du client", "afficher la fiche d'un client" ]
continu = True 
catalogue = {
    'pain_blanc' :15,
    'pain_complet' :8,
    'tarte_sucre' :5,
    'croisant' :25,
    'pistolet' :30
}
clients = {
    'sylvain.dubois@email.com':{
        'nom' : 'Sylvain',
        'prenom' : 'Dubois',
        'panier' : {
            'pain_blanc' : 1,
            'pain_complet' : 1,
            'pistolet' : 3
            }
    }
}

while continu:
    for option in menu_liste:
        print(f"{menu_liste}", {option})
        menu_liste += 1

choix =input("entrez votre choix")

if choix == "0":
    print("au revoir et merci d'avoir utiliser le programme")
    continu = False

elif choix == "1":
    print("nom du produit", end="")
    print("quantite")
    for item, stock in catalogue.items():
        print(f"{item < 10}{stock > 10}")

elif choix == "2" :
    email = input ("entrez une adressez mail ")
    name = input ("name")
    surname = input ("surname")

    clients[email] = {
       " name" : "name",
       "surname" : "surname" ,
        "panier" :{}
    }


elif choix == "3" :
    boucle = True
    clients = input("entrez une adresse mail")

    if clients.get(clients, None) == None :
        
else:
    while boucle: 
        item_choix = input("choissisez votre article")
        if catalogue.get(item_choix, None) == None:
            print("article selectionner n'existe pas")
        else: 
            print(f"{item_choix} : {catalogue.get(item_choix)}")
            qut_input = int(input("choissisez la quantite"))
        
        if qut_input > catalogue.get(item_choix):
            print("pas article en stock")

        else: 

            if clients [clients]["panier"].get(item_choix, None) == None :
                clients[clients]["panier"][item_choix] = qut_input 
                catalogue[item_choix] -= qut_input

            else : 
                clients[clients]["panier"][item_choix] += qut_input
                catalogue[item_choix] -= qut_input

insert_choix = str.lower(input("voulez-vous continuer "))
if insert_choix == "non " :
    boucle = False

elif choix == "4" :






