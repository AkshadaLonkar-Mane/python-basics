# conditional_statements.py
# Demonstrates the use of if, elif, and else for decision-making.


# 1. Simple Conditional statement
x = 20

if x > 30:
    print("x is greater than 30")
elif x == 20:
    print("x is equal to 20")
else:
    print("x is less than 20")




# 2. Conditional Statements with Logical Operators
# logical_operators.py
# Using logical operators (and, or, not) in conditional statements.

temperature = 30
humidity = 70

if temperature > 25 and humidity > 60:
    print("It's hot and humid.")
elif temperature > 25 and humidity <= 60:
    print("It's hot but not humid.")
elif temperature <= 25 and humidity > 60:
    print("It's cool and humid.")
else:
    print("It's cool and not humid.")

# Using the 'not' operator
rainy = False

if not rainy:
    print("It is not raining today.")
else:
    print("It is raining today.")



# 3. Complex Conditions with Multiple Checks
# complex_conditions.py
# Checking multiple conditions in one statement.

grade = 85

if grade >= 90:
    print("You got an A!")
elif 80 <= grade < 90:
    print("You got a B!")
elif 70 <= grade < 80:
    print("You got a C.")
elif 60 <= grade < 70:
    print("You got a D.")
else:
    print("You got an F.")

    

# 4. Conditional Statements in Function Definitions
# conditional_in_function.py
# Using conditional statements within functions.

def categorize_age(age):
    if age < 13:
        return "Child"
    elif 13 <= age < 20:
        return "Teenager"
    elif 20 <= age < 60:
        return "Adult"
    else:
        return "Senior"

# Test the function with different age values
ages = [10, 15, 30, 65]
categories = [categorize_age(age) for age in ages]
print(categories)  




# Output:
"""
x is equal to 20
It's hot and humid.
It is not raining today.
You got a B!
['Child', 'Teenager', 'Adult', 'Senior']
"""
