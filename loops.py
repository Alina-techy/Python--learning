#loops programs
#1. Print 1 to 100
for i in range(1,101):
    print(i)
    
#2. Print Even Numbers (1 to 100)
for i in range(2,101,2):
    print(i)
    
#3. Print Odd Numbers (1 to 100)
for i in range(1,101,2):
    print(i)
    
#4. Sum of First N Numbers
n= int(input("Enter the number: "))

sum=0
for i in range(1,n+1):
    sum= sum+i
    
print("Sum=", sum)

#5. Multiplication Table
x= int(input("Enter a number : "))

for i in range(1,11):
    print(x,"X",i,"=", x * i)

#6. Factorial
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)

#7. Fibonacci Series
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

#8. Check Prime Number
n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not Prime")

#9. Prime Numbers in a Range
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):
    if num > 1:
        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count += 1

        if count == 2:
            print(num)
            
#10. Reverse a Number
n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10                        #Extracts the last digit of the number.
    reverse = reverse * 10 + digit        #Appends the extracted digit to the end of the reversed number.
    n = n // 10                           #Removes the last digit from the number.
print("Reverse =", reverse)

# 11. Sum of Digits
n = int(input("Enter a number: "))

sum = 0

while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10

print("Sum =", sum)

#12. Product of Digits
n = int(input("Enter a number: "))

product = 1

while n > 0:
    digit = n % 10
    product *= digit
    n = n // 10

print("Product =", product)

#13. Count Digits
n = int(input("Enter a number: "))

count = 0

while n > 0:
    count += 1
    n = n // 10

print("Digits =", count)

#14. Largest Digit
n = int(input("Enter a number: "))

largest = 0

while n > 0:
    digit = n % 10

    if digit > largest:
        largest = digit

    n = n // 10

print("Largest Digit =", largest)

#15. Smallest Digit
n = int(input("Enter a number: "))

smallest = 9

while n > 0:
    digit = n % 10

    if digit < smallest:
        smallest = digit

    n = n // 10

print("Smallest Digit =", smallest)

#16. Palindrome Number
n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
    
#17. Armstrong Number
n = int(input("Enter a number: "))

original = n
sum = 0
digits = len(str(n))

while n > 0:
    digit = n % 10
    sum = sum + digit ** digits
    n = n // 10

if sum == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
    
#18. Perfect Number
n = int(input("Enter a number: "))

sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")
    
#19. Strong Number
n = int(input("Enter a number: "))

original = n
sum = 0

while n > 0:
    digit = n % 10

    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    sum += fact
    n = n // 10

if sum == original:
    print("Strong Number")
else:
    print("Not Strong Number")
    
#20. Neon Number
n = int(input("Enter a number: "))

square = n * n
sum = 0

while square > 0:
    digit = square % 10
    sum += digit
    square = square // 10

if sum == n:
    print("Neon Number")
else:
    print("Not Neon Number")
    
#21. Duck Number
n = input("Enter a number: ")

if n[0] == '0':
    print("Not Duck Number")
elif '0' in n:
    print("Duck Number")
else:
    print("Not Duck Number")
    
#22. Spy Number
n = int(input("Enter a number: "))

sum = 0
product = 1

while n > 0:
    digit = n % 10
    sum += digit
    product *= digit
    n = n // 10

if sum == product:
    print("Spy Number")
else:
    print("Not Spy Number")
    
#23. Harshad Number
n = int(input("Enter a number: "))

original = n
sum = 0

while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10

if original % sum == 0:
    print("Harshad Number")
else:
    print("Not Harshad Number")
    
#24. Square Pattern
rows = int(input("Enter rows: "))

for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()
    
#25. Pyramid
rows = int(input("Enter rows: "))

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()
    
#26. Inverted Pyramid
rows = int(input("Enter rows: "))

for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()
    
#27. Diamond Pattern
rows = int(input("Enter rows: "))

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()

for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()
    
