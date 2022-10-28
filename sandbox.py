# importer un module (ici re: expressions régulières en python, bibliothèque standard: dispo avec python)
import re
import requests

# syntaxe fondamentale python
# int : entier
ma_variable = 3
# str: chaine de caractère
truc = "bonjour"
# float: nombres réels
pi = 3.14

# list: liste indexée
liste_elements = [1, 2, "ok", truc]
# dict: dictionnaire, ensemble de paires clé => valeur
key_value = {"key": "value", "other_key": "other_value"}

# affichage de valeurs ou de variables
print(55, "hello", ma_variable, key_value)

# listes vs dictionnaires
print(liste_elements[2])
print(key_value["other_key"])

# structures de contrôle if, for, fonctions
# ATTENTION les blocs sont définis par
#   - un entête se terminant par ":"
#   - un bloc indenté (alinéa de 2 ou 4 espaces, pas de \t)
# on sort du bloc en revenant à l'indentation précédente

if len(liste_elements) > 1:
    # f-string: injection d'expressions python dans des slots {} 
    # à l'intérieur des chaines de caractères 
    print(f" 2ème élément: {liste_elements[1]} ")
# les variables ont une valeur booléenne à côté de valeur de type
elif not liste_elements:
    print("liste vide !")
else:
    print("liste trop courte !")

# boucle for: comme en shell: pour élément dans ensemble
for machin in liste_elements:
    print(machin)


# fonction : bloc de code paramétrable et réutilisable
def my_function(liste, pow):
    results = []
    for num in liste:
        results.append(num ** pow)
    return results

# print(my_function([1, 3, 5, 7], 3))
cubes = my_function([1, 3, 5, 7], 3)
print(cubes)


# ex de re: détection d'ip

target = "mon ip est 192.168.1.21 ou 10.0.0.2"
matches = re.finditer("(\d+\.){3}\d+", target)
print(list(matches))


# ex de paquet tiers: requests: requêtes http
# pip install requests

r = requests.get("https://dawan.fr")

print(f"code de retour http: {r.status_code}")
if 200 <= r.status_code < 300:
    print(r.text)