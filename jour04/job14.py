#supprimer les mot plus petit que n 

my_long_word = ("La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance")
L = my_long_word.split()
n = int(input('Supprimer les mots plus petit que ?: '))

def suppression_mot(liste,n):
    for i in liste[::]:
        if i[::] <= i[0:n]:
            liste.remove(i)
    print(liste)
    return" ".join(liste)    
print(suppression_mot(L, n))