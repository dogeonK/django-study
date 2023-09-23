class Sample():
    planet = "Earth" # Class object attribute

    def __init__(self, name, gpa):
        self.name = name # Attributes
        self.gpa = gpa

stu1 = Sample(name="Jose", gpa=4.0)
stu2 = Sample(name="Mimi", gpa=3.5)

print(stu1.gpa)
print(stu1.planet)