import random

print("Welcome to Guess the Number Game!")
playing = input("Do you want to start this game? (yes/no): ")
if playing.lower() != "yes":
    quit()

while True:
    rnum = random.randint(1, 100)
    guess = 0
    print("In this game, you have to guess a number which is between 1 and 100.")

    while True:
        pnum = input("Guess a number: ")

        if not pnum.isdigit():
            print("Please enter a valid number.")
            continue

        pnum = int(pnum)

        if not (1 <= pnum <= 100):
            print("Number out of range! Enter a number between 1 and 100.")
            continue

        guess += 1

        if pnum == rnum:
            print(f"Correct! Well done, you guessed it in {guess} attempts.")
            break
        elif pnum < rnum:
            print("You are below the number. Try again!")
        else:
            print("You are above the number. Try again!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing! Goodbye!")
        break
