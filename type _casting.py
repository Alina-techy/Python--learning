#type casting programs
#1. String to Integer
number= "100"

print("before conversion:")
print(number)
print(type(number))

number= int(number)

print("\nafter conversion")
print(number)
print(type(number))

#2. Integer to String
age= 10

print("before conversion:")
print(age)
print(type(age))

age=str(age)

print("\nafter conversion")
print(age)
print(type(age))

#3. Float to Integer
price = 99.99

print("Before Conversion:")
print(price)
print(type(price))

price = int(price)

print("\nAfter Conversion:")
print(price)
print(type(price))

#4. Integer to Float
marks = 85

print("Before Conversion:")
print(marks)
print(type(marks))

marks = float(marks)

print("\nAfter Conversion:")
print(marks)
print(type(marks))

#5. Boolean to Integer
a= True
b= False

print("True=", int(a))
print("False=", int(b))

#6. Integer to Boolean
a= 1
b= 0

print("1=", bool(a))
print("0=", bool(b))

#7. Convert User Input into Integer
num= input("Enter a number:")

print("Before conversion:")
print(type(num))

num=int(num)

print("\nAfter conversion:")
print(num)
print(type(num)) 

#8. Add Two Numbers Taken as Strings
num1= input("Enter 1st number: ")
num2= input("Enter 2nd number: ")

sum= int(num1)+int(num2)

print("Sum=", sum)

#9. Convert List into Tuple
students= ["alina", "ritika", "khushi"]

print("Before conversion: ")
print(students)
print(type(students))

students= tuple(students)

print("\nAfter conversion:")
print(students)
print(type(students))

#10. Convert Tuple into List
fruits=("mango","apple","orange")

print("Before conversion:")
print(fruits)
print(type(fruits))

fruits=list(fruits)

print("\nAfter conversion: ")
print(fruits)
print(type(fruits))