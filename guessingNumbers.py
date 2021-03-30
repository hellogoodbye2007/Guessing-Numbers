import random

print("Number Guessing Game")
number = random.randint(1,9)
chances = 5
print("Guess a number between 1 and 9")
while chances>0:
    guess = int(input("What do you think the number is? "))
    
    if(guess == number):
        print("Congrats! You guessed the number right!")
        break
    elif(guess<number):
        print("Your guess is too low. Guess higher.")
    else:
        print("Your guess is too high. Guess lower.")
    
    chances -= 1

if(chances == 0):
    print(f"You didn't guess the number. The number was {number}.")