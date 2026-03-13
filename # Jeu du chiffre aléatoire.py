# Jeu du chiffre aléatoire
import random
tentative = 1

while True:
    print("Choisi le niveau de difficulté :")
    print("=========")
    print("1. niveau facile : 1-50")
    print("2. niveau moyen : 1-100")
    print("3. niveau difficile : 1-1000")

    choix =input ("Choisi le niveau : ")

    if choix == "1":
        max_nombre = 50
    elif choix =="2":
        max_nombre = 100
    elif choix =="3":
        max_nombre = 1000
    else:
        print("Choix invalide")
        exit()
    
    nombre_secret = random.randint(1, max_nombre) 

    while True:
        try:
             nombre_choisit = int(input(f"Choisis un nombre entre 1 et {max_nombre} : "))
        except ValueError:
            print("Veuillez entrer un nombre entier.")
            continue
        
        if nombre_choisit < 1 or nombre_choisit > max_nombre:
            print(f"Merci de choisir un nombre entre 1 et {max_nombre}")
            continue
        
        if nombre_choisit > nombre_secret:
            print("Nombre trop grand")
            tentative += 1

        elif nombre_choisit < nombre_secret:
            print("Nombre trop petit")
            tentative += 1

        else:
            break

    print("Bravo, tu as trouvé en", tentative, "tentatives !")