'''print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
perc = int(input("What % would you lke to give? 5, 10, 15, 20" ))
number = int(input("How many peaople should split the bill? "))
amount = (bill * perc / 100) / number
print(f"Each person should pay {amount} KES")'''

'''number = int(input("Enter a number you want to check: "))
if number % 2 == 0:
    print("This is an even number")
else:
    print("This number is odd")'''

'''height = int(input("What is your height? "))
if height >= 120:
    print("You are tall enough to ride")
    age = int(input("Enter your age: "))
    if age <= 12:
        bill = 100
        print("Your price is 100")
    elif age < 18:
        bill = 150
        print("Your price 150")
    else:
        bill = 300
        print("Your price is 300")
    wants_photo = input("Do you want to take a photo? Y or N? ")
    if wants_photo == 'Y':
        bill += 100
        print(f"Your final price is {bill}")
else:
    print("Eat and grow tall to get on the ride")'''

'''weight = int(input("What is your weight? "))
height = float(input("What is your height in m? "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print("You are overweight")
elif  bmi < 25:
    print("You are within normal")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")'''

'''year = int(input("Enter a year you want to check: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year!")
        else:
            print("Not a leap year")
    else:
        print("Leap year!")
else:
    print("Not a leap year")'''

'''print("Welcome to the Pizza Manyatta!")
size = input("What size of pizza would you like, S, M, or L? ")
peperonni = input("Would you like peperoni, Y or N? ")
cheese = input("Would you like extra cheese, Y or N? ")
bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25

if peperonni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if cheese == 'Y':
    bill += 1

print(f"Your final bill is {bill}. Enjoy your meal!")'''

'''print("Welcome to the Kakamega KFC")
order = input("What would you like to have? \n chicken\n bucket - ")
bill = 0
if order == 'chicken':
    bill += 200
elif order == 'bucket':
    bill += 300
else:
    bill += 500

drinks = input("Would you like a coleslow or a punch with that? ")
if drinks == 'coleslow':
    bill += 50
elif drinks == 'punch':
    bill += 100

print(f"Your total bill is {bill}\n Enjoy your meal")'''


print("Hello and welcome to the love calculator")
name1 = input("Enter a name: ")
name2 = input("Enter a second name: ")

name1_lower = name1.lower()
name2_lower = name2.lower()

combined = name1_lower + name2_lower
t = combined.count('t')
r = combined.count('r')
u = combined.count('u')
e = combined.count('e')

true = t + r + u + e

l = combined.count('l')
o = combined.count('o')
v = combined.count('v')
e = combined.count('e')

love = l + o + v + e 

love_score = int(str(true) + str(love))

print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f("Your love score is {love_score}, you go together like coke and mentos"))
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")