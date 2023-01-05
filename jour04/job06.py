#changement de la première et dernière case d'ine liste

liste = [13, 56, 34,14, 34]
print(liste)

liste[0],liste[-1] = liste[-1],liste[0]
print(liste)