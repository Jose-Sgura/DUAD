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