import random

print("Welcome")
print()

top_range = input("Type a number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Number is larger than 0")
        quit()
else:
    print("Type another number")
    quit()

random_number = random.randint(0 , top_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Type another number")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("Number is smaller than your guess")
    else:
        print("Number is bigger than your guess")

print("You got it in", guesses, "guesses")
