import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

highest = 1000
answer = random.randint(1, highest)
print(answer)

guess = 0 
print("Please guess number between 1 and {}:".format(highest))


while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("well done you guessed it")
    else:
        if guess < answer:
            print("please guess higher")
        else:
            print("please guess lower")
