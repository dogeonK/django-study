# 1. attributes
class Sample():
    planet = "Earth" # Class object attribute

    def __init__(self, name, gpa):
        self.name = name # Attributes
        self.gpa = gpa

stu1 = Sample(name="Jose", gpa=4.0)
stu2 = Sample(name="Mimi", gpa=3.5)

print(stu1.gpa)
print(stu1.planet)

# 2. Method
print()
class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2 #self.pi
    
    def perimeter(self):
        return self.pi * 2 * self.radius

myCircle = Circle(3)
print(myCircle.radius)
print(myCircle.area())
print(myCircle.perimeter())

# 3. Inheritance
print()
class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        print("hello")
    
    def report(self):
        print(f"I am {self.first_name} {self.last_name}")


class Agent(Person):

    def report(self):
        print("I am here")

    def reveal(self, passcode):
        if (passcode == 123):
            print("I am secret agent")
        else:
            self.report()

x = Person("John", "Smith")
x.hello()
x.report()

y = Agent("John", "Smith")
y.hello()
y.report()
y.reveal(123)