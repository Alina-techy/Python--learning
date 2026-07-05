#datatype programs
#1. Print the Data Type of Different Variables
name= "Alina"
age= 20
height= 5.3
is_student= True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

#2. Convert Integer to Float
num = 25
print("Before conversion")
print(num)
print(type(num))
num=float(num)
print("\nAfter conversion")
print(num)
print(type(num))

#3. Convert Float to Integer
rate= 3.4
print("Before conversion")
print(rate)
print(type(rate))
rate=int(rate)
print("\nAfter conversion")
print(rate)
print(type(rate))

#4. Convert String to Integer
age= "35"
print("before conversion")
print(age)
print(type(age))
age= int(age)
print("\nafter conversion")
print(age)
print(type(age))

#5. Convert Integer to String
roll_no= 101
print("before conversion")
print(roll_no)
print(type(roll_no))
roll_no= str(roll_no)
print("\nafter conversion")
print(roll_no)
print(type(roll_no))

#6. Boolean Conversion Examples
print(bool(1))            # 1 -> true
print(bool(0))            # 0-> false
print(bool(""))           # empty string "" -> false
print(bool("Python"))     # non empty string -> true
print(bool([]))           # empty list ->  false
print(bool([1, 2, 3]))    # non empty list -> true

#7. Complex Number Operations
x = 10j
y = 8j
print("Enter the 1st complex number: ", x)
print("Enter the 2nd complex number: ", y)

print("\nAddition=", x+y)
print("Subtraction=", x-y)
print("Multiplication=", x*y)

#8. Check Data Type Using type()
number = 100
decimal = 12.5
name = "Python"
status = False

print("Type of number:", type(number))
print("Type of decimal:", type(decimal))
print("Type of name:", type(name))
print("Type of status:", type(status))

#9. Create Variables of Every Data Type
integer = 50
floating = 12.75
text = "Hello"
boolean = True
complex_num = 3 + 4j
my_list = [10, 20, 30]
my_tuple = (1, 2, 3)
my_set = {5, 6, 7}
my_dict = {"name": "Alina", "age": 20}
nothing = None

print(integer)
print(floating)
print(text)
print(boolean)
print(complex_num)
print(my_list)
print(my_tuple)
print(my_set)
print(my_dict)
print(nothing)

#10. Print Values and Their Types
integer = 100
floating = 25.5
text = "Python"
boolean = True
complex_num = 5 + 2j
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_set = {7, 8, 9}
my_dict = {"A": 1, "B": 2}
nothing = None

print(integer, "-", type(integer))
print(floating, "-", type(floating))
print(text, "-", type(text))
print(boolean, "-", type(boolean))
print(complex_num, "-", type(complex_num))
print(my_list, "-", type(my_list))
print(my_tuple, "-", type(my_tuple))
print(my_set, "-", type(my_set))
print(my_dict, "-", type(my_dict))
print(nothing, "-", type(nothing))
