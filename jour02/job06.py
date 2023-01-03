num = input('entrer un nombre : ')

def nombre(nombre):
    if nombre > 0 :
        print ("positif")
    elif nombre < 0 :
        print ("négatif")
    else :
        print ("je suis le nombre 0")

nombre(int(num))