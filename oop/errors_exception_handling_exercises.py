#exercise 1: Handling zerodivisionerror

def division (x,y):
    if x == 0 or y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x/y
try:
    answer = division(3,0)
    print(answer)
except ZeroDivisionError as e:
    print(e)
    
# exercise 2:  File Handling with FileNotFoundError
# try:
#     file = open('./oop/oop lesson 1.py')
# except FileNotFoundError:
#     print("The file name is not present")
# else:
#     print(file.read())
#     file.close()

# exercise 3: customexception
# class ValueTooHighError(Exception):
#     def __init__(self, number):
#         self.no = number
        
#     def __str__(self) -> str:
#         return f"The number, {self.no}, is too high "
# guess = int(input("Guess a number: "))
# def number_taking (number):
#     if number > 100:
#         raise ValueTooHighError(number)
#     else:
#       print("Well done on your choice!")  
# try:
#     number_taking(guess)
# except ValueTooHighError as e:
#     print(e)


class ValueTooHighError(Exception):
    def __init__(self, number):
        self.no = number
        
    def __str__(self) -> str:
        return f"The number, {self.no}, is too high "

try:
    guess = int(input("Guess a number: "))
    if guess > 100:
        raise ValueTooHighError(guess)
except ValueTooHighError as e:
    print (e)
else:
    print("well done on your effort") 