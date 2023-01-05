#compter le nombre de multipple de 3 dans une liste.

L = [8,24,48,2,16]

def multiple(liste):
    i=0
    nb_multiple = 0
    for i in liste:
        if i % 3 == 0:
            nb_multiple = nb_multiple + 1
        else:
            continue
    print(nb_multiple)
multiple(L)