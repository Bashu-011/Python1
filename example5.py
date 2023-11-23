'''import random
random_integer = random.randint(260, 281)
print(random_integer)
random_float = random.random()
print(random_float)
print(random_float * 10)'''

'''fruits = ['apples', 'pear', 'passion', 'orange']
fruits[1] = 'beef'
print(fruits)
fruits.extend('melon')
print(fruits)'''

'''names = ['Tom', 'Mia', 'Moses', 'Kelly', 'Laura']
import random
len_list = len(names)
rand_num = random.randint(0, len_list - 1)
person = names[rand_num]

print(f"The person paying is {person} ")'''

'''fruits = ['mango', 'melon', 'orange', 'jackfruit', 'apple']
veges = ['spinach', 'kales', 'lettuce', 'tomatos', 'cabbage']

dirty_dozen = [fruits, veges]

print(dirty_dozen[1][1])'''


import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
selection = [rock, paper, scissors]
entry = int(input('Enter 0 for rock, 1 for paper and 2 for scissors\n'))
if entry >= 3 or entry < 0:
    print("You entered an invalid number")
else:
    print(selection[entry])

    comp_entry = random.randint(0, 2)

    print(f"Computer chose: {comp_entry} ")
    print(selection[comp_entry])


    if entry == 0 and comp_entry == 2:
        print('You win!')
    elif comp_entry == 0 and entry == 2:
        print("You loose")
    elif comp_entry > entry:
        print('You loose!')
    elif entry > comp_entry:
        print("You win!")
    elif comp_entry == entry:
        print("It's a draw")
