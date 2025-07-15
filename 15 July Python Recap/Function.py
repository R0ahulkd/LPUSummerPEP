def disp():
    def show():
        return " show function"
    result = show() + " display function"
    return result
print(disp())