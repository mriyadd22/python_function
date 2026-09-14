"""
what is decorator?
Decorator is function that takes another function as input and return a new function.
Decorator let you add extra behavior to a function, without changing the function's code.
"""

#Define the decorator first, then apply

def uppercase(func):    #Here, 'func' is the function that we will decorate
    def wrapper():    #It's function that wraps the original function
        return func().upper()
    return wrapper



def capitalize():
    return "python programming "
capitalize = uppercase(capitalize)  #apply decorator

print(capitalize())




# apply decorator by using syntax ----@

@uppercase
def hello():
    return "python programming"

print(hello())

#===============================================================

#Arguments in the Decorated Function

#Functions that require arguments can also be decorated, just make sure you pass the arguments to the wrapper function:

def uppercase(func):
    def wrapper(x):
        return func(x).upper()
    return wrapper



@uppercase
def capitalize(name):
    return name

print(capitalize("python"))


#===============================================================


"""
Sometimes the decorator function has no control over the arguments passed from decorated function,
to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number, 
and any type of arguments, and pass them to the decorated function.
"""


def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper



@uppercase
def my_word(name, age, roll, address):
    return f"{name} {age} {roll} {address}"

result = my_word("python", 23, roll=123456, address="Milky Way")
print(result)



#====================================================================================

"""
Decorator With Arguments

Decorators can accept their own arguments by adding another wrapper level.
"""

#A decorator factory that takes an argument and transforms the casing based on the argument value.

def changecase(n):
    def changecase(func):
        def wrapper():
            if n == 1:
                a = func().lower()
            elif n == 2:
                a = func().upper()
            else:
                a = "required valid number ( 1/2 )"
            return a
        return wrapper
    return changecase



#apply here

@changecase(2)
def my_word():
    return "Python"

print(my_word())


#==================================================================


"""
Function Metadata

Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.
"""

def func_metadata():
    return "Function has metadata"

print(func_metadata.__name__)



"""
But, when a function is decorated, the metadata of the original function is lost.

Try returning the name from a decorated function and you will not get the same result.
"""

def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper


@uppercase
def word():
    return "hello"

print(word.__name__)




"""
To fix this, Python has a built-in function called functools.
wraps that can be used to preserve the original function's name and docstring.
"""

#Import 'functools.wraps' to preserve the original function name and docstring.

from functools import wraps

def uppercase(func):
    @wraps(func)    #used 'wraps' function
    def wrapper():
        result = func().upper()
        return result
    return wrapper


@uppercase
def func_metadata():
    return "python"

print(func_metadata.__name__)