import random

choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")

computerchoice = random.randint(0,2)

if int(choice) == 0:
    if computerchoice == 0:
        print("I choose Rock! Draw!")
    elif computerchoice == 1:
        print("I choose Paper! I Win!")
    else:
        print("I choose Scissors! You win!")
elif int(choice) == 1:
    if computerchoice == 0:
        print("I choose Rock! You Win!")
    elif computerchoice == 1:
        print("I choose Paper! Draw!")
    else:
        print("I choose Scissors! You Win!")
elif int(choice) == 2:
    if computerchoice == 0:
        print("I choose Rock! I Win!")
    elif computerchoice == 1:
        print("I choose Paper! You Win!")
    else:
        print("I choose Scissors! Draw!")
else:
    print("Error. Choose 0,1, or 2 next time.")