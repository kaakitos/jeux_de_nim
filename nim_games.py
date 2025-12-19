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

def division(a, b):
    if b == 0:
        return "Erreur : division par zéro impossible"
    return a / b

# Appel de la fonction
somme_deux_entiers()
print (division(5, 2))
print("********** AUTRES TEST **********")
somme_deux_entiers()
print (division(5, 5))