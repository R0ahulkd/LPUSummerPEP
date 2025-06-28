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
f = open("student.txt", mode="r")