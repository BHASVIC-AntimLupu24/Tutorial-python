#import random

# 3:32 - 43:12, rock paper scissors game
#  def get_choices():
#     player_choice = input('Enter a choice: rock,paper,scissor: ')
#     options = ['rock','paper','scissor']
#     computer_choice = random.choice(options)
#     choices = {'player':player_choice, 'computer':computer_choice}
#     return choices
#
# def check_win(player, computer):
#     print(f'You chose {player} and computer chose {computer}')
#     if player == computer:
#         return 'Its a tie!'
#     elif player == 'rock':
#         if computer == 'scissor':
#             return 'Rock smashes scissors! You win!'
#         else:
#             return 'Paper covers rocks! You lose.'
#     elif player == 'paper':
#         if computer == 'rock':
#             return 'Paper covers rock! You win!'
#         else:
#             return 'Scissors cuts paper! You lose.'
#     elif player == 'scissors':
#         if computer == 'paper':
#             return 'Scissors cuts paper! You win!'
#         else:
#             return 'Rocks smashes papers! You lose.'
#
# choices = get_choices()
# result = check_win(choices['player'], choices['computer'])
# print(result)

#-----------

# 49:45 - 1:00:36 , data types
# name = 'beau'
# print(isinstance(name,str)) # checks if a variable is an instance of a data type
#
# number = "20"
# age = int(number)
# print(isinstance(age,int))

#-------------

# 1:00:36 -
# age = 8
# age += 8 # age = age +8, can remove the + to any arithmetic operator
# print(age)
# def is_adult(age):
#     if age > 18:
#         return True
#     else:
#         return False
#
# def is_adult2(age):
#     return True if age > 18 else return False
