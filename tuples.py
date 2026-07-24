#1. Create Tuple
numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)

#2. Access Tuple Elements
fruits = ("Apple", "Banana", "Mango", "Orange")

print("First Element:", fruits[0])
print("Last Element:", fruits[-1])

#3. Count Elements
numbers = (10, 20, 30, 20, 40, 20)

count = numbers.count(20)

print("20 appears", count, "times")

#4. Find Index of an Element
fruits = ("Apple", "Banana", "Mango", "Orange")

index = fruits.index("Mango")

print("Index of Mango:", index)

#5. Convert Tuple to List
numbers = (10, 20, 30, 40)

numbers_list = list(numbers)

print("Tuple:", numbers)
print("List:", numbers_list)

#6. Find Maximum Element
numbers = (45, 12, 89, 67, 23)

maximum = max(numbers)

print("Maximum Element:", maximum)

#7. Find Minimum Element
numbers = (45, 12, 89, 67, 23)

minimum = min(numbers)

print("Minimum Element:", minimum)

#8. Sum of Elements
numbers = (10, 20, 30, 40, 50)

total = sum(numbers)

print("Sum =", total)

#9. Concatenate Two Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print("Combined Tuple:", result)

#10. Nested Tuple
students = (
    ("Alina", 85),
    ("Ritika", 90),
    ("Khushi", 88)
)

for student in students:
    print("Name:", student[0], "| Marks:", student[1])
    
#11. Reverse a Tuple
numbers = (10, 20, 30, 40, 50)

reversed_tuple = numbers[::-1]

print("Original Tuple:", numbers)
print("Reversed Tuple:", reversed_tuple)

#12. Sort a Tuple
numbers = (40, 10, 30, 20, 50)

sorted_tuple = tuple(sorted(numbers))

print("Sorted Tuple:", sorted_tuple)

#13. Tuple Unpacking
student = ("Alina", 20, "BCA")

name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)

#14. Check Element Exists
fruits= ("Apple","Mango","Banana")

item= input("Enter fruit: ")

if item in fruits:
    print("Found")
else:
    print("Not  Found")
    
#15. Find Average of Tuple Elements
numbers = (10, 20, 30, 40, 50)

average = sum(numbers) / len(numbers)

print("Average =", average)

#16. Remove Duplicates from a Tuple
numbers = (10, 20, 30, 20, 40, 10, 50)

unique = tuple(set(numbers))

print("Original Tuple:", numbers)
print("Tuple After Removing Duplicates:", unique)