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
    employees.append({"name":input("Name:"),"age":int(input("Age:")),"role":input("Role:"),"salary":float(input("Salary:"))})
def display_employees(): 
    print(employees)

# def delete_employee(name):
#     global employees
#     employees=[e for e in employees if e["name"]!=name]
adding_employee(); 
display_employees(); 
# delete_employee(input("Delete:")); 
 
# 2. Student Report Card
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
 
# report()
 
# 3. Shopping Cart
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

'''---Remove item from cart---'''
# cart_lst.pop()
# print(cart_lst)


'''Display all items in formatted way'''
print(f"A person buy {name} with the {price} rupees  {quantity} quantities")
 
# 4. Login System
users = {"admin": "1234", "john": "john@123"}
 
username = input("Username: ")
password = input("Password: ")
 
if users.get(username) == password:
    print("Login Success")
else:
    print("Login Failed")
 
# 5. Unique Visitors
visitors = set()
 
for _ in range(3):
    name = input("Visitor: ")
    visitors.add(name)
 
print("Unique Visitors:", len(visitors))
 
# 6. String Formatter
name = input("Name: ")
product = input("Product: ")
 
print(f"{name} bought {product}")
print(name.ljust(10, "*"))
print(name.rjust(10, "*"))
print(name.center(10, "*"))
 
# 7. Bank System
balance = 1000
 
deposit = int(input("\nDeposit: "))
balance += deposit
 
withdraw = int(input("Withdraw: "))
balance -= withdraw
 
print("Balance:", balance)
 
# 8. Voting System
votes={"A":0,"B":0}
for _ in range(3):
    v=input("Vote:");
    if v in votes: votes[v]+=1
print("Winner:",max(votes,key=votes.get))
 
# 9. Course Enrollment
students = {}
 
# Add student
name = input("Enter student name: ")
courses = input("Enter courses (comma separated): ").split(",")
students[name] = courses
 
# Update courses
update_name = input("Enter student name to update: ")
if update_name in students:
    new_courses = input("Enter new courses (comma separated): ").split(",")
    students[update_name] = new_courses
else:
    print("Student not found")
 
# Display student details
print("\nStudent Details:")
for name, courses in students.items():
    print(name, "->", courses)
 
# 10. Number Utility
# Function to perform all operations
def number_utility(num):
    print("Binary:", bin(num))
    print("Octal:", oct(num))
    print("Hex:", hex(num))
    print("With Commas:", format(num, ","))
    print("Scientific Notation:", format(num, ".2e"))
 
# Input
num = int(input("Enter a number: "))
 
# Function call
number_utility(num)