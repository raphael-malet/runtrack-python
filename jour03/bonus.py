#inverser une chaine de caractère

chaine_caractere = input('Entrer une chaine de  caractère: ')
def renverser(chaine_caractere):
    chaine_caractere_renverser = chaine_caractere[::-1]
    print(chaine_caractere_renverser)
renverser(chaine_caractere)