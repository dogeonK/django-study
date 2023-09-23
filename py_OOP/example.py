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