# my_class.py

class Greet:
    def __init__(self, name, age=25, gendre="male"):
        self.name = name
        self.age = age
        self.gendre = gendre
    
    def greet(self):
        print(f"Hey!! welcome to the class {self.name}, your age is {self.age} and gender is {self.gendre}")
