steve = {
    "name" : "Wormack",
    "surname" : "Steve",
    "annif" : "1984-01-14",
    "loisir" : ["golf", "foot","astrnomie","lecture"],
    "panier" : {}
}

jean = {
    "name" : "Némare",
    "surname" : "Jean",
    "annif" : "1991-04-25",
    "loisir" : [],
    "panier" : {
                "art-125": 45,
                "art-134": 10,
                "art-099" :3
                }
}

utilisateur = {

"steve@gmail.com" : {
    "name" : "Wormack",
    "surname" : " Steve",
    "annif" : "1984-01-14",
    "loisir" : ["golf","foot","astrnomie","lecture"],
    "panier" : {}


}, 
"jean@gmail.com" : {
  "name" : "Némare",
    "surname" : "Jean",
    "annif" : "1991-04-25",
    "loisir" : [],
    "panier" : {
                "art-125" :45,
                "art-134" : 10,
                "art-099" : 3

    }
}
}
for key, value in utilisateur.items():
    print(f"{key}: \n")
    print(value.get("name"))
    print(value.get("surname"))
    print("\n")