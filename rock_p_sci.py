import random


user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input= input("Type Rock/Paper/Scissors or Q to quit: ").strip().lower()
    if user_input == "q":
        print("Okay Quitting ... ")
        break
    
    if user_input not in options:
        print("Type between rock, paper, scissors")
        continue
    random_number = random.randint(0,2)
    # rock is 1, paper 2, scissors 3
    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + ".")

    if user_input == "rock" and computer_pick =="scissors":
        print("You Won !!")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_pick =="rock":
        print("You Won !!")
        user_wins += 1

        continue
    elif user_input == "scissors" and computer_pick =="paper":
        print("You Won !!")
        user_wins += 1
        continue
    elif user_input == "scissors" and computer_pick =="rock":
        print("You Lost !!")
        computer_wins += 1
        continue
    elif user_input == "paper" and computer_pick =="scissors":
        print("You Lost !!")
        computer_wins += 1
        continue
    elif user_input == "rock" and computer_pick =="paper":
        print("You Lost !!")
        computer_wins += 1
        continue
    else:
        print("It was a Draw")
        continue

print(f"Your Score {user_wins}")
print(f"Computer Score {computer_wins}")
if user_wins > computer_wins:
    print("You Won")
elif computer_wins > user_wins:
    print("Computer Won")
else:
    print("it was a draw")
print("Thanks For Playing")
