# afficher les nombre de 0 a 100 compris sauf 26,37,88

def nombre_100():
    i=0
    while i < 100+1:
        print(i)
        i=i+1
        if i == 26 :
            i=i+1
        if i == 37 :
            i=i+1
        if i == 88 :
            i=i+1
nombre_100()