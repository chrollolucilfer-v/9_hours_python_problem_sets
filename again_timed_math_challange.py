import random
import time

OPERATORS = ["+", "-", "*", "/"]

MAX_OPERATOR = 12
MIN_OPERATOR = 3

TOTAL_PROBLEMS = 10

def generate_probblem():
    left = random.randint(MIN_OPERATOR, MAX_OPERATOR)
    operator = random.choice(OPERATORS)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    exp = str(left) + " " + operator + " " + str(right)
    answer = eval(str)
    return exp, answer

input("Press Enter To Start")
print("--------------------")

start_time = time.time()
for i in range(TOTAL_PROBLEMS):
    exp, answer = generate_problem()
    while True:
        guess = input("Problem" + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1
end_time = time.time()

total_time = round(end_time-start_time)
print("----------------------")
print("Nice Work You Finished in ",total_time)