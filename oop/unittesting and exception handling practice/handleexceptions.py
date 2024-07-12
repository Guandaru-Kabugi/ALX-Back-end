import random
#imported a random module
#Generated a random number
number = random.randint(1,100)
print(number)

#created a custom error class
class FloatError(Exception):
    def __init__(self, number):
        self.number = number
    def __str__(self) -> str:
        return f"You entered {self.number}, which is a float. You need to enter a number without decimals"
 #created a function for handling the user input   
def input_number(guess):
    if isinstance(guess, str):
        raise ValueError
    elif isinstance (guess, float):
        raise FloatError(guess)
    
    if guess > number:
        return f"{guess} is too high"
    elif guess < number:
        return f"{guess} is too low"
    elif guess == number:
        print("Well done on your guess")
        return f"{guess} matches {number}" 
#executed the code here
try:
    #first, we try the user input as a string and is flagged by the first if statement in the function.
    user_input = input("Guess a number between 1 and 100: ")
    try:
        #we then try out the int input and then if its correct, we focus on printing answer
        guess = int(user_input)
        answer = input_number(guess)
        print(answer)
    except ValueError:
        #else, we except the value error which is flagged by the second elif.
        try:
            #we then test if it is a float and we raise the custom error
            guess = float(user_input)
            raise FloatError(guess)
        except ValueError:
            raise ValueError ("You must enter an integer")
    # else:
        # answer = input_number(guess)
        # print(answer)
#here, we except both floaterror and valuerror.
except FloatError as e:
    print(e)
except ValueError as e:
    print(e)