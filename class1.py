from art import tprint

class Hello:
    def tptint(self):
        print("Hello, World!")



class MyHello(Hello):
    def tptint(self):
        super().tptint()
        print("Hello from MyHello!")
