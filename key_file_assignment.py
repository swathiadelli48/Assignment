'''Create a function:
def create_user(name, age, role):
Return user as a dictionary
Store multiple users in a list
Print all users
Add:
Format names using .title()'''

users = []

def create_user(name, age, role):

    return  {
        "name": name.title(), "age":age,"role":role
        }

users.append(create_user("john doe", 25, "admin"))
users.append(create_user("alice smith", 30, "manager"))
users.append(create_user("bob", 22, "developer"))

for i in users:
    print(i)   


'''
 Task 2: Dynamic Calculator (*args)
Create:
def calculate_total(*numbers):
Return sum of all numbers
Accept unlimited inputs
Bonus:
Also return average'''


def calculate_total(*numbers):
    total = 0
    for i in numbers:
        total += i
        average = total/len(numbers)
        
    return total, average


total, average = calculate_total(45,56,43,54,66,89)    
print("Total: ", total)
print("Average: ", average)


'''Task 3: Keyword Config System (**kwargs)
Create:
def system_config(**settings):
Print all key-value pairs
 Example:
mode: debug
version: 1.0'''


def system_config(**settings):
    for key, value in settings.items():
        print(f"{key} : {value}")
        

system_config(mode="debug", version=1.0)  
system_config(name="kalyan", age=20)  
system_config(name="pavan", age=24)  

'''Task 4: Factorial Service (Recursion)
Create:
def factorial(n):
Handle:
n = 0
negative numbers (show error)'''

def factorial(n):
    if n <0:
        return "Error: the value is less than 0"
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("Enter the input:-"))
print(factorial(n))   


''' Task 5: Memory Optimization (Generator)
Create:
def square_generator(n):
Yield squares instead of storing in list
Compare:
Normal list vs generator (print type)'''

def square_generator(n):
    for i in range(n):
        yield i*i
        
res = square_generator(6)
for i in res:
    print(i) 

# Normal list    
def square(n):
    list_ = []
    for i in range(n):
        res = i *i
        list_.append(res)
    return list_    
print(square(5))    

''' Task 6: Exception Handling Module
Take input:
numerator
denominator
Handle:
divide by zero
invalid input
Always print:
Program Completed'''

try:
    numerator = int(input("Enter the number: "))
    denominator = int(input("Enter the input: "))
    print(numerator/denominator)

except ZeroDivisionError:
    print("The denominator value should not be zero")

except ValueError:
    print("The entered values should be a number")
finally:
    print("Program completed")        


''' Task 7: File Handling
Create file: team_data.txt
Write user details into file
Read and display content
Bonus:
Check if file is closed'''

with open("inputfile.txt", "w") as f:
    f.write("name: swathi ")
    f.write("Age: 26")

with open("inputfile.txt", "r") as f:
    print(f.read())
        

print("Is file closed? ", f.closed)
