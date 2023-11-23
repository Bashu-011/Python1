'''fruits = ['lemon', 'apple', 'peach','pineapple']
for x in fruits:
    print(x + ' pie')
    print(x)
    print(fruits)
print(fruits)'''

'''heights = [100, 154, 189, 111, 90, 89, 100, 120, 171]

total_height = 0
for x in heights:
    total_height += x
print(total_height)

population = 0
for y in heights:
    population += 1
print(population)

avg = round(total_height / population)
print(f"The number of people is {population} and their average height is {avg} cm")'''

'''add = 0
for number in range(1, 15, 2):
    
    print(number)'''

'''total = 0
for number in range(1, 101):
    total += number
print(total)'''

'''target = int(input("Enter a number you would like to get the evens added: "))

total = 0

for even in range(0, target + 1):
    if even % 2 == 0:
        total += even
print(f"The total for even numbers is {total}")'''

'''for nums in range(1, 101):
    if nums % 3 == 0 and nums % 5 == 0:
        print("FizzBuzz")
    elif nums % 3 == 0:
        print("Fizz")
    elif nums % 5 == 0:
        print("Buzz")
    else:
        print(nums)'''

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

'''password = ""
for char in range (0, nr_letters + 1):
    password += random.choice(letters)
for char in range (0, nr_symbols + 1):
    password += random.choice(symbols)
for char in range (0, nr_numbers + 1):
    password += random.choice(numbers)
print(password)'''
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = []

for char in range( 0, nr_letters + 1):
    password.append(random.choice(letters))
for char in range( 0, nr_symbols + 1):
    password.append(random.choice(symbols))
for char in range( 0, nr_numbers + 1):
    password.append(random.choice(numbers))
print(password)

final_pass = ""
random.shuffle(password)
for i in password:
    final_pass += i
print(final_pass)

