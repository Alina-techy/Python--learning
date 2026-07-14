#strings --- strings are immutable
#1. Print String
text= "Alina is cute"
print(text)

#2. Length of String
text= input("Enter a string:")
print("Length=", len(text))

#3. Reverse String
text = input("Enter a string: ")

print("Reverse =", text[::-1]) #(start:stop:step)

#4. palindrome 
text= input("Enter a string:")   

if text==text[::-1]:
    print("palindrome")
else:
    print("not palindrome")
    
#5. Count Vowels
text = input("Enter a string: ")

count = 0   #initializes it to 0 because initially no vowels have been counted.

for ch in text.lower():
    if ch in "aeiou": #ch in aeiou means any character in aeiou is counted as vowel.
        count += 1     #count = count + 1

print("Vowels =", count)

#6. Count Consonants
text= input("Enter a string:")

count= 0

for ch in text.lower():
    if ch.isalpha() and ch not in "aeiou":
        count+=1
        
print("Consonants=", count)

#7. Count Digits
text=input("Enter a string:")

count=0

for ch in text:
    if ch.isdigit():
        count+=1
        
print("Digits=", count)

#8. Count Spaces
text=input("Write a sentence:")

count=0

for ch in text:
    if ch.isspace():
        count+=1
        
print("Spaces=", count)

#9. Convert to Uppercase
text= input("Enter a string:")

print(text.upper())

#10. Convert to Lowercase
text= input("Enter a string:")

print(text.lower())

#11. Capitalize
text = input("Enter a string: ")

print(text.capitalize())

#12. Title Case
text = input("Enter a string: ")

print(text.title())

#13. Replace Word
text= input("Enter a sentence: ")

old= input("Word to be replace:")
new= input("New word:")

print(text.replace(old,new))

#14. Split String
text= input("Enter a sentence: ")

print(text.split())

# 15. Join String
words = ["I", "Love", "Python"]

result = " ".join(words)

print(result)

#16. Remove Spaces
text= input("Enter a string: ")

print(text.replace(" ",""))

# 17. Check Substring
text = input("Enter a string: ")

sub = input("Enter substring: ")

if sub in text:
    print("Found")
else:
    print("Not Found")
    
#18. Count Character Frequency
text= input("Enter a string: ")

ch= input("Enter a character: ")

print(text.count(ch))

#19. Find duplicate character
text = input("Enter a string: ")

seen = ""

for ch in text:
    if text.count(ch) > 1 and ch not in seen:  #Using seen ensures each duplicate character is printed only once.
        print(ch)
        seen += ch          #Adds that character to seen.
        
#20. Find first occurence 
text= input("Enter a string: ")
ch= input("Enter a character: ")

print(text.find(ch))

#21. Find last occurence
text = input("Enter a string: ")
ch = input("Enter character: ")

print(text.rfind(ch))

#22. String Slicing
text = input("Enter a string: ")

print(text[0:5])

#23. Reverse Words
text= input("Enter a sentence: ")

words= text.split()    #to separate words
words.reverse()         #reverse the order

print(" ".join(words))    #then join words

#24. Sort Characters
text = input("Enter a string: ")

result = "".join(sorted(text))    #join() combines the list into a single string and sorted() arranges the characters in alphabetical order.

print(result)

# 25. Remove Duplicate Characters
text= input("Enter a string: ")

result=""

for ch in text:
    if ch not in result:
        result+=ch
        
print(result)

#26. ASCII Values
text = input("Enter a string: ")

for ch in text:
    print(ch, "=", ord(ch))        #Displays the ASCII (Unicode) value of every character using ord().

#27. Check Anagram
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1.lower()) == sorted(str2.lower()): #Checks whether two strings contain the same characters in a different order by comparing their sorted versions.
    print("Anagram")
else:
    print("Not Anagram")

#28. Password Validation
password= input("Enter your password: ")

if len(password)>= 8 :
    print("Valid")
else:
    print("Invalid")

# 29. Email Validation
email= input("Enter email: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")

#30. String Formatting
name = input("Enter name: ")
age = int(input("Enter age: "))

print(f"My name is {name} and I am {age} years old.")