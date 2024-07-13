#version 1 args
def long_method(args1, args2):
    return (args1 + args2)
def second_method(args1, args2, arg3, args4):
    return (args1, args2, arg3, args4)
def list_method (listargs):
    return sum(listargs)
second_method(1,2,3,4)
list_method([1,2,3,4])
def simplified(*args):
    return sum(args)
simplified(1,2,2,3,4,4)

#kwargs **
def kwargs_args_understanding(*args, **kwargs):
    print(args)
    print (kwargs)
kwargs_args_understanding(2,3,4,5,6, name= 'kabs', location= 'Kenya')