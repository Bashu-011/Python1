'''def greet():
    print("How are you?")
    print("Nice to meet you")

# arguments is the data inputted to a function
# parameters is the name of the data and it is reused in the fn

def greetings(name, location):   # name is a parameter
    print(f"How are you {name}")
    print(f"Nice meeting you {name}")
    print(f"You are from {location}")
greetings(location = "Nairobi", name = "John" ) # John is an argument'''

n = int(input("Enter a number that you want to check: "))

def prime_number(n):
    if_prime = True
    for i in range (2, n):
        if n % i == 0:
            if_prime = False
    if if_prime == True:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")

prime_number(n)

