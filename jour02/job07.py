langue = input('entrer votre lanuqage de programmation sans majuscule: ')

def je_suis_quoi(langue):
    if langue == 'javascript':
        print('tu es un developpeur web')
    elif langue == 'python':
        print('tu es un developpeur IA')
    elif langue == 'java':
        print('tu es un developpeur logiciel')
    elif langue == 'reacts':
        print('tu es un developpeur mobile')
    else :
        print('un jour, je serai le meilleur developpeur...')

je_suis_quoi(langue)
