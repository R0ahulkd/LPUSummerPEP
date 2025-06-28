# Program to demonstrate class and methods in Python
# class Test(object):
#     def __init__(self):
#         print("Constructor called")
    
#     def m1(self):
#         print("Hello World")

# x = Test()
# x.m1()



# Program to demonstrate class and methods
# class Test(object):
#     def __init__(self):
#         print("Constructor called")

#     def deposit(self):
#         print("Deposit method called")
    
#     def withdraw(self):
#         print("Withdraw method called")

# x = Test()
# x.deposit()
# x.withdraw()



# Program to demonstrate Single level Inheritance in Python
# class Father: # Parent Class
#     def show(self):
#         print("Parent Class Instance method")
    
# class Son(Father): # Child Class (inherits from Father)
#     def display(self):
#         print("Child Class Instance method")

# s = Son()
# s.display()
# s.show()



class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Programmer(Employee):
    salary = 25000
    designation = "Programmer"

class Manager(Employee):
    salary = 30000
    designation = "Manager"

class Tester(Employee):
    salary = 20000
    designation = "Tester"

employees = []

while True:
    print("\n1. CREATE 2. DISPLAY 3. RAISE SAL 4. EXIT")
    choice = input("> ")
    
    if choice == "1":
        name = input("NAME: ")
        age = input("AGE: ")
        desig = input("DESIGNATION (P/M/T): ").upper()
        
        if desig == "P":
            employees.append(Programmer(name, age))
        elif desig == "M":
            employees.append(Manager(name, age))
        elif desig == "T":
            employees.append(Tester(name, age))
            
    elif choice == "2":
        for emp in employees:
            print(f"{emp.name} {emp.age} {emp.salary} {emp.designation}")
            
    elif choice == "3":
        for emp in employees:
            emp.salary += 5000
            
    elif choice == "4":
        break