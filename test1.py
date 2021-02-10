"""
Le but du TP d’aujourd’hui est d’écrire un script dans lequel :
1. Vous choisissez un nombre de 1 à 1000 et vous l’assignez à une variable
2. Puis, tant qu’un utilisateur ne frappe pas la touche ‘q’, vous lui demandez de choisir un nombre
entre 1 et 1000.
3. Si le nombre est inférieur à la variable assignée vous lui dites “Plus grand”
4. Si le nombre est supérieur à la variable assignée, vous lui dites “Plus petit”
5. L’utilisateur gagne s’il trouve la bonne valeur.
6. Vous devez tester que le nombre entré est correct. Par exemple, retournez une erreur si ce
qu’entre l’utilisateur n’est pas un nombre, ou n’est pas compris entre 1 et 1000.
"""
import random
import math

import test_import

a = random.randint(1, 1000)
print(test_import.fibonacci(test_import.mon_variable))

while True:

    nombre_entree = input("Entrer un nombre entre 1 et 1000, faites 'q' pour quitter : ")

    if nombre_entree == 'q':
        break

    elif not nombre_entree.isnumeric():
        print("Vous devez entrer un nombre entier ")
        continue

    elif int(nombre_entree) <= 0:
        print("Entrer un nombre egal à 1")
        continue

    elif int(nombre_entree) > 1000:
        print("Entrer un nombre egal à 1000")
        continue

    elif int(nombre_entree) < a:
        print("Plus grand")
        continue

    elif int(nombre_entree) > a:
        print("Plus petit")
        continue

    elif int(nombre_entree) == a:
        print("Vous avez gagné !!!")
        break
