print("Welcome to my computer quiz")
playing = input("Do you want to play a game:  ")
if playing.lower() != "yes":
    quit()

playing = input("Are you sure once you start, it does not end 💀💀💀  ")
if playing.lower() != "yes":
    quit()

score = 0
while True:

    answer = input("What does CPU stands for: ")
    if answer.lower() == "central processing unit":
        score += 1
    else:
        print("Wrong boooooooooooooooo")
        break

    answer = input("What does GPU stand for: ")
    if answer.lower() == "graphics processing unit":
        score += 1
    else:
        print("Wrong boooooooooooooooo")
        break

    answer = input("What does RAM stand for: ")
    if answer.lower() == "random access memory":
        score += 1
    else:
        print("Wrong boooooooooooooooo")
        break

    answer = input("What does SSD stand for: ")
    if answer.lower() == "solid state drive":
        score += 1
    else:
        print("Wrong boooooooooooooooo")
        break
        
    answer = input("What does ROM stand for: ")
    if answer.lower() == "read only memory":
        score += 1
    else:
        print("Wrong boooooooooooooooo")
        break

    answer = input("What does HDD stand for: ")
    if answer.lower() == "hard disk drive":
        score += 1
    else:
        print("Wrong boooooooooooooooo")

    break


print("You got "+ str(score) + " questions correct")
if(score == 6):
    print("Hurrey! You ", end = '')


print("Scored "+ str(int((score/6)*100))+ "%.")


