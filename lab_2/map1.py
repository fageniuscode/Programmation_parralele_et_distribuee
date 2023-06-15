from functools import reduce

def add(x,y):
    """Une fonction simple qui retourne la somme de ses arguments."""
    return x+y

def multiply(x,y):
    """Une fonction simple qui retourne le produit de ses arguments."""
    return x * y

a = [1,2,3,4,5]

""" Calculer la somme des éléments de la liste a, en commençant par une valeur initiale de 10 """
total = reduce(add, a, 10)
print("La somme des éléments de la liste a, en commençant par 10 :")
print(total)
print()

""" Calculer le produit des éléments de la liste a """
total1 = reduce(multiply, a)
print("Le produit des éléments de la liste a :")
print(total1)