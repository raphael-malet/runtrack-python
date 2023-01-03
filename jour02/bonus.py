a = input('Entrer la longueur la plus grande : ')
b = input('Entrer une longueur : ')
c = input('Entrer la dernière longueur : ')

def triangle(a,b,c):
    if b+c > a :
        if b*b+c*c == a*a and b==c :
            print('je suis un triangle rectangle isocèle.')
        elif b*b+c*c == a*a:
            print('je suis un triangle rectangle')
        elif b==a==c :
            print ('je suis un triangle equilatéral.')
        elif b==c :
            print ('je suis un triangle isocèle.')
        else :
            print('je suis un trinagle quelconque')
            
    else :
        print ('je suis pas un triangle.')
               
triangle(float(a),float(b),float(c))

