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

#======================================================================


#Combining *args and **kwargs

def all_argument(title, *args, **kwargs):
    print("Title: ", title)
    print("Positional arguments: ", args)
    print("Keyword arguments: ", kwargs)

all_argument("User Info", "Tom", "Tobias", age = 25, city = "Dhaka")