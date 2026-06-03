import random
number = random.randint(1, 100)
tries = 0
print("Guess the number between 1 and 100!")
while True:
    guess = int(input("Your guess: "))
    tries = tries + 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it in", tries, "tries!")
        break
