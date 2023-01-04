#afficher nombre premier de 0 à 1000

def nombre_premier():
    for i in range (0,1000+1):
        if i > 1 :
            for j in range (2,i):
                if (i % j) == 0:
                    break
            else:
                print(i)
nombre_premier()