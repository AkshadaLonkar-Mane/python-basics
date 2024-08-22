# 1. List Comprehensions with Conditional Logic
#List comprehensions provide a concise way to create lists. You can also add conditions to filter items.

# Creating list forsquares for even numbers only:
even_sq = [x ** 2 for x in range(10) if x % 2 == 0]
print("Even Squares: ", even_sq) 

# Flattening a nested list:
nested_list = [[1, 2,3], ['A', 'B', 'C'], [7, 8, 9]]
flattened_list = [item for sublist in nested_list for item in sublist]
print("Flattening list: ", flattened_list)

# Output:
"""
Even Squares:  [0, 4, 16, 36, 64]
Flattening list:  [1, 2, 3, 'A', 'B', 'C', 7, 8, 9]
"""


# 2. Zipping and Unzipping Lists and Tuples
# You can combine and separate multiple lists or tuples using zip and unzip.

# Zipping two list:
name = ["Sam", "John", "Doe"]
scores = [90, 85, 75]
zipped = list(zip(name, scores))
print('Zipped List = ', zipped)

# Unzipping List:
unzipped_name, unzipped_scores = zip(*zipped)
print('Unzipped name = ', unzipped_name)
print('Unzipped scores = ', unzipped_scores)

# Output: 
"""
Zipped List =  [('Sam', 90), ('John', 85), ('Doe', 75)]
Unzipped name =  ('Sam', 'John', 'Doe')
Unzipped scores =  (90, 85, 75)
"""


# 3. List and Tuple Slicing with Steps
# Advanced slicing allows you to retrieve elements with specific intervals.

# List slicing:
numbers = list(range(10))
even_numbers = numbers[::2]     # every 2nd element 
reverse_numbers = numbers[::-1] # Reversing the list

print("Even numbers:", even_numbers)
print("Reversed numbers:", reverse_numbers)

# Tuple slicing
tuple_data = (1, 2, 3, 4, 5, 6)
subset = tuple_data[1:5:2]  # Slicing from index 1 to 4 with a step of 2
print("Tuple subset:", subset)

# Output: 
"""
Even numbers: [0, 2, 4, 6, 8]
Reversed numbers: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
Tuple subset: (2, 4)
"""