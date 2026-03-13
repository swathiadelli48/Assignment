'''1.Create two variables a = 10 and b = 6.Print the result of a & b.'''

a = 10 
b = 6
print(a&b)

'''2.Create two variables x = 12 and y = 5.Print the result of x | y.'''

x = 12
y = 5
print(x | y)

'''3.Create a variable num = 8.Print the result of ~num.'''
num = 8
print(~num)

'''4.Create two variables a = 15 and b = 9.Print the result of a ^ b.'''
a = 15 
b = 9
print(a ^ b)

'''5.Create a variable num = 7.Perform left shift by 2 and print the result.'''
num = 7
print(num<<2)

'''6.Create a variable num = 20.Perform right shift by 1 and print the result.'''
num =20
print(num>>1)

'''7.Take two numbers from user input and print AND result.'''

n1 = int(input("Enter a number1 value: "))
n2 = int(input("Enter a number2 value: "))
print(n1 & n2)

'''8.Take two numbers from user input and print XOR result.'''

n1 = int(input("Enter a number1 value: "))
n2 = int(input("Enter a number2 value: "))
print(n1^n2)

'''9.Create a string "hi" and print it 4 times using replication.'''

word = "hi"+" "
print(word *4)

'''10.Create a string "python" and print it 3 times.'''

word = "python"
str = " "
print((word+str)*3)

'''11.Create two strings "super" and "man" and combine them using + operator.'''

str1 = "super"
str2 = "man"
print(str1+str2)

'''12.Create three strings "hello", " ", "world" and print "hello world".'''

str1 = "hello"
str2 = " "
str3 = "world"
print(str1+str2+str3)

'''13.Take a name from user input and print it 5 times.'''

name =input("Enter a name: ")
sep = name + " "
print(sep*5)

'''14.Take two strings from user input and concatenate them.'''

First_Name = input("Enter  First_Name: ")
Last_Name = input("Enter  Last_Name: ")
print(First_Name+Last_Name)

'''
15.Take a name from user input and print its data type.'''

name = input("Enter the name: ")
print(type(name))

'''16.Take age from user input and convert it into integer.'''

age = input("Enter the age: ")
print(int(age))

'''17.Take two numbers from user input and print their sum.'''

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print(num1 + num2)

'''18.Take two marks from user input and print their average.'''

maths = int(input("Enter the maths marks:"))
physics = int(input("Enter physics marks: "))
print((maths+physics)/2)

'''19.Take two numbers from user input and print3*a*2 + b - 2.'''

a = int(input("Enter first number: "))
b = int(input("Enter secondnumber: "))
print(3*a*2 + b - 2)

'''20.Take a number from user input and print its data type before and after type casting.'''

a = input("Enter a number")
print(type(a))
b = int(a)
print(type(b))

'''21.Take a number as string input and print the last digit.'''

num = input("Enter a number")
print(num[len(num)-1])

'''22.Take a number and print the unit digit using % operator.'''

num = int(input("Enter a number: "))
unit_digit = num % 10
print("Unit digit is:", unit_digit)

'''23.Take a number and remove the last digit using // operator.'''

num = int(input("Enter a number: "))
result = num // 10
print("Number after removing last digit:", result)

'''24.Take a number and print the second last digit.'''

num = input("Enter a number")
print(num[len(num)-2])

'''25.Take a 5 digit number and print its last digit.'''

num = "98765"
print(num[len(num)-1])

'''26.Create a program that checks if 10 ≥ 5 and prints a message.'''
n = 10
m = 5
if n>=m:
    print("The give value is greater than the other value")

'''27.Take a number from user input and check if it is greater than 50.'''

n = int(input("Enter a number: "))
if n>50:
    print("True")
 

'''28.Take age from user input and check if age ≥ 18.'''

age = int(input("Enter the age: "))
if age>=18:
    print("True")
 

'''29.Take a number and check if it is greater than 100.'''

n = int(input("Enter a number: "))
if n>100:
    print("True")


'''30.Take a number and check if number ≥ 0.'''

n = int(input("Enter a number: "))
if n>=0:
    print("True")
 

'''31.Take a number and check if it is even or odd.'''

n = int(input("Enter a number: "))
if n%2==0:
    print("Even number")
else:
    print("Odd number") 

'''32.Take marks from user input and check if pass or fail (pass ≥ 35).'''

marks = int(input("Enter a Marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail") 

'''33.Take a number and check if it is positive or negative.'''

number = int(input("Enter a number: "))
if number >= 0:
    print("Positive")
else:
    print("Negative") 

'''34.Take a number and check if it is greater than 10 or not.'''

number = int(input("Enter a number: "))
if number > 10:
    print("Given number is Greaterthan 10")
else:
    print("Given number is Lessthan 10") 

'''
35.Create a program for job eligibility:
Conditions
Age ≥ 18
Height ≥ 160
Weight ≥ 60
Print selected or rejected.'''

age =int(input("Enter the age: "))
height =int(input("Enter the height: "))
weight =int(input("Enter the weight: "))

if age >=18:
    if height>=160:
        if weight>=60:
            print("You're Eligible")
        else:    
            print("You're underweight")
    else:        
        print("Your height doesnt match")
else:
    print("you're not eligible")          
            


'''36.Create a college admission program:
Conditions
Marks ≥ 60
Age ≥ 17'''

marks =int(input("Enter the marks: "))
age =int(input("Enter the age: "))

if marks>=60:
    if age>=17:
        print("You're admitted into the college")
    else:
        print("You're under aged")    
else:
    print("Your admission is rejected")

'''37.Create a sports selection program:
Conditions
Age ≥ 16
Height ≥ 150
Weight ≥ 50'''

age =int(input("Enter the age: "))
height =int(input("Enter the height: "))
weight =int(input("Enter the weight: "))

if age >=16:
    if height>=150:
        if weight>=50:
            print("You're selected")
        else:    
            print("You're underweight")
    else:        
        print("Your height doesnt match")
else:
    print("you're rejected")     


'''38.Take a number (1-7) and print day name using match.'''

num = int(input("Enter a number (1-7): "))

match num:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid input")


'''39.Take a number (1-3) and print:
1 → Red
2 → Blue
3 → Green'''

num = int(input("Enter a number (1-3): "))

match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")
    case _:
        print("Invalid input")

'''40.Take a number (1-4) and print:
1 → Apple
2 → Mango
3 → Orange
4 → Banana
'''

num = int(input("Enter a number (1-4): "))

match num:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")
    case _:
        print("Invalid input")