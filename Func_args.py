"""
*args → Accepts multiple positional arguments  ----tuple
**kwargs → Accepts multiple keyword arguments  -----dictionary

By default, a function must be called with the correct number of arguments.
However, sometimes you may not know how many arguments that will be passed into your function.
*args and **kwargs allow functions to accept an unknown number of arguments.

1) *args
2) **kwargs
3) Unpacking with * and **
4) Function parameter order
5) Lambda function
"""

"""
There are two types of arguments:
1) Positional argument ------ student("Riyad", 22)
2) Keyword argument -------  student(name="Riyad", age=22)

"""


#*args
#==================
"""
              *args
                │
       ┌────────┴─────────┐
       ↓        ↓         ↓
      10       20        30
       └────────┬─────────┘
                ↓
        args = (10, 20, 30)
                │
              tuple
"""


def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

#==================================================================


def my_function(greeting, *names):
    for name in names:
        print(greeting, name)

my_function("Hello", "python", "java", "C++")

#======================================================================



def my_argument(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(my_argument(1, 2, 3, 4, 5))
print(my_argument(10, 20, 30))


#======================================================================

#Finding the maximum value

def max_number(*numbers):
    if len(numbers) == 0:
        return None

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

result = max_number(3, 7, 2, 9, 1)
print("Maximum num is: ",result)





#======================================================================


#**kwargs
#-----------------
"""
                 **kwargs
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
    name=Riyad    age=22     department=CST
        └────────────┼────────────┘
                     ↓
              kwargs = {
                  "name": "Riyad",
                  "age": 22,
                  "department": "CST"
              }
                     │
                  dictionary
"""


def my_func(**kid):
    print("His last name is ", kid["lname"])

my_func(fname = "Tom", lname = "Lucy")

#======================================================================


def my_function(**myvar):
    print("Type: ", type(myvar))
    print("Name: ", myvar["name"])
    print("Age: ", myvar["age"])
    print("all data: ", myvar)

my_function(name = "Tom", age = 10, city = "Bergen")

#======================================================================


#Using **kwargs with Regular Arguments

def my_function(username, **details):
    print("Username: ", username)
    print("Additional details: ")
    for key, value in details.items():
        print("", key, ":", value)

my_function("Tom", age = 25, city = "Dhaka", hobby = "Programming")

#=============================================================================


#Combining *args and **kwargs

def all_argument(title, *args, **kwargs):
    print("Title: ", title)
    print("Positional arguments: ", args)
    print("Keyword arguments: ", kwargs)

all_argument("User Info", "Tom", "Tobias", age = 25, city = "Dhaka")

#================================================================================

#Unpacking Arguments

#Unpacking Lists with *

def positional_argument(a, b, c):
    return a, b, c

my_list = [2, 5, 10]
result = positional_argument(*my_list)
print(result)



#Unpacking Dictionaries with **

def keyword_argument(name, age):
    print(f"{name} - {age}")

person = {
    "name" : "python",
    "age" : 45
}

keyword_argument(**person)



#================================================================================

#Lambda Function
"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

syntax: function_name = lambda arguments : expression
------

The expression is executed and the result is returned.
"""

x = lambda num1, num2: num1 * num2
print(x(4, 5))

#---------------------------------------------------------------------------------------------------

"""
Why Use Lambda Functions?
----------------------------

The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument,
and that argument will be multiplied with an unknown number:
"""

def my_func(x):
    return lambda a : a * x

doubler = my_func(2) #The argument of 'x'
tripler = my_func(3)

print(doubler(10)) #The argument of 'a'
print(tripler(20))


#---------------------------------------------------------------------------------------------------


"""
Lambda with Built-in Functions
--------------------------------

Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().
"""

#Using Lambda with map()
#The map() function applies a function to every item in an iterable:

numbers = [1, 2, 3, 4, 5]

double = list(map(lambda x: x * 2, numbers))
print(double)



#--------------------------------------------------------------------------

#Using Lambda with filter()
#The filter() function creates a list of items for which a function returns True:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


#--------------------------------------------------------------------------

#Using Lambda with sorted()
#The sorted() function can use a lambda as a key for custom sorting.

#Sort a list of tuples by the second element:

students = [("Emil", 20), ("Tobias", 25), ("Linus", 21)]

sorted_students = sorted(students, key=lambda x: x,  reverse=True)
print(sorted_students)


#--------------------------------------------------------------------------

#Sort strings by length:
words = ['banana', 'orange', 'apple', 'cherry', 'coco', 'pie']

sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#--------------------------------------------------------------------------



#Condition Checking

check = lambda x : "Positive" if x > 0 else "Negative" if x < 0 else "Zereo"
print(check(5))
print(check(-5))
print(check(0))