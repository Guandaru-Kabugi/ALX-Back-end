#introduction to decorators

import functools #we first import the decorator


def my_decorator(pass_function_here): #we then create a function where we will pass our code
    @functools.wraps(pass_function_here) #we call the decorator first and pass in the method wraps
    def enclose_function():
        print("The start of the decoration") #here we can say what we want to happen before the functioon
        pass_function_here() #here we pass our function
        print("End of decoration.") #here we can say what will be printed after the function
    
    return enclose_function #here we call the wrapping function. Do not use parenthesis
    
@my_decorator #here we call our decorator
def This_function (): # we then create a function that will be passed in the decorator
    print("Trial function")
This_function()        