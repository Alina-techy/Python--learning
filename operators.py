#arithmetic operators
#1. Calculator
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)

#2. Square of a Number
number = int(input("Enter a Number: "))

square = number * number

print("Square =", square)

#3. Cube of a number
number = int(input("Enter a Number: "))

cube = number ** 3

print("Cube =", cube)

#4. Modulus
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

remainder = num1 % num2

print("Remainder =", remainder)

#5. Exponent
base = int(input("Enter Base: "))
power = int(input("Enter Power: "))

result = base ** power

print("Answer =", result)

#Comparison Operators
#6. Largest Number
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

if(a>b):
    print("Largest is=", a)
else:
    print("Largest is=",b)
    
#7. Smallest Number
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

if(a<b):
    print("Smallest is=", a)
else:
    print("Smallest is=",b)
    
#8. Equal Numbers
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

if a == b:
    print("Both numbers are Equal")
else:
    print("Numbers are Not Equal")
    
#9. Positive or Negative
number = int(input("Enter a Number: "))

if number >= 0:
    print("Positive Number")
else:
    print("Negative Number")
    
#10. Voting Eligibility
age= int(input("Enter your age:"))

if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    
#Logical Operators
#11. Login System
username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "alina" and password == "7777":
    print("Login Successful")
else:
    print("Invalid Username or Password")

# 12. Age Verification
age=int(input("Enter your age:"))

if age>=18 and age<=60:
    print("Valid age")
else:
    print("Invalid age")
    
# 13. Grade Eligibility
marks= int(input("Enter your marks:"))

if marks>=40 and marks<=100:
    print("PASS")
else:
    print("FAIL")

#14. Admission Eligibility
marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 75:
    print("Admission Granted")
else:
    print("Admission Denied")
    
#15. Scholarship Eligibility
percentage = float(input("Enter Percentage: "))
income = int(input("Enter Family Income: "))

if percentage >= 85 and income < 300000:
    print("Eligible for Scholarship")
else:
    print("Not Eligible")
    
# Assignment Operators
#16.+= Example
x = 10

x += 5

print(x)

#17. -= Example
x = 20

x -= 8

print(x)

#18. *= Example
x = 5

x *= 4

print(x)

#19. /= Example
x = 50

x /= 5

print(x)

#20. %= Example
x = 17

x %= 5

print(x)

# Membership Operators
#21. Find Character in String
text= input("Enter a string:")
character= input("Enter a character:")

if character in text:
    print("Character found")
else:
    print("Character not found")
    
#22. Find Item in List
fruits = ["Apple", "Banana", "Mango", "Orange"]

item = input("Enter Fruit Name: ").capitalize() #Capitalize works for: apple, aPPLE, Apple

if item in fruits:
    print("Item Found")
else:
    print("Item Not Found")

#Identity Operators
#23. Compare Two Lists Using is
list1 = [1, 2, 3]
list2 = list1

print(list1 is list2)

#24. Compare Strings
str1 = "Python"
str2 = "Python"

print(str1 is str2)
print(str1 == str2)

# 25. Compare Objects
list1 = [10, 20]
list2 = [10, 20]

print("Using ==")
print(list1 == list2)

print("\nUsing is")
print(list1 is list2)
