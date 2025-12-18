NotesCounter = 1
NonaprovedAmount = 0
AprovedAmount = 0
AprovedAvarage = 0
NonaprovedAvarage = 0
TotalAvarage=0
TotalScore=int(input('Ingrese la cantidad de notas'))

while NotesCounter: TotalScore
CurrentScore = int(input('Add the score: '))
    
if CurrentScore < 70:
    NonaprovedAmount += 1
    NonaprovedAvarage += CurrentScore
else:
    AprovedAmount += 1
    AprovedAvarage += CurrentScore

    TotalAvarage += CurrentScore / TotalScore
    NotesCounter += 1
    if AprovedAmount > 0:
        AprovedAvarage  = AprovedAvarage  / AprovedAmount
    else:
        AprovedAvarage = 0

    if NonaprovedAmount > 0:
        NonaprovedAvarage = NonaprovedAvarage / NonaprovedAmount
    else:
        NonaprovedAvarage = 0

TotalAvarage = TotalAvarage 

print('The student has this amount of notes')
print(f'{AprovedAmount}')
print('This is the avarage of the aprovedscore')
print(f'{AprovedAvarage}')
print('The student has this amount of nonaproved score')
print(f'{NonaprovedAmount}')
print('This is the average of the nonaproved score')
print(f'{NonaprovedAvarage}')
print('This is the total score')
print(f'{TotalAvarage}')
