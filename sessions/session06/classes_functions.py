
def a_function():
    print("This is a standard function, to be called by its name, followed by parentheses")

class AClass:
    def __init__(self):
        print("This is an initialization function inside a Class")
        self.a = "this prints when you call a_class.a"

a_function()

a_class = AClass()

print(a_class.a)


