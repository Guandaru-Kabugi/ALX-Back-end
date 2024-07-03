def user_info(name, age=None):
    """Prints user information."""
    print(f"Name: {name}")
    if age:
        print(f"Age: {age}")
user_info(name="Bob")

# Function definition with default value
def greet(name="World"):
     """Prints a greeting message."""
     print(f"Hello, {name}!")
greet()  # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice! 

def square(number):
 """Returns the square of a number."""
 return number * number
squared_value = square(4)  # squared_value will be 16
print(squared_value)

count = 0  # Global variable
def increment():
    count += 1  # This refers to the local count within the function
    increment()
print(count)  # Output: 0 (Global count remains unchanged)

count = 0
def increment_global():
  global count
  count += 1
increment_global()
print(count)  # Output: 1 (Global count is modified)

def outer_function():
    x = 10  # Variable in the enclosing function

    def inner_function():
        nonlocal x  # Using nonlocal to modify x from the enclosing function
        x += 5  # Modifying the value of x

    inner_function()  # Calling the nested function
    print("Modified value of x from inner function:", x)
outer_function()