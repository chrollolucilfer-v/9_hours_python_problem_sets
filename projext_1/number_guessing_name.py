import random


while True:
    num = input("Enter Your Range from 1 to :- ")
    if num.isdigit() and int(num) >1:
        num = int(num)
        break
    else:
        print("enter a valid number")
        



random_number = random.randint(1,num)

while True:
    guess = int(input(f"enter your guess: from 1 to ${num}:- "))


    if guess == random_number:
        print("your guessed right")
        break

    else:
        print("try again next time")
        continue