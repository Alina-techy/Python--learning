#input and output programs
#1. Take Name as Input
name= input("What is your name? ")
print("Nice name",name )

#2. Take Age as Input
age= int(input("How old are you?"))
print(f"Oh.. you are {age} years old")

#3. Add Two Numbers Entered by User
num1= int(input("Enter number one:"))
num2= int(input("Enter number two:"))

sum= num1+num2

print("The sum of two numbers is:", sum)

#4. Calculate Average of Three Numbers
num1= int(input("Enter 1st number:"))
num2= int(input("Enter 2nd number:"))
num3= int(input("Enter 3rd number:"))

average= (num1+num2+num3/3)

print("The average of three numbers is:", average)

#5. Display Full Address
name= input("Enter name:")
house= input("Enter house number:")
city= input("City name:")
state= input("State:")
country= input("Country:")

print("------Adress-------")
print("Name:", name)
print("House:", house)
print("City:", city)
print("State:", state)
print("Country:", country)

#6. Calculate BMI
weight= float(input("Enter your weight: "))
height= float(input("Enter your height: "))

bmi= (weight/(height*height))

print("BMI:", bmi)

#7. Calculate Percentage
obtained= float(input("Enter obtained marks: "))
total= float(input("Enter total marks: "))

percentage= (obtained/total)*100

print(f"Percetage: {percentage} %")

#8. Area of Square
side= float(input("Enter the side of square: "))

area= (side*side)

print("The area of square is:", area)

#9. Area of Triangle
base= float(input("Enter base:"))
height=float(input("Enter height:"))

area= (1/2*base*height)

# print("Area of triangle is:", area)

#10. Display Formatted Output Using f-string
name= input("Enter your name:")
age= int(input("Enter your age: "))
height= float(input("Enter your height:"))

print(f"{name} is such a nice name")
print(f"ohh you are {age} years old")
print(f"{height} is not bad")
#or 
name= input("Enter your name:")
print(f"{name} is such a nice name")
age= int(input("Enter your age: "))
print(f"ohh you are {age} years old")
height= float(input("Enter your height:"))
print(f"{height} is not bad")


