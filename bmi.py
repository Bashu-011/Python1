def bmi_calculator(name, height, weight):
    bmi = weight / (height ** 2)
    x = str(bmi)
    print("bmi:" + x)
    if bmi < 15:
        return name + " is underweight"
    elif 15 <= bmi <= 25:
        return name + " is within normal"
    else:
        return name + " is overweight"
    
a = input("Enter your name: ")
b = float(input("Enter your height: "))
c = int(input("Enter your weight: "))

result = bmi_calculator(a, b, c)
print(result)