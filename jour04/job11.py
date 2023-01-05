#créer une liste + modification de la liste avec +1

L = []
print(L) #afficher la liste vide

L.append(7)
L.append(11)
L.append(42)
L.append(39)
L.append(2)

print(L) #afficher la liste avec les valeurs données

for i in range (len((L))):
    L[i] += 1
print(L)   #afficher la liste avec + 1 a toutes les valeurs