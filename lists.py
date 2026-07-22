# #lists programs
# #1. Create list
# colors= ["black","red","purple","brown"]

# print(colors)
# print(type(colors))

# #2. Append
# colors= ["black","red","purple","brown"]
# colors.append("pink")

# print(colors)

# #3. Insert
# colors= ["black","red","purple","brown"]
# colors.insert(1,"pink")

# print(colors)

# #4. Remove
# colors= ["black","red","purple","brown"]
# colors.remove("purple")

# print(colors)

# #5. Pop
# colors= ["black","red","purple","brown"]
# shade=colors.pop()

# print("removed: ", shade)
# print(colors)

# #6. Sort
# numbers= [2,4,1,9,3,7]
# numbers.sort()

# print(numbers)

# #7. Reverse
# numbers= [2,4,1,9,3,7]
# numbers.reverse()

# print(numbers)

# #8. Find Maximum
# numbers= [2,4,1,9,3,7]

# print(max(numbers))

# #9. Find Minimum
# numbers= [2,4,1,9,3,7]

# print(min(numbers))

# #10. Sum of list
# numbers= [2,4,1,9,3,7]

# print(sum(numbers))

# # 11. Average 
# num= [1,2,3,4,5]

# average= sum(num)/len(num)
# print(average)

# #12. Second Largest
# numbers = [12, 45, 78, 23, 56]

# numbers.sort()

# print("Second Largest:", numbers[-2])

# #13. Second Smallest
# numbers = [12, 45, 78, 23, 56]

# numbers.sort()

# print("Second smallest", numbers[1])

# #14. Remove Duplicates
# numbers = [1, 2, 2, 3, 4, 4, 5]

# unique = list(set(numbers))

# print(unique)

# #15. Merge Lists
# list1= [1,2,3]
# list2= [4,5,6]

# list3= list1+list2

# print(list3)

# #16. Copy List
# list1 = [10, 20, 30]

# list2 = list1.copy()

# print(list2)

# #17. Count Frequency
# number= [1,1,2,3,2,4,4]

# item= int(input("Enter your number: " ))

# print("Frequency: ", number.count(item))

# #18. Search Element
# number= [1,2,3,4,5,6]

# item= int(input("Enter a number: "))

# if item in number:
#     print("Found")
# else:
#     print("Not Found")
    
# #19. List Comprehension
# numbers = [1, 2, 3, 4, 5]

# square = [i*i for i in numbers]

# print(square)

# #20. Even Numbers
# numbers= [1,2,3,4,5,6,7,8,9,10]

# even= [i for i in numbers if i % 2==0]

# print(even)

# #21. Odd Numbers
# numbers= [1,2,3,4,5,6,7,8,9,10]

# odd= [i for i in numbers if i % 2 !=0]

# print(odd)

# # 22. Prime Numbers
# numbers = [2,3,4,5,6,7,8,9,10,11]

# for num in numbers:
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

# # 23. Square Numbers
# numbers = [1,2,3,4,5]

# square = [i**2 for i in numbers]

# print(square)

# #24. Cube Numbers
# numbers = [1,2,3,4,5]

# cube= [i**3 for i in numbers]

# print(cube)

# # 25. Nested List
# students = [
#     ["Alina", 85],
#     ["Ritika", 90],
#     ["Khushi", 78]
# ]

# print(students)

#26. Matrix Addition
A = [[1,2],
     [3,4]]

B = [[5,6],
     [7,8]]

result = [[0,0],[0,0]]

for i in range(2):
    for j in range(2):
        result[i][j]= A[i][j] + B[i][j]

print(result)

#27. Matrix Multiplication 
A = [[1,2],
     [3,4]]

B = [[5,6],
     [7,8]]

result = [[0,0],[0,0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += A[i][k] * B[k][j]

print(result)

#28. Rotate List
numbers = [1,2,3,4,5]

k = 2

rotated = numbers[-k:] + numbers[:-k]

print(rotated)

#29. Shuffle List
import random

numbers = [1,2,3,4,5]

random.shuffle(numbers)

print(numbers)

#30. Find Common Elements
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

common = []

for i in list1:
    if i in list2:
        common.append(i)

print(common)