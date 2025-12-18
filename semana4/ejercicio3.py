import random
secret = random.randint(1,10)

print('Guess a number from 1 to 10')


while True:
    Try = int(input("Type your number down :  "))

    if Try < secret:
        print("Too low, try again")
    elif Try > secret:
        print("Too high, try again")
    else:
        print(f"!Congrats!, you guessed the number, It was {secret}")
        break