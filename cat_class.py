class Cat:
    #Attributes
    species = "mammal"
    temperament = "fiery"
    #Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return "%s is %d years old" % (self.name, self.age)

    def __str__(self):
        return """
        5s:
        Age: %d
        """ (self.name, self.age)

grover = Cat("Grover", 10)
wendy = Cat("Wendy", 5)


print(grover.describe())
print(wendy.describe()) 