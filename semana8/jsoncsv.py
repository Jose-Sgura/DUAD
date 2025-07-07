def open_list(Songs):
    with open(Songs,'r', encoding='utf-8') as file:
        Themes= [line.strip() for line in file if line.strip()]
    
    print('Original Songs')
    for single in Themes:
        print(f'Track: {single}')

    Themes.sort()

    with open('ordered_Songs.txt', 'w', encoding='utf-8' ) as list:
        for single in Themes:
            list.write(single+'\n')
            print(f'Ordered:{single}')
            
    
    
    

open_list('ordered_Songs.txt')
open_list('Songs.txt')

#Manejo de csv
import csv
#1
header=['name', 'genre', 'developer', 'ESRB']

guest=int(input('Hello! Add the amount of games you want!'))

games=[]

for g in range(guest):
    print(f'Videogame #{g+1}')
    name= input('Name:   ')
    genre= input('Genre:   '  )
    developer= input('Developer:    ')
    esrb= input('ESRB:    ')

    games.append([name, genre, developer, esrb])

with open ('giocchi.csv', 'w', newline='', encoding='utf-8') as newfile:
    writer= csv.writer(newfile)
    writer.writerow(header)
    writer.writerows(games)

print(f'There are {guest} video games saved inside the file {'giocchi.csv'}')

#ejercio2

header=['name', 'genre', 'developer', 'ESRB']

guest=int(input('Hello! Add the amount of games you want!'))

games=[]

for g in range(guest):
    print(f'Videogame #{g+1}')
    name= input('Name:   ')
    genre= input('Genre:   '  )
    developer= input('Developer:    ')
    esrb= input('ESRB:    ')

    games.append([name, genre, developer, esrb])

with open ('videos.csv', 'w', newline='', encoding='utf-8') as newfile:
    writer= csv.writer(newfile, delimiter='\t')
    writer.writerow(header)
    writer.writerows(games)

print(f'There are {guest} video games saved inside the file {'videos.tsv'}')
#json
import json
try:
    with open('pokemon.json', 'r', encoding='utf-8') as p:
        data=json.load(p)
except FileNotFoundError:
    print("The file was not found")
pokems=[
{
    "name": {
    "english": "Pikachu"
    },
    "type": [
    "Electric"
    ],
    "base": {
    "HP": 35,
    "Attack": 55,
    "Defense": 40,
    "Sp. Attack": 50,
    "Sp. Defense": 50,
    "Speed": 90
    }
},
{
    "name": {
    "english": "Charmander"
    },
    "type": [
    "Fire"
    ],
    "base": {
    "HP": 39,
    "Attack": 52,
    "Defense": 43,
    "Sp. Attack": 60,
    "Sp. Defense": 50,
    "Speed": 65
    }
},
{
    "name": {
    "english": "Squirtle"
    },
    "type": [
    "Water"
    ],
    "base": {
    "HP": 44,
    "Attack": 48,
    "Defense": 65,
    "Sp. Attack": 50,
    "Sp. Defense": 64,
    "Speed": 43
    }
}
]
print("Let´s add a new pokemon to the list!!")
name=input('Name:  ')
types=input('Type: ').split(',')
types=[sort.strip() for sort in types]

print("Please add the statistics of your pokemon")
Hp=int(input('HP:'))
Attack=int(input('Attack:  '))
Defense=int(input('Defense:  '))
sp_Attack=int(input('Sp. Attack:  '))
sp_defense= int(input('Sp. Defense:  '))
Speed=int(input('Speed:  '))

new_pokemon={
    "name":{
        "english":name
    },
    "type": types,
    "base":{
        "HP": Hp,
        "Attack": Attack,
        "Defense": Defense,
        "sp. attack": sp_Attack,
        "sp. defense": sp_defense,
        "Speed": Speed,

    }
}
pokems.append(new_pokemon)

with open('pokemon.json', 'w', encoding='utf-8')as p:
    json.dump(pokems, p, indent=4,ensure_ascii=False)

print(f'The new pokemon {name} was added successfully')