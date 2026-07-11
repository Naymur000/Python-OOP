class Car:
    # def __init__(self):
    #     self.model = ""
    #     self.brand = ""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car1 = Car("Toyota", "Corolla")
# car1.brand = "Toyota"
# car1.model = "Corolla"

print(car1.brand)
print(car1.model)

car2 = Car("Honda", "Civic")
# car2.brand = "Honda"
# car2.model = "Civic"

print(car2.brand, car2.model)

