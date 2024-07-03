x = 'james' #global

def greetings ():
    x = 'Alex' #local
    print(x)
greetings()
print(x)

def addition (num1,num2):
    return num1+num2
def subtraction (num1,num2):
    return num1-num2
    
    
answer = addition(2,1)
print(answer)
answer = subtraction(2,1)
print(answer)
count = 10 #global variable

# def outer_function():
#     count = 5  # Local variable within outer_function
#     for _ in range (5):
#         count+=1

#     def inner_function():
#         count = 2  # Local variable within inner_function
#         print(f"Inner function: {count}")  # Accesses local count (2)

#     inner_function()
# print(f"Outer function: {count}")  # Accesses local count (5)

# print(f"Global scope: {count}")  # Accesses global count (10)

# outer_function()

def counting_outer ():
    global count #the global variable is converting into an enclosing variable
    count = 2 #enclosing variable scope
    for _ in range (4):
        count+=1
    print(count)
    def counting_inner():
        count = 2 #local variable scope
        for _ in range (4):
            count+=2
        print(count)
    counting_inner()
counting_outer()
print(count)