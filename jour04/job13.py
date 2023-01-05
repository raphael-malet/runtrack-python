#supprimer les doublon d'une liste.

L = [10,20,30,20,10,50,60,40,80,50,40]

def ordre_croissant(L):
    r=[]
    suppression=[]
    for i in L[::]:
        mini=L[0]
        for i in L:
            if i < mini:
                mini=i
        L.remove(mini)
        r.append(mini)
    for i in r[::]:
        if i not in suppression :
            suppression.append(i)
    print(suppression)
ordre_croissant(L)