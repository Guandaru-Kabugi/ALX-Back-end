#created first method
def methodaddition(another):
    return another() #here we are calling a method for the argument passed
def addition ():
    return 2+3

print(methodaddition(addition)) #we wont add the usual two brackets because we already have a return for that
#we can also have lambda functions or annonymous functions
#for example
print(methodaddition(lambda: 2+3))

#using filter function
my_list = [34,13,45,89,24,62,100]

print (list(filter(lambda x: x!=13, my_list)))

#another way to use lambda function

print((lambda x: x * 3)(5))# the first part before colon present function name second part represents the operation and the 5 in bracket is the argument passed for x
