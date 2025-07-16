class Mobile:
    def __init__(self):
        self.model="Rahul"

    def show_model(self):
        return self.model
        

hello = Mobile()
r = hello.show_model()
print(r)