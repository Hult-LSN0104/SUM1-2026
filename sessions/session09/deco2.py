def magic_box(func):
    def wrapper():
        print("Beep boop - magic_box decorator works!")
        func()
    return wrapper

@magic_box
def say_hello():
    print("Hello!")

say_hello()