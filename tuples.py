# #1. Create Tuple
# numbers = (10, 20, 30, 40, 50)

# print("Tuple:", numbers)

# #2. Access Tuple Elements
# fruits = ("Apple", "Banana", "Mango", "Orange")

# print("First Element:", fruits[0])
# print("Last Element:", fruits[-1])

# #3. Count Elements
# numbers = (10, 20, 30, 20, 40, 20)

# count = numbers.count(20)

# print("20 appears", count, "times")

# #4. Find Index of an Element
# fruits = ("Apple", "Banana", "Mango", "Orange")

# index = fruits.index("Mango")

# print("Index of Mango:", index)

# #5. Convert Tuple to List
# numbers = (10, 20, 30, 40)

# numbers_list = list(numbers)

# print("Tuple:", numbers)
# print("List:", numbers_list)

# #6. Find Maximum Element
# numbers = (45, 12, 89, 67, 23)

# maximum = max(numbers)

# print("Maximum Element:", maximum)

# #7. Find Minimum Element
# numbers = (45, 12, 89, 67, 23)

# minimum = min(numbers)

# print("Minimum Element:", minimum)

# #8. Sum of Elements
# numbers = (10, 20, 30, 40, 50)

# total = sum(numbers)

# print("Sum =", total)

# #9. Concatenate Two Tuples
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)

# result = tuple1 + tuple2

# print("Combined Tuple:", result)

#10. Nested Tuple
students = (
    ("Alina", 85),
    ("Ritika", 90),
    ("Khushi", 88)
)

for student in students:
    print("Name:", student[0], "| Marks:", student[1])