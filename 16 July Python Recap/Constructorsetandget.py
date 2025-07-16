class Mobile:
    def __init__(self):
        self.model = "Apple"

    def set_model(self):
        self.model = "Pine Apple"

realme = Mobile()
print(realme.model)
realme.set_model()
print(realme.model)