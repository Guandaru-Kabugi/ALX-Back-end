def greetings ():
    print("Hello there. Welcome")
def calculator_instructions ():
    print("In this calculator, operators will be (+, -, *, and /)")
    print("We will ask you to give two numbers and\
    also the operator you want")
def Add (num1, num2):
    return num1 + num2
def subtract (num1, num2):
    return num1 - num2
def multiply (num1, num2):
    return num1 * num2
def divide (num1, num2):
    return num1 / num2

greetings()
calculator_instructions()
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator: ")
if operator == "+":
    results = Add (num1,num2)
    print("The final results: " + str(results))
elif operator == "-":
    results = subtract (num1,num2)
    print("The final results: " + str(results))
elif operator == "*":
    results = multiply (num1,num2)
    print("The final results: " + str(results))
elif operator == "/":
    results = divide (num1,num2)
    print("The final results: " + str(results))
else:
    print("Invalid operator")