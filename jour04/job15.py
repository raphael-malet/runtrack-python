#arrondir les nombres d'une liste.
L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def arrondir(L):
    r = []
    for i in L[::]:
        i=float(int((i*10**0)/(10**0)))
        r.append(i)
    return r
arrondir(L)

def ordre_croissant(L):
    r=[]
    while L:
        mini=L[0]
        for i in L:
            if i < mini:
                mini=i
        L.remove(mini)
        r.append(mini)
    return r
print(ordre_croissant(arrondir(L)))