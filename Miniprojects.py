'''Mini Project 1: Employee Management System
Requirements:
Store multiple employees (list of dictionaries)
Each employee: name, age, role, salary
Add new employee
Update employee details
Delete employee
Display all employees

'''
employees=[]
def adding_employee():
    name = input("Ente name: ")
    age = int(input("Enter the age"))
    role = input("Enter the role ")
    salary = float(input("Enter the salary"))
    employees.append({"name":name,"age":age,"role":role,"salary":salary})

def display_employees(): 
    print(employees)

def update_employee():
    display_employees()
    index = int(input("Enter index to update: "))

    if 0 <= index < len(employees):
        employees[index]["name"] = input("New Name: ")
        employees[index]["age"] = int(input("New Age: "))
        employees[index]["role"] = input("New Role: ")
        employees[index]["salary"] = float(input("New Salary: "))
        print("Employee updated")
    else:
        print("Invalid index")
adding_employee()
update_employee() 
display_employees()


'''
Mini Project 2: Student Report Card
Concepts: Dictionary, Functions, Formatting
Create a report system.
Requirements:
Store student name and marks (3 subjects)
Calculate total and average
Print formatted report card
Display grade based on average'''

def std_report():
    name = input("Enter the name: ")
    subj1 = int(input("Enter the Sub1: "))
    subj2 = int(input("Enter the Sub2: "))
    subj3 = int(input("Enter the Sub3: "))
   
    total = subj1 + subj2 + subj3
    avg_val = total / 3
   
    if avg_val >= 80:
        grade = "A"
    elif avg_val >=65:
        grade = "B"
    elif avg_val >=36:
        grade = "C"
    else: 
        grade = "Fail"     
   
    print(f"{name} | Total: {total} | Avg: {avg_val:.2f} | Grade: {grade}")
std_report()

'''-----Mini Project 3: Shopping Cart System-----'''
'''---Add products (name, price, quantity)---'''

cart_lst = []
name = input("Enter the name of the item: ")
price = int(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

cart_lst.append({"name":name, "price":price,"quantity": quantity})
print(cart_lst)

'''---Calculate total bill---'''
total_bill = price * quantity
print("Total bill: ",total_bill)


'''Display all items in formatted way'''
print(f"A person buy {name} with the {price} rupees  {quantity} quantities")


'''Mini Project 4: Login & User Validation
Concepts: Dictionary, Condition
Basic authentication system.
Requirements:
Store users (username & password)
Take login input
Validate credentials
Print success or failure message'''

users = {"admin": "9040", "john": "john@123"}
 
username = input("Username: ")
password = input("Password: ")
 
if username in users:
    if users[username] == password:
        print("Login successful! Welcome,", username)
    else:
        print("Incorrect password")
else:
    print(" Username not found")          


'''Mini Project 5: Unique Visitor Counter
Store visitor names in a set
Avoid duplicates
Print total unique visitors'''
visitors = set()
 
for _ in range(3):
    name = input("Visitor: ")
    visitors.add(name) 
print("Unique Visitors:", len(visitors))

''' Mini Project 6: String Formatter Tool
Concepts: String Formatting
 Build a formatting utility.
Requirements:
Input name and product
Display formatted sentence
Show padded output (left, right, center)'''

name = input("Enter your name: ")
product = input("Enter product name: ")

print(f"{name} has purchased a {product}.")

print(name.ljust(10, "*"))
print(name.rjust(10, "*"))
print(name.center(10, "*"))


'''Mini Project 7: Bank Account System
Concepts: Functions, Dictionary
Simulate bank operations.
Requirements:
Create account (name, balance)
Deposit money
Withdraw money
Check balance'''

account = {}
def create_account():

    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))

    account["name"] = name
    account["balance"] = balance

    print("Account created successfully!\n")

def deposit():
    amount = float(input("Enter amount to deposit: "))
    account["balance"] += amount
    print("Amount deposited!\n")

def withdraw():    
    balance = float(input("Enter initial balance: "))
    withdraw = int(input("Withdraw: "))
    balance -= withdraw
    print("Balance: ",balance)

create_account()
deposit()
withdraw()
 

'''Mini Project 8: Voting System
Concepts: Dictionary, Loop
Count votes for candidates.
Requirements:
Store candidates and votes
Add vote
Display winner'''

votes = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

for candidate in votes:
    # print("-", candidate)
    choice = input("Enter candidate name to vote: ")

    if choice in votes:
        votes[choice] += 1
        print("Vote casted successfully!\n")
    else:
        print("Invalid candidate\n")

for candidate, count in votes.items():
    print(f"{candidate}: {count} votes")

winner = max(votes, key=votes.get)
print(f"\n Winner: {winner} with {votes[winner]} votes")



'''Mini Project 9: Course Enrollment System
Concepts: List + Dictionary
 Manage student enrollments.
Requirements:
Add student with course list
Update courses
Display student details'''

students = {}

name = input("Enter student name: ")
courses = input("Enter courses (comma separated): ").split(",")
students[name] = courses
 
''' Update courses'''
update_name = input("Enter student name to update: ")
if update_name in students:
    new_courses = input("Enter new courses (comma separated): ").split(",")
    students[update_name] = new_courses
else:
    print("Student not found")
 
# Display student details
print("\nStudent Details:")
for name, courses in students.items():
    print(name, "-", courses)


''' Mini Project 10: Number Utility Tool
Concepts: Functions, Formatting
Work with numbers.
Requirements:
Convert number to binary, octal, hex
Format large numbers with commas
Print scientific notation'''

def number_utility(num):
    print(f"Binary      : {bin(num)}")
    print(f"Octal       : {oct(num)}")
    print(f"Hexadecimal : {hex(num)}")
    print("With Commas:", format(num, ","))
    print("Scientific Notation:", format(num, ".2e"))
 
num = int(input("Enter a number: "))
 
number_utility(num)
