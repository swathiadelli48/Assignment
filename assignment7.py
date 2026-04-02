from abc import ABC, abstractmethod
from functools import reduce

'''TASK 2: -----ABSTRACT CLASS------'''

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass

'''TASK 1 Use super() properly
Modify constructors so child classes reuse parent initialization.
Requirement:
User should have name and id
Student adds dept and fees
Faculty adds salary
TempFaculty adds duration'''

class User:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"User: {self.name}, ID: {self.id}"

class   Student(User):

    def __init__(self, name, id,dept,fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees
        super().get_details()

    def get_details(self):
        return f"Student: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


class Faculty(User):
    
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
        
    def get_details(self):
        return f"Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}"
    

class TempFac(Faculty):

    def __init__(self,name, id,salary,duration):
        super().__init__(name, id,salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"



students = [
    Student("Arjun", 502, "CSE", 100000),
    Student("Divya", 503, "ECE", 90000),
    Student("Karthik", 504, "IT", 95000),
    Student("shashi", 501, "ECE", 45000),
    Student("Karthik", 506, "IT", 30000)
]


faculty = [
    Faculty("DEV", 5402, 100000),
    Faculty("Bhavin", 1503,  900000),
    Faculty("Aarthi", 43504, 750000),
    Faculty("Sameeksha", 243504, 600000),
    Faculty("Aarthi", 43504, 25000),
    Faculty("Sameeksha", 243504, 15000)
]


'''Task 3 Create a list of students and sort them.
Requirement:
Sort students by fees
Sort faculty by salary
Example:
students.sort(key=lambda x: x.fees)'''


students.sort(key = lambda students: students.fees)

for i in students:
    print(i.get_details())

faculty.sort(key = lambda fac: fac.salary)

for fac_sort in faculty:
    print(fac_sort.get_details())

'''Task 4: Use map()
Transform data.
Requirement:
Extract only student names using map'''

map_names = list(map(lambda name_map: name_map.name, students))
print(map_names)


'''Task 5: Use filter()
Filter data.
Requirement:
Get students with fees > 50000
Get faculty with salary > 30000'''

high_fee_students = list(filter(lambda s: int(s.fees) > 50000, students))

for i in high_fee_students:
    print('HIGH FEES ',i.get_details())

high_salary_fac = list(filter(lambda x: int(x.salary) > 30000, faculty))

for i in high_salary_fac:
    print('HIGH SALARY: ',i.get_details())
                       
'''Task 6: Use reduce()
Aggregate data.
Requirement:
Calculate total salary of all faculty
Calculate total fees collected
Example:
from functools import reduce'''

total_salary = reduce(lambda x,y: x+int(y.salary), faculty, 0)
print('Total Salary: ', total_salary)

total_fees = reduce(lambda x,y: x + int(y.fees), students, 0)

print('Total Fees: ',total_fees)


'''Task 7: Higher Order Function
Create a function that accepts another function.
Requirement:
Create function process_users(users, func)
Apply any operation (map/filter)
Example:
def process_users(users, func):
    return list(map(func, users))'''


def process_users(users, func):
    return list(map(func, users))

details = process_users(students, lambda s: f"{s.name} - {s.dept}")
print("Student Info:", details)


'''Final Challenge
Build a mini system:
Store multiple students & faculty in lists
Print:
All details (get_details())
Sorted data
Filtered data
Total fees & salary
Use at least 3 functional programming concepts together
'''

print("---- ALL DETAILS ----")
for user in students + faculty:
    print(user.get_details())

total_high_salary = reduce(
    lambda a, b: a + b,
    map(lambda s: s.salary,
        filter(lambda x: x.salary < 50000, faculty)),
    0
)

print("Total salary :", total_high_salary)
