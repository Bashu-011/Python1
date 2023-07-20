a = int(input("Enter a number:"))
b = input("Enter the mathematical sign:")
c = int(input("Enter another number:"))

if b == "+" :
    print(a + c)
elif b == "-":
    print(a-c)
elif b == "*":
    print(a*c)
elif b == "/":
    print(a/c)
else:
    print("This is a syntax error")

    
