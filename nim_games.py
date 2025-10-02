# Programme : Somme de deux entiers

def somme_deux_entiers():
    try:
        # Saisie des deux entiers
        a = int(input("Entrez le premier entier : "))
        b = int(input("Entrez le deuxième entier : "))

        # Calcul de la somme
        resultat = a + b

        # Affichage du résultat
        print(f"La somme de {a} et {b} est : {resultat}")

    except ValueError:
        print("Erreur : Veuillez entrer uniquement des nombres entiers.")

# Appel de la fonction
somme_deux_entiers()
