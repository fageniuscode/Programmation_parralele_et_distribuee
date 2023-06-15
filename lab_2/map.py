def calc_square(x):
    """ Calcule le carré de x """
    return x * x

def find_smallest(a, b, c):
    """ Retourne le plus petit des trois nombres a, b et c. """
    return min(a, b, c)
result = find_smallest(2, 5, 7)
print("Résultat de find_smallest pour retourner le plus petit des trois nombres :")
print(result)
print()

a = [1,2,3,4,5]
b = [6,7,8,9,10]

""" Appliquer la fonction calc_square à la liste a """
result_a = list(map(calc_square, a))
print("Résultat de calc_square appliqué à la liste a :")
print(result_a)
print()

""" Appliquer la fonction calc_square à la liste b """
result_b = list(map(calc_square, b))
print("Résultat de calc_square appliqué à la liste b :")
print(result_b)
print()

""" Appliquer la fonction find_smallest à chaque paire d'éléments de a et b """
result = list(map(find_smallest, a, b, [7] * len(a)))
print("Résultat de find_smallest appliqué aux paires d'éléments de a et b :")
print(result)


