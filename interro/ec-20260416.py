menu_liste = ["quitter le menu", "afficher le catalogue", "enregistrez un noouveau client", "ajouter un article au panier du client", "afficher la fiche d'un client" ]


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
while 