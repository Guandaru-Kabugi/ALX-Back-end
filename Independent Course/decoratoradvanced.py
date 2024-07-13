import functools

def mydecorator (func):
    @functools.wraps(func)
    def wrapfunctionhere():
        print("Here is the start")
        func()
        print("Here is the end")
    return wrapfunctionhere

@mydecorator
def my_function ():
    print("This is my function")
    
my_function()


def decorator_with_arguments(number):
    def my_decorator (function):
        @functools.wraps(function)
        def wrapfunction (*args, **kwargs):
            print("The start")
            if number ==60:
                print ("You guessed the right number")
            else:
                function(*args, **kwargs)
            print("The end")
        return wrapfunction
    return my_decorator

@decorator_with_arguments(90)
def my_function_2(x, y):
    print("Hi there")
    print (x + y)
my_function_2(10, 40)