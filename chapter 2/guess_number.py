import random

goalNumber = random.randint(1, 100)

gamePoint = 100 #set default game point
TIME = 7
print("Woohoo, start game. Now, you can guess a number from 1 to 100")
print(f"You have maximum {TIME} times to guess")
print("Good luck!!!")

# for loop to guess 7 time
for guessTime in range(TIME):
    print("Take a guess ===>")
    guessNumber = int(input("Your number: "))

    if guessNumber < goalNumber:
        print("Oops, your number is too low")
        gamePoint -= 10
    elif guessNumber > goalNumber:
        print("Oops, your number is too high")
        gamePoint -= 10
    else:
        break

if guessNumber == goalNumber:
    print("Woww, congratilation!")
    print("Your point: ", gamePoint)
else: 
    print("Opps, try to next time :((((")