class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(f"Value: {self.value}")
#creating an instance
obj = MyClass(10)
obj.display_value()