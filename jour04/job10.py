#calcul dans un interval.
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
def calcul_interval(liste):
    liste_calcul = 1
    for i in liste:
        if i >= 25 and i <= 90 :
            liste_calcul = liste_calcul * i
        else:
            continue
    return(liste_calcul)
calcul_interval(L)
print(calcul_interval(L))