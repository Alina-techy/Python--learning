#if-else programs
#1. Even/Odd
num= int(input("Enter a number: "))

if num % 2==0:
    print("Even")
else:
    print("Odd")
    
#2. Positive/Negative
num= int(input("Enter a number: "))

if num > 0 :
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
    
#3. Largest of two
num1= int(input("Enter 1st number: "))
num2= int(input("Enter 2nd number: "))

if num1 > num2:
    print("1st number is largest")
elif num1 < num2:
    print("2nd number is largest")
else:
    print("Both are equal")
    
#4. Largest of Three
num1= int(input("Enter 1st number: "))
num2= int(input("Enter 2nd number: "))
num3= int(input("Enter 3rd number: "))

if num1 >= num2 and num1 >= num3:
    print(num1, "is largest")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is largest")
else:
    print(num3, "is largest")
    
#5. Leap Year
year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year") 
    
#6. Voting Eligibility
age= int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible")
    
# 7. Grade Calculator
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")
    
#8. Pass/Fail
marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")
    
#9. Divisible by 5
num = int(input("Enter number: "))

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")
    
#10. Divisible by both 5 and 11
num = int(input("Enter number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both")
else:
    print("Not divisible by both")
    
#11. Character Type
ch = input("Enter a character: ")

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")
    
# 12. Alphabet or Not
ch = input("Enter a character: ")

if ch.isalpha():
    print("Alphabet")
else:
    print("Not an alphabet")
    
#13. Vowel or consonant
ch = input("Enter a letter: ").lower()

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")
    
#14. Profit/Loss
cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

if sp>cp:
    print("Profit=", sp-cp)
elif cp>sp:
    print("Loss=", cp-sp)
else:
    print("No profit No loss")
    
# 15. Electricity Bill
units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("Bill =", bill)

# 16. Income Tax
income = float(input("Enter annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30

print("Tax =", tax)

#17. BMI Checker
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

print("BMI =", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
    
#18. ATM PIN
pin = input("Enter PIN: ")

if pin == "1234":
    print("Access Granted")
else:
    print("Wrong PIN")
    
#19. Login System
username = input("Username: ")
password = input("Password: ")

if username == "alina" and password=="2810":
    print("Login Successful")
else:
    print("Invalid Username or Password")
    
#20. Password Checker
password = input("Enter password: ")

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")
    
#21. Triangle Validity
a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")
    
#22. Triangle Type
a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
    
# 23. Calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator (+,-,*,/): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("Answer =", num1 + num2)
elif op == "-":
    print("Answer =", num1 - num2)
elif op == "*":
    print("Answer =", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Answer =", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid Operator")
    
# 24. Discount Calculator
amount = float(input("Enter shopping amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0

print("Discount =", discount)
print("Final Amount =", amount - discount)

# 25. Movie Ticket Eligibility
age = int(input("Enter age: "))

if age >= 18:
    print("Allowed for Adult Movie")
else:
    print("Not Allowed")
