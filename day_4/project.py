import random


def rps_status(user_one, user_two):
    if user_two.lower():
        return 'Draw'

    if user_one.lower() == 'rock' and user_two.lower() == 'scissors':
        return 'Win'

    if user_one.lower() == 'scissors' and user_two.lower() == 'paper':
        return 'Win'

    if user_one.lower() == 'paper' and user_two.lower() == 'rock':
        return 'Win'

    return 'Lose'


print('Welcome to rock, paper, scissors')

all_choices = ['rock', 'paper', 'scissors']

machine_choice = random.choice(all_choices)
client_choice = input("please choose a one: rock, paper, scissors -> ")
print(f"Your choice: {client_choice} and machine choice: {machine_choice}")

if client_choice.lower() in all_choices:
    print(f"You {rps_status(client_choice, machine_choice)}")
else:
    print("You Lose")
