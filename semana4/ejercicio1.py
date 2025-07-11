Lastname= 'Segura Cubero'

Name = 'Jose Manuel' + Lastname

print(Name)


Sume = 10+5
String = f'La suma es = {Sume}'
print(String)

Age = 49
Employed = f'{Age} es la edad de Ramon'
print(Employed)

Animals = ['neko','inu', 'Cat', 'Dog']


print('Neko is =' + Animals[2] + '--in japonais')
print('Inu is = ' + Animals[3]+ '--in japonais')
print('Dog is ='+ Animals[1]+ '--in Spanish')
print('Cat is ='+ Animals[0]+ '--in Spanish')

Reproduction = ['Baby', 'No baby','WTF!']
People = ['Man', 'Woman']
print(People[0],'+', People[1],'=',Reproduction[0])
print(People[1],'+',People[1], '=',Reproduction[1] )
print(People[0],'+',People[0], '=',Reproduction[2] )


Flt = 1.5
Int = 50
result = 50 * 1.5

print(result)

Android = False
Human = True

if Human:
    print('It is a human let him alive') 
elif Android:
    print('it is a Android! shut it off!')