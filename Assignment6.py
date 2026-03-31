# 1: Encapsulation (User Class)
class User:

    def __init__(self):
        self.user_name = None
        self.pwd = None

    def set_user(self,user_name, pwd):
        self.user_name = user_name
        self.pwd = pwd

    def get_user(self):
        return self.user_name
        
    def register(self):
        print("Registering user: ", self.user_name)
    
    def login(self):
        print("Logging in: ", self.user_name)


user = User()
user.set_user("vetri",9576)
user.register()
user.login()

#2.Inheritance (User → Student, Faculty)

class User:
    
    def register(self):
        print("Registering.....")
    def login(self):
        print("Logging in......")

class Student(User):
    def student_greet(self):
        print("Hello stdent")


class Faculty(User):
    def faculty_greet(self):
        print("Hello faculty")


class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")




user1 = User()
student = Student()
faculty = Faculty()
tempfac = TempFaculty()

student.student_greet()
faculty.faculty_greet()
tempfac.tempFaculty_greet()

student.register()
student.login()

faculty.register()
faculty.login()

tempfac.register()
tempfac.faculty_greet()

# user1.student_greet() #Here parent class not accessing the child class

#3: Method Overriding Use  User, Student, Faculty

class User:
    def greet(self):
        print("Welcome User")


class student(User):
    def greet(self):
        print("Welcome Student")


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")

stu = student()
fac = Faculty()
stu.greet()
fac.greet()


#4: Method Chaining
class User():
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self

user2 =User()
user2.login().greet().register()  


#Combined Task (Real-Time) Build a Mini User System

class User:

    users_count = 0

    def __init__(self):
        self.user_name = None
        self.pwd = None
        User.users_count += 1

    def set_user(self,user_name, pwd):
        self.user_name = user_name
        self.pwd = pwd
        return self

    def get_user(self):
        return self.user_name
    
    def greet(self):
        print("Hello everyone")
        return self

    def register(self):
        print("Registering user: ", self.user_name)
        return self
    
    def login(self):
        print("Logging in: ", self.user_name)
        return self


class Student(User):
    
    def student_greet(self):
        print("Hello stdent")
        return self
    
    def greet(self):
        print("Hello student")
        return self
    

class Faculty(User):

    def faculty_greet(self):
        print("Hello faculty")
        return self

    def greet(self):
        print("Hello Faculty")
        return self



user3 = User()
stu1 = Student()
fac1 = Faculty()

user3.set_user("arjun",64584)
user3.register()
user3.login()

stu1.student_greet()
fac1.faculty_greet()

user3.greet()
stu1.greet()
fac1.greet()

user3.login().greet().register()


print("Total users:", User.users_count)



