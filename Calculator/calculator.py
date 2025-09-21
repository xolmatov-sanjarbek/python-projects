def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    if number2 == 0:
        return "Division by zero is not possible"
    return number1 / number2

while True:
    
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    sign = input("Which operation would you like to do? (+, -, *, /) or q to quit: ")

    if sign == "+":
        print(add(number1, number2))

    elif sign == "-":
        print(subtract(number1, number2))

    elif sign == "*":
        print(multiply(number1, number2))

    elif sign == "/":
        print(divide(number1, number2))

    elif sign == "q":
        break

    else:
        print("Invalid value!")