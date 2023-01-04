#afficher fizz pour les multiplpes de 3 et Buzz pour les multiples de 5.

i=0
for i in range (0,100+1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')  
    elif i % 3 == 0:
        print('buzz')
    elif i % 5 == 0 : 
        print ('Fizz')
    else:
        print(i)