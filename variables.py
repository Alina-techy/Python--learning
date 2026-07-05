#variable programs
#1. Store and Print Your Name
name = "Alina"
print("My name is:", name)

#2. Store Age and Print It
age= 20
print("I am", age, "years old")

#3. Store Two Numbers and Print Their Sum
x= 20
y= 30
print(f"the sum of {x} and {y} is: {x+y}") 
# or you can write
num1= 20
num2=30
sum= num1+num2
print("Enter the 1st number:", num1)
print("Enter the 2nd number", num2)
print("The sum of 2 numbers is:", sum)

#4. Swap Two Variables (Using Third Variable)
a=10
b=20
print("before swapping")
print("a=",a)
print("b=",b)

temp= a
a=b
b=temp

print("after swapping")
print("a=",b)
print("b=",a)

#5. Swap Two Variables (Without Third Variable)
a=39
b=28
print("before swapping")
print("a=",a)
print("b=",b)

a,b=b,a

print("after swapping")
print("a=",b)
print("b=",a)

# 6. Calculate Area of Rectangle
length= 10
breadth= 20
area= length * breadth
print("length=", length)
print("breadth=", breadth)
print("the area of rectangle is:",area)

#7. Calculate Area of Circle
radius= 7
pi= 3.14 
area= pi * radius * radius
print("radius=" ,radius)
print("the area of circle :" ,area) 

#8. Convert Celsius to Fahrenheit
celsius= 32
fahrenheit= (celsius * 9/5) + 32
print("celsius=" , celsius)
print("farenheit=", fahrenheit)

#9. Convert Kilometers to Miles
kilometers= 10
miles= kilometers * 0.621371
print("kilometers=", kilometers)
print("miles=", miles)

#10. Calculate Simple Interest
principal= 100
rate= 8
time= 3
simple_interest= (principal*rate*time/100)
print("principal:", principal)
print("rate:", rate)
print("time:", time)
print("simple interest:", simple_interest)