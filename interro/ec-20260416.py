menu_liste = ["quitter le menu", "afficher le catalogue", "enregistrez un noouveau client", "ajouter un article au panier du client", "afficher la fiche d'un client" ]
def affiche_menu():
    """Affiche le menu principal."""
    print("\nMenu principal :")
    print("0 : quitter le programme")
    print("1 : afficher le catalogue")
    print("2 : enregistrez un nouveau client")
    print("3 : ajouter un artticle au panier du client")
    print("4 : afficher la fiche d'un client")


   

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
choix = input ("quel est votre choix : ")
if choix == "0":
    print("au revoir")







print("nom du produit et la quantité")
for ref, produit in catalogue.items():  
    print(produit["nom"], produit["quantité"])

email = input("email : ")

if email in clients :
    print("client déjà exixstant")
else : 
    nom = input("nom : ")
    prenom = input("prenom: ")

    clients[email] = {
        "nom" : nom,
        "prenom": prenom,
        "panier" : {}
    }
    print ("client ajouté ")