import csv
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