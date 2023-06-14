import math

def add(x,y):
    """Une fonction simple qui retourne la somme de ses arguments."""
    return x+y

def dif(x,y):
    """Une fonction simple qui retourne la différence de ses arguments."""
    return x-y

def prod(x,y):
    """Une fonction simple qui retourne le produit de ses arguments."""
    return x*y


def calc_distance(point1, point2):
    """Calcule la distance entre deux points."""
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance


result = add(3,7)
print(result)

print(add.__name__) # Renvoie le nom de la fonction
print(add.__doc__) # Renvoie la documentation de la fonction
print(add.__module__) # Renvoie le nom du module dans lequel la fonction est définie


def my_map(func, arg1, arg2):
    """Construct"""
    res = []

    for i,j in zip(arg1,arg2):
        """Afficher la fonction appelée et les arguments"""
        print(f"Fonction appelée : {func.__name__}")
        print(f"Arguments : {i}, {j}")
        res.append(func(i,j))
    return res

a = [1,2,3,4,5]
b = [6,7,8,9,10]
point1 = [(1.0,1.0,1.0),(2.0,2.0,2.0),(3.0,3.0,3.0)]
point2 = [(4.0,4.0,4.0),(5.0,5.0,5.0),(6.0,6.0,6.0)]

result1 = my_map(add, a, b)
result2 = my_map(dif, a, b)
result3 = my_map(prod, b, a)
distance = my_map(calc_distance, point1, point2)


print(result1)
print(result2)
print(result3)
print(distance)
