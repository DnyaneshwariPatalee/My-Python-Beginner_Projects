class Demo:
    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age
    def config(self):
        print(f"Name: {self.name}, Age: {self.age}")

obj=Demo('MK',21)
obj.config()
