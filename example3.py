#print("Hello world\nHello world\n hello world")
#print("Hello" + " " + "Angela")
#print("Day 1 - String Manipulation")
#print("String concatnetion is done with the"" + ""sign")

'''name = input("what is your name:")
if name == " ":
    print('Please enter a name:')
else:
    x = len(name)
print(f"Your name is {name} of length {x}")'''

'''a = input("a: ")
b = input("b: ")
c = a
a = b
b = c


print(f"a is {a}")
print(f"b is {b}")'''

'''name1 = input("What is the name of your hometown? ")
name2 = input("What is the name of your first pet? ")

band_name = f"Your band name could be {name1} {name2}"
print(band_name)'''

'''two_digits = (input("Enter a two digit number: "))
print(type(two_digits))
digit = two_digits[0]
digits = two_digits[1]
print(int(digit) + int(digits))'''

'''height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight: "))

bmi = round(weight / height ** 2)
print(f"Your weight and height are {weight}, {height} respectively and your bmi is {bmi}")'''

current_age = int(input("Enter your current age: "))
total_m = (90 * 12) - (current_age * 12)
total_d = (365 * 90) - (current_age * 365)
total_w = (52 * 90) - (current_age * 52)
print(f"you are left with {total_d} days, {total_w} weeks and {total_m} months")
