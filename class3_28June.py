# Program 1 Try Exception
# a = 10
# b = 0
# try:
#     d = a/b
#     print(d)
#     print("This will not execute")
#     print("This will execute only if no exception occurs")

# except ZeroDivisionError:
#     print("Inside except block")

# print("This will execute and Rest of the code will execute")




# Program 2 Try Exception program
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# try:
#     d = a / b
#     print(f"The result is: {d}")
#     print("This will not execute if an exception occurs")

# except ZeroDivisionError:
#     print("You cannot divide by zero. Please enter a valid denominator.")




# Program 3 Try Except Else
# a = 10
# b = 5
# try:
#     d = a / b
#     print(d)
#     print("Inside try")

# except ZeroDivisionError:
#     print("Division by zero is not allowed")

# else:
#     print("Inside else")

# print("Rest of the code")



# Program 4 Try Except Finally
# a = 10
# b = 0
# try:
#     d = a / b
#     print(d)
#     print("Inside try")

# except ZeroDivisionError:
#     print("Division by zero is not allowed")

# else:
#     print("Inside else")

# finally:
#     print("Inside finally")

# print("Rest of the code")



# Program 5 Except Multiple Exceptions
# a = 10
# b = 0
# try:
#     d = a / b
#     print(d)

# except (NameError, ZeroDivisionError) as obj:
#     print(obj)

# print("Rest of the Code")




# Program 6 Extra Exception Handling
# class TooYoungException(Exception):
#     def __init__(self, arg):
#         self.msg = arg

# class TooOldException(Exception):
#     def __init__(self, arg):
#         self.msg = arg

# age = int(input("Enter your age: "))
# if age < 60:
#     raise TooYoungException("Plz wait some more time you will get best match soon!!")
# elif age > 18:
#     raise TooOldException("Your age already crossed marriage age.. no chance of getting")
# else:
#     print("You will get match details soon by email!!!")




# Program 7 File Handling writing
# f = open("student.txt", mode="w")
# f.write("Hello World\n")
# f.write("Python Training\n")
# f.write("How are you\n")
# f.close()
# print("Writing Success")




# Program 8 File Handling reading
# f = open("student.txt", mode="r")
# print(f.read())
# f.close()



# Program 9 File Handling reading and writing
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# f = open("student.txt", mode="w")
# f.write(f"Name: {name}\n")
# f.write(f"Age: {age}")
# f.close()
# print("Writing Success")

# f = open("student.txt", mode="r")
# print(f.read())
# f.close()



# Program 10 File Handling with Inheritance
class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    def get_person_details(self):
        self.name = input("Enter name: ")
        while True:
            try:
                self.age = int(input("Enter age (18-60): "))
                if 18 <= self.age <= 60:
                    break
                else:
                    raise ValueError("Age must be between 18 and 60")
            except ValueError as e:
                print(e)

class Employee(Person):
    def __init__(self):
        super().__init__()
        self.designation = ""
        self.salary = 0

    def get_employee_details(self):
        self.get_person_details()
        while True:
            try:
                d = input("Enter designation (P25/M30/T20): ").upper()
                if d in ["P25", "M30", "T20"]:
                    self.designation = d
                    if d == "P25":
                        self.salary = 25000
                    elif d == "M30":
                        self.salary = 30000
                    else:
                        self.salary = 20000
                    break
                else:
                    raise ValueError("Invalid designation")
            except ValueError as e:
                print(e)

class FileOperations(Employee):
    def create(self):
        self.get_employee_details()
        try:
            with open("employee.txt", "a") as f:
                f.write(f"{self.name},{self.age},{self.designation},{self.salary}\n")
            print("Employee added")
        except Exception as e:
            print("Error writing to file:", e)

    def display(self):
        try:
            with open("employee.txt", "r") as f:
                data = f.readlines()
                if not data:
                    print("No records found")
                else:
                    for line in data:
                        print(line.strip())
        except FileNotFoundError:
            print("File not found")

    def raise_salary(self):
        try:
            name = input("Enter name to raise salary: ")
            percent = float(input("Enter % hike (Max 30): "))
            if percent > 30:
                raise ValueError("Percentage can't exceed 30")
            updated_lines = []
            found = False
            with open("employee.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if parts[0] == name:
                        found = True
                        salary = float(parts[3])
                        new_salary = salary + (salary * percent / 100)
                        updated_line = f"{parts[0]},{parts[1]},{parts[2]},{new_salary:.2f}"
                        updated_lines.append(updated_line)
                    else:
                        updated_lines.append(line.strip())
            if found:
                with open("employee.txt", "w") as f:
                    for line in updated_lines:
                        f.write(line + "\n")
                print("Salary updated")
            else:
                print("Employee not found")
        except ValueError as e:
            print(e)
        except Exception as e:
            print("Error:", e)

obj = FileOperations()
while True:
    print("\n1. Create\n2. Display\n3. Raise Salary\n4. Exit")
    ch = input("Enter your choice: ")
    if ch == '1':
        obj.create()
    elif ch == '2':
        obj.display()
    elif ch == '3':
        obj.raise_salary()
    elif ch == '4':
        break
    else:
        print("Invalid choice")