# Write your code here
from random import choice

game_list = ["rock", "paper", "scissors"]
game_dict = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
rating = 0


def game_logic(rr):
    computer = choice(game_list)
    if user == computer:
        print(f'There is a draw {computer}')
        rr += 50
    else:
        user_index = game_list.index(user)
        new_list = game_list[user_index + 1:] + game_list[:user_index]
        mid = len(new_list) // 2
        win = new_list[:mid]
        lose = new_list[mid:]
        if computer in win:
            print(f'Sorry, but the computer chose {computer}')
        else:
            print(f'Well done. The computer chose {computer} and failed')
            rr += 100
    return rr


user_name = input('Enter your name:')
print(f'Hello, {user_name}')
user_list = input()
print("Okay, let's start")
if len(user_list) != 0:
    game_list = user_list.split(',')
f_obj = open('rating.txt', 'r')
li = f_obj.readlines()
f_obj.close()
for line in li:
    xx = line.split(" ")
    if xx[0] == user_name:
        rating = int(xx[1])

while True:
    user = input()
    if user == "!exit":
        print("Bye!")
        exit()
    elif user in game_list:
        rating = game_logic(rating)
    elif user == "!rating":
        print(f'Your rating: {rating}')
    else:
        print("Invalid input")
