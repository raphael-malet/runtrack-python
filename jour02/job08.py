saison = input ('Entrer votre saison, ete ou hiver : ')
type = input('Entrer fruit ou legume :' )

def fruit_legume(type,saison):
    if type == 'fruits' and saison == 'hiver' :
        print ('orange, mandarine, kiwi')
    elif type == 'fruits' and saison == 'ete' :
        print ('Poire, fraise, cassis')
    elif type == 'legume' and saison == 'hiver' :
        print ('Carotte, topinambour, endive')
    elif type == 'legume' and saison == 'ete' :
        print ('artichaut, aubergine, navet')

fruit_legume(type,saison)