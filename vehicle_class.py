class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print("%d %s %s" % (self.year, self.make, self.model))

car = Vehicle("Porsche", "911", 2019)

car.print_info()