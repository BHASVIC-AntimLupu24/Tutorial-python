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
#x = 'beau'
#print('au' in x)
#name = 'be\'au'
#print(name)
#name ='ja"mie'
#print(name)
# for double and single quote
#name_2 = 'je"\'nifar'
#print(name_2)
#string = 'beau is cool'
#print(string[1:7])
#done = True
#print(type(done) == bool) # checks if a value is boolean
#if done:
#    print('yes') # prints yes when done = true or when any variable is equal to true
#else:
#    print('no')
#num_1 = 2+3j
#num_2 = complex(2,3)
#print(num_1.real)
#print(num_1.imag)
#print(num_2.real)
#print(num_2.imag)
#from enum import Enum
#class State(Enum):
#    INACTIVE = 0
#    ACTIVE = 1
#print(State.ACTIVE.value) # assigns a constant value
#print(list(State)) # prints out the types of states
#print(len(State)) # prints out how many states are there
#age = input('What is your age? ')
#print("your age is "+ age)
# items = ['Rodger','Syd', 1, 2, True]
# print('beau' in dogs) # checks if an item is in an list
# print(dogs[1])
# print(dogs.pop())
# print(dogs)
# dogs.insert(1,'Jean')
# print(dogs)
# items[1:1] = ['Test1', 'Test2']
# print(items)

# names = ['Jamie', 'Hubert','Amy','ben', 'Dean', 'Max', ]
# namescopy = names[:]
# names.sort(key=str.lower)
# print(sorted(names, key=str.lower))
# print(names)
# print(namecopy)

# names = ('Rodger', 'Syd')
# names[0]
# print(names[0])

dog = {'name':'Rodger', 'age': 25, 'colour': 'green'}
# dog['name'] = 'Syd'
# print(dog['name'])
# print(dog.get('name'))
# print(dog.pop('name'))
# print(dog)
# print(dog.popitem())
# print(dog)
# print('colour' in dog)
# print(list(dog.keys()))
# print(list(dog.values()))
# print(list(dog.items()))
# dog['favourite food'] = 'Meat' # adding an item to a list
# print(dog)
# del dog['colour']
# print(dog)
dogCopy
