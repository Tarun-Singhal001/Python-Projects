import random
start = input("Do you want to play a game (yes/no): ")
if(start.lower() != "yes"):
    print("Ok quiting.....", end = ' ')
    print("Done")
box = ["Rock", "Paper", "Scissor"]
c_score = 0
p_score = 0
while True:
    p_input = input("Enter Rock, Paper, Scissor or q(quit): ")
    if(p_input == "q"):
        print("Final Score Oponent's   Your's")
        print(' ' *12 + str(c_score) + ' ' *11 + str(p_score))
        if c_score > p_score:
            print("Even a kid can win this game.")
        elif c_score == p_score:
            print("Hey! Don't go anywhere, It's a Tie.")
        else:
            print("See you In the next game.")
            p_score = 0
            c_score = 0 
            continue
        quit()
    else:
        p_input = p_input.lower()

    randno = random.randint(0,2)
    c_input = box[randno]
    print("Oponent's ", c_input)
    if p_input == "rock" and c_input == "Paper":
        print("You loose, Nice try!")
        c_score += 1

    elif p_input == "rock" and c_input == "Scissor":
        print("You won!")
        p_score += 1

    elif p_input == "paper" and c_input == "Rock":
        print("You won!")
        p_score += 1

    elif p_input == "paper" and c_input == "Scissor":
        print("You loose, Nice try!")
        c_score += 1

    elif p_input == "scissor" and c_input == "Rock":
        print("You loose, Nice try!")
        c_score += 1

    elif p_input == "scissor" and c_input == "Paper":
        print("You won!")
        p_score += 1

    else:
        print("It's a Tie.")

    print("Final Score  Oponent's   Your's")
    print(' ' *12 + str(c_score) + ' ' *11 + str(p_score))
