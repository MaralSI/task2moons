from art import tprint
tprint("PYTHON")

class Hello:
    def greet(self):
        return "Hello, world!"

class NewClass(Hello):
    def greet_with_name(self, name):
        return f"Hello, {name}!"
