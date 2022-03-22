print("Welcome!")
playing = input("Do you want to play? ")

if playing.lower() == "yes":
    print("Starting...")
    print()
else:
    print("Bye!")
    quit()

ans = input("What does CPU stand for? ")
score = 0

if ans.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("What does RAM stand for? ")

if ans.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("What does IDLE stand for? ")

if ans.lower() == "integrated development environment":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("What does URL stand for? ")

if ans.lower() == "uniform resource locator":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("What does PNG stand for? ")

if ans.lower() == "portable network graphics":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print()

print("Your score is " + str(score) + " out of 5" )
