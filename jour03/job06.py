#afficher l'alphabet sous forme pyramidale

def alphabet():
    chaine = 'abcdefghijklmnopqrstuvwxyz'*10
    i = 0
    while i <= len(chaine):
        print(chaine[:i])
        chaine = chaine[::]
        i += 1      
alphabet()