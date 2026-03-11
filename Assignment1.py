'''
Task 1 - Print Formatting
Print the following output using sep and end.
Expected Output:
Hello World Welcome Python
Laptop | Mouse | Keyboard
'''

print("Hello", "World", "Welcome", "python", sep = " ",end = "\n")
print("Laptop", "Mouse", "Keyboard", sep = "|")

'''
Task 2 – Variables
Create variables:
name = "Ravi"
age = 22
city = "Chennai"
Print them in one line separated by -
Example output:
Ravi-22-Chennai
'''
name = "Ravi"
age = 22
city = "Chennai"
print(name, age,city, sep="-")

'''
Task 3 – Multiple Assignment
Assign values using multiple assignment
name = "Meena"
age = 20
student = True
Print the output.
'''
name, age,student = "Meena", 20, True
print("Multiple Assignmrnt: ", name, age, student)

'''
Task 4 – Indexing
Given:
word = "Python"
Print:
First letter
Third letter
Last letter
'''

word = "Pthon"
print("First Letter: ",word[0])
print("Third Letter: ",word[2])
print("Last Letter: ",word[4])

'''
Task 5 – Arithmetic Operators
Calculate and print:
25 + 10
50 - 20
8 * 5
100 / 10
10 % 3
2 ** 4
20 // 3
'''

addition = 25+10
subtraction = 50-20
mul = 8 *5
division = 100/10
modulus = 10%3
power = 2 **4
floor = 20//3

print(addition)
print(subtraction)
print(mul)
print(division)
print(modulus)
print(power)
print(floor)


'''
Task 6 – BODMAS Expression
Find the result:
print(3 + 2 * 5 ** 2)
'''
print(3 + 2 * 5 ** 2)

'''
Task 7 – Assignment Operator
num = 50
num += 25
Print the final value.
Then try:
num = 100
num /= 10
Print the result.
'''
num = 50
num += 25
print(num)

num = 100
num /= 10
print(num)

'''
Task 8 – Comparison Operators
Print the result of the following:
10 > 5
20 < 15
5 == 5
10 != 8
7 >= 7
6 <= 2
'''
print(10 > 5)
print(20 < 15)
print(5 == 5)
print(10 != 8)
print(7 >= 7)
print(6 <= 2)

'''

Task 9 – String Comparison
a = "apple"
b = "Apple"
Check:
print(a == b)
'''
a = "apple"
b = "Apple"
print(a==b)

#Here ashkey values of a and A are different thats why the result is False

'''
Task 10 – Logical Operators
Find the output:
print(10 > 5 and 5 == 5)
print(5 > 10 or 10 == 10)
print(not(5 > 2))
'''
print(10 > 5 and 5 == 5)
print(5 > 10 or 10 == 10)
print(not(5 > 2))

'''
Task 11 – Membership Operator
numbers = [10,20,30,40,50]
Check:
20 in numbers
60 in numbers
30 not in numbers
'''
numbers = [10,20,30,40,50]
print(20 in numbers)
print(60 in numbers)
print(30 not in numbers)

'''
Task 12 – Swap Variables
a = 10
b = 20
Swap the values using single line swap
Expected Output:
a = 20
b = 10
'''
a = 10
b = 20
temp= a
a = b
b = temp
print(a,b)

'''
Task 13 – Bitwise XOR
a = 6
b = 3
Print:
a ^ b
Ask them to check the binary calculation.
'''
a = 6
b = 3
print(a^b)

# 110 = 6
# 011 = 3
# 101 = 5