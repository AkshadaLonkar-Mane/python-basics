
# 1. Function with Default Arguments

def greet(name, greeting = 'Hello'):    # funtion to greet a perdon with default greeting
    return f"{greeting}, {name}!"

# calling the funtion:
print(greet ('Atharva'))

# Output: Hello, Atharva!



# 2. Function with Variable-Length Arguments

#Function to print any number of positional and keyword arguments
def arguments(*args, **kwargs):
    print("positional argument:", args)
    print('keyword argumnets:', kwargs)

# Calling the funtion:
arguments(1, 2, 3, name = 'Atharva', age = '10')

# Output: 
"""
positional argument: (1, 2, 3)
keyword argumnets: {'name': 'Atharva', 'age': '10'}
 """


# 3. Lambda Functions

# Lambda funtion to add two numbers:
add = lambda x, y: x +y


# Lambda funtion to check if number is even or odd:
is_even = lambda x : x%2 == 0

print("Add = ", add(2, 5))
print('x is even: ', is_even(8))
print('x is even: ', is_even(5))

# output:
"""
Add =  7
x is even:  True 
x is even:  False
"""

# 4. Higher-Order Functions: Higher-order functions take other functions as arguments or return functions.

def apply_fun(fun, value):
    return fun(value)

# Funtion to square a number: 
def square(x):
    return x ** 2

# calling apply fun using square:
result = apply_fun(square, 5)
print('square = ', result)

# Output: square =  25


# 6. Functions with Annotations: 
"""Python allows you to add type hints to function parameters and return values,
 improving code readability and helping with debugging."""

def concatenate_strings(a: str, b: str) -> str:
    """Function to concatenate two strings"""
    return a + b

print(concatenate_strings("Hello, ", "Coder!"))

# Output: Hello, Coder!



#7. Closures
# functions_closures.py

def outer_function(x):
    """Outer function that defines a closure"""
    def inner_function(y):
        """Inner function that uses the outer function's variable"""
        return x + y
    return inner_function

# Creating a closure
add_five = outer_function(5)

# Using the closure
print("5 + 10 =", add_five(10))

# Output: 5 + 10 = 15
