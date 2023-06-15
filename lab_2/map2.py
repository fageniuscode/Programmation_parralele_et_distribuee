from functools import reduce

def join_strings(string1, string2):
    """ Concatène deux chaînes de caractères et renvoie le résultat. """
    return string1 + string2

string1 = "Master 2 "
string2 = "Génie Logiciel ISI"

""" Notre Liste de chaînes de caractères. """
strings = ["ISI est une ", "Institut de", "Référence", " dans les TIC au Sénégal."]

result = join_strings(string1, string2)
print("Résultat de la concaténation de string1 et string2 :")
print(result)
print()

""" On utilise ici la fonction reduce pour concaténer les chaînes de caractères. """
result = reduce(join_strings, strings)
print("Résultat de la concaténation des éléments de la liste strings :")
print(result)