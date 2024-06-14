from art import tprint
tprint("PYTHON")

class Hello:
    def greet(self):
        return "Hello, world!"

class NewClass(Hello):
    def greet_with_name(self, name):
        return f"Hello, {name}!"

from class1 import NewClass

def tptin(instance):
    print(instance.greet_with_name("Alice"))

if __name__ == "__main__":
    instance = NewClass()
    tptin(instance)
