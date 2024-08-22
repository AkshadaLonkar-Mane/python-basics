# 1. Nested Loops
# Demonstrates the use of nested loops.

# Creating a multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:2}", end=" ")
    print()

# Output:
"""
 1  2  3  4  5 
 2  4  6  8 10
 3  6  9 12 15
 4  8 12 16 20
 5 10 15 20 25
"""


# 2. Loop Control Statements (break, continue, else)
# Using break, continue, and else in loops.

# Finding the first even number in a list using break
numbers = [1, 3, 5, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break
else:
    print("No even number found.")

# Skipping odd numbers using continue
for num in range(10):
    if num % 2 != 0:
        continue
    print(f"Even number: {num}")

# Output:
"""
First even number found: 8
Even number: 0
Even number: 2
Even number: 4
Even number: 6
Even number: 8
"""

#  3. Looping Over Multiple Iterables with zip
# Looping over multiple iterables simultaneously using zip.

names = ["Alisha", "Rohit", "Sneha"]
ages = [25, 30, 22]
cities = ["Nashville", "Dallas", "Edison"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}.")

# Output:
"""
Alisha is 25 years old and lives in Nashville.
Rohit is 30 years old and lives in Dallas.
Sneha is 22 years old and lives in Edison.
"""


# 4. List Comprehensions with Loops
# Using list comprehensions for concise loops.

# Creating a list of squares using a loop
squares = []
for x in range(10):
    squares.append(x**2)
print("Squares using loop:", squares)

# Creating a list of squares using list comprehension
squares_comprehension = [x**2 for x in range(10)]
print("Squares using comprehension:", squares_comprehension)

# Creating a list of even squares using list comprehension with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even Squares:", even_squares)

# Output:
"""
Squares using loop: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Squares using comprehension: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Even Squares: [0, 4, 16, 36, 64]

"""

# 5. Looping Over Dictionaries
# Iterating over dictionary keys, values, and items.

person = {
    "name": "Alisha",
    "age": 25,
    "city": "Nashville",
    "profession": "Python Developer"
}

# Looping over keys
for key in person:
    print(f"Key: {key}")

# Looping over values
for value in person.values():
    print(f"Value: {value}")

# Looping over items (key-value pairs)
for key, value in person.items():
    print(f"{key}: {value}")

# Output:
"""
Key: name
Key: age
Key: city
Key: profession
Value: Alisha
Value: 25
Value: Nashville
Value: Python Developer
name: Alisha
age: 25
city: Nashville
profession: Python Developer
"""


# 8. Recursive Loops with Function Calls
# Using recursion as an alternative to loops.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the recursive function
print("Factorial of 5:", factorial(5))

def countdown(n):
    if n <= 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n-1)

# Test the recursive countdown
countdown(5)

# Output:
"""
Factorial of 5: 120
5
4
3
2
1
Blast off!
"""