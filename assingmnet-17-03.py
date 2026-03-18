'''Print numbers from 1 to 50 using for loop'''

for i in range(1,51):
    print(i)

'''Print even numbers from 1 to 100'''
for i in range(1,101):
    if i%2==0:
        print(i)

'''Print odd numbers from 1 to 100'''

for i in range(1,101):
    if i%2==1:
        print(i)
'''Print multiplication table of 7'''

for i in range(11):
    print("7", "x", i ,"=",7*i)

'''Find sum of numbers from 1 to 100'''
sum = 0
for i in range(1,101):
    sum += i
print(sum)    

'''Print numbers in reverse from 50 to 1'''
lst = []
for i in range(1,51):
    lst.append(i)     
print(lst[::-1])    

'''Count how many numbers are divisible by 3 (1–100)'''
count = 0
for i in range(1,101):
    if i%3==0:
        count += 1
print(count)

'''Print squares of numbers from 1 to 10'''
for i in range(1, 11):
    print(i ** 2)

'''Print cube of first 10 numbers'''
for i in range(1,11):
    print(i **3)

'''Take input n, print numbers from 1 to n'''

n = int(input("enter a number:- "))
for i in range(1,n+1):
    print(i)

'''Print numbers from 1 to 20 using while'''
num = 0

while num<20:
    num+= 1
    print(num)    

'''Find factorial of a number using while'''

num = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= num:
    factorial = factorial * i
    i += 1
print(factorial)


'''Reverse a number using while'''  

str = input("Enter a number: ")
res = ""
i = len(str) - 1

while i >= 0:
    res += str[i]
    i -= 1

print(res)

'''Count digits in a number'''

num = int(input("Enter a number"))
count = 0
if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10
        count += 1

print(count)

'''Keep asking input until user enters "stop"'''
while True:
    str = input("Enter something to 'stop': ")
    if str == "stop":
        break
    print("You entered:", str)

'''Print pattern:
*
**
***
****'''
for i in range(1,5):
    for j in range(1, i+1):
        continue
    print(i * "*")    

'''Print pattern:
1
12
123
1234'''

for i in range(1,5):
    for j in range(1, i+1):
        print(j, end=" ")
    print()     

'''Print multiplication table (1 to 5) using nested loop'''
for i in range(1, 6):        
    print("Table of", i)
    
    for j in range(1, 11):   
        print(i, "x", j, "=", i * j)
    print() 

'''Print:
A B C
A B C
A B C'''
for i in range(3):         
    for j in range(3):      
        print(chr(65 + j), end=" ")
    print()

'''Print:
1 2 3
4 5 6
7 8 9
'''
num = 1
for i in range(3):          
    for j in range(3):      
        print(num, end=" ")
        num += 1
    print()

'''Count total characters in a string'''
str = input("Enter a string")
length = len(str)
print(length)

'''Count vowels in a string'''

str = input("Enter a string: ")
vowels = 'aeiou'
count = 0
for i in str:
    if i in vowels:
        count += 1
print(count)

'''Count consonants in a string'''
str = input("Enter a string: ")
consonants = 'bcdfghjklmnpqrstvwxyz'
count = 0
for i in str:
    if i in consonants:
        count += 1
print(count)

'''Reverse a string using loop'''
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed string:", rev)

'''Check if string is palindrome''' 
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
if s ==rev:
    print("Palindrome")
else:
    print("Not a palindrome")

'''Print first 5 characters of a string'''
str = input("Ehter a string: ")
print(str[0:5])

'''Print last 3 characters'''
str = input("Ehter a string: ")
print(str[-3:])

'''Print string in reverse using slicing'''
str = "python"
print(str[::-1])

'''Print every 2nd character'''
str = input("ENTER STRING: ")
print(str[1:len(str):2])

'''Remove first and last character from string'''
str = input("ENTER STRING: ")
print(str[1:-1])

'''Create a list of 5 numbers and print sum'''
lst = [1,2,3,4,5]
sum = 0
for i in lst:
    sum = sum+i
print(sum)    

'''Find maximum value in list'''
lst = [10, 25, 7, 99, 3]
print(max(lst))

'''Find minimum value in a list'''
lst = [10, 25, 7, 99, 3]
print(min(lst))

'''Count total elements in a list'''
lst = [10, 25, 7, 99, 3,4645]
print(len(lst))

'''Check if element exists in list'''

lst = [10, 25, 7, 99, 3]
i = int(input("Enter i value: "))
if i in lst:
    print("I value is in the list")
else:
    print("given is not in the list")    

'''Add 3 elements using append()'''
lst = []
lst.append("madhapur")
lst.append("gachibowli")
lst.append("tarnaka")
print(lst)

'''Insert element at specific index'''
lst = ["hyd", "miyapur", "hitechcity"]
lst.insert(1,"Vidyanagar")
print(lst)

'''Remove element using remove()'''

lst = [23,45,76,98]
n = int(input("Enter a number: "))
lst.remove(n)
print(lst)

'''Reverse list without using .reverse()'''
lst = [10, 20, 30, 40]
rev = lst[::-1]
print("Reversed list:", rev)

'''Sort list without using .sort()'''
lst = [5, 2, 9, 1, 7]
for i in range(len(lst)):
    min_index = i
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[min_index]:
            min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]

print("Sorted list:", lst)
