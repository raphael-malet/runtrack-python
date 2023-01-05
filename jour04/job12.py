#écrire dans l'ordre croissant une liste passée en paramètre
L = [ 45, 9, 17, 5, 20, 2]

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
print(ordre_croissant(L))
