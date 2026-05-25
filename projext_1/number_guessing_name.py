import random


while True:
    num = int(input("Enter Your Range from 1 to :- ")).strip()
    if num.isdigit() and num >1:
        break
    else:
        print("enter a valid number")
        continue



random_number = random.randint(1,num)

while True:
    guess = int(input(f"enter your guess: from 1 to ${num}:- "))


    if guess == random_number:
        print("your guessed right")
        break

    else:
        print("try again next time")
        continue