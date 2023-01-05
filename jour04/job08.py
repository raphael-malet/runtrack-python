#calcul des valeurs paire d'une liste.

L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

def somme_paire(liste):
    i = 0
    liste_paire_somme = []
    for i in liste:
        if i % 2 == 0:
            liste_paire_somme.append(i)
        else:
            continue
    print(sum(liste_paire_somme))
somme_paire(L)