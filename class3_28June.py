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
a = 10
b = 5
try:
    d = a / b
    print(d)
    print("Inside try")

except ZeroDivisionError:
    print("Division by zero is not allowed")

else:
    print("Inside else")

print("Rest of the code")