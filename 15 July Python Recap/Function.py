# def disp():
#     def show():
#         return " show function"
#     result = show() + " display function"
#     return result
# print(disp())


#return statement with parameters
def disp(name):
    def show():
        return " show function"
    result = show() + " display function for " + name
    return result

print(disp("Python"))